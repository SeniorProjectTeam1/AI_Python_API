from src.projecty import AI


if __name__ == "__main__":
    gpt = AI()
    gpt.set_message(
        "Tell me 3 computer engineering project idea for 500 dollars that has a 40 percent innovative and has to do with a oxygen reader for astmah using iot, embedded design, and electronic design."
    )
    print(gpt.get_response())
