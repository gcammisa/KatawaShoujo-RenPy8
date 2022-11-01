label imachine:
    jump_out NOP1

label NOP1:
    call iscene ("NOP1") from _call_iscene
    jump_out op_video

label op_video:
    call iscene ("op_vid1") from _call_iscene_1
    jump_out NOP2

label NOP2:
    call iscene ("NOP2") from _call_iscene_2
    jump_out tc_act1

label tc_act1:
    if not renpy.ios:
        call act_op ("base_tc_act1.mp4") from _call_act_op
    else:
        call act_op ("ios_tc_act1.mp4") from _call_act_op
    jump_out A1

label A1:
    call iscene ("A1") from _call_iscene_3
    call imenu ("choiceA1") from _call_imenu

    if _return == m1:

        call iscene ("A1a") from _call_iscene_4
    else:

        $ attraction_sc += 1
        call iscene ("A1b") from _call_iscene_5
    call iscene ("A1c") from _call_iscene_6
    jump_out A2

label A2:
    call iscene ("A2") from _call_iscene_7
    if seen_scene ("A1a"):
        call iscene ("A2a") from _call_iscene_8
    else:
        call iscene ("A2b") from _call_iscene_9
    call iscene ("A2c") from _call_iscene_10
    if seen_scene ("A1b"):
        call iscene ("A2d") from _call_iscene_11
    else:
        call iscene ("A2e") from _call_iscene_12
    call iscene ("A2f") from _call_iscene_13
    jump_out A3

label A3:
    call iscene ("A3") from _call_iscene_14
    call imenu ("choiceA3") from _call_imenu_1
    if _return == m1:

        $ attraction_hanako += 1
        call iscene ("A3a") from _call_iscene_15
    elif _return == m2:

        call iscene ("A3b") from _call_iscene_16
    else:

        $ attraction_sc += 1
        call iscene ("A3c") from _call_iscene_17
    call iscene ("A3d") from _call_iscene_18
    jump_out A4

label A4:
    call iscene ("A4") from _call_iscene_19
    jump_out A5

label A5:
    call iscene ("timeskip") from _call_iscene_20
    call iscene ("A5") from _call_iscene_21
    jump_out A6

label A6:
    call iscene ("A6") from _call_iscene_22
    call imenu ("choiceA6") from _call_imenu_2

    if _return == m1:

        $ attraction_sc += 1
        call iscene ("A6a") from _call_iscene_23
    else:
        call iscene ("A6b") from _call_iscene_24
    call iscene ("A6c") from _call_iscene_25
    jump_out A7

label A7:
    call iscene ("A7") from _call_iscene_26
    jump_out A8

label A8:
    call iscene ("A8") from _call_iscene_27
    call imenu ("choiceA8") from _call_imenu_3

    if _return == m1:
        call iscene ("A8a") from _call_iscene_28

        if seen_scene("A1b"):
            call iscene ("A8aa") from _call_iscene_29
        call iscene ("A8ab") from _call_iscene_30
    else:

        $ attraction_hanako +=1
        call iscene ("A8b") from _call_iscene_31
    call iscene ("A8c") from _call_iscene_32
    if seen_scene ("A8a"):
        call iscene ("A8d") from _call_iscene_33
    else:
        call iscene ("A8e") from _call_iscene_34
    call iscene ("A8f") from _call_iscene_35
    jump_out A9

label A9:
    call iscene ("A9") from _call_iscene_36
    call imenu ("choiceA9") from _call_imenu_4
    if _return == m1:

        $ attraction_hanako += 1
        call iscene ("A9a") from _call_iscene_37
    else:

        call iscene ("A9b") from _call_iscene_38
    call iscene ("A9c") from _call_iscene_39
    jump_out A10

label A10:
    call iscene ("timeskip") from _call_iscene_40
    call iscene ("A10") from _call_iscene_41
    if attraction_sc > 1 and attraction_hanako > 1:
        call imenu ("choiceA10a") from _call_imenu_5
        if _return == m1:
            call iscene ("A10a") from _call_iscene_42
        elif _return == m2:
            call iscene ("A10b") from _call_iscene_43
            jump_out A11_2
        else:
            call iscene ("A10c") from _call_iscene_44
    elif attraction_sc > 1:
        call imenu ("choiceA10b") from _call_imenu_6
        if _return == m1:
            call iscene ("A10c") from _call_iscene_45
        else:
            call iscene ("A10a") from _call_iscene_46
    elif attraction_hanako > 1:
        call imenu ("choiceA10c") from _call_imenu_7
        if _return == m1:
            call iscene ("A10a") from _call_iscene_47
        else:
            call iscene ("A10b") from _call_iscene_48
            jump_out A11_2
    else:
        call iscene ("A10a") from _call_iscene_49
    jump_out A11_1

label A11_1:
    call iscene ("A11") from _call_iscene_50
    call iscene ("A11a") from _call_iscene_51
    call iscene ("A11b") from _call_iscene_52
    if seen_scene ("A10c"):
        call iscene ("A11x") from _call_iscene_53
        jump_out A12
    call iscene ("A11y") from _call_iscene_54
    jump_out A15


label A11_2:
    call iscene ("A11c") from _call_iscene_55
    call iscene ("A11a") from _call_iscene_56
    call iscene ("A11d") from _call_iscene_57
    jump_out A13

label A12:
    call iscene ("A12") from _call_iscene_58
    jump_out A16 

label A13:
    call iscene ("A13") from _call_iscene_59
    jump_out A15

label A15:
    call iscene ("A15") from _call_iscene_60
    jump_out A16

label A16:
    call iscene ("A16") from _call_iscene_61
    jump_out A17

label A17:
    call iscene ("A17") from _call_iscene_62
    call imenu ("choiceA17") from _call_imenu_8

    if _return == m1:

        call iscene ("A17a") from _call_iscene_63
    else:

        call iscene ("A17b") from _call_iscene_64
    call iscene ("A17c") from _call_iscene_65
    jump_out A18

label A18:
    call iscene ("A18") from _call_iscene_66
    jump_out A19

label A19:
    call iscene ("timeskip") from _call_iscene_67
    call iscene ("A19") from _call_iscene_68
    if seen_scene ("A17a"):
        call iscene ("A19a") from _call_iscene_69
    else:
        call iscene ("A19b") from _call_iscene_70
    call iscene ("A19c") from _call_iscene_71
    if seen_scene ("A11b"):
        call iscene ("A19i") from _call_iscene_72
    call iscene ("A19j") from _call_iscene_73
    if seen_scene ("A17a"):
        call iscene ("A19d") from _call_iscene_74
    else:
        call iscene ("A19e") from _call_iscene_75
    call iscene ("A19f") from _call_iscene_76
    if seen_scene ("A17a"):
        call iscene ("A19g") from _call_iscene_77
    else:
        call iscene ("A19h") from _call_iscene_78
    jump_out A20

