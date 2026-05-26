"""Shared response helpers for MCP servers."""


def create_error_response(message: str, error_code: str, **additional_data) -> dict:
    """Create a standardized error response."""
    response = {"status": "error", "message": message, "error_code": error_code}
    response.update(additional_data)
    return response


def create_success_response(message: str, **additional_data) -> dict:
    """Create a standardized success response."""
    response = {"status": "success", "message": message}
    response.update(additional_data)
    return response
