% This is a comment and we are noobs
:- use_module(library(apply)).

novel("A B C D E F").

word_analysis(Element, List) :-
    write(Element),
    List is [Element|List].

p() :-
    novel(X),
    split_string(X, " ", "", L),
    maplist(write, L).