label A20:
    call iscene ("A20") from _call_iscene_79
    jump_out A21

label A21:
    call iscene ("A21") from _call_iscene_80
    call imenu ("choiceA21") from _call_imenu_9

    if _return == m1:

        call iscene ("A21a") from _call_iscene_81
        jump_out A22
    call iscene ("A21b") from _call_iscene_82
    if seen_scene ("A13"):
        call iscene ("A21c") from _call_iscene_83
    else:
        call iscene ("A21d") from _call_iscene_84
    jump_out A23

label A22:
    call iscene ("A22") from _call_iscene_85
    if not seen_scene ("A12"):
        call iscene ("A22a") from _call_iscene_86
        jump_out A23
    jump_out A22_2

label A22_2:
    call iscene ("A22b") from _call_iscene_87
    if seen_scene ("A21c"):

        jump_out A24
    jump_out A24_1

label A23:
    if not seen_scene ("A22a"):
        jump_out A23_1
    if not seen_scene ("A21c"):
        jump_out A23_2
    jump_out A24 

label A23_1:
    call iscene ("A23") from _call_iscene_88
    if seen_scene ("A21c"):
        jump_out A24
    jump_out A23_2

label A23_2:
    call iscene ("A23a") from _call_iscene_89
    if seen_scene ("A21c"):
        jump_out A24
    jump_out A24_1

label A24:
    call iscene ("A24") from _call_iscene_90
    if seen_scene ("A21a"):

        call iscene ("A24c") from _call_iscene_91
    else:
        call iscene ("A24d") from _call_iscene_92
    call iscene ("A24e") from _call_iscene_93
    jump_out A24_1

label A24_1:
    if seen_scene("A17a"):
        call iscene ("A24a") from _call_iscene_94
        jump_out A25
    call iscene ("A24b") from _call_iscene_95
    jump_out A26


label A25:
    call iscene ("timeskip") from _call_iscene_96
    call iscene ("A25") from _call_iscene_97
    call imenu ("choiceA25") from _call_imenu_10
    if _return == m1:
        call iscene ("A25b") from _call_iscene_98
        jump_out A27
    call iscene ("A25a") from _call_iscene_99
    jump_out A26

label A26:
    if not seen_scene ("A25"):
        call iscene ("timeskip") from _call_iscene_100
        call iscene ("A26") from _call_iscene_101
    call iscene ("A26a") from _call_iscene_102
    if not seen_scene ("A22b"):
        call iscene ("A26e") from _call_iscene_103
        jump_out A27_2
    jump_out A26_1

label A26_1:
    call iscene ("A26b") from _call_iscene_104
    call imenu ("choiceA26") from _call_imenu_11

    if _return == m1:

        call iscene ("A26c") from _call_iscene_105
        jump_out A28

    $ attraction_kenji += 1
    call iscene ("A26d") from _call_iscene_106
    jump_out A27_2

label A27:
    call iscene ("A27") from _call_iscene_107
    if seen_scene ("A22b"):
        jump_out A27_1
    call iscene ("A27e") from _call_iscene_108
    jump_out A29

label A27_1:
    call iscene ("A27a") from _call_iscene_109
    call imenu ("choiceA27") from _call_imenu_12
    if _return == m1:
        call iscene ("A27b") from _call_iscene_110
        $ attraction_kenji += 1
        call iscene ("A27f") from _call_iscene_111
        jump_out A29 
    call iscene ("A27c") from _call_iscene_112
    if seen_scene ("A25b"):
        call imenu ("choice2A27") from _call_imenu_13
        if _return == m1:
            call iscene ("A27h") from _call_iscene_113
            call iscene ("A27e") from _call_iscene_114
            jump_out A29                                     
    call iscene ("A27i") from _call_iscene_115
    jump_out A28

label A27_2:
    call iscene ("A27d") from _call_iscene_116
    if seen_scene ("A26d"):
        call iscene ("A27f") from _call_iscene_117
    else:
        call iscene ("A27e") from _call_iscene_118
    jump_out A29


label A28:
    call iscene ("A28") from _call_iscene_119
    if seen_scene ("A26c"):
        call iscene ("A28a") from _call_iscene_120
    call iscene ("A28b") from _call_iscene_121
    jump_out A36

label A29:
    if not seen_scene ("A25b"):
        call iscene ("A29") from _call_iscene_122
        if seen_scene ("A27f"):
            call iscene ("A29x") from _call_iscene_123
    else:
        call iscene ("A29a") from _call_iscene_124
    call iscene ("A29b") from _call_iscene_125
    if seen_scene ("A25b"):
        call iscene ("A29c") from _call_iscene_126
        jump_out A31
    jump_out A30

label A30:
    call iscene ("A30") from _call_iscene_127
    if seen_scene ("A26d") or seen_scene ("A27b"):

        call iscene ("A30a") from _call_iscene_128
        jump_out A31
    call imenu ("choiceA30") from _call_imenu_14
    if _return == m2:
        $ attraction_kenji += 1
        call iscene ("A30a") from _call_iscene_129
        jump_out A31
    call iscene ("A30b") from _call_iscene_130
    if seen_scene ("A11c"):
        call iscene ("A30c") from _call_iscene_131
    call iscene ("A30d") from _call_iscene_132
    jump_out A31

label A31:
    call iscene ("timeskip") from _call_iscene_133
    call iscene ("A31") from _call_iscene_134
    if seen_scene ("A25b"):
        call iscene ("A31b") from _call_iscene_135
    else:
        call iscene ("A31c") from _call_iscene_136
    call iscene ("A31d") from _call_iscene_137
    if attraction_kenji > 0:
        call iscene ("A31e") from _call_iscene_138
        jump_out A38
    elif seen_scene ("A29c"):
        jump_out A32
    elif seen_scene ("A24d"):
        jump_out A35
    jump_out A32

label A32:
    call iscene ("A32") from _call_iscene_139
    if seen_scene ("A23a"):
        call iscene ("A32a") from _call_iscene_140
    call iscene ("A32b") from _call_iscene_141
    if seen_scene ("A25b"):
        jump_out A34
    jump_out A33

label A33:
    call iscene ("A33") from _call_iscene_142
    call imenu ("choiceA33") from _call_imenu_15
    if _return == m2:
        call iscene ("A33a") from _call_iscene_143
    else:
        call iscene ("A33b") from _call_iscene_144
    jump_out A38

label A34:
    call iscene ("A34") from _call_iscene_145
    call iscene ("A34a") from _call_iscene_146
    jump_out A38

label A35:
    call iscene ("A35") from _call_iscene_147
    call imenu ("choiceA35") from _call_imenu_16
    if _return == m1:
        call iscene ("A35a") from _call_iscene_148
        jump_out A38
    jump_out A37

