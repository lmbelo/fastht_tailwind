from .modal import Modal

def load_extension(module_name):
    try:
        module = __import__(module_name, fromlist=['extend_modal'])
        module.extend_modal(Modal)
    except ImportError:
        print(f"Extension {module_name} not installed.")