init -2 python:
    def named_config():
        config.file_entry_format = (('%(time)s // ') + (displayStrings.play_time_label)) + (': %(playtime)s\n%(save_name)s')
        config.time_format = displayStrings.timeformat
        config.window_title = displayStrings.window_name
        config.main_menu = [(displayStrings.main_menu_start, ui.jumps('start_from_mm', 'game_main_transition'), 'True'), (displayStrings.main_menu_load, ui.jumps('load_screen', 'main_game_transition'), 'renpy.list_saved_games()'), (displayStrings.main_menu_extra, ui.jumps('extra_from_mm'), 'get_available_scenes() or get_available_music() or get_available_images()'), (displayStrings.main_menu_config, ui.jumps('prefs_screen', 'main_game_transition'), 'True'), (displayStrings.main_menu_credits, ui.jumps('show_credits'), 'True'), (displayStrings.main_menu_quit, ui.jumps('softquit'), 'True')]
        config.game_menu = [('return', displayStrings.game_menu_return, ui.jumps('_return'), 'True'), ('gm_image', displayStrings.game_menu_show, ui.jumps('gm_image'), 'True'), ('gm_image', displayStrings.game_menu_history, ui.jumps('text_history_gm', 'intra_transition'), 'True'), ('skipping', displayStrings.game_menu_skip, ui.jumps('_return_skipping'), 'config.allow_skipping and not mm_context()'), ('automode', displayStrings.game_menu_auto, ui.jumps('afm_on'), 'True'), ('prefs', displayStrings.game_menu_config, ui.jumps('prefs_screen', 'intra_transition'), 'True'), ('save', displayStrings.game_menu_save, ui.jumps('save_screen', 'intra_transition'), 'playthroughflag and not mm_context()'), ('load', displayStrings.game_menu_load, ui.jumps('load_screen', 'intra_transition'), 'renpy.list_saved_games()'), ('mainmenu', displayStrings.game_menu_main, ui.jumps('confirm_mm', 'intra_transition'), 'not mm_context()'), ('quit', displayStrings.game_menu_quit, ui.jumps('confirm_quit', 'intra_transition'), 'True')]
        config.joystick_keys = [(displayStrings.joy_left, 'joy_left'), (displayStrings.joy_right, 'joy_right'), (displayStrings.joy_up, 'joy_up'), (displayStrings.joy_down, 'joy_down'), (displayStrings.joy_dismiss, 'joy_dismiss'), (displayStrings.joy_rollback, 'joy_rollback'), (displayStrings.joy_holdskip, 'joy_holdskip'), (displayStrings.joy_toggleskip, 'joy_toggleskip'), (displayStrings.joy_hide, 'joy_hide'), (displayStrings.joy_menu, 'joy_menu')]

init 2 python:
    def get_available_music():
        available_music = []
        for (title, filename) in ex_m_tracks:
            if (renpy.seen_audio(filename) or filename.count('bonus') > 0  or has_devlvl()):
                available_music.append(filename)
        if (len(available_music)) > (1):
            return available_music
        else:
            return False

    ks_music('Anfang_(bonus_by_Ajoura)', 'bonus')
    ks_music('Heiterkeit_(bonus_by_Ajoura)', 'bonus')
    ks_music('Invisible_Snow_(bonus_by_Ajoura)', 'bonus')
    ks_music('Magnet_Mind_(bonus_by_Ajoura)', 'bonus')
    ks_music('Nine_(bonus_by_Ajoura)', 'bonus')
    ks_music('Soft_Machine_(bonus_by_Ajoura)', 'bonus')
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
