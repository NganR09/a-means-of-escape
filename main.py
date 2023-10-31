@namespace
class SpriteKind:
    Positioning = SpriteKind.create()
    Patient = SpriteKind.create()
    enemy_projectile = SpriteKind.create()
    Object = SpriteKind.create()
    Background = SpriteKind.create()
"""

The MC's idle animation which triggers when the player isn't moving, making the character seem realistic and human rather than just a block of pixels.

"""
"""

Custom key binding?

"""
"""

A little introduction to the first patient the player will have to fight in order to help them.

"""
"""

Brief explanation of the controls.

"""
"""

Quick explanation of what the player would need to do on each level of the game.

"""
"""

Positions the MC and sets the MC's lives.

"""
"""

Destroys the enemy's sprite if the player manages to destroy it.

"""
"""

Overlap event where if the enemy's projectiles overlap the player, the player loses a life.

"""
"""

Prevents lag on cool down and frame skipping.

"""
"""

Creates a firing animation for the MC.

"""
"""

The therapy part of the game where the player's dialogue options impacts the ending they may get.

"""
"""

A timer for the player to follow to know how much time they have to find and defeat their patient, otherwise it means a game over.

"""
"""

Results screens telling the player how much money they have earnt.

"""
"""

The good ending, resulting in a victory for the player.

"""
def patients_memories():
    global Gun, Photograph, Lighter
    Gun = sprites.create(assets.image("""
        gun
    """), SpriteKind.Object)
    tiles.place_on_tile(Gun, tiles.get_tile_location(6, 25))
    Photograph = sprites.create(assets.image("""
        photograph
    """), SpriteKind.Object)
    tiles.place_on_tile(Photograph, tiles.get_tile_location(11, 61))
    Lighter = sprites.create(assets.image("""
        lighter
    """), SpriteKind.Object)
    tiles.place_on_tile(Lighter, tiles.get_tile_location(6, 45))

def on_on_overlap(sprite, otherSprite):
    if enemy_projectiles.overlaps_with(MC):
        sprite.destroy()
        scene.camera_shake(3, 1000)
        info.change_life_by(-1)
    if info.life() == 0:
        results_screen_2()
sprites.on_overlap(SpriteKind.enemy_projectile,
    SpriteKind.player,
    on_on_overlap)

def set_patient_1_position():
    global patient_1
    patient_1_enemy.destroy()
    enemy_projectiles.destroy()
    sprites.destroy_all_sprites_of_kind(SpriteKind.enemy)
    sprites.destroy_all_sprites_of_kind(SpriteKind.projectile)
    patient_1 = sprites.create(assets.image("""
            Patient_1_true_form
        """),
        SpriteKind.Patient)
    patient_1.ay = gravity
    tiles.place_on_tile(patient_1, tiles.get_tile_location(14, 96))
    pause(2000)
    info.stop_countdown()
    results_screen_1()
def game_timer_1():
    info.start_countdown(300)
"""

MC's firing animation

"""

def on_b_pressed():
    global projectile_thrown
    if characterAnimations.matches_rule(MC, characterAnimations.rule(Predicate.FACING_RIGHT)):
        animation.run_image_animation(MC,
            assets.animation("""
                MC firing animation right
            """),
            1000,
            False)
    if characterAnimations.matches_rule(MC, characterAnimations.rule(Predicate.FACING_LEFT)):
        animation.run_image_animation(MC,
            assets.animation("""
                MC firing animation left
            """),
            1000,
            False)
    set_MC_projectiles()
    music.set_volume(80)
    music.play_sound_effect(music.create_sound_effect(WaveShape.NOISE,
            2782,
            1534,
            255,
            0,
            500,
            SoundExpressionEffect.VIBRATO,
            InterpolationCurve.LINEAR),
        SoundExpressionPlayMode.IN_BACKGROUND)
    projectile_cool_down()
    pause(cool_down)
    projectile_thrown = 1
controller.B.on_event(ControllerButtonEvent.PRESSED, on_b_pressed)