label A36:
    call iscene ("timeskip") from _call_iscene_149
    call iscene ("A36") from _call_iscene_150
    jump_out A38

label A37:
    call iscene ("A37") from _call_iscene_151
    jump_out A38

label A38:
    call iscene ("timeskip") from _call_iscene_152
    call iscene ("A38") from _call_iscene_153
    if seen_scene ("A31e"):
        jump_out A43
    elif seen_scene ("A36"):
        call iscene ("A38a") from _call_iscene_154
        call iscene ("A38e") from _call_iscene_155
        jump_out A44
    elif seen_scene ("A35") or seen_scene ("A37"):
        call iscene ("A38b") from _call_iscene_156
        call iscene ("A38e") from _call_iscene_157
        if seen_scene ("A37"):
            jump_out A42
        jump_out A41
    elif seen_scene ("A33a"):
        call iscene ("A38c") from _call_iscene_158
        call iscene ("A38e") from _call_iscene_159
        jump_out A40
    elif seen_scene ("A34"):
        call iscene ("A38d") from _call_iscene_160
        call iscene ("A38e") from _call_iscene_161
        jump_out A39
    jump_out A43

label A39:
    call iscene ("A39") from _call_iscene_162
    jump_out tc_act2_emi

label A40:
    call iscene ("A40") from _call_iscene_163
    jump_out tc_act2_rin

label A41:

    call iscene ("A41b") from _call_iscene_164
    call iscene ("A41a") from _call_iscene_165
    jump_out tc_act2_lilly

label A42:
    call iscene ("A41b") from _call_iscene_166
    call iscene ("A42") from _call_iscene_167
    jump_out H2

label A43:
    call iscene ("A43") from _call_iscene_168
    call path_end from _call_path_end
    jump_out restart

label A44:
    call iscene ("A44") from _call_iscene_169
    jump_out tc_act2_shizune

label H2:

    call iscene ("H2") from _call_iscene_170
    jump_out tc_act2_hanako

label tc_act2_hanako:
    if not renpy.ios:
        call act_op ("base_tc_act2_hanako.mp4") from _call_act_op_1
    else:
        call act_op ("ios_tc_act2_hanako.mp4") from _call_act_op_1
    jump_out H3

label H3:
    call iscene ("H3") from _call_iscene_171
    jump_out H4

label H4:
    call iscene ("timeskip") from _call_iscene_172
    call iscene ("H4") from _call_iscene_173
    call imenu ("choiceH4") from _call_imenu_17

    if _return == m1:

        jump_out H5_1
    else:

        jump_out H5_2

label H5_1:
    call iscene ("H5_1") from _call_iscene_174
    jump_out H6

label H5_2:
    call iscene ("H5_2") from _call_iscene_175
    jump_out H6

label H6:
    call iscene ("timeskip") from _call_iscene_176
    call iscene ("H6") from _call_iscene_177
    jump_out H7

label H7:
    call iscene ("H7") from _call_iscene_178
    if seen_scene("H5_1"):
        call iscene ("H7a") from _call_iscene_179
    elif seen_scene("H5_2"):
        call iscene ("H7b") from _call_iscene_180
    call iscene ("H7c") from _call_iscene_181
    jump_out H8

label H8:
    call iscene ("timeskip") from _call_iscene_182
    call iscene ("H8") from _call_iscene_183
    jump_out H9

label H9:
    call iscene ("H9") from _call_iscene_184
    jump_out H10

label H10:
    call iscene ("H10") from _call_iscene_185
    jump_out tc_act3_hanako

label tc_act3_hanako:
    if not renpy.ios:
        call act_op ("base_tc_act3_hanako.mp4") from _call_act_op_2
    else:
        call act_op ("ios_tc_act3_hanako.mp4") from _call_act_op_2
    jump_out H11

label H11:
    call iscene ("H11") from _call_iscene_186
    jump_out H12

label H12:
    call iscene ("timeskip") from _call_iscene_187
    call iscene ("H12") from _call_iscene_188
    call imenu ("choiceH12") from _call_imenu_18

    if _return == m1:

        call iscene ("H12a") from _call_iscene_189
    else:

        call iscene ("H12b") from _call_iscene_190
    call iscene ("H12c") from _call_iscene_191
    jump_out H13

label H13:
    call iscene ("timeskip") from _call_iscene_192
    call iscene ("H13") from _call_iscene_193
    jump_out H14

label H14:
    call iscene ("timeskip") from _call_iscene_194
    call iscene ("H14") from _call_iscene_195
    jump_out H15

label H15:
    call iscene ("H15") from _call_iscene_196
    jump_out H16

label H16:
    call iscene ("timeskip") from _call_iscene_197
    call iscene ("H16") from _call_iscene_198
    jump_out H17

label H17:
    call iscene ("timeskip") from _call_iscene_199
    call iscene ("H17") from _call_iscene_200
    jump_out H18

label H18:
    call iscene ("timeskip") from _call_iscene_201
    call iscene ("H18") from _call_iscene_202
    jump_out H19

label H19:
    call iscene ("timeskip") from _call_iscene_203
    call iscene ("H19") from _call_iscene_204
    jump_out H20

label H20:
    call iscene ("timeskip") from _call_iscene_205
    call iscene ("H20") from _call_iscene_206
    call imenu ("choiceH20") from _call_imenu_19

    if _return == m1:

        call iscene ("H20_1") from _call_iscene_207
    else:

        call iscene ("H20_2") from _call_iscene_208
    jump_out tc_act4_hanako

label tc_act4_hanako:
    if not renpy.ios:
        call act_op ("base_tc_act4_hanako.mp4") from _call_act_op_3
    else:
        call act_op ("ios_tc_act4_hanako.mp4") from _call_act_op_3
    jump_out H21

label H21:
    call iscene ("H21") from _call_iscene_209
    jump_out H22

label H22:
    call iscene ("timeskip") from _call_iscene_210
    call iscene ("H22") from _call_iscene_211
    call imenu ("choiceH22") from _call_imenu_20
    if _return == m1 and seen_scene ("H20_1"):
        call iscene ("H22a") from _call_iscene_212
        jump_out H25
    else:
        if seen_scene ("H20_1"):
            call iscene ("H22c") from _call_iscene_213
            jump_out H24
        else:
            call iscene ("H22b") from _call_iscene_214
    jump_out H23

label H23:

    call iscene ("H23") from _call_iscene_215
    call path_end ("hanakorage", True) from _call_path_end_1
    jump_out restart

label H24:

    call iscene ("H24") from _call_iscene_216
    call path_end ("hanakosad", True) from _call_path_end_2
    jump_out restart

label H25:
    call iscene ("timeskip") from _call_iscene_217
    call iscene ("H25") from _call_iscene_218
    if seen_scene ("H12a"):
        call iscene ("H25a") from _call_iscene_219
    call iscene ("H25c") from _call_iscene_220
    jump_out H26

