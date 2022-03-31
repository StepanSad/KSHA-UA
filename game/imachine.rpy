





label imachine:
    jump_out NOP1









label NOP1:
    call iscene ("NOP1") from _call_iscene_170
    jump_out op_video

label op_video:
    call iscene ("op_vid1") from _call_iscene_171
    jump_out NOP2

label NOP2:
    call iscene ("NOP2") from _call_iscene_172
    jump_out tc_act1

label tc_act1:
    call act_op ("tc_act1.webm") from _call_act_op
    jump_out A1

label A1:
    call iscene ("A1") from _call_iscene_173
    call imenu ("choiceA1") from _call_imenu_13

    if _return == m1:

        call iscene ("A1a") from _call_iscene_174
    else:

        $ attraction_sc += 1
        call iscene ("A1b") from _call_iscene_175
    call iscene ("A1c") from _call_iscene_176
    jump_out A2

label A2:
    call iscene ("A2") from _call_iscene_177
    if seen_scene ("A1a"):
        call iscene ("A2a") from _call_iscene_178
    else:
        call iscene ("A2b") from _call_iscene_179
    call iscene ("A2c") from _call_iscene_180
    if seen_scene ("A1b"):
        call iscene ("A2d") from _call_iscene_181
    else:
        call iscene ("A2e") from _call_iscene_182
    call iscene ("A2f") from _call_iscene_183
    jump_out A3

label A3:
    call iscene ("A3") from _call_iscene_184
    call imenu ("choiceA3") from _call_imenu_14
    if _return == m1:

        $ attraction_hanako += 1
        call iscene ("A3a") from _call_iscene_185
    elif _return == m2:

        call iscene ("A3b") from _call_iscene_186
    else:

        $ attraction_sc += 1
        call iscene ("A3c") from _call_iscene_187
    call iscene ("A3d") from _call_iscene_188
    jump_out A4

label A4:
    call iscene ("A4") from _call_iscene_189











    jump_out A5



label A5:
    call iscene ("timeskip") from _call_iscene_190
    call iscene ("A5") from _call_iscene_191
    jump_out A6

label A6:
    call iscene ("A6") from _call_iscene_192
    call imenu ("choiceA6") from _call_imenu_15

    if _return == m1:

        $ attraction_sc += 1
        call iscene ("A6a") from _call_iscene_193
    else:
        call iscene ("A6b") from _call_iscene_194
    call iscene ("A6c") from _call_iscene_195
    jump_out A7

label A7:
    call iscene ("A7") from _call_iscene_196
    jump_out A8

label A8:
    call iscene ("A8") from _call_iscene_197
    call imenu ("choiceA8") from _call_imenu_16

    if _return == m1:
        call iscene ("A8a") from _call_iscene_198

        if seen_scene("A1b"):
            call iscene ("A8aa") from _call_iscene_199
        call iscene ("A8ab") from _call_iscene_200
    else:

        $ attraction_hanako +=1
        call iscene ("A8b") from _call_iscene_201
    call iscene ("A8c") from _call_iscene_202
    if seen_scene ("A8a"):
        call iscene ("A8d") from _call_iscene_203
    else:
        call iscene ("A8e") from _call_iscene_204
    call iscene ("A8f") from _call_iscene_205
    jump_out A9

label A9:
    call iscene ("A9") from _call_iscene_206
    call imenu ("choiceA9") from _call_imenu_17
    if _return == m1:

        $ attraction_hanako += 1
        call iscene ("A9a") from _call_iscene_207
    else:

        call iscene ("A9b") from _call_iscene_208
    call iscene ("A9c") from _call_iscene_209
    jump_out A10



label A10:
    call iscene ("timeskip") from _call_iscene_210
    call iscene ("A10") from _call_iscene_211
    if attraction_sc > 1 and attraction_hanako > 1:
        call imenu ("choiceA10a") from _call_imenu_18
        if _return == m1:
            call iscene ("A10a") from _call_iscene_212
        elif _return == m2:
            call iscene ("A10b") from _call_iscene_213
            jump_out A11_2
        else:
            call iscene ("A10c") from _call_iscene_214
    elif attraction_sc > 1:
        call imenu ("choiceA10b") from _call_imenu_19
        if _return == m1:
            call iscene ("A10c") from _call_iscene_215
        else:
            call iscene ("A10a") from _call_iscene_216
    elif attraction_hanako > 1:
        call imenu ("choiceA10c") from _call_imenu_20
        if _return == m1:
            call iscene ("A10a") from _call_iscene_217
        else:
            call iscene ("A10b") from _call_iscene_218
            jump_out A11_2
    else:
        call iscene ("A10a") from _call_iscene_219
    jump_out A11_1

label A11_1:
    call iscene ("A11") from _call_iscene_220
    call iscene ("A11a") from _call_iscene_221
    call iscene ("A11b") from _call_iscene_222
    if seen_scene ("A10c"):
        call iscene ("A11x") from _call_iscene_223
        jump_out A12
    call iscene ("A11y") from _call_iscene_224
    jump_out A15


label A11_2:
    call iscene ("A11c") from _call_iscene_225
    call iscene ("A11a") from _call_iscene_226
    call iscene ("A11d") from _call_iscene_227
    jump_out A13

label A12:
    call iscene ("A12") from _call_iscene_228
    jump_out A16 

label A13:
    call iscene ("A13") from _call_iscene_229
    jump_out A15



label A15:
    call iscene ("A15") from _call_iscene_230
    jump_out A16

label A16:
    call iscene ("A16") from _call_iscene_231
    jump_out A17

label A17:
    call iscene ("A17") from _call_iscene_232
    call imenu ("choiceA17") from _call_imenu_21

    if _return == m1:

        call iscene ("A17a") from _call_iscene_233
    else:

        call iscene ("A17b") from _call_iscene_234
    call iscene ("A17c") from _call_iscene_235
    jump_out A18

label A18:
    call iscene ("A18") from _call_iscene_236
    jump_out A19


label A19:
    call iscene ("timeskip") from _call_iscene_237
    call iscene ("A19") from _call_iscene_238
    if seen_scene ("A17a"):
        call iscene ("A19a") from _call_iscene_239
    else:
        call iscene ("A19b") from _call_iscene_240
    call iscene ("A19c") from _call_iscene_241
    if seen_scene ("A11b"):
        call iscene ("A19i") from _call_iscene_242
    call iscene ("A19j") from _call_iscene_243
    if seen_scene ("A17a"):
        call iscene ("A19d") from _call_iscene_244
    else:
        call iscene ("A19e") from _call_iscene_245
    call iscene ("A19f") from _call_iscene_246
    if seen_scene ("A17a"):
        call iscene ("A19g") from _call_iscene_247
    else:
        call iscene ("A19h") from _call_iscene_248
    jump_out A20

