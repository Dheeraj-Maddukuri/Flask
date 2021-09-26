# Flask
## Get all the text which lie inside a rectangle in the natural reading order (top to bottom, left to right).

### Problem :
The user will provide a rectangle [x0_user, y0_user, x2_user, y2_user] and the CSV file name as inputs.
We need to read the appropriate file and get all the text that lies inside this rectangle in the natural reading order (top to bottom, left to right).
The csv file contains (x0, y0), (x2, y2) and the text 
where 
    x0: The top left x-coordinate of the text.
    y0:  The top left y-coordinate of the text.
    x2:  The bottom right x-coordinate of the text.
    y2:  The bottom right y-coordinate of the text.
    Text: The text is present in the rectangle pointed by the (x0,y0) and (x2,y2) coordinates

The Flask app has the endpoint  /search/text/
This endpoint will accept POST request with the following JSON body:
 {“file_name”: "<name_of_the_csv_file>", “position”: [x0_user, y0_user, x2_user, y2_user]}
 The JSON response will be as follows:
{"text": "<All the Text that lie inside the rectangle given by the user>"}