label H26:
    call iscene ("timeskip") from _call_iscene_221
    call iscene ("H26") from _call_iscene_222
    jump_out H27

label H27:
    call iscene ("timeskip") from _call_iscene_223
    call iscene ("H27") from _call_iscene_224
    jump_out H28

label H28:
    call iscene ("timeskip") from _call_iscene_225
    call iscene ("H28") from _call_iscene_226
    jump_out H29

label H29:
    call iscene ("timeskip") from _call_iscene_227
    call iscene ("H29") from _call_iscene_228
    call iscene ("H29h", is_h=True) from _call_iscene_229
    call iscene ("H29x") from _call_iscene_230
    jump_out H30

label H30:
    call iscene ("timeskip") from _call_iscene_231
    call iscene ("H30") from _call_iscene_232
    jump_out H31

label H31:
    call iscene ("H31") from _call_iscene_233
    call path_end ("hanako", True) from _call_path_end_3
    jump_out restart

label tc_act2_lilly:
    if not renpy.ios:
        call act_op ("base_tc_act2_lilly.mp4") from _call_act_op_4
    else:
        call act_op ("ios_tc_act2_lilly.mp4") from _call_act_op_4
    jump_out L1

label L1:
    call iscene ("L1") from _call_iscene_234
    jump_out L2

label L2:
    call iscene ("timeskip") from _call_iscene_235
    call iscene ("L2") from _call_iscene_236
    jump_out L3

label L3:
    call iscene ("timeskip") from _call_iscene_237
    call iscene ("L3") from _call_iscene_238
    jump_out L4

label L4:
    call iscene ("timeskip") from _call_iscene_239
    call iscene ("L4") from _call_iscene_240
    jump_out L5

label L5:
    call iscene ("L5") from _call_iscene_241
    jump_out L6

label L6:
    call iscene ("timeskip") from _call_iscene_242
    call iscene ("L6i") from _call_iscene_243
    call imenu ("choiceL6_1") from _call_imenu_21
    if _return == m1:
        call iscene ("L6a") from _call_iscene_244
    else:
        call iscene ("L6b") from _call_iscene_245
    call iscene ("L6c") from _call_iscene_246
    jump_out L7

label L7:
    call iscene ("timeskip") from _call_iscene_247
    call iscene ("L7") from _call_iscene_248
    jump_out L8

label L8:
    call iscene ("timeskip") from _call_iscene_249
    call iscene ("L8") from _call_iscene_250
    jump_out tc_act3_lilly

label tc_act3_lilly:
    if not renpy.ios:
        call act_op ("base_tc_act3_lilly.mp4") from _call_act_op_5
    else:
        call act_op ("ios_tc_act3_lilly.mp4") from _call_act_op_5
    jump_out L9

label L9:
    call iscene ("L9") from _call_iscene_251
    jump_out L10

label L10:
    call iscene ("timeskip") from _call_iscene_252
    call iscene ("L10") from _call_iscene_253

    call imenu ("choiceL10_1") from _call_imenu_22
    if _return == m1:
        call iscene ("L10a") from _call_iscene_254
    else:
        call iscene ("L10b") from _call_iscene_255
    call iscene ("L10c") from _call_iscene_256
    call imenu ("choiceL10_2") from _call_imenu_23
    if _return == m1:
        call iscene ("L10d") from _call_iscene_257
    else:
        call iscene ("L10e") from _call_iscene_258
    call iscene ("L10f") from _call_iscene_259
    jump_out L11

label L11:
    call iscene ("timeskip") from _call_iscene_260
    call iscene ("L11") from _call_iscene_261
    jump_out L12

label L12:
    call iscene ("timeskip") from _call_iscene_262
    call iscene ("L12") from _call_iscene_263
    jump_out L13

label L13:
    call iscene ("timeskip") from _call_iscene_264
    call iscene ("L13") from _call_iscene_265
    jump_out L14

label L14:
    call iscene ("timeskip") from _call_iscene_266
    call iscene ("L14") from _call_iscene_267
    jump_out L15

label L15:
    call iscene ("timeskip") from _call_iscene_268
    call iscene ("L15") from _call_iscene_269
    call imenu ("choiceL15") from _call_imenu_24
    if _return == m1:

        call iscene ("L15a") from _call_iscene_270
    else:
        call iscene ("L15b") from _call_iscene_271
    call iscene ("L15c") from _call_iscene_272
    jump_out L16

label L16:
    call iscene ("timeskip") from _call_iscene_273
    call iscene ("L16") from _call_iscene_274
    jump_out L17

label L17:
    call iscene ("L17") from _call_iscene_275
    call iscene ("L17h", is_h=True, is_end=True) from _call_iscene_276
    jump_out L18

label L18:
    call iscene ("timeskip") from _call_iscene_277
    call iscene ("L18") from _call_iscene_278
    jump_out L19

label L19:
    call iscene ("L19") from _call_iscene_279
    call iscene ("L19h", is_h=True) from _call_iscene_280
    jump_out L20

label L20:
    call iscene ("timeskip") from _call_iscene_281
    call iscene ("L20") from _call_iscene_282
    call imenu ("choiceL20") from _call_imenu_25
    if _return == m1:
        call iscene ("L20a") from _call_iscene_283
    else:
        call iscene ("L20b") from _call_iscene_284
    call iscene ("L20c") from _call_iscene_285
    jump_out tc_act4_lilly

label tc_act4_lilly:
    if not renpy.ios:
        call act_op ("base_tc_act4_lilly.mp4") from _call_act_op_6
    else:
        call act_op ("ios_tc_act4_lilly.mp4") from _call_act_op_6
    jump_out L21

label L21:
    call iscene ("L21") from _call_iscene_286
    jump_out L22

label L22:
    call iscene ("timeskip") from _call_iscene_287
    call iscene ("L22") from _call_iscene_288
    jump_out L23

label L23:
    call iscene ("timeskip") from _call_iscene_289
    call iscene ("L23") from _call_iscene_290
    jump_out L24

label L24:
    call iscene ("timeskip") from _call_iscene_291
    call iscene ("L24") from _call_iscene_292
    call imenu ("choiceL24") from _call_imenu_26
    if _return == m1:
        call iscene ("L24a") from _call_iscene_293
    else:

        call iscene ("L24b") from _call_iscene_294
    call iscene ("L24c") from _call_iscene_295
    jump_out L25

label L25:
    call iscene ("timeskip") from _call_iscene_296
    call iscene ("L25") from _call_iscene_297
    jump_out L26

label L26:
    call iscene ("timeskip") from _call_iscene_298
    call iscene ("L26") from _call_iscene_299
    call iscene ("L26h", is_h=True) from _call_iscene_300
    call iscene ("L26x") from _call_iscene_301
    jump_out L27