label A20:
    call iscene ("A20") from _call_iscene_249
    jump_out A21

label A21:
    call iscene ("A21") from _call_iscene_250
    call imenu ("choiceA21") from _call_imenu_22

    if _return == m1:

        call iscene ("A21a") from _call_iscene_251
        jump_out A22
    call iscene ("A21b") from _call_iscene_252
    if seen_scene ("A13"):
        call iscene ("A21c") from _call_iscene_253
    else:
        call iscene ("A21d") from _call_iscene_254
    jump_out A23

label A22:
    call iscene ("A22") from _call_iscene_255
    if not seen_scene ("A12"):
        call iscene ("A22a") from _call_iscene_256
        jump_out A23
    jump_out A22_2

label A22_2:
    call iscene ("A22b") from _call_iscene_257
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
    call iscene ("A23") from _call_iscene_258
    if seen_scene ("A21c"):
        jump_out A24
    jump_out A23_2

label A23_2:
    call iscene ("A23a") from _call_iscene_259
    if seen_scene ("A21c"):
        jump_out A24
    jump_out A24_1

label A24:
    call iscene ("A24") from _call_iscene_260
    if seen_scene ("A21a"):

        call iscene ("A24c") from _call_iscene_261
    else:
        call iscene ("A24d") from _call_iscene_262
    call iscene ("A24e") from _call_iscene_263
    jump_out A24_1

label A24_1:
    if seen_scene("A17a"):
        call iscene ("A24a") from _call_iscene_264
        jump_out A25
    call iscene ("A24b") from _call_iscene_265
    jump_out A26


label A25:
    call iscene ("timeskip") from _call_iscene_266
    call iscene ("A25") from _call_iscene_267
    call imenu ("choiceA25") from _call_imenu_23
    if _return == m1:
        call iscene ("A25b") from _call_iscene_268
        jump_out A27
    call iscene ("A25a") from _call_iscene_269
    jump_out A26

label A26:
    if not seen_scene ("A25"):
        call iscene ("timeskip") from _call_iscene_270
        call iscene ("A26") from _call_iscene_271
    call iscene ("A26a") from _call_iscene_272
    if not seen_scene ("A22b"):
        call iscene ("A26e") from _call_iscene_273
        jump_out A27_2
    jump_out A26_1

label A26_1:
    call iscene ("A26b") from _call_iscene_274
    call imenu ("choiceA26") from _call_imenu_24

    if _return == m1:

        call iscene ("A26c") from _call_iscene_275
        jump_out A28

    $ attraction_kenji += 1
    call iscene ("A26d") from _call_iscene_276
    jump_out A27_2


label A27:
    call iscene ("A27") from _call_iscene_277
    if seen_scene ("A22b"):
        jump_out A27_1
    call iscene ("A27e") from _call_iscene_278
    jump_out A29

label A27_1:
    call iscene ("A27a") from _call_iscene_279
    call imenu ("choiceA27") from _call_imenu_25
    if _return == m1:
        call iscene ("A27b") from _call_iscene_280
        $ attraction_kenji += 1
        call iscene ("A27f") from _call_iscene_281
        jump_out A29 
    call iscene ("A27c") from _call_iscene_282
    if seen_scene ("A25b"):
        call imenu ("choice2A27") from _call_imenu_26
        if _return == m1:
            call iscene ("A27h") from _call_iscene_283
            call iscene ("A27e") from _call_iscene_284
            jump_out A29                                     
    call iscene ("A27i") from _call_iscene_285
    jump_out A28

label A27_2:
    call iscene ("A27d") from _call_iscene_286
    if seen_scene ("A26d"):
        call iscene ("A27f") from _call_iscene_287
    else:
        call iscene ("A27e") from _call_iscene_288
    jump_out A29


label A28:
    call iscene ("A28") from _call_iscene_289
    if seen_scene ("A26c"):
        call iscene ("A28a") from _call_iscene_290
    call iscene ("A28b") from _call_iscene_291
    jump_out A36

label A29:
    if not seen_scene ("A25b"):
        call iscene ("A29") from _call_iscene_292
        if seen_scene ("A27f"):
            call iscene ("A29x") from _call_iscene_293
    else:
        call iscene ("A29a") from _call_iscene_294
    call iscene ("A29b") from _call_iscene_295
    if seen_scene ("A25b"):
        call iscene ("A29c") from _call_iscene_296
        jump_out A31
    jump_out A30

label A30:
    call iscene ("A30") from _call_iscene_297
    if seen_scene ("A26d") or seen_scene ("A27b"):

        call iscene ("A30a") from _call_iscene_298
        jump_out A31
    call imenu ("choiceA30") from _call_imenu_27
    if _return == m2:
        $ attraction_kenji += 1
        call iscene ("A30a") from _call_iscene_299
        jump_out A31
    call iscene ("A30b") from _call_iscene_300
    if seen_scene ("A11c"):
        call iscene ("A30c") from _call_iscene_301
    call iscene ("A30d") from _call_iscene_302
    jump_out A31


label A31:
    call iscene ("timeskip") from _call_iscene_303
    call iscene ("A31") from _call_iscene_304
    if seen_scene ("A25b"):
        call iscene ("A31b") from _call_iscene_305
    else:
        call iscene ("A31c") from _call_iscene_306
    call iscene ("A31d") from _call_iscene_307
    if attraction_kenji > 0:
        call iscene ("A31e") from _call_iscene_308
        jump_out A38
    elif seen_scene ("A29c"):
        jump_out A32
    elif seen_scene ("A24d"):
        jump_out A35
    jump_out A32

label A32:
    call iscene ("A32") from _call_iscene_309
    if seen_scene ("A23a"):
        call iscene ("A32a") from _call_iscene_310
    call iscene ("A32b") from _call_iscene_311
    if seen_scene ("A25b"):
        jump_out A34
    jump_out A33

label A33:
    call iscene ("A33") from _call_iscene_312
    call imenu ("choiceA33") from _call_imenu_28
    if _return == m2:
        call iscene ("A33a") from _call_iscene_313
    else:
        call iscene ("A33b") from _call_iscene_314
    jump_out A38

label A34:
    call iscene ("A34") from _call_iscene_315
    call iscene ("A34a") from _call_iscene_316
    jump_out A38

