from llm_retrival.call_llm.controller import Controller

additional_text = """Before college the two main things I worked on, outside of school, were writing and programming. I didn't write essays. I wrote what beginning writers were supposed to write then, and probably still are: short stories. My stories were awful. They had hardly any plot, just characters with strong feelings, which I imagined made them deep.

The first programs I tried writing were on the IBM 1401 that our school district used for what was then called "data processing." This was in 9th grade, so I was 13 or 14. The school district's 1401 happened to be in the basement of our junior high school, and my friend Rich Draves and I got permission to use it. It was like a mini Bond villain's lair down there, with all these alien-looking machines — CPU, disk drives, printer, card reader — sitting up on a raised floor under bright fluorescent lights.

The language we used was an early version of Fortran. You had to type programs on punch cards, then stack them in the card reader and press a button to load the program into memory and run it. The result would ordinarily be to print something on the spectacularly loud printer."""


paraList = [i for i  in additional_text.split("\n") if i ]
# controller = Controller(additional_text)
NewParaList = []

for i in paraList:
    print(i)
    controller = Controller(i)
    new = {
          "original":  controller.get_text(),
          "simplified": controller.get_paraphrase(controller.get_text()),
        "keywords": controller.get_key_word(controller.get_text())
        }
    NewParaList.append(new)



object = {
"title": "The Need to Read",
      "date": "November 2023",
      "paragraphs": NewParaList
    }
print(object)