def Ending_2():
    MC.destroy()
    patient_1_enemy.destroy()
    music.power_up.play()
    game.set_dialog_cursor(img("""
        2 2 2 2 2 2 2 2 2 2 2 2 
                2 2 2 2 2 2 2 2 2 2 2 2 
                2 2 1 1 1 f 1 1 1 1 2 2 
                2 2 1 1 1 f 1 1 1 1 2 2 
                2 2 1 1 1 f 1 1 1 1 2 2 
                2 2 1 1 1 f f f f f 2 2 
                2 2 f f f f f 1 1 1 2 2 
                2 2 1 1 1 1 f 1 1 1 2 2 
                2 2 1 1 1 1 f 1 1 1 2 2 
                2 2 1 1 1 1 f 1 1 1 2 2 
                2 2 2 2 2 2 2 2 2 2 2 2 
                2 2 2 2 2 2 2 2 2 2 2 2
    """))
    game.show_long_text("You have succeeded in treating your patient!",
        DialogLayout.CENTER)
    game.over(True, effects.star_field)
"""

Overlap event where the enemy takes damage if the player's projectile hits it.

"""
def game_play_explanation():
    game.set_dialog_frame(assets.image("""
        Picture frame
    """))
    game.show_long_text("It's the 1950s. You play as a German psychiatrist who has some unorthodox methods to treat his patients.",
        DialogLayout.CENTER)
    game.show_long_text("Find your patient, he is located at the bottom of the \"battlefield\".",
        DialogLayout.CENTER)
    game.show_long_text("You need to find and defeat him before \"sunset\".",
        DialogLayout.CENTER)
    main_menu()

def on_countdown_end():
    results_screen_2()
info.on_countdown_end(on_countdown_end)

def results_screen_2():
    info.stop_countdown()
    MC.destroy()
    patient_1_enemy.destroy()
    game.set_dialog_frame(assets.image("""
        Picture frame
    """))
    game.set_dialog_cursor(img("""
        2 2 2 2 2 2 2 2 2 2 2 2 
                2 2 2 2 2 2 2 2 2 2 2 2 
                2 2 1 1 1 f 1 1 1 1 2 2 
                2 2 1 1 1 f 1 1 1 1 2 2 
                2 2 1 1 1 f 1 1 1 1 2 2 
                2 2 1 1 1 f f f f f 2 2 
                2 2 f f f f f 1 1 1 2 2 
                2 2 1 1 1 1 f 1 1 1 2 2 
                2 2 1 1 1 1 f 1 1 1 2 2 
                2 2 1 1 1 1 f 1 1 1 2 2 
                2 2 2 2 2 2 2 2 2 2 2 2 
                2 2 2 2 2 2 2 2 2 2 2 2
    """))
    carnival.custom_game_over_expanded("You failed!", effects.melt, music.power_down)
"""

Trying to destroy enemy projectiles when the patient's sprite is created.

"""

def on_on_zero(status):
    status.sprite_attached_to().destroy(effects.halo, 500)
    patient_1_enemy.set_flag(SpriteFlag.AUTO_DESTROY, True)
    pause(500)
    set_patient_1_position()
statusbars.on_zero(StatusBarKind.enemy_health, on_on_zero)

"""

Sets up the enemy's projectiles.

"""
def MCs_position():
    global MC
    MC = sprites.create(assets.image("""
        MC sprite idle
    """), SpriteKind.player)
    tiles.place_on_tile(MC, tiles.get_tile_location(10, 6))
    MC.ay = gravity
    MC.set_flag(SpriteFlag.STAY_IN_SCREEN, True)
    scene.camera_follow_sprite(MC)
    info.set_life(3)
    controller.move_sprite(MC, player_speed, 0)
    controller.player2.move_sprite(MC, player_speed, 0)
"""

Simple jump mechanic.

"""

def on_player2_button_up_pressed():
    if MC.is_hitting_tile(CollisionDirection.BOTTOM):
        music.play_sound_effect(music.create_sound_effect(WaveShape.TRIANGLE,
                400,
                600,
                255,
                0,
                100,
                SoundExpressionEffect.NONE,
                InterpolationCurve.LINEAR),
            SoundExpressionPlayMode.IN_BACKGROUND)
        spriteutils.jump_impulse(MC, 50)
