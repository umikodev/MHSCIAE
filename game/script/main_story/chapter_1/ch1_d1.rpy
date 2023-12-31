label ch1_d1:
    scene black
    with fade
    centered "Chapter 1 - Day 1\n Tuesday 29th August 13040"
    
    scene bg school hallway
    with fade
    "My first day back at school."
    show mc school_uni_blazer eye_close_smile
    with dissolve
    "I take a deep breath."
    show mc school_uni_blazer eye_close_talk
    voice "audio/VoiceVox/Chapter 1/Day1/MC/MC001.wav"
    mc "Phew, I made it..."
    show mc school_uni_blazer eye_close_smile
    "Some people would call me strange, but I like school!"
    "However, after being away for a few weeks, my body clock freaked out... so I ended up almost being late."
    show mc school_uni_blazer eye_open_talk
    voice "audio/VoiceVox/Chapter 1/Day1/MC/MC002.wav"
    mc "Right, let's do this!"
    show mc school_uni_blazer eye_open_smile

    scene bg classroom day
    show mc school_uni_blazer eye_open_smile
    with fade
    "I enter the classroom."
    "It's already mostly full. I didn't realise I was {i}that{/i} late..."
    "The teacher isn't here, at least."
    "I take my seat and wait patiently."
    "After a few minutes, she arrives."
    show mc at left with move
    show jennifer teacher_uni eye_open_smile at center with moveinright
    show jennifer teacher_uni eye_open_talk
    voice "audio/VoiceVox/Chapter 1/Day1/Jen/Jen001.wav"
    jen "Okay, everyone, settle down!"
    show jennifer teacher_uni eye_open_smile
    "The class begins to quieten with her entry."
    show jennifer teacher_uni eye_open_talk
    voice "audio/VoiceVox/Chapter 1/Day1/Jen/Jen002.wav"
    jen "Welcome back to school, everyone! Let's make this an exciting year!"
    voice "audio/VoiceVox/Chapter 1/Day1/Jen/Jen003.wav"
    jen "I also have some news for you all."
    show jennifer teacher_uni eye_open_smile
    "Huh, news...?"
    "I wonder what it could be..."
    show jennifer teacher_uni eye_close_talk
    voice "audio/VoiceVox/Chapter 1/Day1/Jen/Jen004.wav"
    jen "You can come in now."
    show jennifer teacher_uni eye_close_smile
    "A moment of silence, before..."
    show hareka school_uni eye_open_neutral at right with moveinright
    show mc school_uni_blazer eye_open_surprised_blush
    "...an unfamiliar girl enters the classroom."
    "My heart skips a beat."
    show jennifer teacher_uni eye_open_talk
    voice "audio/VoiceVox/Chapter 1/Day1/Jen/Jen005.wav"
    jen "Everyone, we have a new addition to the class, starting today."
    voice "audio/VoiceVox/Chapter 1/Day1/Jen/Jen006.wav"
    jen "Why don't you introduce yourself?"
    show jennifer teacher_uni eye_open_smile
    show hareka school_uni eye_open_neutral_talk
    voice "audio/VoiceVox/Chapter 1/Day1/Hareka/Hareka001.wav"
    hareka "Hello. My name is Hareka Kiratani."
    show hareka school_uni eye_open_neutral
    "Hushed whispers fill the room."
    "I can't stop staring at her."
    "She's so..."
    show jennifer teacher_uni eye_open_talk
    voice "audio/VoiceVox/Chapter 1/Day1/Jen/Jen007.wav"
    jen "You can sit in the middle there, next to Alexander."
    show jennifer teacher_uni eye_open_smile
    "WHAT-"
    show hareka school_uni eye_open_neutral_talk
    voice "audio/VoiceVox/Chapter 1/Day1/Hareka/Hareka002.wav"
    hareka "Okay."
    show hareka school_uni eye_open_neutral
    hide jennifer with dissolve
    show hareka at center with move
    "Hareka heads to the seat next to me."
    show mc school_uni_blazer eye_open_surprised_talk_blush
    voice "audio/VoiceVox/Chapter 1/Day1/MC/MC003.wav"
    mc "H-Hello..."
    show mc school_uni_blazer eye_open_surprised_blush
    show hareka school_uni eye_open_neutral_talk
    voice "audio/VoiceVox/Chapter 1/Day1/Hareka/Hareka003.wav"
    hareka "Hello."
    show hareka school_uni eye_open_neutral
    "She... She said hello to me!"
    voice "audio/VoiceVox/Chapter 1/Day1/Jen/Jen008.wav"
    jen "Okay, everyone, let's begin work!"
    show mc school_uni_blazer eye_close_surprised_blush
    "I take a deep breath."
    "I must focus..."
    show mc school_uni_blazer eye_open_smile
    "Yes, I can do it!"

    scene bg classroom day
    show mc school_uni_blazer eye_open_smile at left
    show hareka school_uni eye_open_neutral at center
    with fade
    "Before I know it, it's lunchtime."
    "I somehow managed to get through it..."
    "I think I'm getting used to having her sit next to me already. Thank goodness."
    show mc school_uni_blazer eye_open_talk
    voice "audio/VoiceVox/Chapter 1/Day1/MC/MC004.wav"
    mc "Let's go to the cafeteria, Hareka."
    show mc school_uni_blazer eye_open_smile
    show hareka school_uni eye_open_neutral_talk
    voice "audio/VoiceVox/Chapter 1/Day1/Hareka/Hareka004.wav"
    hareka "I was planning to."
    show hareka school_uni eye_open_neutral
    show mc school_uni_blazer eye_close_talk
    voice "audio/VoiceVox/Chapter 1/Day1/MC/MC005.wav"
    mc "Ah, yeah, of course..."
    show mc school_uni_blazer eye_close_smile

    scene bg cafeteria day
    show mc school_uni_blazer eye_open_smile at left
    show hareka school_uni eye_open_neutral at center
    with fade
    "We head to the cafeteria together."
    "After grabbing our meals, we find an empty table and sit down."
    "I should probably use this time to get to know her better..."
    menu ch1_d1_gettoknowhareka_questions:
        "What should I ask her?"
        "What are your hobbies?" if not ch1_d1_gettoknowhareka_hobbiesunlock:
            $ ch1_d1_gettoknowhareka_hobbiesunlock = True
            show mc school_uni_blazer eye_open_talk
            voice "audio/VoiceVox/Chapter 1/Day1/MC/MC006.wav"
            mc "So... What do you like to do in your free time, Hareka?"
            show mc school_uni_blazer eye_open_smile
            show hareka school_uni eye_open_neutral_talk
            voice "audio/VoiceVox/Chapter 1/Day1/Hareka/Hareka005.wav"
            hareka "I like writing and art."
            show hareka school_uni eye_open_neutral
            show mc school_uni_blazer eye_open_talk
            voice "audio/VoiceVox/Chapter 1/Day1/MC/MC007.wav"
            mc "Oh, wow! So you're the artsy type!"
            voice "audio/VoiceVox/Chapter 1/Day1/MC/MC008.wav"
            mc "I like art too!"
            show mc school_uni_blazer eye_open_smile
            "Phew, we have something in common already!"
            show hareka school_uni eye_open_neutral_talk
            voice "audio/VoiceVox/Chapter 1/Day1/Hareka/Hareka006.wav"
            hareka "Oh."
            show hareka school_uni eye_open_neutral
            show mc school_uni_blazer eye_open_frown
            "..."
            "What was that flat response?!"
            "I begin to feel nervous."
            "Maybe she's just shy?"
            "It's best not to think too hard into it."
            show mc school_uni_blazer eye_open_smile
            jump ch1_d1_gettoknowhareka_questions
        "Why did you move to this school?" if not ch1_d1_gettoknowhareka_schoolmoveunlock:
            $ ch1_d1_gettoknowhareka_schoolmoveunlock = True
            show mc school_uni_blazer eye_open_talk
            voice "audio/VoiceVox/Chapter 1/Day1/MC/MC009.wav"
            mc "So... Why did you move to this school, Hareka?"
            show mc school_uni_blazer eye_open_smile
            show hareka school_uni eye_open_neutral_talk
            voice "audio/VoiceVox/Chapter 1/Day1/Hareka/Hareka007.wav"
            hareka "I'd rather not speak about that."
            show hareka school_uni eye_open_neutral
            show mc school_uni_blazer eye_open_talk
            voice "audio/VoiceVox/Chapter 1/Day1/MC/MC010.wav"
            mc "O-Oh... Okay..."
            show mc school_uni_blazer eye_open_smile
            "Huh, strange..."
            "I'd better respect her decision though."
            jump ch1_d1_gettoknowhareka_questions
        "What do you think of the school so far?" if not ch1_d1_gettoknowhareka_schoolopinionunlock:
            $ ch1_d1_gettoknowhareka_schoolopinionunlock = True
            show mc school_uni_blazer eye_open_talk
            voice "audio/VoiceVox/Chapter 1/Day1/MC/MC011.wav"
            mc "So... What do you think of the school so far?"
            voice "audio/VoiceVox/Chapter 1/Day1/MC/MC012.wav"
            mc "Like, through the morning you've been here?"
            show mc school_uni_blazer eye_open_smile
            show hareka school_uni eye_open_neutral_talk
            voice "audio/VoiceVox/Chapter 1/Day1/Hareka/Hareka008.wav"
            hareka "I think it's nice."
            show hareka school_uni eye_open_neutral
            show mc school_uni_blazer eye_open_talk
            voice "audio/VoiceVox/Chapter 1/Day1/MC/MC013.wav"
            mc "Oh, good!"
            voice "audio/VoiceVox/Chapter 1/Day1/MC/MC014.wav"
            mc "I'm glad you're liking it so far."
            show mc school_uni_blazer eye_open_smile
            "That's great! I'm glad she's happy."
            "Why am I so glad, though...?"
            jump ch1_d1_gettoknowhareka_questions
        "Done" if ch1_d1_gettoknowhareka_hobbiesunlock or ch1_d1_gettoknowhareka_schoolmoveunlock or ch1_d1_gettoknowhareka_schoolopinionunlock:
            jump ch1_d1_aftermenuone
