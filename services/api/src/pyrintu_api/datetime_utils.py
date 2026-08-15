"""Datetime normalization utilities for timezone-aware UTC handling."""

from datetime import datetime, timezone
from typing import Optional


def normalize_to_utc(dt: Optional[datetime]) -> Optional[datetime]:
    """
    Normalize a datetime to timezone-aware UTC.
    
    If the datetime is naive, interpret it as UTC and make it aware.
    If the datetime is already aware, convert it to UTC.
    If the datetime is None, return None.
    
    This ensures all datetimes used in domain logic are timezone-aware UTC,
    preventing "can't compare offset-naive and offset-aware datetimes" errors.
    
    Args:
        dt: The datetime to normalize (can be naive, aware, or None)
        
    Returns:
        A timezone-aware UTC datetime, or None if input was None
    """
    if dt is None:
        return None
    
    if dt.tzinfo is None:
        # Naive datetime - interpret as UTC
        return dt.replace(tzinfo=timezone.utc)
    
    # Aware datetime - convert to UTC
    return dt.astimezone(timezone.utc)


def utc_now() -> datetime:
    """
    Get current time as timezone-aware UTC datetime.
    
    This is the canonical way to generate timestamps in the application.
    """
    return datetime.now(timezone.utc)
