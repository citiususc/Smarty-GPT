from smartygpt import SmartyGPT

if __name__=="__main__":
    s = SmartyGPT(prompt="DoctorAdvice", path="/home/marcos/") #### model text-davinci-003 by default
    result = s.wrapper("Can Vitamin D cure COVID-19?")
    print(result)