
import google.generativeai as genai

genai.configure(api_key='AIzaSyDkZV-Draj29cp_8o0cfvRIHSVP0VubXyU')

  
model = genai.GenerativeModel('gemini-1.5-flash-latest')




# prompt = 

def chat(prompt):

    response = model.generate_content(prompt)

    if response and response.candidates and response.candidates[0].safety_ratings:
        safety_ratings = response.candidates[0].safety_ratings

        if any(rating.blocked for rating in safety_ratings):
            return safety_ratings
            # return "Response was blocked due to safety reasons."
        else:
            generated_text = response.text
            return generated_text
            
    else:
        return "No valid response from the server."
    
print(chat("how to give you system instructions , to this code 'response = model.generate_content(prompt)'"))