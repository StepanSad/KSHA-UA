








label replay_A2:
    call iscene ("A2") from _call_iscene
    call iscene ("A2b") from _call_iscene_1
    call iscene ("A2c") from _call_iscene_2
    call iscene ("A2d") from _call_iscene_3
    call iscene ("A2f") from _call_iscene_4
    $ replay_end()



label replay_A8:
    call iscene ("A8") from _call_iscene_5
    call imenu ("choiceA8") from _call_imenu
    if _return == m1:
        call iscene ("A8a") from _call_iscene_6
        call iscene ("A8aa") from _call_iscene_7
        call iscene ("A8ab") from _call_iscene_8
    else:
        call iscene ("A8b") from _call_iscene_9
    call iscene ("A8c") from _call_iscene_10
    if seen_scene ("A8a"):
        call iscene ("A8d") from _call_iscene_11
    else:
        call iscene ("A8e") from _call_iscene_12
    call iscene ("A8f") from _call_iscene_13
    $ replay_end()



label replay_A10:
    call iscene ("A10") from _call_iscene_14
    call imenu ("choiceA10a") from _call_imenu_1
    if _return == m1:
        call iscene ("A10a") from _call_iscene_15
    elif _return == m2:
        call iscene ("A10b") from _call_iscene_16
    else:
        call iscene ("A10c") from _call_iscene_17
    $ replay_end()

label replay_A11_1:
    call iscene ("A11") from _call_iscene_18
    call iscene ("A11a") from _call_iscene_19
    call iscene ("A11b") from _call_iscene_20
    call iscene ("A11x") from _call_iscene_21
    $ replay_end()


label replay_A19:
    call iscene ("A19") from _call_iscene_22
    call iscene ("A19a") from _call_iscene_23
    call iscene ("A19c") from _call_iscene_24
    call iscene ("A19j") from _call_iscene_25
    call iscene ("A19d") from _call_iscene_26
    call iscene ("A19f") from _call_iscene_27
    call iscene ("A19g") from _call_iscene_28
    $ replay_end()


label replay_A21:
    call iscene ("A21") from _call_iscene_29
    call imenu ("choiceA21") from _call_imenu_2
    if _return == m1:
        call iscene ("A21a") from _call_iscene_30
        $ replay_end()
    call iscene ("A21b") from _call_iscene_31
    call iscene ("A21c") from _call_iscene_32
    $ replay_end()

label replay_A22:
    call iscene ("A22") from _call_iscene_33
    call iscene ("A22a") from _call_iscene_34
    $ replay_end()

label replay_A23_1:
    call iscene ("A23") from _call_iscene_35
    $ replay_end()

label replay_A23_2:
    call iscene ("A23a") from _call_iscene_36
    $ replay_end()


label replay_A24:
    call iscene ("A24") from _call_iscene_37
    call iscene ("A24d") from _call_iscene_38
    call iscene ("A24e") from _call_iscene_39
    $ replay_end()


label replay_A26:
    call iscene ("A26") from _call_iscene_40
    call iscene ("A26a") from _call_iscene_41
    call iscene ("A26e") from _call_iscene_42
    $ replay_end()

label replay_A26_1:
    call iscene ("A26b") from _call_iscene_43
    call imenu ("choiceA26") from _call_imenu_3
    if _return == m1:
        call iscene ("A26c") from _call_iscene_44
        $ replay_end()
    call iscene ("A26d") from _call_iscene_45
    $ replay_end()

label replay_A27_1:
    call iscene ("A27") from _call_iscene_46
    call iscene ("A27a") from _call_iscene_47
    call imenu ("choiceA27") from _call_imenu_4
    if _return == m1:
        call iscene ("A27b") from _call_iscene_48
        $ attraction_kenji += 1
        call iscene ("A27f") from _call_iscene_49
        $ replay_end()
    call iscene ("A27c") from _call_iscene_50
    call imenu ("choice2A27") from _call_imenu_5
    if _return == m1:
        call iscene ("A27h") from _call_iscene_51
        call iscene ("A27e") from _call_iscene_52
        $ replay_end()                                    
    call iscene ("A27i") from _call_iscene_53
    jump_out A28