label A35:
    call iscene ("A35") from _call_iscene_317
    call imenu ("choiceA35") from _call_imenu_29
    if _return == m1:
        call iscene ("A35a") from _call_iscene_318
        jump_out A38
    jump_out A37

label A36:
    call iscene ("timeskip") from _call_iscene_319
    call iscene ("A36") from _call_iscene_320
    jump_out A38

label A37:
    call iscene ("A37") from _call_iscene_321
    jump_out A38


label A38:
    call iscene ("timeskip") from _call_iscene_322
    call iscene ("A38") from _call_iscene_323
    if seen_scene ("A31e"):
        jump_out A43
    elif seen_scene ("A36"):
        call iscene ("A38a") from _call_iscene_324
        call iscene ("A38e") from _call_iscene_325
        jump_out A44
    elif seen_scene ("A35") or seen_scene ("A37"):
        call iscene ("A38b") from _call_iscene_326
        call iscene ("A38e") from _call_iscene_327
        if seen_scene ("A37"):
            jump_out A42
        jump_out A41
    elif seen_scene ("A33a"):
        call iscene ("A38c") from _call_iscene_328
        call iscene ("A38e") from _call_iscene_329
        jump_out A40
    elif seen_scene ("A34"):
        call iscene ("A38d") from _call_iscene_330
        call iscene ("A38e") from _call_iscene_331
        jump_out A39
    jump_out A43

label A39:
    call iscene ("A39") from _call_iscene_332
    jump_out tc_act2_emi

label A40:
    call iscene ("A40") from _call_iscene_333
    jump_out tc_act2_rin

label A41:

    call iscene ("A41b") from _call_iscene_334
    call iscene ("A41a") from _call_iscene_335
    jump_out tc_act2_lilly

label A42:
    call iscene ("A41b") from _call_iscene_336
    call iscene ("A42") from _call_iscene_337
    jump_out H2

label A43:
    call iscene ("A43") from _call_iscene_338
    call path_end from _call_path_end_1
    jump_out restart

label A44:
    call iscene ("A44") from _call_iscene_339
    jump_out tc_act2_shizune





label H2:

    call iscene ("H2") from _call_iscene_340
    jump_out tc_act2_hanako

label tc_act2_hanako:
    call act_op ("tc_act2_hanako.webm") from _call_act_op_1
    jump_out H3

label H3:
    call iscene ("H3") from _call_iscene_341
    jump_out H4

label H4:
    call iscene ("timeskip") from _call_iscene_342
    call iscene ("H4") from _call_iscene_343
    call imenu ("choiceH4") from _call_imenu_30

    if _return == m1:

        jump_out H5_1
    else:

        jump_out H5_2

label H5_1:
    call iscene ("H5_1") from _call_iscene_344
    jump_out H6

label H5_2:
    call iscene ("H5_2") from _call_iscene_345
    jump_out H6

label H6:
    call iscene ("timeskip") from _call_iscene_346
    call iscene ("H6") from _call_iscene_347
    jump_out H7

label H7:
    call iscene ("H7") from _call_iscene_348
    if seen_scene("H5_1"):
        call iscene ("H7a") from _call_iscene_349
    elif seen_scene("H5_2"):
        call iscene ("H7b") from _call_iscene_350
    call iscene ("H7c") from _call_iscene_351
    jump_out H8

label H8:
    call iscene ("timeskip") from _call_iscene_352
    call iscene ("H8") from _call_iscene_353
    jump_out H9

label H9:
    call iscene ("H9") from _call_iscene_354
    jump_out H10

label H10:
    call iscene ("H10") from _call_iscene_355
    jump_out tc_act3_hanako

label tc_act3_hanako:
    call act_op ("tc_act3_hanako.webm") from _call_act_op_2
    jump_out H11

label H11:
    call iscene ("H11") from _call_iscene_356
    jump_out H12

label H12:
    call iscene ("timeskip") from _call_iscene_357
    call iscene ("H12") from _call_iscene_358
    call imenu ("choiceH12") from _call_imenu_31

    if _return == m1:

        call iscene ("H12a") from _call_iscene_359
    else:

        call iscene ("H12b") from _call_iscene_360
    call iscene ("H12c") from _call_iscene_361
    jump_out H13

label H13:
    call iscene ("timeskip") from _call_iscene_362
    call iscene ("H13") from _call_iscene_363
    jump_out H14

label H14:
    call iscene ("timeskip") from _call_iscene_364
    call iscene ("H14") from _call_iscene_365
    jump_out H15

label H15:
    call iscene ("H15") from _call_iscene_366
    jump_out H16

label H16:
    call iscene ("timeskip") from _call_iscene_367
    call iscene ("H16") from _call_iscene_368
    jump_out H17

label H17:
    call iscene ("timeskip") from _call_iscene_369
    call iscene ("H17") from _call_iscene_370
    jump_out H18

label H18:
    call iscene ("timeskip") from _call_iscene_371
    call iscene ("H18") from _call_iscene_372
    jump_out H19

label H19:
    call iscene ("timeskip") from _call_iscene_373
    call iscene ("H19") from _call_iscene_374
    jump_out H20

label H20:
    call iscene ("timeskip") from _call_iscene_375
    call iscene ("H20") from _call_iscene_376
    call imenu ("choiceH20") from _call_imenu_32

    if _return == m1:

        call iscene ("H20_1") from _call_iscene_377
    else:

        call iscene ("H20_2") from _call_iscene_378
    jump_out tc_act4_hanako

label tc_act4_hanako:
    call act_op ("tc_act4_hanako.webm") from _call_act_op_3
    jump_out H21

label H21:
    call iscene ("H21") from _call_iscene_379
    jump_out H22

label H22:
    call iscene ("timeskip") from _call_iscene_380
    call iscene ("H22") from _call_iscene_381
    call imenu ("choiceH22") from _call_imenu_33
    if _return == m1 and seen_scene ("H20_1"):
        call iscene ("H22a") from _call_iscene_382
        jump_out H25
    else:
        if seen_scene ("H20_1"):
            call iscene ("H22c") from _call_iscene_383
            jump_out H24
        else:
            call iscene ("H22b") from _call_iscene_384
    jump_out H23

label H23:

    call iscene ("H23") from _call_iscene_385
    call path_end ("hanakorage", True) from _call_path_end_2
    jump_out restart

label H24:

    call iscene ("H24") from _call_iscene_386
    call path_end ("hanakosad", True) from _call_path_end_3
    jump_out restart

