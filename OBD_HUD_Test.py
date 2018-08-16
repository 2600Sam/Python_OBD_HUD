import pygame
from pygame.locals import *
import math
import obd
from obd import OBDStatus

pygame.init()

#connection = obd.OBD()
#connect = obd.Async(fast=False)

screen = pygame.display.set_mode((0,0),pygame.FULLSCREEN)
screen_w = screen.get_width()
screen_h = screen.get_height()
circle_y = screen_h / 2
circle1_x = screen_w * .25
circle2_x = screen_w * .5
circle3_x = screen_w * .75
circle_rad = (circle2_x - circle1_x) / 2
speed_text_x = screen_w * .25
speed_text_y = screen_h * .25
rpm_text_x = screen_w * .5
rpm_text_y = screen_h * .25
load_text_x = screen_w * .75
load_text_y = screen_h * .25
headerFont = pygame.font.SysFont("Arial", 50)
digitFont = pygame.font.SysFont("Arial", 45)
numberFont = pygame.font.SysFont("Arial", 10)
white = (255, 255, 255)
black = (0, 0, 0)
green = (0, 255, 0)
yellow = (255, 255, 0)
vcolor = green
grey = (112, 128, 144)
red = (255, 0, 0)
blue = (0, 0, 255)
speed = 0
rpm = 0
load = 0
angle = 5.4

raspberry = 3.141592653

def draw_hud():
	screen.fill(grey)
	#print (ports)
	pygame.draw.circle(screen, black, (int(circle1_x), int(circle_y)), int(circle_rad), 5)
        for step in xrange(0,150,10):
                angle1 = (angle - ((step / .031) / 1000))
                line_x = (circle_rad - 8) * math.sin(angle1) + circle1_x
                line_y = (circle_rad - 8) * math.cos(angle1) + circle_y
                pygame.draw.circle(screen, white, [int(line_x), int(line_y)], 2)
                number_text = numberFont.render(str(step), True, white)
                number_text_loc = number_text.get_rect(center=(line_x, line_y+8))
                screen.blit(number_text, number_text_loc)
	pygame.draw.circle(screen, black, (int(circle2_x), int(circle_y)), int(circle_rad), 5)
        for step in xrange(0,9000,500):
                vcolor = white
                if step >= 4500:
                        vcolor = yellow
                if step >= 6000:
                        vcolor = red
                angle2 = (angle - ((step / 1.9) / 1000))
                line_x = (circle_rad - 8) * math.sin(angle2) + circle2_x
                line_y = (circle_rad - 8) * math.cos(angle2) + circle_y
                number_text = numberFont.render(str(step), True, vcolor)
                number_text_loc = number_text.get_rect(center=(line_x, line_y+8))
                screen.blit(number_text, number_text_loc)
                pygame.draw.circle(screen, vcolor, [int(line_x), int(line_y)], 2)
	pygame.draw.circle(screen, black, (int(circle3_x), int(circle_y)), int(circle_rad), 5)
        for step in xrange(0,110,10):
                angle3 = (angle - ((step / .022) / 1000))
                line_x = (circle_rad - 8) * math.sin(angle3) + circle3_x
                line_y = (circle_rad - 8) * math.cos(angle3) + circle_y
                number_text = numberFont.render(str(step), True, white)
                number_text_loc = number_text.get_rect(center=(line_x, line_y+8))
                screen.blit(number_text, number_text_loc)
                pygame.draw.circle(screen, white, [int(line_x), int(line_y)], 2)
	speed_text = headerFont.render("SPEED", True, black)
	rpm_text = headerFont.render("RPM", True, black)
	load_text = headerFont.render("LOAD", True, black)
	speed_text_loc = speed_text.get_rect(center=(speed_text_x, speed_text_y))
	rpm_text_loc = rpm_text.get_rect(center=(rpm_text_x, rpm_text_y))
	load_text_loc = load_text.get_rect(center=(load_text_x, load_text_y))
	screen.blit(speed_text, speed_text_loc)
	screen.blit(rpm_text, rpm_text_loc)
	screen.blit(load_text, load_text_loc)
def get_speed(s):
	global speed
	if not s.is_null():
		#speed = int(s.value.magnitude) #for kph
		speed = int(s.value.magnitude * .060934) #for mph
def get_rpm(r):
	global rpm
	if not r.is_null():
		rpm = int(r.value.mangitude)
def get_load(l):
	global load
	if not l.is_null():
		load = int(l.value.mangitude)
#connection.watch(obd.commands.SPEED, callback=get_speed)
#connection.watch(obd.commands.RPM, callback=get_rpm)
#connection.watch(obd.commands.ENGINE_LOAD, callback=get_load)
#connection.start()
		
running = True
while running:
	for event in pygame.event.get():
		if event.type == KEYDOWN:
			if event.key == K_ESCAPE:
				#connection.stop()
				#connection.close()
				running = False
			elif event.type == QUIT:
				#connection.stop()
				#connection.close()
				running = False
	draw_hud()
	speedDisplay = digitFont.render(str(speed), 3, white)
	angle1 = (angle - ((speed / .031) / 1000))
        line_x = (circle_rad - 10) * math.sin(angle1) + circle1_x
	line_y = (circle_rad - 10) * math.cos(angle1) + circle_y
	pygame.draw.line(screen, blue, [circle1_x, circle_y], [line_x, line_y], 4)
	
	rpmDisplay = digitFont.render(str(rpm), 3, white)
	if rpm >= 4500:
                vcolor = yellow
        if rpm >= 6000:
                vcolor = red
	angle2 = (angle - ((rpm / 1.9) / 1000))
	line_x = (circle_rad - 10) * math.sin(angle2) + circle2_x
	line_y = (circle_rad - 10) * math.cos(angle2) + circle_y
	pygame.draw.line(screen, vcolor, [circle2_x, circle_y], [line_x, line_y], 2)
	
	loadDisplay = digitFont.render(" " + str(int(load)) + '%', 3, white)
        angle3 = (angle - ((load / .022) / 1000))
        line_x = (circle_rad - 10) * math.sin(angle3) + circle3_x
	line_y = (circle_rad - 10) * math.cos(angle3) + circle_y
	pygame.draw.line(screen, red, [circle3_x, circle_y], [line_x, line_y], 6)
	
	screen.blit(loadDisplay, (circle3_x -((circle3_x / 8) - 40), circle_y + 60))
	screen.blit(rpmDisplay, (circle2_x - (circle2_x / 8) + 10, circle_y + 60))
	screen.blit(speedDisplay,(circle1_x -(circle1_x / 8) + 10, circle_y + 60))
	pygame.display.update()
	pygame.display.flip()
	#rpm += 5
	#speed += .05
	#load += .05
pygame.quit()