label replay_A27_2:
    call iscene ("A27d") from _call_iscene_54
    call iscene ("A27e") from _call_iscene_55
    $ replay_end()

label replay_A28:
    call iscene ("A28") from _call_iscene_56
    call iscene ("A28a") from _call_iscene_57
    call iscene ("A28b") from _call_iscene_58
    $ replay_end()

label replay_A29:
    call iscene ("A29") from _call_iscene_59
    call iscene ("A29x") from _call_iscene_60
    call iscene ("A29b") from _call_iscene_61
    call iscene ("A29c") from _call_iscene_62
    $ replay_end()

label replay_A30:
    call iscene ("A30") from _call_iscene_63
    call imenu ("choiceA30") from _call_imenu_6
    if _return == m2:
        call iscene ("A30a") from _call_iscene_64
        $ replay_end()
    call iscene ("A30b") from _call_iscene_65
    call iscene ("A30c") from _call_iscene_66
    call iscene ("A30d") from _call_iscene_67
    $ replay_end()


label replay_A31:
    call iscene ("A31") from _call_iscene_68
    call iscene ("A31c") from _call_iscene_69
    call iscene ("A31d") from _call_iscene_70
    call iscene ("A31e") from _call_iscene_71
    $ replay_end()


label replay_A38:
    call iscene ("A38") from _call_iscene_72
    $ replay_end()



label replay_H7:
    call iscene ("H7") from _call_iscene_73
    call iscene ("H7a") from _call_iscene_74
    call iscene ("H7c") from _call_iscene_75
    $ replay_end()

label replay_H22:
    call iscene ("H22") from _call_iscene_76
    call imenu ("choiceH22") from _call_imenu_7
    if _return == m1:
        call iscene ("H22a") from _call_iscene_77
    else:
        call iscene ("H22c") from _call_iscene_78
    $ replay_end()

label replay_H25:
    call iscene ("H25") from _call_iscene_79
    call iscene ("H25a") from _call_iscene_80
    call iscene ("H25c") from _call_iscene_81
    $ replay_end()




label replay_E11:
    call iscene ("E11a") from _call_iscene_82
    call iscene ("E11x") from _call_iscene_83
    call iscene ("E11z") from _call_iscene_84
    call imenu ("choiceE11") from _call_imenu_8
    if _return == m1:
        call iscene ("E11b") from _call_iscene_85
    else:
        call iscene ("E11c") from _call_iscene_86
    call iscene ("E11d") from _call_iscene_87
    $ replay_end()

label replay_E12:
    call iscene ("E12a") from _call_iscene_88
    call iscene ("E12b") from _call_iscene_89
    call iscene ("E12d") from _call_iscene_90
    $ replay_end()

label replay_E18:
    call iscene ("E18") from _call_iscene_91
    call iscene ("E18a") from _call_iscene_92
    call iscene ("E18x") from _call_iscene_93
    $ replay_end()

label replay_E26:
    call iscene ("E26") from _call_iscene_94
    call iscene ("E26a") from _call_iscene_95
    call iscene ("E26b") from _call_iscene_96
    call iscene ("E26e") from _call_iscene_97
    call iscene ("E26f") from _call_iscene_98
    call imenu ("choiceE26") from _call_imenu_9
    if _return == m2:
        call iscene ("E26d") from _call_iscene_99
        $ replay_end()
    call iscene ("E26c") from _call_iscene_100
    $ replay_end()

label replay_E30:
    call iscene ("E30") from _call_iscene_101
    call iscene ("E30a") from _call_iscene_102
    call iscene ("E30b") from _call_iscene_103
    call iscene ("E30d") from _call_iscene_104
    call iscene ("E30e") from _call_iscene_105
    $ replay_end()



