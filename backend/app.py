from flask import Flask, request, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)  # Para permitir llamadas desde frontend (localhost)

@app.route('/api/process', methods=['POST'])
def process_text():
    data = request.json
    user_text = data.get('text', '').lower()
    
    # Simulación de respuestas básicas tipo IA
    if 'hola' in user_text:
        response = "¡Hola! ¿Cómo puedo ayudarte hoy?"
    elif 'hora' in user_text:
        from datetime import datetime
        response = f"La hora actual es {datetime.now().strftime('%H:%M')}."
    elif 'adiós' in user_text:
        response = "¡Hasta luego! Que tengas un buen día."
        
        # Comandos para el hogar inteligente
    elif 'encender luces' in user_text:
        response = "Encendiendo las luces."
    elif 'apagar luces' in user_text:
        response = "Apagando las luces."
    elif 'abrir puerta principal' in user_text:
        response = "Abriendo la puerta principal."
    elif 'cerrar puerta principal' in user_text:
        response = "Cerrando la puerta principal."
    elif 'subir cortinas' in user_text:
        response = "Subiendo las cortinas."
    elif 'bajar cortinas' in user_text:
        response = "Bajando las cortinas."
    elif 'prender televisión' in user_text or 'encender televisión' in user_text:
        response = "Encendiendo la televisión."
    elif 'apagar televisión' in user_text:
        response = "Apagando la televisión."
    elif 'ayuda' in user_text or 'emergencia' in user_text:
        response = "Enviando señal de ayuda a tu contacto de emergencia."
    elif 'tu estado' in user_text:
        response = "Yo, bien gracias, cualquier consulta o accion que quieras, aqui estare para ayudarte."
    elif 'clima' in user_text:
        response = "Actualmente hace 24 grados y está soleado."  # Simulado
    elif 'poner música' in user_text:
        response = "Reproduciendo tu lista de música favorita."
    elif 'detener música' in user_text:
        response = "Deteniendo la música."
    else:
        response = "Lo siento, no entendí tu solicitud."

    return jsonify({'response': response})

if __name__ == '__main__':
    app.run(debug=True)
