from experta import *

class Diagnosis(Fact):
    """Fact class representing a single symptom input."""
    symptom = Field(str)

class PestDiseaseExpert(KnowledgeEngine):
    def __init__(self, input_symptoms, rules_data):
        super().__init__()
        self.input_symptoms = input_symptoms
        self.rules_data = rules_data
        self.diagnosis_result = []
        self.reset()

    @Rule(Diagnosis(symptom=MATCH.symptom))
    def process_symptom(self, symptom):
        """Match each symptom with diagnosis from rules_data."""
        for rule in self.rules_data:
            if symptom.strip().lower() == rule['symptom'].strip().lower():
                self.diagnosis_result.append(rule['diagnosis'])

    def diagnose(self):
        """Run the engine with declared symptoms."""
        for s in self.input_symptoms:
            self.declare(Diagnosis(symptom=s))
        self.run()
        return self.diagnosis_result