label L27:
    call iscene ("timeskip") from _call_iscene_302
    call iscene ("L27") from _call_iscene_303
    jump_out L28

label L28:
    call iscene ("timeskip") from _call_iscene_304
    call iscene ("L28") from _call_iscene_305
    jump_out L29

label L29:
    call iscene ("timeskip") from _call_iscene_306
    call iscene ("L29") from _call_iscene_307
    if seen_scene("L6b") and seen_scene("L15a") and seen_scene("L24a"):
        jump_out L30
    else:
        call path_end ("lilly") from _call_path_end_4
        jump_out restart

label L30:
    call iscene ("timeskip") from _call_iscene_308
    call iscene ("L30") from _call_iscene_309
    jump_out L31

label L31:
    call iscene ("timeskip") from _call_iscene_310
    call iscene ("L31") from _call_iscene_311
    jump_out L32

label L32:
    call iscene ("L32") from _call_iscene_312
    call path_end ("lilly", True) from _call_path_end_5
    jump_out L33

label L33:
    call iscene ("L33") from _call_iscene_313
    jump_out restart

label tc_act2_emi:
    if not renpy.ios:
        call act_op ("base_tc_act2_emi.mp4") from _call_act_op_7
    else:
        call act_op ("ios_tc_act2_emi.mp4") from _call_act_op_7
    jump_out E3

label E3:
    call iscene ("E3") from _call_iscene_314
    jump_out E4

label E4:
    call iscene ("E4") from _call_iscene_315

    jump_out E5

label E5:
    call iscene ("E5") from _call_iscene_316
    jump_out E6

label E6:
    call iscene ("E6") from _call_iscene_317
    jump_out E7

label E7:
    call iscene ("E7") from _call_iscene_318
    jump_out E8

label E8:
    call iscene ("timeskip") from _call_iscene_319
    call iscene ("E8") from _call_iscene_320
    jump_out E9

label E9:
    call iscene ("timeskip") from _call_iscene_321
    call iscene ("E9") from _call_iscene_322
    jump_out E10

label E10:
    call iscene ("timeskip") from _call_iscene_323
    call iscene ("E10") from _call_iscene_324
    jump_out E11

label E11:
    call iscene ("timeskip") from _call_iscene_325
    call iscene ("E11a") from _call_iscene_326
    if seen_scene("A12") or seen_scene ("A35a"):
        call iscene ("E11x") from _call_iscene_327
    else:
        call iscene ("E11y") from _call_iscene_328
    call iscene ("E11z") from _call_iscene_329
    call imenu ("choiceE11") from _call_imenu_27
    if _return == m1:
        call iscene ("E11b") from _call_iscene_330
    else:
        call iscene ("E11c") from _call_iscene_331
    call iscene ("E11d") from _call_iscene_332
    jump_out E12

label E12:
    call iscene ("timeskip") from _call_iscene_333
    call iscene ("E12a") from _call_iscene_334
    if seen_scene("E11b"):
        call iscene ("E12b") from _call_iscene_335
    else:
        call iscene ("E12c") from _call_iscene_336
    call iscene ("E12d") from _call_iscene_337
    jump_out E13

label E13:
    call iscene ("E13") from _call_iscene_338
    jump_out E14

label E14:
    call iscene ("timeskip") from _call_iscene_339
    call iscene ("E14") from _call_iscene_340
    jump_out E15

label E15:
    call iscene ("E15") from _call_iscene_341
    jump_out tc_act3_emi


label tc_act3_emi:
    if not renpy.ios:
        call act_op ("base_tc_act3_emi.mp4") from _call_act_op_8
    else:
        call act_op ("ios_tc_act3_emi.mp4") from _call_act_op_8
    jump_out E16

label E16:
    call iscene ("E16") from _call_iscene_342
    jump_out E17

label E17:
    call iscene ("timeskip") from _call_iscene_343
    call iscene ("E17") from _call_iscene_344
    call imenu ("choiceE17") from _call_imenu_28
    if _return == m1:
        call iscene ("E17a") from _call_iscene_345
    else:
        call iscene ("E17b") from _call_iscene_346
    call iscene ("E17x") from _call_iscene_347
    jump_out E18

label E18:
    call iscene ("timeskip") from _call_iscene_348
    call iscene ("E18") from _call_iscene_349
    if seen_scene("E17a"):
        call iscene ("E18a") from _call_iscene_350
    else:
        call iscene ("E18b") from _call_iscene_351
    call iscene ("E18x") from _call_iscene_352
    jump_out E19

label E19:
    call iscene ("E19") from _call_iscene_353
    jump_out E20

label E20:
    call iscene ("E20") from _call_iscene_354
    call iscene ("E20h", is_h=True) from _call_iscene_355
    call iscene ("E20x") from _call_iscene_356
    jump_out E21

label E21:
    call iscene ("timeskip") from _call_iscene_357
    call iscene ("E21") from _call_iscene_358
    call iscene ("E21h", is_h=True) from _call_iscene_359
    call iscene ("E21x") from _call_iscene_360
    jump_out E22

label E22:
    call iscene ("E22") from _call_iscene_361
    jump_out E23

label E23:
    call iscene ("timeskip") from _call_iscene_362
    call iscene ("E23") from _call_iscene_363
    jump_out E24

label E24:
    call iscene ("timeskip") from _call_iscene_364
    call iscene ("E24") from _call_iscene_365
    call imenu ("choiceE24") from _call_imenu_29
    if _return == m1:
        call iscene ("E24a") from _call_iscene_366
    else:
        call iscene ("E24b") from _call_iscene_367
    call iscene ("E24c") from _call_iscene_368
    jump_out E25

label E25:

    call iscene ("E25") from _call_iscene_369
    if seen_scene ("E24a"):
        call imenu ("choiceE25") from _call_imenu_30
        if _return == m1:
            call iscene ("E25a") from _call_iscene_370
        else:
            call iscene ("E25b") from _call_iscene_371
    call iscene ("E25c") from _call_iscene_372
    jump_out E26

label E26:
    call iscene ("timeskip") from _call_iscene_373
    call iscene ("E26") from _call_iscene_374
    if seen_scene ("E25a"):
        call iscene ("E26a") from _call_iscene_375
    call iscene ("E26b") from _call_iscene_376
    if seen_scene ("E25a"):
        call iscene ("E26e") from _call_iscene_377
    call iscene ("E26f") from _call_iscene_378
    if seen_scene ("E24a"):
        call imenu ("choiceE26") from _call_imenu_31
        if _return == m2:
            call iscene ("E26d") from _call_iscene_379
            jump_out tc_act4_emi
    call iscene ("E26c") from _call_iscene_380
    jump_out E27

label E27:
    call iscene ("timeskip") from _call_iscene_381
    call iscene ("E27") from _call_iscene_382
    call imenu ("choiceE27") from _call_imenu_32
    if _return == m1:
        call iscene ("E27a") from _call_iscene_383
        call path_end ("emi") from _call_path_end_6
        jump_out restart
    call iscene ("E27b") from _call_iscene_384
    jump_out tc_act4_emi

