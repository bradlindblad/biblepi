import vlc
import easygui
import random
import time


def main():

    while True:

        timerYN = easygui.buttonbox(
            title="BiblePi",
            msg="Play on timer or free play?",
            choices=["Timer", "Freeplay"],
        )

        choices = [
            "Matt",
            "Mark",
            "Luke",
            "John",
            "Acts",
            "Rom",
            "1Cor",
            "2Cor",
            "Galat",
            "Eph",
            "Phil",
            "Colos",
            "1Thes",
            "2Thes",
            "1Tim",
            "2Tim",
            "Titus",
            "Philp",
            "Heb",
            "James",
            "1Pete",
            "2Pete",
            "1John",
            "2John",
            "3John",
            "Jude",
            "Rev",
        ]


        media = random.choice(choices)
        instance = vlc.MediaPlayer("bible/" + media)

        while True:

            choice = easygui.buttonbox(
                title="BiblePi",
                msg=f"Press Play to start\n\nMode = {timerYN}",
                choices=["Play", "Pause", "Stop", "Start Over"],
            )
            print(choice)
            if timerYN == "Timer":
                playlen = easygui.buttonbox(
                    title="BiblePi",
                    msg="Play for how many minutes?",
                    choices=["5", "10", "20", "60"],
                )
                playlen = int(playlen)

            if choice == "Play":
                instance.play()
            elif choice == "Pause":
                instance.pause()
            elif choice == "Stop":
                instance.stop()
            elif choice == "Start Over":
                instance.stop()
                break
            if timerYN == "Timer":
                time.sleep(playlen * 60)
                instance.stop()
                timerYN = "Freeplay"
                break


if __name__ == "__main__":
    main()