label replay_R11:
    call iscene ("R11") from _call_iscene_106
    call imenu ("choiceR11aaa") from _call_imenu_10
    if _return == m1:
        call iscene ("R11a") from _call_iscene_107
        call iscene ("R11g") from _call_iscene_108
    elif _return == m2:
        call iscene ("R11b") from _call_iscene_109
        call iscene ("R11i") from _call_iscene_110
    elif _return == m3:
        call iscene ("R11c") from _call_iscene_111
        call iscene ("R11h") from _call_iscene_112
    elif _return == m4:
        call iscene ("R11d") from _call_iscene_113
        call iscene ("R11i") from _call_iscene_114
    elif _return == m5:
        call iscene ("R11e") from _call_iscene_115
        call iscene ("R11h") from _call_iscene_116
    else:
        call iscene ("R11f") from _call_iscene_117
        call iscene ("R11g") from _call_iscene_118
    call iscene ("R11j") from _call_iscene_119
    $ replay_end()

label replay_R12:
    call iscene ("R12") from _call_iscene_120
    call iscene ("R12b") from _call_iscene_121
    call iscene ("R12c") from _call_iscene_122
    call iscene ("R12e") from _call_iscene_123
    call iscene ("R12f") from _call_iscene_124
    $ replay_end()

label replay_R16:
    call iscene ("R16") from _call_iscene_125
    call imenu ("choiceR16") from _call_imenu_11
    if _return == m1:
        call iscene ("R16a") from _call_iscene_126
    else:
        call iscene ("R16b") from _call_iscene_127
    call iscene ("R16c") from _call_iscene_128
    call iscene ("R16d") from _call_iscene_129
    call iscene ("R16e") from _call_iscene_130
    $ replay_end()

label replay_R19:
    call iscene ("R19") from _call_iscene_131
    call iscene ("R19a") from _call_iscene_132
    call iscene ("R19b") from _call_iscene_133
    $ replay_end()

label replay_R28:
    call iscene ("R28") from _call_iscene_134
    call imenu ("choiceR28_1") from _call_imenu_12
    if _return == m1:
        call iscene ("R28a") from _call_iscene_135
    elif _return == m2:
        call iscene ("R28b") from _call_iscene_136
    else:
        $ replay_end()
    call iscene ("R28c") from _call_iscene_137
    $ replay_end()

label replay_R30:
    call iscene ("R30") from _call_iscene_138
    call iscene ("R30y") from _call_iscene_139
    call iscene ("R30z") from _call_iscene_140
    $ replay_end()

label replay_R36:
    call iscene ("R36") from _call_iscene_141
    call iscene ("R36a") from _call_iscene_142
    call iscene ("R36x") from _call_iscene_143
    $ replay_end()


label replay_S17:
    call iscene ("S17") from _call_iscene_144
    call iscene ("S17a") from _call_iscene_145
    call iscene ("S17x") from _call_iscene_146
    $ replay_end()

label replay_S22:
    call iscene ("S22") from _call_iscene_147
    call iscene ("S22a") from _call_iscene_148
    call iscene ("S22c") from _call_iscene_149
    call iscene ("S22h", is_h=True) from _call_iscene_150
    call iscene ("S22x") from _call_iscene_151
    $ replay_end()

label replay_S23:
    call iscene ("timeskip") from _call_iscene_152
    call iscene ("S23") from _call_iscene_153
    call iscene ("S23a") from _call_iscene_154
    call iscene ("S23x") from _call_iscene_155
    $ replay_end()

label replay_S26:
    call iscene ("S26") from _call_iscene_156
    call iscene ("S26a") from _call_iscene_157
    call iscene ("S26c") from _call_iscene_158
    $ replay_end()

label replay_S29_2:
    call iscene ("S29") from _call_iscene_159
    call iscene ("S29b") from _call_iscene_160
    call iscene ("S29x") from _call_iscene_161
    call iscene ("S29xb") from _call_iscene_162
    call iscene ("S29xba") from _call_iscene_163
    call iscene ("S29xbc") from _call_iscene_164
    call iscene ("S29y") from _call_iscene_165
    call iscene ("S29yb") from _call_iscene_166
    $ replay_end()

label replay_S34:
    call iscene ("S34") from _call_iscene_167
    call iscene ("S34b") from _call_iscene_168
    call iscene ("S34c") from _call_iscene_169
    $ replay_end()
