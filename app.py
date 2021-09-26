import os
import csv
from flask import Flask, request



app = Flask(__name__) #Creating the Flask Class Object



def does_text_lie_inside_rectangle(rectangle_position, text_position) :

    r_x0, r_y0, r_x2, r_y2 = rectangle_position
    t_x0, t_y0, t_x2, t_y2 = text_position

    """
    If the Text Lies inside the Rectange, Then its bottom-left coordinates will be greater than the rectangle's bottom-left coordinates and
    Its top-left coordinates will be less than the rectangle's top-left coordinates.
    """
    if (((t_x0 > r_x0) and (t_y0 > r_y0)) and ((t_x2 < r_x2) and (t_y2 < r_y2))) :
        return True
    else :
        return False



def get_text_inside_rectange(file_name, rectangle_position) :

    texts = []
    basepath = ""
    file_path = os.path.join(basepath, file_name)
    if (os.path.exists(file_path)) :
        with open(file_path, "r") as csv_file :
            csv_reader = csv.reader(csv_file, delimiter = ",", lineterminator = "\n")
            
            next(csv_reader)
            
            for row in csv_reader :
                text = row[4]
                text_position = row[0 : 4]
                text_position = [int(i) for i in text_position]
                if(does_text_lie_inside_rectangle(rectangle_position, text_position)) :
                    texts.append(text)

    texts_str = " ".join(texts)

    return texts_str



@app.route("/search/text/", methods = ["POST"])
def search():
    request_data = request.get_json()

    file_name = request_data["file_name"]
    position = request_data["position"]

    text = get_text_inside_rectange(file_name, position)

    data = {"text" : text}
    return data



if __name__ == "__main__" :
    app.run(debug = True)