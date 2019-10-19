:- use_module(library(apply)).

novel("att vara ganska tragisk").

word_analysis(Element, Strength) :-
    word_strength(Element, Strength).

p() :-
    novel(X),
    split_string(X, " ", "", L),
    convlist(word_analysis, L, Out),
    maplist(write, Out).
