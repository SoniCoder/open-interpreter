from interpreter import interpreter
import os

# let us set the env variable ANONYMIZED_TELEMETRY to False

os.environ["ANONYMIZED_TELEMETRY"] = "False"
interpreter.offline = True # Disables online features like Open Procedures
interpreter.llm.model = "openai/x" # Tells OI to send messages in OpenAI's format
interpreter.llm.api_key = "fake_key" # LiteLLM, which we use to talk to LM Studio, requires this
interpreter.llm.api_base = "http://ip:1234/v1" # Point this at any OpenAI compatible server
# interpreter.llm.context_window = 32768
interpreter.llm.context_window = 16384
# interpreter.llm.max_tokens = 16384
interpreter.llm.max_tokens = 4096
interpreter.chat()
