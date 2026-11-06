import io
import json
from contextlib import redirect_stdout

from groq import Groq

from embeding_search import search_database
from web_search import search_web
from media.audio import speak_text, speak_to_file
from media.image import generate_image


client = Groq(api_key = "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")
TOOLS = [
    {
        "type": "function",
        "function": {
            "name": "search_database",
            "description": (
                "Search the local educational knowledge base for information "
                "relevant to the user's question."
            ),
            "parameters": {
                "type": "object",
                "properties": {
                    "query": {
                        "type": "string",
                        "description": "The question or terms to search for."
                    }
                },
                "required": ["query"]
            }
        }
    },
    {
        "type": "function",
        "function": {
            "name": "search_web",
            "description": (
                "Search the web through Exa for current or external information."
            ),
            "parameters": {
                "type": "object",
                "properties": {
                    "query": {
                        "type": "string",
                        "description": "The web search query."
                    },
                    "num_results": {
                        "type": "integer",
                        "description": "Number of results to return; defaults to 5."
                    },
                    "search_type": {
                        "type": "string",
                        "description": "Exa search mode; defaults to auto."
                    }
                },
                "required": ["query"]
            }
        }
    },
    {
        "type": "function",
        "function": {
            "name": "speak_text",
            "description": (
                "Speak the supplied text aloud using the computer's default voice."
            ),
            "parameters": {
                "type": "object",
                "properties": {
                    "text": {
                        "type": "string",
                        "description": "The text to speak aloud."
                    }
                },
                "required": ["text"]
            }
        }
    },
    {
        "type": "function",
        "function": {
            "name": "speak_to_file",
            "description": "Convert text to speech and save it as an audio file.",
            "parameters": {
                "type": "object",
                "properties": {
                    "text": {
                        "type": "string",
                        "description": "The text to convert to speech."
                    },
                    "output_path": {
                        "type": "string",
                        "description": "Destination path for the audio file."
                    },
                    "rate": {
                        "type": "integer",
                        "description": "Speech rate; defaults to 165."
                    }
                },
                "required": ["text", "output_path"]
            }
        }
    },
    {
        "type": "function",
        "function": {
            "name": "generate_image",
            "description": (
                "Create and save an educational graphic using Pillow. "
                "Provide a title and content, and optionally customize its appearance."
            ),
            "parameters": {
                "type": "object",
                "properties": {
                    "title": {
                        "type": "string",
                        "description": "Title displayed on the graphic."
                    },
                    "content": {
                        "type": "string",
                        "description": "Main educational text displayed on the graphic."
                    },
                    "output_path": {
                        "type": "string",
                        "description": "Save path; defaults to educational_graphic.png."
                    },
                    "width": {
                        "type": "integer",
                        "description": "Image width in pixels; defaults to 1200."
                    },
                    "height": {
                        "type": "integer",
                        "description": "Image height in pixels; defaults to 750."
                    },
                    "font": {
                        "type": "string",
                        "description": "Optional path to a font file."
                    },
                    "title_font_size": {
                        "type": "integer",
                        "description": "Title font size; defaults to 54."
                    },
                    "content_font_size": {
                        "type": "integer",
                        "description": "Content font size; defaults to 27."
                    },
                    "text_colour": {
                        "type": "string",
                        "description": "Title text colour; defaults to #18212F."
                    },
                    "background_colour": {
                        "type": "string",
                        "description": "Image background colour; defaults to #F6F8FC."
                    },
                    "accent_colour": {
                        "type": "string",
                        "description": "Accent colour; defaults to #3767E8."
                    },
                    "content_colour": {
                        "type": "string",
                        "description": "Optional content text colour; defaults to text_colour."
                    },
                    "alignment": {
                        "type": "string",
                        "enum": ["left", "center", "right"],
                        "description": "Text alignment; defaults to left."
                    },
                    "padding": {
                        "type": "integer",
                        "description": "Inner card padding; defaults to 72."
                    },
                    "line_spacing": {
                        "type": "integer",
                        "description": "Spacing between text lines; defaults to 12."
                    },
                    "title_max_lines": {
                        "type": "integer",
                        "description": "Maximum wrapped title lines; defaults to 3."
                    },
                    "add_footer": {
                        "type": "boolean",
                        "description": "Whether to show a footer; defaults to true."
                    },
                    "footer_text": {
                        "type": "string",
                        "description": "Footer label; defaults to Study note."
                    },
                    "corner_radius": {
                        "type": "integer",
                        "description": "Rounded card corner radius; defaults to 28."
                    }
                },
                "required": ["title", "content"]
            }
        }
    }
]

def run_tool(name, arguments):
    if name == "search_database":
        output = io.StringIO()

        # search_database currently prints results instead of returning them
        with redirect_stdout(output):
            result = search_database(query=arguments["query"])

        return result if result is not None else output.getvalue()

    if name == "search_web":
        return search_web(
            query=arguments["query"],
            num_results=arguments.get("num_results", 5),
            search_type=arguments.get("search_type", "auto")
        )

    if name == "speak_text":
        speak_text(text=arguments["text"])
        return {"success": True, "message": "Text was spoken."}

    if name == "speak_to_file":
        speak_to_file(
            text=arguments["text"],
            output_path=arguments["output_path"],
            rate=arguments.get("rate", 165)
        )
        return {
            "success": True,
            "output_path": arguments["output_path"]
        }

    if name == "generate_image":
        image = generate_image(**arguments)
        return {
            "success": True,
            "output_path": arguments.get(
                "output_path", "educational_graphic.png"
            ),
            "width": image.width,
            "height": image.height
        }

    raise ValueError(f"Unknown tool: {name}")


def ask_model(user_text):
    messages = [
        {
            "role": "system",
            "content": (
                "You are an educational assistant. Use the available tools when "
                "they help answer the user. Review each tool result and decide "
                "whether another tool call is needed."
            )
        },
        {"role": "user", "content": user_text}
    ]

    tool_calls_used = 0
    max_tool_calls = 15

    while True:
        request = {
            "model": "openai/gpt-oss-120b",
            "messages": messages
        }

        if tool_calls_used < max_tool_calls:
            request["tools"] = TOOLS
            request["tool_choice"] = "auto"

        response = client.chat.completions.create(**request)
        assistant_message = response.choices[0].message
        tool_calls = assistant_message.tool_calls or []

        if not tool_calls:
            return assistant_message.content or ""

        if tool_calls_used >= max_tool_calls:
            return "The 15 tool-call limit was reached before I could finish."

        messages.append(assistant_message)

        for tool_call in tool_calls:
            if tool_calls_used >= max_tool_calls:
                result = {
                    "success": False,
                    "error": "The limit of 15 tool calls for this request was reached."
                }
            else:
                tool_calls_used += 1
                arguments = json.loads(tool_call.function.arguments)

                try:
                    result = run_tool(tool_call.function.name, arguments)
                except Exception as error:
                    result = {"success": False, "error": str(error)}

            messages.append({
                "role": "tool",
                "tool_call_id": tool_call.id,
                "name": tool_call.function.name,
                "content": json.dumps(result, ensure_ascii=False, default=str)
            })

def main():
    print("COGNiX is ready. Type 'exit' to quit.")

    while True:
        user_text = input("You: ").strip()

        if user_text.lower() in {"exit", "quit"}:
            print("Goodbye.")
            break

        if not user_text:
            continue

        try:
            answer = ask_model(user_text)
            print(f"COGNiX: {answer}")
        except Exception as error:
            print(f"Error: {error}")


if __name__ == "__main__":
    main()