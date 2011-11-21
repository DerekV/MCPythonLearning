# Here is a example of global i found, though on overstack a forum was discussing how you shouldn't use global, so for the time being im going to ignore it.

_cached_result = None
def myComputationallyExpensiveFunction():
    global _cached_result
    if _cached_result:
       return _cached_result

    # ... figure out result

    _cached_result = result
    return result
