#!/usr/bin/env python
# encoding: utf-8

"""Sources of snippet definitions."""

from UltiSnips.snippet.source._base import SnippetSource
from UltiSnips.snippet.source.added import AddedSnippetsSource
from UltiSnips.snippet.source.file.snipmate import SnipMateFileSource
from UltiSnips.snippet.source.file.ultisnips import UltiSnipsFileSource, \
    find_all_snippet_files, find_snippet_files