controller.player2.on_button_event(ControllerButton.UP,
    ControllerButtonEvent.PRESSED,
    on_player2_button_up_pressed)

def patient_negotiation():
    animation.run_image_animation(patient_1,
        assets.animation("""
            Patient_1_idle_animation
        """),
        500,
        True)
    info.set_score(0)
    story.sprite_say_text(patient_1,
        "Oh, so you've broken my shell...",
        15,
        1,
        story.TextSpeed.NORMAL)
    story.sprite_say_text(patient_1,
        "Doctor, I need your advice.",
        15,
        1,
        story.TextSpeed.NORMAL)
    story.sprite_say_text(patient_1,
        "I've been having the same kind of repeated nightmares recently,",
        15,
        1,
        story.TextSpeed.NORMAL)
    story.sprite_say_text(patient_1,
        "And I need to know what's been causing them.",
        15,
        1,
        story.TextSpeed.FAST)
    story.show_player_choices("Hmm, give me an insight to your past.", "Oh?")
    if story.check_last_answer("Hmm, give me an insight to your past."):
        info.change_score_by(10)
    if story.check_last_answer("Oh?"):
        info.change_score_by(3)
    story.sprite_say_text(patient_1,
        "Let me give you an idea:",
        15,
        1,
        story.TextSpeed.NORMAL)
    story.sprite_say_text(patient_1,
        "Do you know where I've been? What I've seen?",
        15,
        1,
        story.TextSpeed.FAST)
    pause(200)
    story.show_player_choices("You're a soldier, I assume you've accomplished many things.",
        "Not at all")
    if story.check_last_answer("You're a soldier, I assume you've accomplished many things."):
        info.change_score_by(10)
        story.sprite_say_text(patient_1, "Then let me ask:", 15, 1, story.TextSpeed.SLOW)
    if story.check_last_answer("Not at all"):
        info.change_score_by(-10)
    story.sprite_say_text(patient_1,
        "Have you had to kill anyone before?",
        15,
        1,
        story.TextSpeed.FAST)
    pause(100)
    story.sprite_say_text(patient_1,
        "Have you ever been killed before?",
        15,
        1,
        story.TextSpeed.NORMAL)
    story.show_player_choices("Well of course not.", "...")
    if story.check_last_answer("Well of course not."):
        info.change_score_by(10)
        story.sprite_say_text(patient_1, "...", 15, 1, story.TextSpeed.VERY_SLOW)
    if story.check_last_answer("..."):
        info.change_score_by(-5)
    story.sprite_say_text(patient_1,
        "Have you ever been so haunted by shame and regret?",
        15,
        1,
        story.TextSpeed.VERY_FAST)
    story.sprite_say_text(patient_1,
        "So much so that you cried until you puked?",
        15,
        1,
        story.TextSpeed.VERY_FAST)
    story.sprite_say_text(patient_1,
        "And everyone around you would say to just \"Suck it up.\"",
        15,
        1,
        story.TextSpeed.VERY_FAST)
    pause(200)
    story.sprite_say_text(patient_1,
        "Have you ever had friends that were told the exact same thing?",
        15,
        1,
        story.TextSpeed.VERY_FAST)
    story.sprite_say_text(patient_1,
        "And took their lives for it?",
        15,
        1,
        story.TextSpeed.VERY_FAST)
    story.show_player_choices("I can't say that I have.",
        "Grief can be extremely difficult to move on from.")
    if story.check_last_answer("I can't say that I have."):
        info.change_score_by(-5)
        story.sprite_say_text(patient_1,
            "No, of course not...",
            15,
            1,
            story.TextSpeed.NORMAL)
        story.sprite_say_text(patient_1,
            "I seem to be the only one who is affected by what I've seen.",
            15,
            1,
            story.TextSpeed.NORMAL)
        story.sprite_say_text(patient_1,
            "I don't see how any normal person could understand.",
            15,
            1,
            story.TextSpeed.NORMAL)
        story.sprite_say_text(patient_1,
            "Thanks for seeing me, doctor.",
            15,
            1,
            story.TextSpeed.NORMAL)
        game.set_dialog_frame(assets.image("""
            Documents
        """))
        game.set_dialog_cursor(assets.image("""
            Dialogue choice
        """))
        music.jump_up.play()
        game.show_long_text("You have earned 9 Deutschemarks. ", DialogLayout.CENTER)
        Ending_1()
    if story.check_last_answer("Grief can be extremely difficult to move on from."):
        info.change_score_by(20)
        story.sprite_say_text(patient_1,
            "And I don't understand why I keep reliving these things that I've seen!",
            15,
            1,
            story.TextSpeed.NORMAL)
        story.show_player_choices("There isn't a treatment for nightmares.",
            "You may be experiencing Shell Shock.")
        if story.check_last_answer("There isn't a treatment for nightmares."):
            info.change_score_by(-50)
            story.sprite_say_text(patient_1,
                "I knew no medical professional could understand.",
                15,
                1,
                story.TextSpeed.FAST)
            story.sprite_say_text(patient_1,
                "Thank you for listening anyway, doctor.",
                15,
                1,
                story.TextSpeed.NORMAL)
            game.set_dialog_frame(assets.image("""
                Documents
            """))
            game.set_dialog_cursor(assets.image("""
                Dialogue choice
            """))
            music.jump_up.play()
            game.show_long_text("You have earned 9 Deutschemarks. ", DialogLayout.CENTER)
            Ending_1()
        if story.check_last_answer("You may be experiencing Shell Shock."):
            info.change_score_by(30)
            story.sprite_say_text(patient_1,
                "I've heard of that before!",
                15,
                1,
                story.TextSpeed.NORMAL)
            story.sprite_say_text(patient_1,
                "You're the first person who has listened to me.",
                15,
                1,
                story.TextSpeed.NORMAL)
            story.sprite_say_text(patient_1, "Thank you.", 15, 1, story.TextSpeed.SLOW)
            game.set_dialog_frame(assets.image("""
                Documents
            """))
            game.set_dialog_cursor(assets.image("""
                Dialogue choice
            """))
            music.jump_up.play()
            game.show_long_text("You have earned 9 Deutschemarks. ", DialogLayout.CENTER)
            Ending_2()
