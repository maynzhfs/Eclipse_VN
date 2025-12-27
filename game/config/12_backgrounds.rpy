## ----------------------------------------------------
## 12_BACKGROUNDS.RPY: AUTOLOAD BACKGROUNDS (FULLSCREEN)
## ----------------------------------------------------

define default_bg_transition = Fade(0.5, 0.0, 0.5)

init python:
    import os
    
    BG_PATH_PREFIX = "images/backgrounds/"
    
    all_files = renpy.list_files()
    
    for full_path in all_files:
        if full_path.startswith(BG_PATH_PREFIX):
            filename = os.path.basename(full_path)
            
            if filename.lower().endswith(('.jpg', '.png', '.jpeg')):
                tag = os.path.splitext(filename)[0].lower()
                
                renpy.image(
                    tag,
                    im.Scale(
                        full_path,
                        config.screen_width,
                        config.screen_height
                    )
                )
