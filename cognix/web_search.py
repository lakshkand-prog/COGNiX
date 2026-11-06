import json
import os
import requests

# Importing your API key directly from your variable.py file
try:
    from .variable import exa_api_key as EXA_API_KEY
except ImportError:
    from variable import exa_api_key as EXA_API_KEY

EXA_SEARCH_ENDPOINT = "https://api.exa.ai/search"


def get_api_key(api_key: str | None = None) -> str:
    """Resolves and returns the Exa API key from argument, environment, or config."""
    return api_key or os.getenv("EXA_API_KEY", EXA_API_KEY)


def search_web(
    query: str,
    num_results: int = 5,
    search_type: str = "auto",
    api_key: str | None = None,
) -> dict:
    """
    Searches the web via Exa API and returns a structured JSON dictionary.
    """
    resolved_key = get_api_key(api_key)
    if not resolved_key:
        return {"success": False, "error": "EXA_API_KEY is not configured."}

    headers = {
        "Content-Type": "application/json",
        "Authorization": f"Bearer {resolved_key}",
    }

    payload = {
        "query": query,
        "type": search_type,
        "numResults": num_results,
        "contents": {
            "highlights": True,
            "text": True,
        },
    }

    try:
        response = requests.post(
            EXA_SEARCH_ENDPOINT, headers=headers, json=payload, timeout=25
        )
        response.raise_for_status()
        return response.json()

    except requests.exceptions.HTTPError as http_err:
        return {
            "success": False,
            "status_code": response.status_code,
            "error": str(http_err),
            "response_text": response.text,
        }
    except Exception as err:
        return {
            "success": False,
            "error": str(err),
        }