label ch1_d1_aftermenuone:
    show hareka school_uni eye_open_neutral_talk
    voice "audio/VoiceVox/Chapter 1/Day1/Hareka/Hareka009.wav"
    hareka "Why are you so interested in getting to know me?"
    show hareka school_uni eye_open_neutral
    show mc school_uni_blazer eye_open_surprised_talk_blush
    voice "audio/VoiceVox/Chapter 1/Day1/MC/MC015.wav"
    mc "O-Oh!"
    show mc school_uni_blazer eye_open_surprised_blush
    "Aah, what do I even say?! That took me totally off guard..."
    "Why do I... That's a good question..."
    show mc school_uni_blazer eye_close_surprised_talk_blush
    voice "audio/VoiceVox/Chapter 1/Day1/MC/MC016.wav"
    mc "W-Well... Uhm..."
    show mc school_uni_blazer eye_close_surprised_blush
    "I should just ask her to be friends with me..."
    "I don't know why I'm so overwhelmed by her, but surely..."
    menu ch1_d1_harekafriendchoice:
        "Ask her.":
            $ ch1_d1_harekafriendask = True
            show mc school_uni_blazer eye_open_surprised_talk_blush
            voice "audio/VoiceVox/Chapter 1/Day1/MC/MC017.wav"
            mc "Well..."
            voice "audio/VoiceVox/Chapter 1/Day1/MC/MC018.wav"
            mc "I want to be friends with you..."
            voice "audio/VoiceVox/Chapter 1/Day1/MC/MC019.wav"
            mc "I-If you want..."
            show mc school_uni_blazer eye_close_surprised_blush
            "Damn it, that's so embarrassing!"
            "I wish I could take it back..."
            "Aaaah..."
            "There's a moment of silence."
            show hareka school_uni eye_open_neutral_talk
            voice "audio/VoiceVox/Chapter 1/Day1/Hareka/Hareka010.wav"
            hareka "Okay."
            show hareka school_uni eye_open_neutral
            show mc school_uni_blazer eye_open_surprised_talk_blush
            voice "audio/VoiceVox/Chapter 1/Day1/MC/MC020.wav"
            mc "W-What?!"
            show mc school_uni_blazer eye_open_surprised_blush
            "There's no way..."
            show hareka school_uni eye_open_neutral_talk
            voice "audio/VoiceVox/Chapter 1/Day1/Hareka/Hareka011.wav"
            hareka "Sure, you can be my friend."
            show hareka school_uni eye_open_neutral
            "Woah..."
            "I..."
            show mc school_uni_blazer eye_open_surprised_talk_blush
            voice "audio/VoiceVox/Chapter 1/Day1/MC/MC021.wav"
            mc "O-Okay!"
            voice "audio/VoiceVox/Chapter 1/Day1/MC/MC022.wav"
            mc "I'll try my best to, um... be a good friend!"
            show mc school_uni_blazer eye_open_surprised_blush
            show hareka school_uni eye_open_neutral_talk
            voice "audio/VoiceVox/Chapter 1/Day1/Hareka/Hareka012.wav"
            hareka "Okay. I look forward to it."
            show hareka school_uni eye_open_neutral
            "W-Woah..."
            jump ch1_d1_aftermenutwo
        "Don't ask her.":
            "I decide not to ask her. It'd be wayyy too awkward."
            jump ch1_d1_aftermenutwo
