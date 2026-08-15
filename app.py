from flask import Flask, render_template, session, request, jsonify
from assets.model import TrainerModel
import json

app = Flask(__name__)
app.secret_key = "admin"

def get_or_create_model():
    """Create model and restore state from session"""
    model = TrainerModel()
    
    # Restore training data from session
    if 'training_data' in session:
        model.data = session['training_data']
    
    return model

def save_model_state(model):
    """Save model state to session"""
    session['training_data'] = model.data
    session.modified = True

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/chat")
def chat():
    # Initialize session if needed
    if 'training_data' not in session:
        session['training_data'] = []
        session.modified = True
    
    return render_template("chat.html")

@app.route("/fetch", methods=['POST'])
def fetch():
    """Endpoint for chat messages using POST"""
    data = request.get_json()
    message = data.get('message', '') if data else ''
    
    if not message or message.strip() == '':
        return jsonify({
            'response': 'Please enter a valid message.',
            'error': True
        })
    
    # Get or create model
    model = get_or_create_model()
    
    # Process the message
    result = model.process(message)
    
    # Save updated model state
    save_model_state(model)
    
    return jsonify({
        'response': result,
        'error': False,
        'data_count': len(model.data)
    })

if __name__ == "__main__":
    app.run(debug=True)