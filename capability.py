capabilities = {
    "post_facebook": True,
    "generate_content": True,
    "analyze_engagement": False,
    "auto_optimize": False
}

def get_capabilities():
    return capabilities

def update_capability(name, status):
    capabilities[name] = status
