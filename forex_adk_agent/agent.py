import os
from dotenv import load_dotenv
import requests
from google.adk.agents import Agent
from google.adk.models.lite_llm import LiteLlm

load_dotenv()

groq_api_key = os.getenv("GROQ_API_KEY")


def get_exchange_rate(base: str, target: str) -> dict:
    """Get the latest exchange rate between two currencies.

    Returns the latest exchange rate for the specified base and target currency.
    Use this tool whenever the user asks about exchange rates, forex, or currency conversion.
    Provide the base and target currency symbols as input parameters.

    Args:
        base (str): Base currency symbol (e.g. USD).
        target (str): Target currency symbol (e.g. NPR).

    Returns:
        dict: A dictionary containing the exchange rate information.
    """

    try:
        url = (
            f"https://api.frankfurter.dev/v2/rate/"
            f"{base.upper()}/{target.upper()}"
        )

        response = requests.get(url)
        data = response.json()

        if not data:
            return {
                "error": "Exchange rate not available for the provided currency symbols."
            }

        result = {
            "base_currency": data["base"],
            "target_currency": data["quote"],
            "exchange_rate": data["rate"],
            "date": data["date"]
        }

        return result

    except Exception as e:
        return {
            "message": "An error occurred while fetching exchange rate data.",
            "error": str(e)
        }


SYSTEM_PROMPT = """
You are a helpful assistant that can answer questions about foreign exchange rates.

If the user asks about:
- exchange rates
- currency conversion
- forex
- value of one currency in another

you should use the relevant tool to get the exchange rate information.

Anything not related to forex should be answered based on your own knowledge.
"""


root_agent = Agent(
    name="forex_agent",
    model=LiteLlm(model="groq/llama-3.3-70b-versatile"),
    description="Answers the user query related to forex and currency exchange rates.",
    instruction=SYSTEM_PROMPT,
    tools=[get_exchange_rate]
)