def Day_1():
    game.splash("Patient no. 1", "23rd November 1953")
    scene.set_background_image(assets.image("""
        MC office background
    """))
    game.set_dialog_frame(assets.image("""
        Documents
    """))
    game.set_dialog_cursor(img("""
        2 2 2 f f 2 2 2 
                2 2 2 f d f 2 2 
                2 2 2 f f 2 2 2 
                f f f f f f f f 
                2 f f f f f f 2 
                2 2 f f f f 2 2 
                2 2 f f f f 2 2 
                2 2 2 f f 2 2 2
    """))
    game.set_dialog_text_color(15)
    game.show_long_text("Patient case info:      " + "Name: Leon Bauer     " + "Age: 30          " + "Occupation: soldier",
        DialogLayout.FULL)
    game.set_dialog_frame(img("""
        c c c c c c c c c c c c c c c 
                c c c c c c c c c c c c c c c 
                c c c c c c c c c c c c c c c 
                c c c 1 1 1 1 1 1 1 1 1 c c c 
                c c c 1 1 1 1 1 1 1 1 1 c c c 
                c c c 1 1 1 1 1 1 1 1 1 c c c 
                c c c 1 1 1 1 1 1 1 1 1 c c c 
                c c c 1 1 1 1 1 1 1 1 1 c c c 
                c c c 1 1 1 1 1 1 1 1 1 c c c 
                c c c 1 1 1 1 1 1 1 1 1 c c c 
                c c c 1 1 1 1 1 1 1 1 1 c c c 
                c c c 1 1 1 1 1 1 1 1 1 c c c 
                c c c c c c c c c c c c c c c 
                c c c c c c c c c c c c c c c 
                c c c c c c c c c c c c c c c
    """))
    game.show_long_text("He asked to see me in private...", DialogLayout.BOTTOM)
    game.show_long_text("He could prove hard to treat.", DialogLayout.BOTTOM)
    level_1()
def results_screen_1():
    info.stop_countdown()
    music.power_up.play()
    game.set_dialog_frame(assets.image("""
        Picture frame
    """))
    game.show_long_text("You succeeded in getting your patient to open up, well done.",
        DialogLayout.CENTER)
    patient_negotiation()
