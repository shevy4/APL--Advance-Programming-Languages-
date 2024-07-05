import google.generativeai as genai


def Analyze(result, code):
    genai.configure(api_key='AIzaSyAzRbqEKSVapK17LGZaClA81x3GOvARY1o')
    generation_config = {
        "temperature": 1,
        "top_p": 0.95,
        "top_k": 64,
        "max_output_tokens": 8192,
        "response_mime_type": "text/plain",
    }

    model = genai.GenerativeModel(
        model_name="gemini-1.5-flash",
        generation_config=generation_config,
        system_instruction="Evaluate the expressions given, # are representations of lambda symbols, keep the analysis "
                           "short, about 3 or 4 lines, then give the results in the form of expression received -> "
                           "output. you can show alliterations to get to the final output."
    )
    history = []

    user_input = "You : Analyze How My Program Solves " + code + " , Here are the steps my program took," + result
    chat_session = model.start_chat(
        history=history
    )

    response = chat_session.send_message(user_input)
    model_response = response.text

    print('Gemini: ', model_response)
    print()
    history.append({"role": "user", "parts": [user_input]})
    history.append({"role": "model", "parts": [model_response]})
    return model_response