label H25:
    call iscene ("timeskip") from _call_iscene_387
    call iscene ("H25") from _call_iscene_388
    if seen_scene ("H12a"):
        call iscene ("H25a") from _call_iscene_389
    call iscene ("H25c") from _call_iscene_390
    jump_out H26

label H26:
    call iscene ("timeskip") from _call_iscene_391
    call iscene ("H26") from _call_iscene_392
    jump_out H27

label H27:
    call iscene ("timeskip") from _call_iscene_393
    call iscene ("H27") from _call_iscene_394
    jump_out H28

label H28:
    call iscene ("timeskip") from _call_iscene_395
    call iscene ("H28") from _call_iscene_396
    jump_out H29

label H29:
    call iscene ("timeskip") from _call_iscene_397
    call iscene ("H29") from _call_iscene_398
    call iscene ("H29h", is_h=True) from _call_iscene_399
    call iscene ("H29x") from _call_iscene_400
    jump_out H30

label H30:
    call iscene ("timeskip") from _call_iscene_401
    call iscene ("H30") from _call_iscene_402
    jump_out H31

label H31:
    call iscene ("H31") from _call_iscene_403
    call path_end ("hanako", True) from _call_path_end_4
    jump_out restart






label tc_act2_lilly:
    call act_op ("tc_act2_lilly.webm") from _call_act_op_4
    jump_out L1

label L1:
    call iscene ("L1") from _call_iscene_404
    jump_out L2

label L2:
    call iscene ("timeskip") from _call_iscene_405
    call iscene ("L2") from _call_iscene_406
    jump_out L3

label L3:
    call iscene ("timeskip") from _call_iscene_407
    call iscene ("L3") from _call_iscene_408
    jump_out L4

label L4:
    call iscene ("timeskip") from _call_iscene_409
    call iscene ("L4") from _call_iscene_410
    jump_out L5

label L5:
    call iscene ("L5") from _call_iscene_411
    jump_out L6

label L6:
    call iscene ("timeskip") from _call_iscene_412
    call iscene ("L6i") from _call_iscene_413
    call imenu ("choiceL6_1") from _call_imenu_34
    if _return == m1:
        call iscene ("L6a") from _call_iscene_414
    else:
        call iscene ("L6b") from _call_iscene_415
    call iscene ("L6c") from _call_iscene_416
    jump_out L7

label L7:
    call iscene ("timeskip") from _call_iscene_417
    call iscene ("L7") from _call_iscene_418
    jump_out L8

label L8:
    call iscene ("timeskip") from _call_iscene_419
    call iscene ("L8") from _call_iscene_420
    jump_out tc_act3_lilly

label tc_act3_lilly:
    call act_op ("tc_act3_lilly.webm") from _call_act_op_5
    jump_out L9

label L9:
    call iscene ("L9") from _call_iscene_421
    jump_out L10

label L10:
    call iscene ("timeskip") from _call_iscene_422
    call iscene ("L10") from _call_iscene_423

    call imenu ("choiceL10_1") from _call_imenu_35
    if _return == m1:
        call iscene ("L10a") from _call_iscene_424
    else:
        call iscene ("L10b") from _call_iscene_425
    call iscene ("L10c") from _call_iscene_426
    call imenu ("choiceL10_2") from _call_imenu_36
    if _return == m1:
        call iscene ("L10d") from _call_iscene_427
    else:
        call iscene ("L10e") from _call_iscene_428
    call iscene ("L10f") from _call_iscene_429
    jump_out L11

label L11:
    call iscene ("timeskip") from _call_iscene_430
    call iscene ("L11") from _call_iscene_431
    jump_out L12

label L12:
    call iscene ("timeskip") from _call_iscene_432
    call iscene ("L12") from _call_iscene_433
    jump_out L13

label L13:
    call iscene ("timeskip") from _call_iscene_434
    call iscene ("L13") from _call_iscene_435
    jump_out L14

label L14:
    call iscene ("timeskip") from _call_iscene_436
    call iscene ("L14") from _call_iscene_437
    jump_out L15

label L15:
    call iscene ("timeskip") from _call_iscene_438
    call iscene ("L15") from _call_iscene_439
    call imenu ("choiceL15") from _call_imenu_37
    if _return == m1:

        call iscene ("L15a") from _call_iscene_440
    else:
        call iscene ("L15b") from _call_iscene_441
    call iscene ("L15c") from _call_iscene_442
    jump_out L16

label L16:
    call iscene ("timeskip") from _call_iscene_443
    call iscene ("L16") from _call_iscene_444
    jump_out L17

label L17:
    call iscene ("L17") from _call_iscene_445
    call iscene ("L17h", is_h=True, is_end=True) from _call_iscene_446
    jump_out L18

label L18:
    call iscene ("timeskip") from _call_iscene_447
    call iscene ("L18") from _call_iscene_448
    jump_out L19

label L19:
    call iscene ("L19") from _call_iscene_449
    call iscene ("L19h", is_h=True) from _call_iscene_450
    jump_out L20

label L20:
    call iscene ("timeskip") from _call_iscene_451
    call iscene ("L20") from _call_iscene_452
    call imenu ("choiceL20") from _call_imenu_38
    if _return == m1:
        call iscene ("L20a") from _call_iscene_453
    else:
        call iscene ("L20b") from _call_iscene_454
    call iscene ("L20c") from _call_iscene_455
    jump_out tc_act4_lilly

label tc_act4_lilly:
    call act_op ("tc_act4_lilly.webm") from _call_act_op_6
    jump_out L21

label L21:
    call iscene ("L21") from _call_iscene_456
    jump_out L22

label L22:
    call iscene ("timeskip") from _call_iscene_457
    call iscene ("L22") from _call_iscene_458
    jump_out L23

label L23:
    call iscene ("timeskip") from _call_iscene_459
    call iscene ("L23") from _call_iscene_460
    jump_out L24

label L24:
    call iscene ("timeskip") from _call_iscene_461
    call iscene ("L24") from _call_iscene_462
    call imenu ("choiceL24") from _call_imenu_39
    if _return == m1:
        call iscene ("L24a") from _call_iscene_463
    else:

        call iscene ("L24b") from _call_iscene_464
    call iscene ("L24c") from _call_iscene_465
    jump_out L25

label L25:
    call iscene ("timeskip") from _call_iscene_466
    call iscene ("L25") from _call_iscene_467
    jump_out L26

label L26:
    call iscene ("timeskip") from _call_iscene_468
    call iscene ("L26") from _call_iscene_469
    call iscene ("L26h", is_h=True) from _call_iscene_470
    call iscene ("L26x") from _call_iscene_471
    jump_out L27

