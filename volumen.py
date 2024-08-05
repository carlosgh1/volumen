from flask import Flask, jsonify, request

app = Flask(__name__)

def calculate_perimetro(lado):
    return 4 * lado

def calculate_area(lado):
    return lado ** 2

def calculate_volume(lado):
    return lado ** 3

@app.route('/calculate', methods=['POST'])
def calculate():
    data = request.get_json()
    lado = data.get('lado')
    
    if not lado:
        return jsonify({"error": "requiere un lado"}), 400
    
    if data['type'] == 'perimetro':
        result = calculate_perimetro(lado)
        output_unit = 'perimetro'
        
    if data['type'] == 'area':
        result = calculate_area(lado)
        output_unit = 'area'
   
    if data['type'] == 'volumen':
        result = calculate_volume(lado)
        output_unit = 'volumen'
    
    
    return jsonify({
        "Calculo": result, "Tipo": output_unit
    })

if __name__ == '__main__':
    app.run(debug=False)



