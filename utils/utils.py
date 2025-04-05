# Utility to print context in desired format
def context_str(context):
    return f"({', '.join(f'{k}={v}' for k, v in context.items())})"