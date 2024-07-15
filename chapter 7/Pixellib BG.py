# Example 7.43 Pixellib background editing
import pixellib
from pixellib.tune_bg import alter_bg

change_bg = alter_bg(model_type = "pb")
change_bg.load_pascalvoc_model("xception_pascalvoc.pb")
change_bg.blur_bg("person1.jpeg", extreme = True, detect = "person", output_image_name="out.jpg")