label L27:
    call iscene ("timeskip") from _call_iscene_472
    call iscene ("L27") from _call_iscene_473
    jump_out L28

label L28:
    call iscene ("timeskip") from _call_iscene_474
    call iscene ("L28") from _call_iscene_475
    jump_out L29

label L29:
    call iscene ("timeskip") from _call_iscene_476
    call iscene ("L29") from _call_iscene_477
    if seen_scene("L6b") and seen_scene("L15a") and seen_scene("L24a"):
        jump_out L30
    else:
        call path_end ("lilly") from _call_path_end_5
        jump_out restart

label L30:
    call iscene ("timeskip") from _call_iscene_478
    call iscene ("L30") from _call_iscene_479
    jump_out L31

label L31:
    call iscene ("timeskip") from _call_iscene_480
    call iscene ("L31") from _call_iscene_481
    jump_out L32

label L32:
    call iscene ("L32") from _call_iscene_482
    call path_end ("lilly", True) from _call_path_end_6
    jump_out L33

label L33:
    call iscene ("L33") from _call_iscene_483
    jump_out restart





label tc_act2_emi:
    call act_op ("tc_act2_emi.webm") from _call_act_op_7
    jump_out E3

label E3:
    call iscene ("E3") from _call_iscene_484
    jump_out E4

label E4:
    call iscene ("E4") from _call_iscene_485

    jump_out E5

label E5:
    call iscene ("E5") from _call_iscene_486
    jump_out E6

label E6:
    call iscene ("E6") from _call_iscene_487
    jump_out E7

label E7:
    call iscene ("E7") from _call_iscene_488
    jump_out E8

label E8:
    call iscene ("timeskip") from _call_iscene_489
    call iscene ("E8") from _call_iscene_490
    jump_out E9

label E9:
    call iscene ("timeskip") from _call_iscene_491
    call iscene ("E9") from _call_iscene_492
    jump_out E10

label E10:
    call iscene ("timeskip") from _call_iscene_493
    call iscene ("E10") from _call_iscene_494
    jump_out E11

label E11:
    call iscene ("timeskip") from _call_iscene_495
    call iscene ("E11a") from _call_iscene_496
    if seen_scene("A12") or seen_scene ("A35a"):
        call iscene ("E11x") from _call_iscene_497
    else:
        call iscene ("E11y") from _call_iscene_498
    call iscene ("E11z") from _call_iscene_499
    call imenu ("choiceE11") from _call_imenu_40
    if _return == m1:
        call iscene ("E11b") from _call_iscene_500
    else:
        call iscene ("E11c") from _call_iscene_501
    call iscene ("E11d") from _call_iscene_502
    jump_out E12

label E12:
    call iscene ("timeskip") from _call_iscene_503
    call iscene ("E12a") from _call_iscene_504
    if seen_scene("E11b"):
        call iscene ("E12b") from _call_iscene_505
    else:
        call iscene ("E12c") from _call_iscene_506
    call iscene ("E12d") from _call_iscene_507
    jump_out E13

label E13:
    call iscene ("E13") from _call_iscene_508
    jump_out E14

label E14:
    call iscene ("timeskip") from _call_iscene_509
    call iscene ("E14") from _call_iscene_510
    jump_out E15

label E15:
    call iscene ("E15") from _call_iscene_511
    jump_out tc_act3_emi


label tc_act3_emi:
    call act_op ("tc_act3_emi.webm") from _call_act_op_8
    jump_out E16

label E16:
    call iscene ("E16") from _call_iscene_512
    jump_out E17

label E17:
    call iscene ("timeskip") from _call_iscene_513
    call iscene ("E17") from _call_iscene_514
    call imenu ("choiceE17") from _call_imenu_41
    if _return == m1:
        call iscene ("E17a") from _call_iscene_515
    else:
        call iscene ("E17b") from _call_iscene_516
    call iscene ("E17x") from _call_iscene_517
    jump_out E18

label E18:
    call iscene ("timeskip") from _call_iscene_518
    call iscene ("E18") from _call_iscene_519
    if seen_scene("E17a"):
        call iscene ("E18a") from _call_iscene_520
    else:
        call iscene ("E18b") from _call_iscene_521
    call iscene ("E18x") from _call_iscene_522
    jump_out E19

label E19:
    call iscene ("E19") from _call_iscene_523
    jump_out E20

label E20:
    call iscene ("E20") from _call_iscene_524
    call iscene ("E20h", is_h=True) from _call_iscene_525
    call iscene ("E20x") from _call_iscene_526
    jump_out E21

label E21:
    call iscene ("timeskip") from _call_iscene_527
    call iscene ("E21") from _call_iscene_528
    call iscene ("E21h", is_h=True) from _call_iscene_529
    call iscene ("E21x") from _call_iscene_530
    jump_out E22

label E22:
    call iscene ("E22") from _call_iscene_531
    jump_out E23

label E23:
    call iscene ("timeskip") from _call_iscene_532
    call iscene ("E23") from _call_iscene_533
    jump_out E24

label E24:
    call iscene ("timeskip") from _call_iscene_534
    call iscene ("E24") from _call_iscene_535
    call imenu ("choiceE24") from _call_imenu_42
    if _return == m1:
        call iscene ("E24a") from _call_iscene_536
    else:
        call iscene ("E24b") from _call_iscene_537
    call iscene ("E24c") from _call_iscene_538
    jump_out E25

label E25:

    call iscene ("E25") from _call_iscene_539
    if seen_scene ("E24a"):
        call imenu ("choiceE25") from _call_imenu_43
        if _return == m1:
            call iscene ("E25a") from _call_iscene_540
        else:
            call iscene ("E25b") from _call_iscene_541
    call iscene ("E25c") from _call_iscene_542
    jump_out E26

label E26:
    call iscene ("timeskip") from _call_iscene_543
    call iscene ("E26") from _call_iscene_544
    if seen_scene ("E25a"):
        call iscene ("E26a") from _call_iscene_545
    call iscene ("E26b") from _call_iscene_546
    if seen_scene ("E25a"):
        call iscene ("E26e") from _call_iscene_547
    call iscene ("E26f") from _call_iscene_548
    if seen_scene ("E24a"):
        call imenu ("choiceE26") from _call_imenu_44
        if _return == m2:
            call iscene ("E26d") from _call_iscene_549
            jump_out tc_act4_emi
    call iscene ("E26c") from _call_iscene_550
    jump_out E27