label tc_act4_emi:
    if not renpy.ios:
        call act_op ("base_tc_act4_emi.mp4") from _call_act_op_9
    else:
        call act_op ("ios_tc_act4_emi.mp4") from _call_act_op_9

    if seen_scene ("E27b"):
        jump_out E30
    jump_out E28

label E28:
    call iscene ("E28") from _call_iscene_385
    jump_out E29

label E29:
    call iscene ("timeskip") from _call_iscene_386
    call iscene ("E29") from _call_iscene_387
    jump_out E30

label E30:
    if seen_scene ("E29"):
        call iscene ("timeskip") from _call_iscene_388
    call iscene ("E30") from _call_iscene_389
    if seen_scene ("E29"):
        call iscene ("E30a") from _call_iscene_390
    call iscene ("E30b") from _call_iscene_391
    if seen_scene ("E27"):
        call iscene ("E30c") from _call_iscene_392
    else:
        call iscene ("E30d") from _call_iscene_393
    call iscene ("E30e") from _call_iscene_394
    jump_out E31

label E31:
    call iscene ("E31") from _call_iscene_395
    call iscene ("E31h", is_h=True) from _call_iscene_396
    call iscene ("E31x") from _call_iscene_397
    jump_out E32

label E32:
    call iscene ("timeskip") from _call_iscene_398
    call iscene ("E32") from _call_iscene_399
    call path_end ("emi", True) from _call_path_end_7
    jump_out restart

label tc_act2_rin:
    if not renpy.ios:
        call act_op ("base_tc_act2_rin.mp4") from _call_act_op_10
    else:
        call act_op ("ios_tc_act2_rin.mp4") from _call_act_op_10
    jump_out R1

label R1:
    call iscene ("R1") from _call_iscene_400
    jump_out R2

label R2:
    call iscene ("R2") from _call_iscene_401
    call imenu ("choiceR2") from _call_imenu_33
    if _return == m1:
        call iscene ("R2a") from _call_iscene_402
    else:
        call iscene ("R2b") from _call_iscene_403
    call iscene ("R2c") from _call_iscene_404
    jump_out R3

label R3:
    call iscene ("R3") from _call_iscene_405
    jump_out R4

label R4:
    call iscene ("timeskip") from _call_iscene_406
    call iscene ("R4") from _call_iscene_407
    jump_out R5

label R5:
    call iscene ("timeskip") from _call_iscene_408
    call iscene ("R5") from _call_iscene_409
    jump_out R6

label R6:
    call iscene ("timeskip") from _call_iscene_410
    call iscene ("R6") from _call_iscene_411
    call imenu ("choiceR6") from _call_imenu_34
    if _return == m1:
        call iscene ("R6a") from _call_iscene_412
    else:
        call iscene ("R6b") from _call_iscene_413
    call iscene ("R6c") from _call_iscene_414
    jump_out R7

label R7:
    call iscene ("timeskip") from _call_iscene_415
    call iscene ("R7") from _call_iscene_416
    jump_out R8

label R8:
    call iscene ("timeskip") from _call_iscene_417
    call iscene ("R8") from _call_iscene_418
    jump_out R9

label R9:
    call iscene ("R9") from _call_iscene_419
    call imenu ("choiceR9") from _call_imenu_35
    if _return == m1:
        call iscene ("R9a") from _call_iscene_420
    else:
        call iscene ("R9b") from _call_iscene_421
    call iscene ("R9c") from _call_iscene_422
    jump_out R10

label R10:
    call iscene ("timeskip") from _call_iscene_423
    call iscene ("R10") from _call_iscene_424
    jump_out R11

label R11:
    call iscene ("timeskip") from _call_iscene_425
    call iscene ("R11") from _call_iscene_426

    if seen_scene("R2a"):
        if seen_scene("R6a"):
            if seen_scene("R9a"):
                call imenu ("choiceR11aaa") from _call_imenu_36
            else:
                call imenu ("choiceR11aab") from _call_imenu_37
        else:
            if seen_scene("R9a"):
                call imenu ("choiceR11aba") from _call_imenu_38
            else:
                call imenu ("choiceR11abb") from _call_imenu_39
    else:
        if seen_scene("R6a"):
            if seen_scene("R9a"):
                call imenu ("choiceR11baa") from _call_imenu_40
            else:
                call imenu ("choiceR11bab") from _call_imenu_41
        else:
            if seen_scene("R9a"):
                call imenu ("choiceR11bba") from _call_imenu_42
            else:
                call imenu ("choiceR11bbb") from _call_imenu_43

    if _return == m1:
        call iscene ("R11a") from _call_iscene_427
        call iscene ("R11g") from _call_iscene_428
    elif _return == m2:
        call iscene ("R11b") from _call_iscene_429
        call iscene ("R11i") from _call_iscene_430
    elif _return == m3:
        call iscene ("R11c") from _call_iscene_431
        call iscene ("R11h") from _call_iscene_432
    elif _return == m4:
        call iscene ("R11d") from _call_iscene_433
        call iscene ("R11i") from _call_iscene_434
    elif _return == m5:
        call iscene ("R11e") from _call_iscene_435
        call iscene ("R11h") from _call_iscene_436
    else:
        call iscene ("R11f") from _call_iscene_437
        call iscene ("R11g") from _call_iscene_438
    call iscene ("R11j") from _call_iscene_439
    jump_out R12

label R12:
    call iscene ("timeskip") from _call_iscene_440
    call iscene ("R12") from _call_iscene_441
    if seen_scene("A12") or seen_scene ("A35a"):
        call iscene ("R12b") from _call_iscene_442
    else:
        call iscene ("R12a") from _call_iscene_443
    call iscene ("R12c") from _call_iscene_444
    if seen_scene("A12") or seen_scene ("A35a"):
        call iscene ("R12e") from _call_iscene_445
    else:
        call iscene ("R12d") from _call_iscene_446
    call iscene ("R12f") from _call_iscene_447
    jump_out R13

label R13:
    call iscene ("timeskip") from _call_iscene_448
    call iscene ("R13") from _call_iscene_449
    jump_out R14

label R14:
    call iscene ("timeskip") from _call_iscene_450
    call iscene ("R14") from _call_iscene_451
    jump_out R15

label R15:
    call iscene ("timeskip") from _call_iscene_452
    call iscene ("R15") from _call_iscene_453
    jump_out R16

label R16:
    call iscene ("timeskip") from _call_iscene_454
    call iscene ("R16") from _call_iscene_455
    call imenu ("choiceR16") from _call_imenu_44
    if _return == m1:
        call iscene ("R16a") from _call_iscene_456
    else:
        call iscene ("R16b") from _call_iscene_457
    call iscene ("R16c") from _call_iscene_458
    if seen_scene ("R11g"):
        call iscene ("R16d") from _call_iscene_459
    call iscene ("R16e") from _call_iscene_460
    jump_out tc_act3_rin

