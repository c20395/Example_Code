# Example 7.41 Pixellib background editing

import pixellib
from pixellib.tune_bg import alter_bg

change_bg = alter_bg(model_type="pb")
change_bg.load_pascalvoc_model("xception_pascalvoc.pb")
change_bg.change_video_bg("person.mp4", "londoneye.jpg", frames_per_second = 10, output_video_name="output_video.mp4", detect = "person")
