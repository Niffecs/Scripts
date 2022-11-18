import platform

def os_bindings(path: str) -> str:
        """
        Changes the paths from Linux to Windows.
        It's really only about the backslash.
        """
        if "Windows" in platform.platform():
            return path.replace("/", "\\")
