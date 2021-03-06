from __future__ import absolute_import


class ConfigNotFound(LookupError):
    """Raise this exception to signal that a requested config item
       was not found in the config."""
    pass


class UnsupportedPasteDeployFeature(NotImplementedError):
    """Raise this exception to signal a PasteDeploy feature unsupported by Montague."""
    pass