label E27:
    call iscene ("timeskip") from _call_iscene_551
    call iscene ("E27") from _call_iscene_552
    call imenu ("choiceE27") from _call_imenu_45
    if _return == m1:
        call iscene ("E27a") from _call_iscene_553
        call path_end ("emi") from _call_path_end_7
        jump_out restart
    call iscene ("E27b") from _call_iscene_554
    jump_out tc_act4_emi

label tc_act4_emi:
    call act_op ("tc_act4_emi.webm") from _call_act_op_9
    if seen_scene ("E27b"):
        jump_out E30
    jump_out E28

label E28:
    call iscene ("E28") from _call_iscene_555
    jump_out E29

label E29:
    call iscene ("timeskip") from _call_iscene_556
    call iscene ("E29") from _call_iscene_557
    jump_out E30

label E30:
    if seen_scene ("E29"):
        call iscene ("timeskip") from _call_iscene_558
    call iscene ("E30") from _call_iscene_559
    if seen_scene ("E29"):
        call iscene ("E30a") from _call_iscene_560
    call iscene ("E30b") from _call_iscene_561
    if seen_scene ("E27"):
        call iscene ("E30c") from _call_iscene_562
    else:
        call iscene ("E30d") from _call_iscene_563
    call iscene ("E30e") from _call_iscene_564
    jump_out E31

label E31:
    call iscene ("E31") from _call_iscene_565
    call iscene ("E31h", is_h=True) from _call_iscene_566
    call iscene ("E31x") from _call_iscene_567
    jump_out E32

label E32:
    call iscene ("timeskip") from _call_iscene_568
    call iscene ("E32") from _call_iscene_569
    call path_end ("emi", True) from _call_path_end_8
    jump_out restart





label tc_act2_rin:
    call act_op ("tc_act2_rin.webm") from _call_act_op_10
    jump_out R1

label R1:
    call iscene ("R1") from _call_iscene_570
    jump_out R2

label R2:
    call iscene ("R2") from _call_iscene_571
    call imenu ("choiceR2") from _call_imenu_46
    if _return == m1:
        call iscene ("R2a") from _call_iscene_572
    else:
        call iscene ("R2b") from _call_iscene_573
    call iscene ("R2c") from _call_iscene_574
    jump_out R3

label R3:
    call iscene ("R3") from _call_iscene_575
    jump_out R4

label R4:
    call iscene ("timeskip") from _call_iscene_576
    call iscene ("R4") from _call_iscene_577
    jump_out R5

label R5:
    call iscene ("timeskip") from _call_iscene_578
    call iscene ("R5") from _call_iscene_579
    jump_out R6

label R6:
    call iscene ("timeskip") from _call_iscene_580
    call iscene ("R6") from _call_iscene_581
    call imenu ("choiceR6") from _call_imenu_47
    if _return == m1:
        call iscene ("R6a") from _call_iscene_582
    else:
        call iscene ("R6b") from _call_iscene_583
    call iscene ("R6c") from _call_iscene_584
    jump_out R7

label R7:
    call iscene ("timeskip") from _call_iscene_585
    call iscene ("R7") from _call_iscene_586
    jump_out R8

label R8:
    call iscene ("timeskip") from _call_iscene_587
    call iscene ("R8") from _call_iscene_588
    jump_out R9

label R9:
    call iscene ("R9") from _call_iscene_589
    call imenu ("choiceR9") from _call_imenu_48
    if _return == m1:
        call iscene ("R9a") from _call_iscene_590
    else:
        call iscene ("R9b") from _call_iscene_591
    call iscene ("R9c") from _call_iscene_592
    jump_out R10

label R10:
    call iscene ("timeskip") from _call_iscene_593
    call iscene ("R10") from _call_iscene_594
    jump_out R11

label R11:
    call iscene ("timeskip") from _call_iscene_595
    call iscene ("R11") from _call_iscene_596



    if seen_scene("R2a"):
        if seen_scene("R6a"):
            if seen_scene("R9a"):
                call imenu ("choiceR11aaa") from _call_imenu_49
            else:
                call imenu ("choiceR11aab") from _call_imenu_50
        else:
            if seen_scene("R9a"):
                call imenu ("choiceR11aba") from _call_imenu_51
            else:
                call imenu ("choiceR11abb") from _call_imenu_52
    else:
        if seen_scene("R6a"):
            if seen_scene("R9a"):
                call imenu ("choiceR11baa") from _call_imenu_53
            else:
                call imenu ("choiceR11bab") from _call_imenu_54
        else:
            if seen_scene("R9a"):
                call imenu ("choiceR11bba") from _call_imenu_55
            else:
                call imenu ("choiceR11bbb") from _call_imenu_56

    if _return == m1:
        call iscene ("R11a") from _call_iscene_597
        call iscene ("R11g") from _call_iscene_598
    elif _return == m2:
        call iscene ("R11b") from _call_iscene_599
        call iscene ("R11i") from _call_iscene_600
    elif _return == m3:
        call iscene ("R11c") from _call_iscene_601
        call iscene ("R11h") from _call_iscene_602
    elif _return == m4:
        call iscene ("R11d") from _call_iscene_603
        call iscene ("R11i") from _call_iscene_604
    elif _return == m5:
        call iscene ("R11e") from _call_iscene_605
        call iscene ("R11h") from _call_iscene_606
    else:
        call iscene ("R11f") from _call_iscene_607
        call iscene ("R11g") from _call_iscene_608
    call iscene ("R11j") from _call_iscene_609
    jump_out R12

label R12:
    call iscene ("timeskip") from _call_iscene_610
    call iscene ("R12") from _call_iscene_611
    if seen_scene("A12") or seen_scene ("A35a"):
        call iscene ("R12b") from _call_iscene_612
    else:
        call iscene ("R12a") from _call_iscene_613
    call iscene ("R12c") from _call_iscene_614
    if seen_scene("A12") or seen_scene ("A35a"):
        call iscene ("R12e") from _call_iscene_615
    else:
        call iscene ("R12d") from _call_iscene_616
    call iscene ("R12f") from _call_iscene_617
    jump_out R13

label R13:
    call iscene ("timeskip") from _call_iscene_618
    call iscene ("R13") from _call_iscene_619
    jump_out R14

label R14:
    call iscene ("timeskip") from _call_iscene_620
    call iscene ("R14") from _call_iscene_621
    jump_out R15

label R15:
    call iscene ("timeskip") from _call_iscene_622
    call iscene ("R15") from _call_iscene_623
    jump_out R16

