import json

TAB = "  "
NL = "\n"
ALPH = "abcdefghijkl"


def generate_event(event, default_picture, loc_strings, id_ctr):
    prefix = "he_news"
    id_hidden = str(id_ctr)
    id_shown = str(id_ctr + 1)
    gfx_picture = default_picture
    if event["picture"] is not None:
        gfx_picture = event["picture"]
    out_text = ""
    out_text += "news_event = { # HIDDEN" + NL
    out_text += TAB + "id =  " + prefix + "." + id_hidden + NL
    out_text += TAB + "hidden = yes" + NL
    out_text += TAB + "fire_only_once = yes" + NL
    out_text += TAB + "mean_time_to_happen = { days = 1 }" + NL
    out_text += TAB + "trigger = {" + NL
    # TODO extract me!!!
    out_text += TAB + TAB + "check_variable = { he_show_ethiopia_war = 1 }" + NL
    out_text += TAB + TAB + "date > " + event["date"] + " # " + event["title"] + NL
    out_text += TAB + "}" + NL
    out_text += TAB + "immediate = {" + NL
    out_text += TAB + TAB + "URG = { news_event = { id = he_news." + id_shown + " days = 1 } }" + NL
    out_text += TAB + "}" + NL
    out_text += "}" + NL

    out_text += "news_event = {" + NL
    loc_title = prefix + "." + id_shown + ".t"
    loc_desc = prefix + "." + id_shown + ".d"
    event_title = event["date"] + " - " + event["title"]
    event_desc = event["desc"]
    loc_strings.append(f"{loc_title}: \"{event_title}\"")
    loc_strings.append(f"{loc_desc}: \"{event_desc}\"")
    out_text += TAB + "id =  " + prefix + "." + id_shown + NL
    out_text += TAB + "title = " + loc_title + NL
    out_text += TAB + "desc = " + loc_desc + NL
    out_text += TAB + "picture = " + gfx_picture + NL
    out_text += TAB + "major = yes" + NL
    out_text += TAB + "is_triggered_only = yes" + NL
    out_text += TAB + "option = {" + NL
    for i in range(len(event["options"])):
        text_option = event["options"][i]["text"]
        loc_option = prefix + "." + id_shown + "." + ALPH[i]
        out_text += TAB + TAB + "name = " + loc_option + NL
        loc_strings.append(f"{loc_option}: \"{text_option}\"")
    out_text += TAB + "}" + NL
    out_text += "}" + NL

    return out_text


def main():
    json_file = "events/he_ethiopian_war.json"
    data = None
    with open(json_file, "r") as f:
        data = json.load(f)

    if data is None:
        print("could not read data")
        return
    # print(json.dumps(data, indent=2))

    loc_strings = []
    event_texts = []
    id_ctr = 1
    default_picture = data["default_picture"]
    for event in data["events"]:
        event_text = generate_event(event, default_picture, loc_strings, id_ctr)
        event_texts.append(event_text)
        id_ctr += 2

    print("*** EVENT TEXTS ***")
    for event_text in event_texts:
        print(event_text)

    print("*** LOC STRINGS ***")
    for loc_string in loc_strings:
        print(loc_string)


if __name__ == "__main__":
    main()
