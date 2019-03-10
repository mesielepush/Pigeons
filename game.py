import os
import time
import pygame
import numpy as np
from scipy.stats import truncnorm
from sklearn.externals import joblib

########################################################################
######################  Pygame Init
########################################################################

pygame.init()
pygame.display.set_caption("The Pigeon")
clock=pygame.time.Clock()
dw=800
dh=600
disp=pygame.display.set_mode((dw,dh), pygame.RESIZABLE | pygame.HWSURFACE | pygame.DOUBLEBUF )

from constants import *


def getVIs(mean):
    """returns a list of 60 ints from a truncated normal distribution"""

    X = truncnorm(-2,2,loc= mean,scale= mean*0.33)
    ready = False
    while ready is False:
        x=[int(x) for x in X.rvs(60)]
        print(np.mean(x))
        if (mean-0.1) <np.mean(x)< (mean+0.3):
            return(x)
            ready = True

def plot_session(data,user,session):
    """This is to save three plots as jpg.
    
    1.- Frequency of response over time.
    2.- Ratio of response over time.
    3.- Frequency of response over reinforcments.
    """
    import matplotlib.pyplot as plt
    if not os.path.exists(r'data\{0}\session_{1}'.format(user,session)):
                os.makedirs(r'data\{0}\session_{1}'.format(user,session))

    ###### FREQUENCY OF RESPONSE OVER TIME
    ######
    
    time_range = np.arange(0.0,round(data['total_time'],1),0.1)

    count = 0
    left  = [] 
    for i in time_range:
        if i <= data['left_click'][count]:
            left.append(count)
        else:
            if count == len(data['left_click'])-1:
                left.append(count)
            else:
                count += 1
                left.append(count)
    count = 0
    right = []
    for b in time_range:
        if b <= data['right_click'][count]:
            right.append(count)
        else:
            if count == len(data['right_click'])-1:
                right.append(count)
            else:
                count +=1
                right.append(count)
    left_ratio  = []
    right_ratio = []
    for a, b in zip(left,right):
        total = a+b
        try:
            left_ratio.append(a/total)
            right_ratio.append(b/total)
        except:
            left_ratio.append(0)
            right_ratio.append(0)

    plt.suptitle('{0},  session {1}'.format(user,session), x = 0.515, y= 1)
    plt.title('frequency of responses',fontsize=12)
    plt.plot(left,color = 'blue', label = 'left')
    plt.plot(right,color= 'red', label = 'right')
    plt.xlabel('tenths of a second',fontsize=12)
    plt.ylabel('responses',fontsize=12)
    plt.legend()
    plt.savefig('data/{0}/session_{1}/freq_of_resp_{1}.jpg'.format(user,session))

    ###### RATIO OF RESPONSE OVER TIME
    ######
    
    plt.close('all')
    left_ratio  = []
    right_ratio = []
    for a, b in zip(left,right):
        total = a+b
        try:
            left_ratio.append(a/total)
            right_ratio.append(b/total)
        except:
            left_ratio.append(0)
            right_ratio.append(0)

    plt.suptitle('{0},  session {1}'.format(user,session), x = 0.515, y= 1)
    plt.title('ratio of responses',fontsize=12)
    plt.xlabel('tenths of a second',fontsize=12)
    plt.ylabel('% responses',fontsize=12)
    plt.plot(left_ratio,color='red', label = 'left')
    plt.plot(right_ratio,color='blue', label = 'right')
    plt.legend()
    plt.savefig('data/{0}/session_{1}/ratio_of_resp_{1}.jpg'.format(user,session))

    #### FREQUENCY OF RESPONSE OVER REINFORCEMENT
    ####

    plt.close('all')
    r_res_l = []
    for a in data['earn_left']:
        r_res_l.append(len([x for x in data['left_click'] if x< a]))
        
    r_res_r = []
    for a in data['earn_right']:
        r_res_r.append(len([x for x in data['right_click'] if x< a]))

    plt.title('left: VI-{0}   VI-{1}: right\npigeon: {2}, Session: {3}'.format(
        int(np.mean(data['left'])),
        int(np.mean(data['right'])),
        user,session))
    
    plt.xlabel('reinforcement by session',fontsize=12)
    plt.ylabel('frequency of response',fontsize=12)        
    plt.plot(r_res_l, label = 'left')
    plt.plot(r_res_r, label = 'right')
    plt.legend()
    plt.savefig('data/{0}/session_{1}/freq_by_reinf_{1}.jpg'.format(user,session))
  
