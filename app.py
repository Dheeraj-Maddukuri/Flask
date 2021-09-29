import os
import csv
from flask import Flask, request



app = Flask(__name__) #Creating the Flask Class Object



def does_text_lie_inside_rectangle(rectangle_position, text_position) :

    r_x0, r_y0, r_x2, r_y2 = rectangle_position
    t_x0, t_y0, t_x2, t_y2 = text_position

    if (((t_x0 >= r_x0) and (t_y0 >= r_y0)) and ((t_x2 <= r_x2) and (t_y2 <= r_y2))) :
        """
        Validation to check if the text lies completely inside the user rectangle.
        If the Text Lies inside the Rectange, Then its top-left coordinates will be greater than the rectangle's top-left coordinates and
        Its bottom-right coordinates will be less than the rectangle's bottom-right coordinates.
        If it is completely inside, return True.
        """
        return True
    elif ((t_x2 <= r_x0) or (t_x0 >= r_x2) or (t_y2 <= r_y0) or (t_y0 >= r_y2)) :
        """
        Validation to check if the text completely outside the rectangle.
        If it lies away from the rectangle, return False
        """
        return False
    else :
        """
        Text is neither completely inside nor completely outside.
        It is partially inside the user rectangle.
        Check if Major portion of the text lies inside the rectangle. Which means, if more than 50% of its area lies inside the user rectangle, then return True.
        If Minor portion of the text (less than 50%) of its total area, lies inside the user rectangle, Then ignore the text and return False
        """
        text_total_length = (t_x2 - t_x0)
        text_total_breadth = (t_y2 - t_y0)
        text_total_area = (text_total_length * text_total_breadth)

        left_bound = (t_x0 if (t_x0 > r_x0) else r_x0) # Take the Left Boundary to calculate length inside the user rectangle.
        right_bound = (t_x2 if (t_x2 < r_x2) else r_x2) # Take the Right Boundary to calculate length inside the user rectangle.
        upper_bound = (t_y0 if (t_y0 > r_y0) else r_y0) # Take the Upper Boundary to calculate breadth inside the user rectangle.
        lower_bound = (t_y2 if (t_y2 < r_y2) else r_y2) # Take the Lower Boundary to calculate breadth inside the user rectangle.
        text_length_inside_user_rectangle = (right_bound - left_bound) # Text Length inside user rectangle.
        text_breadth_inside_user_rectangle = (lower_bound - upper_bound) # Text Breadth inside user rectangle.
        text_area_inside_user_rectangle = (text_length_inside_user_rectangle * text_breadth_inside_user_rectangle) # Text Area inside user rectangle
        percentage_text_area_inside_user_rectangle = ((text_area_inside_user_rectangle/text_total_area) * 100) # Percentage Text Area inside user rectangle.
        if (percentage_text_area_inside_user_rectangle >= 50) :
            return True
        else :
            return False



def get_text_inside_rectange(file_name, rectangle_position) :

    texts = []
    """
    basepath = ""
    file_path = os.path.join(basepath, file_name)
    """
    file_path = file_name
    if (os.path.exists(file_path)) :
        with open(file_path, "r") as csv_file :
            csv_reader = csv.reader(csv_file, delimiter = ",", lineterminator = "\n")
            
            next(csv_reader)
            
            for row in csv_reader :
                text = row[4:]
                text = "".join(text)
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
    app.run(host = "0.0.0.0", port = 5000, debug = True)