"""
Helper functions for various tasks.
"""

import requests


def make_request(method, url, **kwargs):
    """Make a request to the given URL with the specified method and additional parameters"""
    timeout = kwargs.pop('timeout', 5)  # Set a default timeout of 5 seconds
    return requests.request(method, url, timeout=timeout, **kwargs)
