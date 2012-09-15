: subroutine
     me @ "Hi, I'm a secondary function!" notify
     var thingy
     "I'm a scoped variable" thingy !
     thingy @ me @ swap notify
     { { "Hi" 1 2 3 } intostr "The program just registered a stackrange of " swap strcat "." strcat me @ swap notify
     } array_make "And now it made an array!" me @ swap notify
     { "Hi" 1 2 3 4 } array_make_dict
;

: main
    1 5 1 for
        pop
        "Hello, there!" me @ swap notify
    repeat

    1 if
        "This message appears if the first condition is true." me @ swap notify
    else
        "This message appears if the first condition is false." me @ swap notify
    then
    subroutine
    "We've returned to the main function now." me @ swap notify
    me @ "Testprop" getprop me @ swap notify
    me @ "testkey" "testvalue" setprop "Successful setting of value." me @ swap notify
;
