from dataclasses import dataclass


@dataclass
class Settings:
    """Workflow Settings

    The class contains all the settings the user can specify in their workflow.
    """
    # Global
    overrideEnvVar: bool = True
    # Paths
    localMode: bool = True
    defaultPathScheme: str = 'file'
