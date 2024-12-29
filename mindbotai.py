# mindbot.py
import google.generativeai as mindbotai

def generate_ai_response(api_key, prompt):
   try:
     mindbotai.configure(api_key=api_key)
     model = mindbotai.GenerativeModel("gemini-1.5-flash")
     response = model.generate_content(prompt)
     return response.text
   except Exception as e:
       print(f"Error generating response: {e}")
       return None

if __name__ == '__main__':
  api_key = "YOUR_API_KEY" #Dont Type Any Thing Here
  test_prompt = "Hi!"
  response = generate_ai_response(api_key, test_prompt)

  if response:
      print("Test Response:> ")
      print(response)
  else:
    print("Failed to get a response during testing.")