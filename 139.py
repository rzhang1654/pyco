#!/usr/bin/env python
import cStringIO
import formatter
from htmllib import HTMLParser
import httplib
import os
import sys
import urllib
import urlparse

class Retriever(object):
  __slots__ = ('url','file')
  
