from pasco.control_node_device import ControlNodeDevice
from pasco.pasco_ble_device import PASCOBLEDevice
import os
os.environ['PYGAME_HIDE_SUPPORT_PROMPT'] = "hide" #Esta cosa solo sirve para quitar el mensaje de saludo de pygame, si se pone delante del import entonces no sirve
import pygame
import time

pygame.init()
pygame.joystick.init()
joysticks = []

vel_a = 360
vel_b = 360
accel_a = 360
accel_b = 360
vel_a_rev = vel_a * -1
vel_b_rev = vel_b * -1
    
def main():

    print("Hello, this is just a test message!\n")
    controlNode = ControlNodeDevice()
    print("Type the device's ID to connect: ")
    ControlNodeId = input()
    controlNode.connect_by_id(ControlNodeId)

    while True:
        for event in pygame.event.get():
            if event.type == pygame.JOYDEVICEADDED:
                joy = pygame.joystick.Joystick(event.device_index)
                joysticks.append(joy)
                for joystick in joysticks:
                    print("Gamepad name: " + str(joystick.get_name()))

            #Se presiona un boton
            elif event.type == pygame.JOYBUTTONDOWN:
                if event.button == 0:  
                    controlNode.rotate_steppers_continuously(vel_a, accel_a, vel_b, accel_b)
                    print("PRESSED A")
                elif event.button == 1:
                    print("PRESSED B")
                elif event.button == 2:  
                    controlNode.rotate_steppers_continuously(vel_a_rev, accel_a, vel_b_rev, accel_b)
                    print("PRESSED X")
                elif event.button == 3:
                    print("PRESSED Y")

            #Se suelta un boton
            elif event.type == pygame.JOYBUTTONUP:
                if event.button == 0:
                    controlNode.stop_steppers(accel_a, accel_b)
                    print("RELEASED A")
                elif event.button == 1:
                        print("RELEASED B")
                elif event.button == 2:
                    controlNode.stop_steppers(accel_a, accel_b)
                    print("RELEASED X")
                elif event.button == 3:
                    print("RELEASED Y")

if __name__ == "__main__":
    main()