"""

Positions the enemy and creates a health bar for them.

"""
def set_patient_1_enemy():
    global patient_1_enemy, status_bar
    patient_1_enemy = sprites.create(assets.image("""
            Patient_1_enemy_sprite
        """),
        SpriteKind.enemy)
    tiles.place_on_tile(patient_1_enemy, tiles.get_tile_location(14, 96))
    patient_1_enemy.ay = gravity
    status_bar = statusbars.create(30, 4, StatusBarKind.enemy_health)
    status_bar.attach_to_sprite(patient_1_enemy)
    status_bar.position_direction(CollisionDirection.TOP)
    status_bar.set_status_bar_flag(StatusBarFlag.SMOOTH_TRANSITION, True)
    status_bar.set_color(2, 7)

def on_sprite_kind_update_interval(sprite2):
    global enemy_projectiles
    enemy_projectiles = sprites.create_projectile_from_sprite(assets.image("""
            enemy_1_projectile
        """),
        patient_1_enemy,
        -60,
        0)
    enemy_projectiles.set_kind(SpriteKind.enemy_projectile)
    animation.run_image_animation(enemy_projectiles,
        assets.animation("""
            patient_1_projectile
        """),
        75,
        True)
    enemy_projectiles.start_effect(effects.trail)
    enemy_projectiles.x += randint(-5, -8)
    enemy_projectiles.y += randint(-15, 20)
spriteutils.on_sprite_kind_update_interval(SpriteKind.enemy, 1000, on_sprite_kind_update_interval)

"""

The bad ending, resulting in a game over.

"""
def Ending_1():
    MC.destroy()
    patient_1_enemy.destroy()
    music.power_down.play()
    game.set_dialog_cursor(img("""
        2 2 2 2 2 2 2 2 2 2 2 2 
                2 2 2 2 2 2 2 2 2 2 2 2 
                2 2 1 1 1 f 1 1 1 1 2 2 
                2 2 1 1 1 f 1 1 1 1 2 2 
                2 2 1 1 1 f 1 1 1 1 2 2 
                2 2 1 1 1 f f f f f 2 2 
                2 2 f f f f f 1 1 1 2 2 
                2 2 1 1 1 1 f 1 1 1 2 2 
                2 2 1 1 1 1 f 1 1 1 2 2 
                2 2 1 1 1 1 f 1 1 1 2 2 
                2 2 2 2 2 2 2 2 2 2 2 2 
                2 2 2 2 2 2 2 2 2 2 2 2
    """))
    game.show_long_text("You haven't succeeded in treating your patient.",
        DialogLayout.CENTER)
    game.over(False, effects.dissolve)
def set_MC_projectiles():
    global MCs_magic, projectile_thrown
    if projectile_thrown == 1:
        if characterAnimations.matches_rule(MC, characterAnimations.rule(Predicate.FACING_RIGHT)):
            MCs_magic = sprites.create_projectile_from_sprite(assets.image("""
                MC projectile
            """), MC, 120, 5)
        if characterAnimations.matches_rule(MC, characterAnimations.rule(Predicate.FACING_LEFT)):
            MCs_magic = sprites.create_projectile_from_sprite(assets.image("""
                MC projectile
            """), MC, -120, -5)
        MCs_magic.x += 20
        MCs_magic.y += 8
        MCs_magic.start_effect(effects.warm_radial, 1000)
        scene.camera_shake(1, 100)
        animation.run_image_animation(MCs_magic,
            assets.animation("""
                MC animated projectile
            """),
            75,
            True)
        projectile_thrown = 0
"""

A cool down function, so players can't spam projectiles and win too easily.

"""
def projectile_cool_down():
    global cool_down, projectile_thrown
    cool_down = 900
    projectile_thrown = 0

def on_b_released():
    animation.stop_animation(animation.AnimationTypes.IMAGE_ANIMATION, MC)
controller.B.on_event(ControllerButtonEvent.RELEASED, on_b_released)

