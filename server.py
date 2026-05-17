from flask import Flask, render_template, request, jsonify
from EmotionDetection.emotion_detection import emotion_detector

app = Flask(__name__)

@app.route("/")
def render_index_page():
    """Renders the main application dashboard frontend template."""
    return render_template('index.html')

@app.route("/emotionDetector")
def emotion_analyzer():
    """Receives user input text, runs emotion analysis, and reports back formatted strings."""
    # Grab the text argument sent from the browser input box
    text_to_analyze = request.args.get('textToAnalyze')
    
    # Task 7: Check if input string is entirely blank or spaces
    if not text_to_analyze or text_to_analyze.strip() == "":
        return jsonify({
            "status": "error",
            "message": "Invalid text! Please try again."
        })
        
    # Run the core detector package logic
    response = emotion_detector(text_to_analyze)
    
    # Task 7: Catch edge case where dictionary returns empty/None states
    if response['dominant_emotion'] is None:
        return jsonify({
            "status": "error",
            "message": "Invalid text! Please try again."
        })
        
    # Task 3/6 Output layout requirements format matching string template rules
    output_message = (
        f"For the given statement, the system response is: "
        f"'anger': {response['anger']}, 'disgust': {response['disgust']}, "
        f"'fear': {response['fear']}, 'joy': {response['joy']} and "
        f"'sadness': {response['sadness']}. The dominant emotion is {response['dominant_emotion']}."
    )
    
    return jsonify({
        "status": "success",
        "message": output_message
    })

if __name__ == "__main__":
    # Start server listening on port 5000
    app.run(host="0.0.0.0", port=5000, debug=True)