from . import algo

# Export variables by reference to maintain global state
def __getattr__(name):
    if name == 'RTOL':
        return algo.RTOL
    elif name == 'ATOL':
        return algo.ATOL
    else:
        raise AttributeError(f"module '{__name__}' has no attribute '{name}'")