import requests

def get_google_theme_color():
  """Gets the theme color of Google."""
  response = requests.get("https://www.google.com/")
  theme_color = response.headers["theme-color"]
  return theme_color

theme_color = get_google_theme_color()

print(theme_color)
