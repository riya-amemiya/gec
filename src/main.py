import guidance
from dotenv import load_dotenv
import os
import json

load_dotenv()


def main():
    # set the default language model used to execute guidance programs
    guidance.llm = guidance.llms.OpenAI(model="gpt-3.5-turbo")

    def parse(data):
        global ask
        global res
        if data.get("flag") is None:
            data["flag"] = "true"
        elif data["flag"] == "true":
            if data["context"] == "{{ask}}" and ask is not None:
                data["context"] = ask
            elif (
                data["context"] == "{{gen 'res' n=1 temperature=0 max_tokens=2000}}"
                and res is not None
            ):
                data["context"] = res
            return data
        if data.get("context") is None:
            if data["role"] == "assistant":
                data["context"] = "{{gen 'res' n=1 temperature=0 max_tokens=2000}}"
            elif data["role"] == "user":
                data["context"] = "{{ask}}"
        data["role"] = ["{{#" + data["role"] + "~}}", "{{~/" + data["role"] + "}}"]

        return data

    def create_pronpt(data):
        return f"""{data["role"][0]}
    {data["context"]}
    {data["role"][1]}
    """

    data = [
        {
            "role": "user",
        },
        {
            "role": "assistant",
        },
    ]
    ask = None
    tmpAsk = None
    res = None
    output = ""
    tmp = list(map(parse, data))
    pronpt = "".join(list(map(create_pronpt, tmp)))
    try:
        while True:
            if tmpAsk is None:
                ask = input(">>")
            if ask == "exit":
                break
            elif ask == "save":
                tmpData = data
                tmpData = list(map(parse, tmpData))
                tmpPronpt = pronpt
                tmpPronpt = "".join(list(map(create_pronpt, tmpData)))
                if os.path.exists("save") == False:
                    os.mkdir("save")
                id = input("save id:")
                if os.path.exists(f"save/{id}") == False:
                    os.mkdir(f"save/{id}")
                else:
                    print("already exists")
                    overRide = input("override? [y/n]:")
                    if overRide == "y":
                        pass
                    else:
                        continue
                with open(f"save/{id}/log.txt", mode="w") as f:
                    f.write(output)
                with open(f"save/{id}/pronpt.txt", mode="w") as f:
                    f.write(str(tmpPronpt))
                with open(f"save/{id}/data.txt", mode="w") as f:
                    f.write(json.dumps({"data": tmpData}))
                continue
            elif ask == "read":
                with open("ask.txt", mode="r") as f:
                    tmpAsk = f.read()
                    ask = None
                continue
            elif ask == "load":
                id = input("load id:")
                with open(f"save/{id}/log.txt", mode="r") as f:
                    output = f.read()
                with open(f"save/{id}/data.txt", mode="r") as f:
                    data = json.loads(f.read())["data"]
                continue
            elif ask == "nowData":
                print(data)
                print(pronpt)
                continue
            tmp = list(map(parse, data))
            pronpt = "".join(list(map(create_pronpt, tmp)))
            program = guidance(pronpt)
            if tmpAsk:
                ask = tmpAsk
                tmpAsk = None
            executed_program = program(
                ask=ask,
            )
            ask = executed_program["ask"]
            res = executed_program["res"]
            data += [
                {
                    "role": "user",
                },
                {
                    "role": "assistant",
                },
            ]
            with open("log.txt", mode="w") as f:
                print(executed_program["res"])
                output += (
                    "\n" + f"user:{ask}" + "\n" + f"ai:{executed_program['res']}" + "\n"
                )
                f.write(output)
    except KeyboardInterrupt:
        pass


if __name__ == "__main__":
    main()
