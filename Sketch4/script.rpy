# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

define i = Character("I")
define w = Character("Waitress")
define c = Character("Customer on Next Table")
define m = Character("Manager")
define s = Character("Sally")

image bg restaurant = im.Scale("bg restaurant.jpg", 1280, 720)
transform slightleft:
    xalign 0.25
    yalign 1.0


# The game starts here.

label start:

    $ score = 0
    $ goal = 3

    # Show a background. This uses a placeholder by default, but you can
    # add a file (named either "bg room.png" or "bg room.jpg") to the
    # images directory to show it.

    scene bg restaurant

    # This shows a character sprite. A placeholder is used, but you can
    # replace it by adding a file named "eileen happy.png" to the images
    # directory.

    # These display lines of dialogue.

    play music "bgm.mp3" fadeout 1

    i "(It's been so long since I ordered. Almost 40 minutes. What is the waitress doing? She probably forgot to put my order...)"
    i "(It's so hot in here. Is the air conditioner still working? I'm almost sweating... And my beer is done.)"
    i "(The air in this restaurant isn't very pleasing either. And the crowd is so noisy... Why would I choose to come here on Monday?)"

    play sound "coin.mp3"

    show waitress happy at slightleft with dissolve:
        xzoom 0.6
        yzoom 0.6

    w "Sorry for the long wait! We've been experiencing the peak hours of the day. Here is you chicken spaghetti. Enjoy!"
    i "(...)"
    i "(This doesn't seem to be the right dish I ordered...)"

    menu:

        "This is not what I ordered. I ordered the spaghetti with mussels, not chicken.":
            jump choice1_wrong

        "Mmmm... Thank you.":
            jump choice1_right

    label choice1_wrong:

        $ menu1_flag = "wrong"
        $ score += 1
        play sound "bubble.mp3"

        w "Really? Let me check. Hold on one second please."

        jump choice1_done

    label choice1_right:

        $ menu1_flag = "right"

        w "Hold on... That's not what you ordered! You got the spaghetti with mussels. I made such a mistake!"

        jump choice1_done

    label choice1_done:

        # ... the game continues here.

        w "Oh I'm so sorry. I've been so messed up today!"
        w "It's all my bad. Please let me make it up for you. OK?"
        i "OK... (Sure you should.)"

        menu:
            w "Would you like a refund or would you like me to replace your dish?"

            "I'd like a refund.":

                $ score += 1
                play sound "bubble.mp3"

                $ menu2_flag = "refund"

                i "(That's probably going to make it easier for both of us.)"
                w "Sure. I'll take that off your check!"

            "I'd like my dish replaced.":

                $ menu2_flag = "replace"

                i "(I don't care. It was her fault... I just want my food.)"
                w "No problem! It'll be ready for you in a few minutes this time."

        i "Thanks. Besides, can I have another beer?"

        if menu2_flag == "refund":

            w "Of course! You've been waiting here for so long... How about I get you this beer for free too?"
            i "(That sounds not bad at all! She's almost kind of lovely now.)"
            i "That's very generous of you. I appreciate it."

        if menu2_flag == "replace":

            w "Sure. I'll be right back with it."

        hide waitress happy

        i "(That's about to make me feel just a little bit better... But the waitress is actually cute. Alright, I should probably just forgive her.)"
        i "(Whew... finally I can start to enjoy some time tonight.)"

        play sound "coin.mp3"

        show waitress happy at slightleft with dissolve:
            xzoom 0.6
            yzoom 0.6

        w "Here is your beer! I brought you extra ice since it's so hot in here. Hopefully that cools you down a little bit."

        if menu2_flag == "replace":
            w "And here is your spaghetti with mussels."

        i "Thanks. (She smiles so warmly that I cannot think of another word to blame her.)"
        i "By the way..."
        w "Ah-uh?"

        menu:

            "I like your earrings. They look pretty on you.":
                jump choice3_earrings

            "...Nothing.":
                jump choice3_nothing

        label choice3_earrings:

            $ score += 1
            play sound "bubble.mp3"

            show waitress blush at slightleft with dissolve:
                xzoom 0.6
                yzoom 0.6

            w "Thank you. Those are my favorites."

            jump choice3_done

        label choice3_nothing:

            w "I'll be here whenever you need me. Enjoy your meal."

            jump choice3_done

        label choice3_done:

            # ... the game continues here.

            hide waitress blush

            i "(She's really cute.)"
            i "(Maybe I've seen her when I came here before. Maybe I just didn't pay attention.)"
            i "(Plus, the food is not bad here. I might even come back to this restaurant sometime this week.)"
            i "(Maybe I'll get to see her again.)"
            i "(Should I come on each Monday? She probably has the same shift every week.)"
            i "(...)"
            i "(What am I thinking? I don't even know her name.)"
            i "(...)"

            play sound "coin.mp3"

            w "Sorry for the wait. Here is your meal."
            c "Why did it take so long? It's been 30 minutes."
            w "We're currently having our busiest hour of the day. I'm really sorry about that."
            c "This is ridiculous. Go get your manager."
            w "I..."
            c "Go get your manager."


            m "What's going on here?"
            c "I waited for my food for half an hour. What the hell is the waitress doing?"
            w "..."
            m "Sorry about that, sir. What's wrong with you, Sally?"
            w "We're just really busy right now..."
            m "It's your job to deal with it! If you don't want to get fired, stop being tardy!"
            w "..."
            m "You hear me?"
            w "Yes..."

            i "(Her name is Sally...)"

            "After a while"
            play sound "coin.mp3"
            show waitress happy at slightleft with dissolve:
                xzoom 0.6
                yzoom 0.6

            s "How is everything? You need more beer?"
            i "(She is trying to smile as warmly as she was. But I can tell she is not happy.)"

            menu:
                "No, thanks. I'm good.":
                    jump choice4_ok
                "I'm good. Thank you... I think you actually did a good job.":
                    jump choice4_good

            label choice4_ok:
                s "OK. Let me know when you need me."

                jump choice4_done

            label choice4_good:
                $ score += 1
                play sound "bubble.mp3"

                s "Huh?"
                i "I said you did a good job, Sally. Your manager was being really mean."
                s "..."
                s "Thank you for saying that."
                i "As long as it make you feel better."
                s "I feel a lot better now. Thank you, sir."
                i "By the way, my name is Michael."
                s "Nice to meet you, Michael. Let me know when you need me again."

                jump choice4_done

            label choice4_done:
                # ... the game continues here.
                hide waitress happy

                i "(That was nice. I wanted to say more but that was good enough already. She has my name now.)"
                i "(I wish I could buy her a drink or something, if it's in a bar. So that she might feel much better.)"

                "After a while"
                i "Can I get my check please?"

                play sound "coin.mp3"
                show waitress happy at slightleft with dissolve:
                    xzoom 0.6
                    yzoom 0.6

                w "Sure. Here it is."
                i "(She was very patient and sweet serving me tonight. Maybe I should tip her extra.)"

                menu:

                    "I'll leave $50 tip.":
                        jump choice5_50

                    "I'll leave $20 tip.":
                        jump choice5_20

                    "I'll leave a $5 tip.":
                        jump choice5_5

                label choice5_50:
                    jump choice5_done

                label choice5_20:
                    $ score += 1
                    play sound "bubble.mp3"

                    jump choice5_done

                label choice5_5:
                    jump choice5_done

                label choice5_done:

                    # ... the game continues here.

                    i "(I'm about to leave... What else should I say?)"
                    i "Would you be interested in grabbing a beer some other day? I'll treat you back."

                    if score > goal:

                        show waitress blush at slightleft with dissolve:
                            xzoom 0.6
                            yzoom 0.6

                        w "Beer sounds good. You wanna go to a secret place that I love?"
                        i "That would be great! I'm looking forward."
                        w "OK. Here is my number. Call me!"

                    else:

                        w "I don't really drink alcohol, but thank you."
                        i "Alright..."
                        i "(Funny that I thought I got a chance... Never mind. It's time to go home.)"
                        i "(It's not a bad dinner experience anyways. I'm just a little bit disappointed... Just a little.)"

                        # This ends the game.
                        return
