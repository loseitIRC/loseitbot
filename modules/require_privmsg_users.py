from __future__ import unicode_literals, absolute_import, print_function, division

from sopel import module
import functools

def require_privmsg_users(usernames):
    """Decorate a function to only be triggerable from a private message for
    a list of specific usernames.
    """
    usernames = [u.lower() for u in usernames]
    def actual_decorator(function):
        @functools.wraps(function)
        def _nop(*args, **kwargs):
            # Assign trigger and bot for easy access later
            bot, trigger = args[0:2]
            user = str(trigger.nick).lower()
            cmd = trigger.group(0)
            if user not in usernames or trigger.is_privmsg:
                return function(*args, **kwargs)
            else:
                bot.msg(user, "The {cmd} command is restricted to PM usage for you.".format(cmd=cmd))
        return _nop
    return actual_decorator
