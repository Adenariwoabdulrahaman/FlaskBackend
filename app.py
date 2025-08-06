from flask import Flask, request, jsonify # type: ignore
from flask_cors import CORS # type: ignore
from db_config import get_db_connection
from rules import PestDiseaseExpert

app = Flask(__name__)
CORS(app)

def get_rules_data():
    print("Fetching rules data from SQLite...")
    conn = get_db_connection()

    if not conn:
        return []

    try:
        cursor = conn.cursor()
        query = """
        SELECT s.name AS symptom, d.name AS diagnosis, d.type, d.treatment
        FROM rules r
        JOIN symptoms s ON r.symptom_id = s.id
        JOIN diagnoses d ON r.diagnosis_id = d.id
        """
        cursor.execute(query)
        rows = cursor.fetchall()
        return [dict(row) for row in rows]
    except Exception as e:
        print("Error fetching rules data:", e)
        return []
    finally:
        conn.close()

@app.route("/diagnose", methods=["POST"])
def diagnose():
    data = request.json
    symptoms = data.get("symptoms", [])
    print("Received symptoms from frontend:", symptoms)

    rules_data = get_rules_data()
    if not rules_data:
        return jsonify([{
            "diagnosis": "Error",
            "type": "",
            "treatment": "Could not connect to database."
        }]), 500

    engine = PestDiseaseExpert(symptoms, rules_data)
    results = engine.diagnose()

    if not results:
        return jsonify([{
            "diagnosis": "Symptom not recognized",
            "type": "",
            "treatment": "Please check your input or try a different symptom."
        }]), 200

    unique_results = []
    seen = set()
    for r in results:
        if r not in seen:
            seen.add(r)
            diagnosis = next((item for item in rules_data if item['diagnosis'] == r), None)
            if diagnosis:
                unique_results.append(diagnosis)

    return jsonify(unique_results), 200

@app.route("/symptoms", methods=["GET"])
def get_symptoms():
    print("Fetching symptom list...")
    conn = get_db_connection()
    if not conn:
        return jsonify({"error": "Database connection failed"}), 500

    try:
        cursor = conn.cursor()
        cursor.execute("SELECT name FROM symptoms")
        symptoms = [row["name"] for row in cursor.fetchall()]
        print(f"✅ Symptoms fetched: {symptoms}")
        return jsonify(symptoms), 200
    except Exception as e:
        print("Error fetching symptoms:", e)
        return jsonify({"error": "Failed to fetch symptoms"}), 500
    finally:
        conn.close()

if __name__ == "__main__":
    app.run(host='0.0.0.0', debug=True)
    