def sound_play_cooldown(sound, time_counter, cooldown=0):
    """
    Joue un son avec un cooldown
    :param sound: Son voulu
    :param time_counter: timer correspondant au cooldown du son
    :param cooldown: optionel cooldown manuel

    :return: Nouveau Timer
    ex utilisation:
    self.step_sound_timer -= elapsed #temps entre 2 frames
    self.step_sound_timer = sound_play_cooldown(step_sound,self.step_sound_timer,self.scene.elapsed)
    """
    if time_counter <= 0:
        sound.play(fade_ms=20)
        if cooldown == 0:
            return sound.get_length() * 1000
        else:
            return cooldown
    else:
        return time_counter
