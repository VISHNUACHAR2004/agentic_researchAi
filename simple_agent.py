import requests
def tool_weather(city):
    url = f"https://wttr.in/{city}?format=3"
    try:
        response = requests.get(url, timeout=5)
        response.raise_for_status()
        return response.text
    except Exception as e:
        return f"[TOOL_ERROR] Weather tool failed: {e}"

def agent(task):
    if "weather" in task.lower():
        city = task.split()[-1]
        result = tool_weather(city)
        return f"Tool result: {result}"
    else:
        return "I don't know how to solve this yet."

print(agent("weather delhi"))
ss
ss