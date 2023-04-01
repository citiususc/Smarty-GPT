from smartygpt import SmartyGPT, Models

if __name__=="__main__":
    s = SmartyGPT(model=Models.FlanT5, prompt="perplexity", path="/home/marcos/") #### model text-davinci-003 by default
    print("Context:", s.get_context())
    result = s.wrapper("Continue the sentence")
    print(result)