"""

The main menu for the game which lets the player choose to start the game or read about the lore behind the game.

"""
"""

The start of a battle sequence. Here, the level is loaded and key components like gravity is set.

"""
def main_menu():
    story.show_player_choices("Start", "Controls", "Game play")
    if story.check_last_answer("Start"):
        music.sonar.play()
        Day_1()
    if story.check_last_answer("Controls"):
        controls()
    if story.check_last_answer("Game play"):
        game_play_explanation()

def on_on_overlap2(sprite3, otherSprite2):
    if MC.overlaps_with(Gun):
        game.set_dialog_frame(assets.image("""
            dirtied documents
        """))
        game.set_dialog_cursor(img("""
            2 2 2 f f 2 2 2 
                        2 2 2 f d f 2 2 
                        2 2 2 f f 2 2 2 
                        f f f f f f f f 
                        2 f f f f f f 2 
                        2 2 f f f f 2 2 
                        2 2 f f f f 2 2 
                        2 2 2 f f 2 2 2
        """))
        game.show_long_text("A P-38. Could this have been the type of pistol he used to fight?",
            DialogLayout.CENTER)
        Gun.destroy(effects.disintegrate, 1000)
    if MC.overlaps_with(Photograph):
        game.set_dialog_frame(assets.image("""
            dirtied documents
        """))
        game.show_long_text("A family photograph? He clearly values others a lot.",
            DialogLayout.CENTER)
        Photograph.destroy(effects.fire, 1000)
    if MC.overlaps_with(Lighter):
        game.set_dialog_frame(assets.image("""
            dirtied documents
        """))
        game.show_long_text("A Barton lighter. Perhaps he used this to pass the time with his friends in the trenches.",
            DialogLayout.CENTER)
        Lighter.destroy(effects.disintegrate, 1000)
sprites.on_overlap(SpriteKind.player, SpriteKind.Object, on_on_overlap2)

def controls():
    game.show_long_text("For computer users:    " + "←→: move        " + "↑: jump     " + "F: fire",
        DialogLayout.FULL)
    game.show_long_text("For mobile users:    " + "D-pad: to move         " + "Up: jump                " + "B: fire",
        DialogLayout.FULL)
    main_menu()

def on_on_overlap3(sprite4, otherSprite3):
    sprite4.destroy()
    statusbars.get_status_bar_attached_to(StatusBarKind.enemy_health, patient_1_enemy).value += -10
sprites.on_overlap(SpriteKind.projectile, SpriteKind.enemy, on_on_overlap3)

"""

Creates and animates the projectile from the player. Adds effects for when the projectile is thrown. Positions the projectile to follow the enemy.

"""
def level_1():
    global gravity, jump_height, player_speed, projectile_velocity, cool_down, jump_velocity
    scene.set_background_image(img("""
        9999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999
                9999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999
                9999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999
                9999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999
                9999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999
                9999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999
                9999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999
                9999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999
                9999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999
                9999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999
                9999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999
                9999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999
                9999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999
                9999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999
                9999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999
                9999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999
                9999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999
                9999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999
                9999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999
                9999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999
                9999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999
                9999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999
                9999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999
                9999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999
                9999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999
                9999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999
                9999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999
                9999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999
                9999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999
                9999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999
                9999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999
                9999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999
                9999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999
                9999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999
                9999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999
                9999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999
                9999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999
                9999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999
                9999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999
                9999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999
                9999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999
                9999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999
                9999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999
                9999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999
                9999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999
                9999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999
                9999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999
                9999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999
                9999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999
                9999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999
                9999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999
                9999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999
                9999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999
                9999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999
                9999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999
                9999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999
                9999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999
                9999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999
                9999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999
                9999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999
                9999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999
                9999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999
                9999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999
                9999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999
                9999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999
                9999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999
                9999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999
                9999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999
                9999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999
                9999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999
                9999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999
                9999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999
                9999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999
                9999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999
                9999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999
                9999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999
                9999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999
                9999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999
                9999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999
                9999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999
                9999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999
                9999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999
                9999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999
                9999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999
                9999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999
                9999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999
                9999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999
                9999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999
                9999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999
                9999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999
                9999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999
                9999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999
                9999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999
                9999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999
                9999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999
                9999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999
                9999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999
                9999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999
                9999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999
                9999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999
                9999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999
                9999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999
                9999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999
                9999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999
                9999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999
                9999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999
                9999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999
                9999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999
                9999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999
                9999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999
                9999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999
                9999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999
                9999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999
                9999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999
                9999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999
                9999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999
                9999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999
                9999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999
                9999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999
                9999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999
    """))
    effects.clouds.start_screen_effect()
    tiles.set_current_tilemap(tilemap("""
        Cuphead
    """))
    gravity = 300
    jump_height = 90
    player_speed = 100
    projectile_velocity = 150
    cool_down = 500
    jump_velocity = 0 - Math.sqrt(2 * (gravity * jump_height))
    MCs_position()
    set_patient_1_enemy()
    game_timer_1()
    patients_memories()
