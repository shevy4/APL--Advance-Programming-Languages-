import google.generativeai as genai


def Analyze(result, code):
    # Configuring the generative AI with the API key
    genai.configure(api_key='AIzaSyAzRbqEKSVapK17LGZaClA81x3GOvARY1o')

    # Configuration for text generation
    generation_config = {
        "temperature": 1,  # Controls the randomness of text generation
        "top_p": 0.95,  # Controls diversity via nucleus sampling
        "top_k": 64,  # Controls diversity via top-k sampling
        "max_output_tokens": 8192,  # Maximum length of the generated text
        "response_mime_type": "text/plain",  # Specifies the response format as plain text
    }

    # Initializing the GenerativeModel with specific parameters
    model = genai.GenerativeModel(
        model_name="gemini-1.5-flash",
        generation_config=generation_config,
        system_instruction="Evaluate the expressions given, # are representations of lambda symbols, keep the analysis "
                           "short, about 3 or 4 lines, then give the results in the form of expression received -> "
                           "output. you can show alliterations to get to the final output."
    )
    history = []

    # Constructing user input for the chat session
    user_input = "You : Analyze How My Program Solves " + code + " , Here are the steps my program took," + result

    # Starting a chat session with the generative model
    chat_session = model.start_chat(
        history=history
    )

    # Sending user input to the model and receiving response
    response = chat_session.send_message(user_input)
    model_response = response.text

    # Printing the model's response
    print('Gemini: ', model_response)
    print()

    # Updating the conversation history with user and model parts (not used)
    history.append({"role": "user", "parts": [user_input]})
    history.append({"role": "model", "parts": [model_response]})
    return model_response

