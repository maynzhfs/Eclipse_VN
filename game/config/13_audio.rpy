init python:
    renpy.music.register_channel("ambience", mixer="ambience", loop=True)
    
label play_music(file_name, volume=1.0, fade_time=1.5, loop=True):
    $ renpy.music.set_volume(volume, channel="music")
    $ renpy.music.play(file_name, channel="music", fadein=fade_time, loop=loop)
    return

label stop_music(fade_time=1.5):
    $ renpy.music.stop(channel="music", fadeout=fade_time)
    return
    
label change_music(file_name, volume=1.0, fade_time=1.5):
    $ renpy.music.set_volume(volume, channel="music")
    $ renpy.music.play(file_name, channel="music", fadein=0.0, fadeout=fade_time)
    return

label play_sfx(file_name, volume=1.0):
    $ renpy.sound.play(file_name, channel="sound", volume=volume)
    return

label play_ambience(file_name, volume=0.7, fade_time=3.0, loop=True):
    $ renpy.music.set_volume(volume, channel="ambience")
    $ renpy.music.play(file_name, channel="ambience", fadein=fade_time, loop=loop)
    return

label stop_ambience(fade_time=3.0):
    $ renpy.music.stop(channel="ambience", fadeout=fade_time)
    return