from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

from hsc_result import HscResult
from sslc_result import SslcResult

__all__ = ["Base", "HscResult", "SslcResult"]