def print_text(texto,x,y,fontsize,color = (0,255,0), font ='futura'):
	"""This prints text through pygame display"""
	
	marcador=pygame.font.Font(r'.\fonts\{0}.ttf'.format(font),fontsize)
	tsuper=marcador.render(texto,True,color)
	trect= tsuper.get_rect()
	trect.center=(x,y)
	disp.blit(tsuper,trect)

def opening():
    """This is the opening scene, returns the user name."""
    beep()
    name = ''
    getting = True

    while getting is True:
        disp.fill((0, 0, 0))
        print_text('type your name',400,100,40,white,'russo')

        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.unicode.isalpha(): name += event.unicode
                elif event.key == pygame.K_BACKSPACE: name = name[:-1]
                elif event.key == pygame.K_RETURN:

                    disp.fill((0, 0, 0))
                    print_text('Your name is: ',400,100,40,white,'russo')
                    print_text(name,400,300,80,red,'russo')
                    pygame.display.flip()
                    time.sleep(1)
                    getting = False
                    
                elif event.type == QUIT:
                    pygame.quit()
                    quit()

        print_text(name,400,300,70,white,'russo')
        pygame.display.flip()

    return name

def intro():
    """ Simple intro """
    disp.blit(intbg2,(0,0))
    pygame.display.update()
    boop()
    
def selection():
    """Selects the mean seconds for reinforcement, returns 2 lists with 60 ints.
    
    There are four different means:
    
    Pigeon mean       : Original mean from the Herrstein experiment, 90 seconds.
    Thinker mean      : 60 seconds.
    Normal people mean: 45 seconds.
    ADHD people mean  : 23 seconds.
    """
    sel_screen = True
    ch_sound.play()
    
    while sel_screen is True:
	
        disp.blit(bachoo,(0,0))
        disp.blit(niveles,(0,0))
        mouse=pygame.mouse.get_pos()
        tit=pygame.mouse.get_pressed()
        for i in pygame.event.get():
            if i.type == pygame.QUIT:
                pygame.quit()
                quit()
            
            if 40 < mouse[0] < 340 and 289 < mouse[1] < 390:
                disp.blit(botpig,(0,0))
                if tit[0] == 1:
                    ch_sound.stop()
                    mean = 90
                    ONIN.play()
                    time.sleep(2)
                    sel_screen = False
            
            if 415 < mouse[0] < 800 and 160 < mouse[1] < 250:
                disp.blit(botpen,(0,0))
                if tit[0] == 1:
                    ch_sound.stop()
                    mean = 60        
                    ONIN.play()
                    time.sleep(2)
                    sel_screen = False
            
            if 415 < mouse[0] < 800 and 290 < mouse[1] < 390:
                disp.blit(bothum,(0,0))
                if tit[0] == 1:
                    ch_sound.stop()
                    mean = 45
                    ONIN.play()
                    time.sleep(2)
                    sel_screen = False
            
            if 415 < mouse[0] < 800 and 420 < mouse[1] < 510:
                disp.blit(bothiper,(0,0))
                if tit[0] == 1:
                    ch_sound.stop()
                    mean = 23
                    ONIN.play()
                    time.sleep(2)
                    sel_screen = False
            pygame.display.update()

    # This create the time for the onset of each reinforcer
    # The four diferent ratios for the programs are taken directly from Herrstain (1961)
    programs = [ [1,1], [0.75,1.5], [0.6,3], [0.5,0] ]
    pr = programs[np.random.choice(4)]
    pr = [ getVIs(mean*pr[0]), getVIs(mean*pr[1]) ]
    order = np.random.choice([0,1],2,replace=False)
    left_key  = pr[order[0]]
    right_key = pr[order[1]]
    
    return left_key, right_key