label R16:
    call iscene ("timeskip") from _call_iscene_624
    call iscene ("R16") from _call_iscene_625
    call imenu ("choiceR16") from _call_imenu_57
    if _return == m1:
        call iscene ("R16a") from _call_iscene_626
    else:
        call iscene ("R16b") from _call_iscene_627
    call iscene ("R16c") from _call_iscene_628
    if seen_scene ("R11g"):
        call iscene ("R16d") from _call_iscene_629
    call iscene ("R16e") from _call_iscene_630
    jump_out tc_act3_rin

label tc_act3_rin:
    call act_op ("tc_act3_rin.webm") from _call_act_op_11
    jump_out R17

label R17:
    call iscene ("R17") from _call_iscene_631
    jump_out R18

label R18:
    call iscene ("timeskip") from _call_iscene_632
    call iscene ("R18") from _call_iscene_633
    jump_out R19

label R19:
    call iscene ("timeskip") from _call_iscene_634
    call iscene ("R19") from _call_iscene_635
    if seen_scene ("R16b"):
        call iscene ("R19a") from _call_iscene_636
    call iscene ("R19b") from _call_iscene_637
    if seen_scene ("R16d"):
        jump_out R20
    else:
        jump_out R21

label R20:
    call iscene ("R20") from _call_iscene_638
    call imenu ("choiceR20") from _call_imenu_58
    if _return == m1:
        call iscene ("R20a") from _call_iscene_639
    else:
        call iscene ("R20b") from _call_iscene_640
    call iscene ("R20c") from _call_iscene_641
    jump_out R22

label R21:
    call iscene ("R21") from _call_iscene_642
    call imenu ("choiceR21") from _call_imenu_59
    if _return == m1:
        call iscene ("R21a") from _call_iscene_643
    else:
        call iscene ("R21b") from _call_iscene_644
    call iscene ("R21c") from _call_iscene_645
    jump_out R22

label R22:
    call iscene ("timeskip") from _call_iscene_646
    call iscene ("R22") from _call_iscene_647
    jump_out R23

label R23:
    call iscene ("timeskip") from _call_iscene_648
    call iscene ("R23") from _call_iscene_649
    jump_out R23_2

label R23_2:
    call iscene ("timeskip") from _call_iscene_650
    call iscene ("R23_2") from _call_iscene_651
    jump_out R24

label R24:
    call iscene ("timeskip") from _call_iscene_652
    call iscene ("R24") from _call_iscene_653
    jump_out R25

label R25:
    call iscene ("R25") from _call_iscene_654
    jump_out R26

label R26:
    call iscene ("timeskip") from _call_iscene_655
    call iscene ("R26") from _call_iscene_656
    call imenu ("choiceR26") from _call_imenu_60
    if _return == m1:
        call iscene ("R26a") from _call_iscene_657
    else:
        call iscene ("R26b") from _call_iscene_658
    call iscene ("R26c") from _call_iscene_659
    jump_out R27

label R27:
    call iscene ("R27") from _call_iscene_660
    call iscene ("R27h", is_h=True) from _call_iscene_661
    call iscene ("R27x") from _call_iscene_662
    jump_out R28

label R28:
    call iscene ("timeskip") from _call_iscene_663


    call iscene ("R28") from _call_iscene_664
    if (seen_scene("R20a") or seen_scene("R21a")):
        call imenu ("choiceR28_1") from _call_imenu_61
    else:
        call imenu ("choiceR28_2") from _call_imenu_62

    if _return == m1:
        call iscene ("R28a") from _call_iscene_665
    elif _return == m2:
        call iscene ("R28b") from _call_iscene_666
    else:
        jump_out R29
    call iscene ("R28c") from _call_iscene_667
    jump_out tc_act4_rin

label R29:
    call iscene ("R29") from _call_iscene_668
    call path_end ("rin", False) from _call_path_end_9
    jump_out restart



label tc_act4_rin:
    call act_op ("tc_act4_rin.webm") from _call_act_op_12
    jump_out R30

label R30:
    call iscene ("R30") from _call_iscene_669
    if (seen_scene("R16d")):
        call iscene ("R30x") from _call_iscene_670
    else:
        call iscene ("R30y") from _call_iscene_671
    call iscene ("R30z") from _call_iscene_672
    jump_out R31

label R31:
    call iscene ("timeskip") from _call_iscene_673
    call iscene ("R31") from _call_iscene_674
    jump_out R32

label R32:
    call iscene ("timeskip") from _call_iscene_675
    call iscene ("R32") from _call_iscene_676
    call imenu ("choiceR32") from _call_imenu_63
    if _return == m1:
        call iscene ("R32a") from _call_iscene_677
        jump_out R35
    call iscene ("R32b") from _call_iscene_678
    jump_out R34



label R34:

    call iscene ("timeskip") from _call_iscene_679
    call iscene ("R33") from _call_iscene_680
    call iscene ("R34") from _call_iscene_681
    jump_out R38



label R35:
    call iscene ("timeskip") from _call_iscene_682
    call iscene ("R33") from _call_iscene_683
    call iscene ("R35") from _call_iscene_684
    jump_out R36

label R36:
    call iscene ("timeskip") from _call_iscene_685
    call iscene ("R36") from _call_iscene_686
    if not seen_scene("R19a"):
        call iscene ("R36a") from _call_iscene_687
    call iscene ("R36x") from _call_iscene_688
    jump_out R37

label R37:
    call iscene ("R37") from _call_iscene_689
    call path_end ("rintrue", True) from _call_path_end_10
    jump_out restart



label R38:
    call iscene ("R38") from _call_iscene_690
    jump_out R39

label R39:
    call iscene ("R39") from _call_iscene_691
    jump_out R40

label R40:
    call iscene ("R40") from _call_iscene_692
    jump_out R41

label R41:
    call iscene ("timeskip") from _call_iscene_693
    call iscene ("R41") from _call_iscene_694
    call iscene ("R41h", is_h=True) from _call_iscene_695
    jump_out R42

label R42:
    call iscene ("R42") from _call_iscene_696
    call path_end ("rin", True) from _call_path_end_11
    jump_out restart






label tc_act2_shizune:
    call act_op ("tc_act2_shizune.webm") from _call_act_op_13
    jump_out S8

label S8:
    call iscene ("S8") from _call_iscene_697
    jump_out S9

label S9:
    call iscene ("timeskip") from _call_iscene_698
    call iscene ("S9") from _call_iscene_699
    jump_out S10

label S10:
    call iscene ("timeskip") from _call_iscene_700
    call iscene ("S10") from _call_iscene_701
    jump_out S11

label S11:
    call iscene ("timeskip") from _call_iscene_702
    call iscene ("S11") from _call_iscene_703
    jump_out S12

