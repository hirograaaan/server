from flask import Flask, request, render_template
app = Flask(__name__)
file_path = "./final_sensor_data.csv"
port_num = 21013

@app.route('/', methods=['GET'])
def get_html():
  return render_template('./final_index.html')


@app.route('/temp', methods=['POST'])
def update_temp():
  time = request.form["time"]
  temp = request.form["temp"]

  try:
    f = open(file_path, 'w')
    f.write(time + "," + temp)
    return "succeeded to write"
  except Exception as e:
    print(e)
    return "failed to write"
  finally:
    f.close()

@app.route('/temp', methods=['GET'])
def get_temp():
  try:
    f = open(file_path, 'r')
    for row in f:
      temp = row
  except Exception as e:
    print(e)
  finally:
    f.close()
    return temp
  

if __name__ == '__main__':
  app.run(debug=True, host='0.0.0.0', port=port_num)