label tc_act3_rin:
    if not renpy.ios:
        call act_op ("base_tc_act3_rin.mp4") from _call_act_op_11
    else:
        call act_op ("ios_tc_act3_rin.mp4") from _call_act_op_11
    jump_out R17

label R17:
    call iscene ("R17") from _call_iscene_461
    jump_out R18

label R18:
    call iscene ("timeskip") from _call_iscene_462
    call iscene ("R18") from _call_iscene_463
    jump_out R19

label R19:
    call iscene ("timeskip") from _call_iscene_464
    call iscene ("R19") from _call_iscene_465
    if seen_scene ("R16b"):
        call iscene ("R19a") from _call_iscene_466
    call iscene ("R19b") from _call_iscene_467
    if seen_scene ("R16d"):
        jump_out R20
    else:
        jump_out R21

label R20:
    call iscene ("R20") from _call_iscene_468
    call imenu ("choiceR20") from _call_imenu_45
    if _return == m1:
        call iscene ("R20a") from _call_iscene_469
    else:
        call iscene ("R20b") from _call_iscene_470
    call iscene ("R20c") from _call_iscene_471
    jump_out R22

label R21:
    call iscene ("R21") from _call_iscene_472
    call imenu ("choiceR21") from _call_imenu_46
    if _return == m1:
        call iscene ("R21a") from _call_iscene_473
    else:
        call iscene ("R21b") from _call_iscene_474
    call iscene ("R21c") from _call_iscene_475
    jump_out R22

label R22:
    call iscene ("timeskip") from _call_iscene_476
    call iscene ("R22") from _call_iscene_477
    jump_out R23

label R23:
    call iscene ("timeskip") from _call_iscene_478
    call iscene ("R23") from _call_iscene_479
    jump_out R23_2

label R23_2:
    call iscene ("timeskip") from _call_iscene_480
    call iscene ("R23_2") from _call_iscene_481
    jump_out R24

label R24:
    call iscene ("timeskip") from _call_iscene_482
    call iscene ("R24") from _call_iscene_483
    jump_out R25

label R25:
    call iscene ("R25") from _call_iscene_484
    jump_out R26

label R26:
    call iscene ("timeskip") from _call_iscene_485
    call iscene ("R26") from _call_iscene_486
    call imenu ("choiceR26") from _call_imenu_47
    if _return == m1:
        call iscene ("R26a") from _call_iscene_487
    else:
        call iscene ("R26b") from _call_iscene_488
    call iscene ("R26c") from _call_iscene_489
    jump_out R27

label R27:
    call iscene ("R27") from _call_iscene_490
    call iscene ("R27h", is_h=True) from _call_iscene_491
    call iscene ("R27x") from _call_iscene_492
    jump_out R28

label R28:
    call iscene ("timeskip") from _call_iscene_493


    call iscene ("R28") from _call_iscene_494
    if (seen_scene("R20a") or seen_scene("R21a")):
        call imenu ("choiceR28_1") from _call_imenu_48
    else:
        call imenu ("choiceR28_2") from _call_imenu_49

    if _return == m1:
        call iscene ("R28a") from _call_iscene_495
    elif _return == m2:
        call iscene ("R28b") from _call_iscene_496
    else:
        jump_out R29
    call iscene ("R28c") from _call_iscene_497
    jump_out tc_act4_rin

label R29:
    call iscene ("R29") from _call_iscene_498
    call path_end ("rin", False) from _call_path_end_8
    jump_out restart

label tc_act4_rin:
    if not renpy.ios:
        call act_op ("base_tc_act4_rin.mp4") from _call_act_op_12
    else:
        call act_op ("ios_tc_act4_rin.mp4") from _call_act_op_12
    jump_out R30

label R30:
    call iscene ("R30") from _call_iscene_499
    if (seen_scene("R16d")):
        call iscene ("R30x") from _call_iscene_500
    else:
        call iscene ("R30y") from _call_iscene_501
    call iscene ("R30z") from _call_iscene_502
    jump_out R31

label R31:
    call iscene ("timeskip") from _call_iscene_503
    call iscene ("R31") from _call_iscene_504
    jump_out R32

label R32:
    call iscene ("timeskip") from _call_iscene_505
    call iscene ("R32") from _call_iscene_506
    call imenu ("choiceR32") from _call_imenu_50
    if _return == m1:
        call iscene ("R32a") from _call_iscene_507
        jump_out R35
    call iscene ("R32b") from _call_iscene_508
    jump_out R34

label R34:

    call iscene ("timeskip") from _call_iscene_509
    call iscene ("R33") from _call_iscene_510
    call iscene ("R34") from _call_iscene_511
    jump_out R38

label R35:
    call iscene ("timeskip") from _call_iscene_512
    call iscene ("R33") from _call_iscene_513
    call iscene ("R35") from _call_iscene_514
    jump_out R36

label R36:
    call iscene ("timeskip") from _call_iscene_515
    call iscene ("R36") from _call_iscene_516
    if not seen_scene("R19a"):
        call iscene ("R36a") from _call_iscene_517
    call iscene ("R36x") from _call_iscene_518
    jump_out R37

label R37:
    call iscene ("R37") from _call_iscene_519
    call path_end ("rintrue", True) from _call_path_end_9
    jump_out restart

label R38:
    call iscene ("R38") from _call_iscene_520
    jump_out R39

label R39:
    call iscene ("R39") from _call_iscene_521
    jump_out R40

label R40:
    call iscene ("R40") from _call_iscene_522
    jump_out R41

label R41:
    call iscene ("timeskip") from _call_iscene_523
    call iscene ("R41") from _call_iscene_524
    call iscene ("R41h", is_h=True) from _call_iscene_525
    jump_out R42

label R42:
    call iscene ("R42") from _call_iscene_526
    call path_end ("rin", True) from _call_path_end_10
    jump_out restart

label tc_act2_shizune:
    if not renpy.ios:
        call act_op ("base_tc_act2_shizune.mp4") from _call_act_op_13
    else:
        call act_op ("ios_tc_act2_shizune.mp4") from _call_act_op_13
    jump_out S8

label S8:
    call iscene ("S8") from _call_iscene_527
    jump_out S9

label S9:
    call iscene ("timeskip") from _call_iscene_528
    call iscene ("S9") from _call_iscene_529
    jump_out S10

label S10:
    call iscene ("timeskip") from _call_iscene_530
    call iscene ("S10") from _call_iscene_531
    jump_out S11

label S11:
    call iscene ("timeskip") from _call_iscene_532
    call iscene ("S11") from _call_iscene_533
    jump_out S12

