import os
from dataset.utils import (
    check_filename_by_extension,
    check_filename_by_pattern,
    is_leaf,
)


class Explorer():
    def __init__(self, dataset, leaves_only=False):
        self.dataset = dataset
        self.folders = self.crawl_for_folders(dataset)
        if leaves_only is True:
            self.folders = [f for f in self.folders if is_leaf(f)]

    def crawl_for_folders(self, folder):
        """Get (recursively) all subfolders within given folder.

        Parameters
        ----------
        folder : str
            Folder whose all subfolders are to be rertrieved.

        Returns
        -------
        crawled : list
            List of all subfolders contained within folder.

        """
        subfolders = [os.path.join(folder, f) for f in os.listdir(folder)]
        subfolders = [s for s in subfolders if os.path.isdir(s)]

        crawled = [folder]
        if len(subfolders) == 0:
            return crawled
        else:
            for subfolder in subfolders:
                crawled = crawled + self.crawl_for_folders(subfolder)
            return crawled

    def get_folders(self):
        pass

    def get_files(self, include_extension=None, exclude_extension=None,
                  include_pattern=None, exclude_pattern=None):
        """Get files from dataset.

        Parameters
        ----------
        include_extension : list
            List of allowed extensions (without colon), case insensitive.

        exclude_extension : list
            List of not allowed extensions (without colon), case insensitive.

        include_pattern : list
            List of allowed patterns.

        exclude_pattern : list
            List of not allowed patterns.

        Returns
        -------
        filenames : list
            List of filenames (full path) that comply with given
            include/exclude rules.

        """
        # include and exclude cannot be both set
        assert not (include_extension is not None and \
                    exclude_extension is not None)
        assert not (include_pattern is not None and \
                    exclude_pattern is not None)

        filenames = []
        for folder in self.folders:
            content = [os.path.join(folder, f) for f in os.listdir(folder)]
            content = [c for c in content if os.path.isdir(c) is False]
            content = [c for c in content if check_filename_by_extension(
                       c, include_extension, exclude_extension)]
            content = [c for c in content if check_filename_by_pattern(
                       c, include_pattern, exclude_pattern)]
            filenames = filenames + content
        return filenames
