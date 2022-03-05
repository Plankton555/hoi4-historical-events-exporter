import json

TAB = "  "
NL = "\n"
ALPH = "abcdefghijkl"


def main():
    json_file = "events/he_ethiopian_war.json"
    data = None
    with open(json_file, "r") as f:
        data = json.load(f)

    if data is None:
        print("could not read data")
        return
    # print(json.dumps(data, indent=2))

    id_ctr = 1
    default_picture = data["default_picture"]
    for event in data["events"]:
        gfx_picture = default_picture
        if event["picture"] is not None:
            gfx_picture = event["picture"]
        out_text = ""
        id_ctr += 1
        out_text += "news_event = { # HIDDEN" + NL
        out_text += TAB + "id =  he_news." + str(id_ctr) + NL
        out_text += TAB + "hidden = yes" + NL
        out_text += TAB + "fire_only_once = yes" + NL
        out_text += TAB + "mean_time_to_happen = { days = 1 }" + NL
        out_text += TAB + "trigger = {" + NL
        out_text += TAB + TAB + "check_variable = { he_show_ethiopia_war = 1 }" + NL
        out_text += TAB + TAB + "date > " + event["date"] + " # " + event["title"] + NL
        out_text += TAB + "}" + NL
        out_text += TAB + "immediate = {" + NL
        out_text += TAB + TAB + "URG = { news_event = { id = he_news." + str(id_ctr + 1) + " days = 1 } }" + NL
        out_text += TAB + "}" + NL
        out_text += "}" + NL

        id_ctr += 1
        out_text += "news_event = {" + NL
        out_text += TAB + "id =  he_news." + str(id_ctr) + NL
        out_text += TAB + "title = he_news." + str(id_ctr) + ".t" + NL
        out_text += TAB + "desc = he_news." + str(id_ctr) + ".d" + NL
        out_text += TAB + "picture = " + gfx_picture + NL
        out_text += TAB + "major = yes" + NL
        out_text += TAB + "is_triggered_only = yes" + NL
        out_text += TAB + "option = {" + NL
        for i in range(len(event["options"])):
            out_text += TAB + TAB + "name = he_news." + str(id_ctr) + "." + ALPH[i] + NL
        out_text += TAB + "}" + NL
        out_text += "}" + NL

        print(out_text)


if __name__ == "__main__":
    main()
