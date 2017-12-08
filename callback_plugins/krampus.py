from ansible.plugins.callback.default import CallbackModule
from ansible.utils.color import stringc
from ansible import constants as C

class CallbackModule(CallbackModule):

    CALLBACK_VERSION = 2.0
    CALLBACK_TYPE = 'stdout'
    CALLBACK_NAME = 'krampus'
    CALLBACK_NEEDS_WHITELIST = True

    def v2_playbook_on_stats(self, stats):
        super(CallbackModule, self).v2_playbook_on_stats(stats)
        if len(stats.failures) or len(stats.dark):
            print stringc("krampus sees you when you're sleeping", C.COLOR_ERROR)
            print stringc('''
                    *          
            *                 *
           )       (\___/)     (
        * /(       \ (. .)     )\ *
          # )      c\   >'    ( #
           '         )-_/      '
         \\|,    ____| |__    ,|//
           \ )  (  `  ~   )  ( /
            #\ / /| . ' .) \ /#
            | \ / )   , / \ / |
             \,/ ;;,,;,;   \,/
              _,#;,;;,;,
             /,i;;;,,;#,;
            ((  %;;,;,;;,;
             ))  ;#;,;%;;,,
           _//    ;,;; ,#;,
          /_)     #,;  //
                 //    \|_
                 \|_    |#|
                  |#\    -"
                   -"''', C.COLOR_ERROR)
