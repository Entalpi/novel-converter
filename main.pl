:- use_module(library(apply)).
:- use_module(library(lists)).

novel("NU SKA JAG berätta en saga. Den handlar om en människa,
Pomperipossa kan vi kalla henne, för det brukar ju folk heta i
sagorna. Hon bodde i ett land som vi kan kalla Monismanien,
nånting måste vi ju kalla det.").

% Converts positive words to negative ones if defined.
positive_to_negative() :- true.

% Clamps the value to one side of 0
clamp(Value, NewValue) :-
    not(positive_to_negative()),
    (integer(Value) > 0 ->
         NewValue is  integer(Value) ;
         NewValue is -integer(Value)).

clamp(Value, NewValue) :-
    positive_to_negative(),
    (integer(Value) > 0 ->
         NewValue is -integer(Value) ;
         NewValue is  integer(Value)).

% Random word with the same class and inverse sentimental score
word_analysis(Element, NewWord) :-
    string_lower(Element, LowerCase),
    word_strength(LowerCase, Strength),
    clamp(Strength, InvStrength),
    InvStrength is -integer(Strength),
    findall(NewWord, word_strength(NewWord, InvStrength), StrengthWords),
    word_class(LowerCase, WordClass),
    findall(NewWord, word_class(NewWord, WordClass), ClassWords),
    intersection(StrengthWords, ClassWords, NewWords),
    random_member(NewWord, NewWords).

% Words which do not exist in the database
word_analysis(Element, Element).

p() :-
    novel(X),
    split_string(X, " ", "", L),
    maplist(word_analysis, L, Out),
    write(Out).