label ch1_d1_aftermenutwo:
    scene bg cafeteria day
    show mc school_uni_blazer eye_open_smile at left
    show hareka school_uni eye_open_neutral at center
    with fade
    "Soon enough, lunchtime is over."
    show mc school_uni_blazer eye_open_talk
    voice "audio/VoiceVox/Chapter 1/Day1/MC/MC023.wav"
    mc "Guess it's class time..."
    show mc school_uni_blazer eye_open_smile
    show hareka school_uni eye_open_neutral_talk
    voice "audio/VoiceVox/Chapter 1/Day1/Hareka/Hareka013.wav"
    hareka "Yes, it is."
    show hareka school_uni eye_open_neutral
    "We clear our trays and head back to class."

    scene bg classroom day
    show mc school_uni_blazer eye_open_smile at left
    show hareka school_uni eye_open_neutral at center
    with fade
    "The day finishes rather quickly."
    "I pack up and turn to Hareka."
    show mc school_uni_blazer eye_open_talk
    voice "audio/VoiceVox/Chapter 1/Day1/MC/MC024.wav"
    mc "How do you get home?"
    show mc school_uni_blazer eye_open_smile
    show hareka school_uni eye_open_neutral_talk
    voice "audio/VoiceVox/Chapter 1/Day1/Hareka/Hareka014.wav"
    hareka "I take the train."
    show hareka school_uni eye_open_neutral
    show mc school_uni_blazer eye_happy_talk
    voice "audio/VoiceVox/Chapter 1/Day1/MC/MC025.wav"
    mc "Oh! So do I!"
    show mc school_uni_blazer eye_open_talk
    voice "audio/VoiceVox/Chapter 1/Day1/MC/MC026.wav"
    mc "Do you want to go home together?"
    show mc school_uni_blazer eye_open_surprised_blush
    "W-Wait..."
    "Why did I say that?!"
    "Ohhhh no, that's bad... that's really bad..."
    "It was impulsive..."
    show hareka school_uni eye_open_neutral_talk
    voice "audio/VoiceVox/Chapter 1/Day1/Hareka/Hareka015.wav"
    hareka "Okay."
    show hareka school_uni eye_open_neutral
    show mc school_uni_blazer eye_open_surprised_talk_blush
    voice "audio/VoiceVox/Chapter 1/Day1/MC/MC027.wav"
    mc "O-O-Oh! O-Okay!"
    voice "audio/VoiceVox/Chapter 1/Day1/MC/MC028.wav"
    mc "Um, let's go then...!"
    show mc school_uni_blazer eye_open_surprised_blush
    window hide
    pause 0.1
    
    show bg train day
    show mc school_uni_blazer eye_open_surprised_blush
    show hareka school_uni eye_open_neutral
    with fade
    "Oh my gosh... I don't believe it..."
    "I'm going home with a girl..."
    "I'm on a train with a girl!"
    if ch1_d1_harekafriendask:
        "A girl I'm {i}friends{/i} with!!"
    "This is the greatest day of my life!!!"
    show hareka school_uni eye_open_neutral_talk
    voice "audio/VoiceVox/Chapter 1/Day1/Hareka/Hareka016.wav"
    hareka "Are you okay?"
    show hareka school_uni eye_open_neutral
    show mc school_uni_blazer eye_open_surprised_talk_blush
    voice "audio/VoiceVox/Chapter 1/Day1/MC/MC029.wav"
    mc "W-W-What??"
    show mc school_uni_blazer eye_open_surprised_blush
    show hareka school_uni eye_open_neutral_talk
    voice "audio/VoiceVox/Chapter 1/Day1/Hareka/Hareka017.wav"
    hareka "You look really flushed. Are you too warm?"
    show hareka school_uni eye_open_neutral
    show mc school_uni_blazer eye_open_surprised_talk_blush
    voice "audio/VoiceVox/Chapter 1/Day1/MC/MC030.wav"
    mc "O-Oh..."
    show mc school_uni_blazer eye_open_surprised_blush
    "Shit. She noticed."
    show mc school_uni_blazer eye_close_surprised_talk_blush
    voice "audio/VoiceVox/Chapter 1/Day1/MC/MC031.wav"
    mc "M-Maybe..."
    show mc school_uni_blazer eye_close_surprised_blush
    show hareka school_uni eye_open_neutral_talk
    voice "audio/VoiceVox/Chapter 1/Day1/Hareka/Hareka018.wav"
    hareka "Why don't you take off your blazer?"
    show hareka school_uni eye_open_neutral
    "Oh, right..."
    show mc school_uni_noblazer eye_close_smile
    "I remove it as she asked."
    "I begin to calm down a bit."
    show mc school_uni_noblazer eye_open_smile
    "The ride continues in silence."
    "After a while, the train announces her stop. She stands up."
    show hareka school_uni eye_open_neutral_talk
    voice "audio/VoiceVox/Chapter 1/Day1/Hareka/Hareka019.wav"
    hareka "Thank you for coming with me."
    show hareka school_uni eye_open_neutral
    show mc school_uni_noblazer eye_open_surprised_talk_blush
    voice "audio/VoiceVox/Chapter 1/Day1/MC/MC032.wav"
    mc "O-Oh, you're welcome!"
    show mc school_uni_noblazer eye_open_surprised_blush
    "Damn it, I was caught off guard... I didn't expect her to thank me..."
    show hareka school_uni eye_open_neutral_talk
    voice "audio/VoiceVox/Chapter 1/Day1/Hareka/Hareka020.wav"
    hareka "I'll see you tomorrow."
    show hareka school_uni eye_open_neutral
    show mc school_uni_noblazer eye_open_surprised_talk_blush
    voice "audio/VoiceVox/Chapter 1/Day1/MC/MC033.wav"
    mc "Yeah, okay!"
    voice "audio/VoiceVox/Chapter 1/Day1/MC/MC034.wav"
    mc "Bye!"
    show mc school_uni_noblazer eye_open_surprised_blush
    hide hareka with dissolve
    "She exits the train."
    "I'm left with a rush of dopamine."
    "Wow... I can't believe this happened..."
    "She's so..."
    "Aaaah..."

    scene bg futon room
    show mc school_uni_noblazer eye_open_smile
    with fade
    "I finally return home."
    "My stop is much further than hers..."
    "Going to a school so far away was always a pain, even though I liked going... but maybe I don't mind so much now."
    show mc school_uni_noblazer eye_close_smile
    "She's so... cool..."
    if ch1_d1_harekafriendask:
        "And she's my friend now... I can't believe it..."
    show mc school_uni_noblazer eye_open_smile
    "Well, I'd better get started on dinner."

    scene bg futon room night
    with fade
    "I made spaghetti bolognese for dinner, and then played some video games for a while."
    "Now it's finally time for bed..."
    "I snuggle into my bed. It's nice and warm."
    "I can't wait to see her tomorrow..."

    scene black
    with fade
    centered "Chapter 1 - Day 1 complete!"
    menu ch1_d1_completemenu:
        "Would you like to replay the day, or move onto the next day?"
        "Replay.":
            "You've chosen to replay {b}Chapter 1 - Day 1{/b}.\nEnjoy!"
            jump ch1_d1
        "Move on.":
            "You've chosen to move on to {b}Chapter 1 - Day 2{/b}.\nEnjoy!"
            jump ch1_d2