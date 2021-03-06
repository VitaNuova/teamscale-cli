from __future__ import absolute_import
from __future__ import unicode_literals

from teamscale_client.utils import auto_str


@auto_str
class PreCommitUploadData(object):
    """Represents precommit upload data for Teamscale.

    Args:
        uniformPathToContentMap (dict[unicode, unicode]): A map from uniform paths to the content of changed files
        deletedUniformPaths (List[str]): List of names of deleted files
    """

    def __init__(self, uniformPathToContentMap, deletedUniformPaths):
        self.uniformPathToContentMap = uniformPathToContentMap
        self.deletedUniformPaths = deletedUniformPaths
