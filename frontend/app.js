const startBtn = document.getElementById('start-btn');
const transcriptEl = document.getElementById('transcript');
const responseEl = document.getElementById('response');

let recognition;
let recognizing = false;

// Inicializar reconocimiento de voz
function initRecognition() {
    if (!('webkitSpeechRecognition' in window) && !('SpeechRecognition' in window)) {
        alert("Tu navegador no soporta reconocimiento de voz.");
        return;
    }

    const SpeechRecognition = window.SpeechRecognition || window.webkitSpeechRecognition;
    recognition = new SpeechRecognition();

    recognition.lang = 'es-PE'; // Español Perú
    recognition.interimResults = false;
    recognition.maxAlternatives = 1;

    recognition.onstart = () => {
        recognizing = true;
        startBtn.textContent = "Detener Reconocimiento";
    };

    recognition.onresult = async (event) => {
        const text = event.results[0][0].transcript;
        transcriptEl.textContent = text;
        // Enviar texto al backend para procesar
        const response = await fetch('http://127.0.0.1:5000/api/process', {
            method: 'POST',
            headers: { 'Content-Type': 'application/json' },
            body: JSON.stringify({ text })
        });
        const data = await response.json();
        responseEl.textContent = data.response;
        speakText(data.response);
    };

    recognition.onerror = (event) => {
        console.error(event.error);
        recognizing = false;
        startBtn.textContent = "Iniciar Reconocimiento";
    };

    recognition.onend = () => {
        recognizing = false;
        startBtn.textContent = "Iniciar Reconocimiento";
    };
}

function speakText(text) {
    if (!('speechSynthesis' in window)) {
        return;
    }
    const utterance = new SpeechSynthesisUtterance(text);
    utterance.lang = 'es-PE';
    speechSynthesis.speak(utterance);
}

startBtn.addEventListener('click', () => {
    if (!recognition) {
        initRecognition();
    }

    if (recognizing) {
        recognition.stop();
    } else {
        recognition.start();
    }
});
