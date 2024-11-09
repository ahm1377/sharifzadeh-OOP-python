# نام سیستم عامل ، سیستم پلتفرم و نسخه 
import os
import platform
if(os.name=='nt'):
    print("\n system    : ",platform.system()
          ,"\n release   : ",platform.release())
    
