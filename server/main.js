var express = require('express');
var app = express();
var fs = require('fs');

app.get('/word-analysis', function(req, res) {
    const s = ':- [word_db], word_analysis(' + req.query.word + ', X), write(X), halt.';
    const cmd_arg = 'cd .. && echo ' + '"' + s + '"' + '| cat main.pl - > cmd_file.pl';
    const output = require('child_process').execSync(cmd_arg).toString();
    console.log(output);

    const cmd = 'cd .. && swipl -q cmd_file.pl && rm cmd_file.pl';
    const cmd_result = require('child_process').execSync(cmd).toString();
    console.log(cmd_result);

    res.send(cmd_result);
});

var server = app.listen(8888, function() {
  var host = server.address().address;
  var port = server.address().port;
  console.log("Example app listening at http://%s:%s", host, port);
});