def Session(left,right,user):
    """Main simulation loop, returns a list (as .pkl) with session data as dictionary."""

    session = {
        'total_time' : 0,
        'total_reinf_left' : 0,
        'total_reinf_right': 0,
        'left' : left,
        'right': right,
        'left_click' : [],
        'right_click': [],
        'earn_left' : [],
        'earn_right': []}

    cha1.play(bg_noise, loops=-1)
    x = 286
    y = dh-340
    vel= 5
    time_elapsed = 0

    reinf_count_left = 0
    reinf_count_right= 0

    current_time_left = 0
    current_time_right= 0

    left_cond  = False
    right_cond = False
    
    On = True

    while On is True:
        
        times = clock.tick()
        time_elapsed += times /1000
        next_left = left[reinf_count_left]
        next_right= right[reinf_count_right]

        current_time_left  += times /1000
        current_time_right += times /1000

        

        disp.blit(bg,(0,0))
        print_text( str(reinf_count_left + reinf_count_right) ,405,242,15)
        disp.blit(p1,(x,y))
        


        os.system('cls')
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                On = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                    cha2.play(arr,loops=-1)
                if event.key == pygame.K_DOWN:
                    cha2.play(gases,loops=-1)
                if event.key == pygame.K_SPACE:
                    
                    if x == -10:
                        session['left_click'].append(round(time_elapsed,1))
                        if left_cond == True:
                            reinf_count_left += 1
                            session['earn_left'].append(round(time_elapsed,1))
                            cha3.play(moneda,loops=0)
                            time.sleep(1)
                            current_time_left = 0
                            left_cond = False
                            
                        elif left_cond == False:
                            if next_left == 0:
                                pass
                            elif next_left <= current_time_left:
                                left_cond = True
                    if x == 550:
                        session['right_click'].append(round(time_elapsed,1))
                        if right_cond == True:
                            reinf_count_right += 1
                            session['earn_right'].append(round(time_elapsed,1))
                            cha3.play(moneda,loops=0)
                            time.sleep(1)
                            current_time_right = 0
                            right_cond = False
                            
                        elif right_cond == False:
                            if next_right == 0:
                                pass
                            elif next_right <= current_time_right:
                                right_cond = True

                        
            if event.type == pygame.KEYUP:
                cha2.stop()
        
        keys = pygame.key.get_pressed()

        if keys[pygame.K_LEFT]:
            
            x-= vel
            if x<=-10:
                x=-10
            disp.blit(bg,(0,0))
            print_text( str(reinf_count_left + reinf_count_right) ,405,242,15)
            disp.blit(p2,(x,y))

        if keys[pygame.K_RIGHT]:
            
            x+= vel
            if x>=550:
                x=550
            disp.blit(bg,(0,0))
            print_text( str(reinf_count_left + reinf_count_right) ,405,242,15)
            disp.blit(p3,(x,y))

        if keys[pygame.K_DOWN]:
            
            disp.blit(bg,(0,0))
            print_text( str(reinf_count_left + reinf_count_right) ,405,242,15)
            disp.blit(p3,(x,dh-240))

        if keys[pygame.K_SPACE]:

            if x == -10:
                cha2.play(slip)
                disp.blit(bg,(0,0))
                print_text( str(reinf_count_left + reinf_count_right) ,405,242,15)
                disp.blit(bizq,(45,282))
                disp.blit(p4,(x,y))
            if x == 550:
                cha2.play(slip)
                disp.blit(bg,(0,0))
                print_text( str(reinf_count_left + reinf_count_right) ,405,242,15)
                disp.blit(bder,(669,282))
                disp.blit(p5,(x-80,y))

        if len(session['earn_right'])+len(session['earn_left']) >= 60:
	    # This is the outro of the Session, appends the current session to the user data file.
	
            session['total_time'] = time_elapsed
            session['total_reinf_left'] = len(session['earn_left'])
            session['total_reinf_right']= len(session['earn_right'])

            if not os.path.exists(r'data\{0}'.format(user)):
                os.makedirs(r'data\{0}'.format(user))
            try:
                data = joblib.load(r'data\{0}\{0}_sessions.pkl'.format(user))
                data.append(session)
                joblib.dump(data,r'data\{0}\{0}_sessions.pkl'.format(user))
            except:
                data=[session]
                joblib.dump(data,r'data\{0}\{0}_sessions.pkl'.format(user))
            
           
            cha2.play(off,loops=0)
            disp.blit(apagado,(0,0))
            if x == -10:
                disp.blit(off_p,(x+10,y))
            else:
                disp.blit(off_p,(x,y))
            pygame.display.update()
            time.sleep(3)
            disp.fill((0, 0, 0))
            print_text('Your session is over',400,200,40,white,'russo')
            print_text('come back soon {0}'.format(user),400,250,40,white,'russo')
            pygame.display.update()
            boop()
            

            On = False

        pygame.display.update()
        
    plot_session(data[-1],user,len(data))
    


    
