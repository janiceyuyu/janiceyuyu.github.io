import urllib.request as request
import json
src="https://padax.github.io/taipei-day-trip-resources/taipei-attractions-assignment.json"
with request.urlopen(src) as response:
    data=json.loads(response.read().decode("utf-8"))
slist=data["result"]["results"]

with open("attraction.csv","w",encoding="utf-8") as file:
    for i in slist:
        file_text = i["file"].lower()
        start_index = file_text.find("https://")  
        end_index = file_text.find(".jpg", start_index)  
        first_image_text = file_text[start_index:end_index+4]
        
        file.write(i["stitle"]+","
                +i["address"][5:8]+","
                +i["longitude"]+","
                +i["latitude"]+","
                +first_image_text
                +"\n")

mrt_stitle_dict = {}  

for a in slist:
    mrt_value = a["MRT"]
    if mrt_value is not None:
        stitle_value = a["stitle"]
        if mrt_value in mrt_stitle_dict:
            mrt_stitle_dict[mrt_value].append(stitle_value)  
        else:
            mrt_stitle_dict[mrt_value] = [stitle_value]  

with open("mrt.csv", "w", encoding="utf-8") as file:
    for mrt, stitles in mrt_stitle_dict.items():
        stitles_str = ",".join(stitles)  
        line = f"{mrt},{stitles_str}\n"
        file.write(line)