label S12:
    call iscene ("timeskip") from _call_iscene_704
    call iscene ("S12") from _call_iscene_705
    jump_out S13

label S13:
    call iscene ("timeskip") from _call_iscene_706
    call iscene ("S13") from _call_iscene_707
    jump_out S14

label S14:
    call iscene ("timeskip") from _call_iscene_708
    call iscene ("S14") from _call_iscene_709
    jump_out S15

label S15:
    call iscene ("timeskip") from _call_iscene_710
    call iscene ("S15") from _call_iscene_711
    jump_out S16

label S16:
    call iscene ("timeskip") from _call_iscene_712
    call iscene ("S16") from _call_iscene_713
    jump_out tc_act3_shizune

label tc_act3_shizune:
    call act_op ("tc_act3_shizune.webm") from _call_act_op_14
    jump_out S17

label S17:
    call iscene ("S17") from _call_iscene_714
    if seen_scene ("A26b"):
        call iscene ("S17a") from _call_iscene_715
    call iscene ("S17x") from _call_iscene_716
    jump_out S18

label S18:
    call iscene ("timeskip") from _call_iscene_717
    call iscene ("S18") from _call_iscene_718
    jump_out S19

label S19:
    call iscene ("timeskip") from _call_iscene_719
    call iscene ("S19") from _call_iscene_720
    jump_out S20

label S20:
    call iscene ("timeskip") from _call_iscene_721
    call iscene ("S20") from _call_iscene_722
    jump_out S21

label S21:
    call iscene ("timeskip") from _call_iscene_723
    call iscene ("S21") from _call_iscene_724
    jump_out S22

label S22:
    call iscene ("S22") from _call_iscene_725
    if seen_scene ("A26b"):
        call iscene ("S22a") from _call_iscene_726
    else:
        call iscene ("S22b") from _call_iscene_727
    call iscene ("S22c") from _call_iscene_728
    call iscene ("S22h", is_h=True) from _call_iscene_729
    call iscene ("S22x") from _call_iscene_730
    jump_out S23

label S23:
    call iscene ("timeskip") from _call_iscene_731
    call iscene ("S23") from _call_iscene_732
    if not seen_scene ("A2b"):
        call iscene ("S23a") from _call_iscene_733
    call iscene ("S23x") from _call_iscene_734
    jump_out S24

label S24:
    call iscene ("timeskip") from _call_iscene_735
    call iscene ("S24") from _call_iscene_736
    jump_out S25

label S25:
    call iscene ("timeskip") from _call_iscene_737
    call iscene ("S25") from _call_iscene_738
    jump_out S26

label S26:
    call iscene ("timeskip") from _call_iscene_739
    call iscene ("S26") from _call_iscene_740
    if seen_scene ("A26b"):
        call iscene ("S26a") from _call_iscene_741
    else:
        call iscene ("S26b") from _call_iscene_742
    call iscene ("S26c") from _call_iscene_743
    jump_out S27

label S27:
    call iscene ("timeskip") from _call_iscene_744
    call iscene ("S27") from _call_iscene_745
    jump_out S28

label S28:
    call iscene ("timeskip") from _call_iscene_746
    call iscene ("S28") from _call_iscene_747
    call imenu ("choiceS28") from _call_imenu_64
    if _return == m1:
        call iscene ("S28a") from _call_iscene_748
        call iscene ("S28h", is_h=True) from _call_iscene_749
        jump_out S29_1
    else:
        call iscene ("S28b") from _call_iscene_750
    jump_out S29_2

label S29_1:
    call iscene ("timeskip") from _call_iscene_751
    call iscene ("S29") from _call_iscene_752
    call iscene ("S29a") from _call_iscene_753
    call iscene ("S29x") from _call_iscene_754
    call iscene ("S29xa") from _call_iscene_755
    call iscene ("S29y") from _call_iscene_756
    call iscene ("S29ya") from _call_iscene_757
    jump_out tc_act4_shizune

label S29_2:
    call iscene ("timeskip") from _call_iscene_758
    call iscene ("S29") from _call_iscene_759
    call iscene ("S29b") from _call_iscene_760
    call iscene ("S29x") from _call_iscene_761
    call iscene ("S29xb") from _call_iscene_762
    if seen_scene ("A26b"):
        call iscene ("S29xba") from _call_iscene_763
    else:
        call iscene ("S29xbb") from _call_iscene_764
    call iscene ("S29xbc") from _call_iscene_765
    call iscene ("S29y") from _call_iscene_766
    call iscene ("S29yb") from _call_iscene_767
    jump_out tc_act4_shizune

label tc_act4_shizune:
    call act_op ("tc_act4_shizune.webm") from _call_act_op_15
    jump_out S30

label S30:
    call iscene ("S30") from _call_iscene_768
    jump_out S31

label S31:
    call iscene ("timeskip") from _call_iscene_769
    call iscene ("S31") from _call_iscene_770
    jump_out S32

label S32:
    call iscene ("timeskip") from _call_iscene_771
    call iscene ("S32") from _call_iscene_772
    jump_out S33

label S33:
    call iscene ("timeskip") from _call_iscene_773
    call iscene ("S33") from _call_iscene_774
    if seen_scene("S28a"):
        jump_out S38
    jump_out S34


label S34:
    call iscene ("timeskip") from _call_iscene_775
    call iscene ("S34") from _call_iscene_776
    if not seen_scene ("A26b"):
        call iscene ("S34a") from _call_iscene_777
    else:
        call iscene ("S34b") from _call_iscene_778
    call iscene ("S34c") from _call_iscene_779
    jump_out S35

label S35:
    call iscene ("timeskip") from _call_iscene_780
    call iscene ("S35") from _call_iscene_781
    call iscene ("S35h", is_h=True) from _call_iscene_782
    call iscene ("S35x") from _call_iscene_783
    jump_out S36

label S36:
    call iscene ("S36") from _call_iscene_784
    jump_out S37

label S37:
    call iscene ("timeskip") from _call_iscene_785
    call iscene ("S37") from _call_iscene_786
    call path_end ("shizune", True) from _call_path_end_12
    jump_out restart


label S38:
    call iscene ("timeskip") from _call_iscene_787
    call iscene ("S38") from _call_iscene_788
    jump_out S39

label S39:
    call iscene ("timeskip") from _call_iscene_789
    call iscene ("S39") from _call_iscene_790
    jump_out S40

label S40:
    call iscene ("timeskip") from _call_iscene_791
    call iscene ("S40") from _call_iscene_792
    call path_end ("shizune") from _call_path_end_13
    jump_out restart
