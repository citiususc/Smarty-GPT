from smartygpt import SmartyGPT, Models

if __name__=="__main__":
    s = SmartyGPT(model=Models.GPT4, prompt="Rapper", path="/home/marcos/") #### model text-davinci-003 by default
    print("Context:", s.get_context())
    result = s.wrapper("Rap in the same style as Eminem")
    print(result)