label S12:
    call iscene ("timeskip") from _call_iscene_534
    call iscene ("S12") from _call_iscene_535
    jump_out S13

label S13:
    call iscene ("timeskip") from _call_iscene_536
    call iscene ("S13") from _call_iscene_537
    jump_out S14

label S14:
    call iscene ("timeskip") from _call_iscene_538
    call iscene ("S14") from _call_iscene_539
    jump_out S15

label S15:
    call iscene ("timeskip") from _call_iscene_540
    call iscene ("S15") from _call_iscene_541
    jump_out S16

label S16:
    call iscene ("timeskip") from _call_iscene_542
    call iscene ("S16") from _call_iscene_543
    jump_out tc_act3_shizune

label tc_act3_shizune:
    if not renpy.ios:
        call act_op ("base_tc_act3_shizune.mp4") from _call_act_op_14
    else:
        call act_op ("ios_tc_act3_shizune.mp4") from _call_act_op_14
    jump_out S17

label S17:
    call iscene ("S17") from _call_iscene_544
    if seen_scene ("A26b"):
        call iscene ("S17a") from _call_iscene_545
    call iscene ("S17x") from _call_iscene_546
    jump_out S18

label S18:
    call iscene ("timeskip") from _call_iscene_547
    call iscene ("S18") from _call_iscene_548
    jump_out S19

label S19:
    call iscene ("timeskip") from _call_iscene_549
    call iscene ("S19") from _call_iscene_550
    jump_out S20

label S20:
    call iscene ("timeskip") from _call_iscene_551
    call iscene ("S20") from _call_iscene_552
    jump_out S21

label S21:
    call iscene ("timeskip") from _call_iscene_553
    call iscene ("S21") from _call_iscene_554
    jump_out S22

label S22:
    call iscene ("S22") from _call_iscene_555
    if seen_scene ("A26b"):
        call iscene ("S22a") from _call_iscene_556
    else:
        call iscene ("S22b") from _call_iscene_557
    call iscene ("S22c") from _call_iscene_558
    call iscene ("S22h", is_h=True) from _call_iscene_559
    call iscene ("S22x") from _call_iscene_560
    jump_out S23

label S23:
    call iscene ("timeskip") from _call_iscene_561
    call iscene ("S23") from _call_iscene_562
    if not seen_scene ("A2b"):
        call iscene ("S23a") from _call_iscene_563
    call iscene ("S23x") from _call_iscene_564
    jump_out S24

label S24:
    call iscene ("timeskip") from _call_iscene_565
    call iscene ("S24") from _call_iscene_566
    jump_out S25

label S25:
    call iscene ("timeskip") from _call_iscene_567
    call iscene ("S25") from _call_iscene_568
    jump_out S26

label S26:
    call iscene ("timeskip") from _call_iscene_569
    call iscene ("S26") from _call_iscene_570
    if seen_scene ("A26b"):
        call iscene ("S26a") from _call_iscene_571
    else:
        call iscene ("S26b") from _call_iscene_572
    call iscene ("S26c") from _call_iscene_573
    jump_out S27

label S27:
    call iscene ("timeskip") from _call_iscene_574
    call iscene ("S27") from _call_iscene_575
    jump_out S28

label S28:
    call iscene ("timeskip") from _call_iscene_576
    call iscene ("S28") from _call_iscene_577
    call imenu ("choiceS28") from _call_imenu_51
    if _return == m1:
        call iscene ("S28a") from _call_iscene_578
        call iscene ("S28h", is_h=True) from _call_iscene_579
        jump_out S29_1
    else:
        call iscene ("S28b") from _call_iscene_580
    jump_out S29_2

label S29_1:
    call iscene ("timeskip") from _call_iscene_581
    call iscene ("S29") from _call_iscene_582
    call iscene ("S29a") from _call_iscene_583
    call iscene ("S29x") from _call_iscene_584
    call iscene ("S29xa") from _call_iscene_585
    call iscene ("S29y") from _call_iscene_586
    call iscene ("S29ya") from _call_iscene_587
    jump_out tc_act4_shizune

label S29_2:
    call iscene ("timeskip") from _call_iscene_588
    call iscene ("S29") from _call_iscene_589
    call iscene ("S29b") from _call_iscene_590
    call iscene ("S29x") from _call_iscene_591
    call iscene ("S29xb") from _call_iscene_592
    if seen_scene ("A26b"):
        call iscene ("S29xba") from _call_iscene_593
    else:
        call iscene ("S29xbb") from _call_iscene_594
    call iscene ("S29xbc") from _call_iscene_595
    call iscene ("S29y") from _call_iscene_596
    call iscene ("S29yb") from _call_iscene_597
    jump_out tc_act4_shizune

label tc_act4_shizune:
    if not renpy.ios:
        call act_op ("base_tc_act4_shizune.mp4") from _call_act_op_15
    else:
        call act_op ("ios_tc_act4_shizune.mp4") from _call_act_op_15
    jump_out S30

label S30:
    call iscene ("S30") from _call_iscene_598
    jump_out S31

label S31:
    call iscene ("timeskip") from _call_iscene_599
    call iscene ("S31") from _call_iscene_600
    jump_out S32

label S32:
    call iscene ("timeskip") from _call_iscene_601
    call iscene ("S32") from _call_iscene_602
    jump_out S33

label S33:
    call iscene ("timeskip") from _call_iscene_603
    call iscene ("S33") from _call_iscene_604
    if seen_scene("S28a"):
        jump_out S38
    jump_out S34

label S34:
    call iscene ("timeskip") from _call_iscene_605
    call iscene ("S34") from _call_iscene_606
    if not seen_scene ("A26b"):
        call iscene ("S34a") from _call_iscene_607
    else:
        call iscene ("S34b") from _call_iscene_608
    call iscene ("S34c") from _call_iscene_609
    jump_out S35

label S35:
    call iscene ("timeskip") from _call_iscene_610
    call iscene ("S35") from _call_iscene_611
    call iscene ("S35h", is_h=True) from _call_iscene_612
    call iscene ("S35x") from _call_iscene_613
    jump_out S36

label S36:
    call iscene ("S36") from _call_iscene_614
    jump_out S37

label S37:
    call iscene ("timeskip") from _call_iscene_615
    call iscene ("S37") from _call_iscene_616
    call path_end ("shizune", True) from _call_path_end_11
    jump_out restart


label S38:
    call iscene ("timeskip") from _call_iscene_617
    call iscene ("S38") from _call_iscene_618
    jump_out S39

label S39:
    call iscene ("timeskip") from _call_iscene_619
    call iscene ("S39") from _call_iscene_620
    jump_out S40

label S40:
    call iscene ("timeskip") from _call_iscene_621
    call iscene ("S40") from _call_iscene_622
    call path_end ("shizune") from _call_path_end_12
    jump_out restart
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
