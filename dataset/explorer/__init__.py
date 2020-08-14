import os
import numpy as np


class Explorer():
    def __init__(self, dataset, leaves_only=False):
        self.dataset = dataset
        self.folders = self.crawl_for_folders(dataset)
        if leaves_only is True:
            self.folders = [f for f in self.folders if self.is_leaf(f)]


    def crawl_for_folders(self, folder):
        subfolders = [os.path.join(folder, f) for f in os.listdir(folder)]
        subfolders = [s for s in subfolders if os.path.isdir(s)]

        crawled = [folder]
        if len(subfolders) == 0:
            return crawled
        else:
            for s in subfolders:
                crawled = crawled + self.crawl_for_folders(s)
            return crawled

    def is_leaf(self, folder):
        content = [os.path.join(folder, f) for f in os.listdir(folder)]
        content = [c for c in content if os.path.isdir(c)]
        if len(content) == 0:
            return True
        else:
            return False

    def get_folders(self):
        pass

    def check_filename_by_extension(self, filename,
                                    include=None, exclude=None):
        assert not (include is not None and exclude is not None)
        if include is not None:
            include = ['.' + i.lower() for i in include]
            if os.path.splitext(filename)[-1].lower() not in include:
                return False

        if exclude is not None:
            exclude = ['.' + e.lower() for e in exclude]
            if os.path.splitext(filename)[-1].lower() in exclude:
                return False

        return True

    def check_filename_by_pattern(self, filename, include=None, exclude=None):
        assert not (include is not None and exclude is not None)
        if include is not None:
            if any([i.lower() in filename.lower() for i in include]) is False:
                return False

        if exclude is not None:
            if any([e.lower() in filename.lower() for e in exclude]) is False:
                return False

        return True


    def get_files(self, include_extension=None, exclude_extension=None,
                  include_pattern=None, exclude_pattern=None):
        # include and exclude cannot be both set
        assert not (include_extension is not None and \
                    exclude_extension is not None)
        assert not (include_pattern is not None and \
                    exclude_pattern is not None)

        filenames = []
        for folder in self.folders:
            content = [os.path.join(folder, f) for f in os.listdir(folder)]
            content = [c for c in content if os.path.isdir(c) is False]
            content = [c for c in content if self.check_filename_by_extension(
                       c, include_extension, exclude_extension)]
            content = [c for c in content if self.check_filename_by_pattern(
                       c, include_pattern, exclude_pattern)]
            filenames = filenames + content
        return filenames
