from flask import Flask

app = Flask(__name__)

@app.route("/")
def status():
    return {
        "message": "Teste"
    }

@app.route("/health")
def health():
    return {
        "status": "ok"
    }

@app.route("/status")
def service_status():
    return {
        "status": "online",
        "service": "OpsTrack API"
    }

@app.route("/tickets")
def tickets():
    return {
        "tickets": [
            {
                "id": 1,
                "title": "Servidor indisponível",
                "status": "aberto"
            },
            {
                "id": 2,
                "title": "Erro no sistema de login",
                "status": "em andamento"
            },
            {
                "id": 3,
                "title": "Atualização de software",
                "status": "fechado"
            }
        ]
    }

@app.route("/sobre")
def sobre():
    return {
        "name": "OpsTrack API",
        "version": "1.0.0"
    }

if __name__ == "__main__":
    app.run(debug=True)