"""

Overlap event where the player loses all their lives if the player overlaps the enemy and it results in a game over.

"""

def on_on_overlap4(sprite5, otherSprite4):
    sprite5.destroy()
    otherSprite4.destroy()
    info.change_life_by(-3)
    scene.camera_shake(3, 1000)
    results_screen_2()
sprites.on_overlap(SpriteKind.player, SpriteKind.enemy, on_on_overlap4)

"""

A quick splash screen of a potential title for the game.

"""
jump_velocity = 0
projectile_velocity = 0
jump_height = 0
MCs_magic: Sprite = None
status_bar: StatusBarSprite = None
player_speed = 0
projectile_thrown = 0
cool_down = 0
gravity = 0
patient_1: Sprite = None
patient_1_enemy: Sprite = None
MC: Sprite = None
enemy_projectiles: Sprite = None
Lighter: Sprite = None
Photograph: Sprite = None
Gun: Sprite = None
music.big_crash.play()
scene.set_background_color(15)
game.set_dialog_cursor(assets.image("""
    cursor
"""))
game.splash("A Means of Escape")
pause(100)
main_menu()

def on_on_update():
    characterAnimations.loop_frames(MC,
        assets.animation("""
            MC idle animation right
        """),
        600,
        characterAnimations.rule(Predicate.NOT_MOVING, Predicate.FACING_RIGHT))
    characterAnimations.loop_frames(MC,
        assets.animation("""
            Mc idle animation left
        """),
        600,
        characterAnimations.rule(Predicate.NOT_MOVING, Predicate.FACING_LEFT))
    characterAnimations.loop_frames(MC,
        assets.animation("""
            MC moving right
        """),
        600,
        characterAnimations.rule(Predicate.MOVING, Predicate.FACING_RIGHT))
    characterAnimations.loop_frames(MC,
        assets.animation("""
            MC moving left
        """),
        600,
        characterAnimations.rule(Predicate.MOVING, Predicate.FACING_LEFT))
    characterAnimations.loop_frames(MC,
        assets.animation("""
            crouch animation
        """),
        600,
        characterAnimations.rule(Predicate.FACING_DOWN, Predicate.NOT_MOVING))
    characterAnimations.loop_frames(MC,
        assets.animation("""
            jumping animation
        """),
        600,
        characterAnimations.rule(Predicate.MOVING, Predicate.NOT_MOVING, Predicate.FACING_UP))
game.on_update(on_on_update)

def on_forever():
    MakeyMakey.set_simulator_keymap(MakeyMakey.PlayerNumber.ONE,
        MakeyMakey.MakeyMakeyKey.W,
        MakeyMakey.MakeyMakeyKey.S,
        MakeyMakey.MakeyMakeyKey.A,
        MakeyMakey.MakeyMakeyKey.D,
        MakeyMakey.MakeyMakeyKey.SPACE,
        MakeyMakey.MakeyMakeyKey.F)
    MakeyMakey.set_simulator_keymap(MakeyMakey.PlayerNumber.TWO,
        MakeyMakey.MakeyMakeyKey.UP,
        MakeyMakey.MakeyMakeyKey.DOWN,
        MakeyMakey.MakeyMakeyKey.LEFT,
        MakeyMakey.MakeyMakeyKey.RIGHT,
        MakeyMakey.MakeyMakeyKey.G,
        MakeyMakey.MakeyMakeyKey.RIGHT_CLICK)
forever(on_forever)
