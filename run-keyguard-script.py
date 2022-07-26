import os
import sys
import subprocess

print('Hello! You are setting up keyguard!')

try:
    energy = 'systemctl unmask sleep' # 'systemctl mask sleep.target suspend.target hibernate.target hybrid-sleep.target
    energyrun = subprocess.call(energy, shell=True)

except:
    failed_command = subprocess.call(["false"])
    print("The exit code was: error")


try:
    ti = 'sudo timedatectl set-timezone Europe/Moscow'
    tirun = subprocess.call(ti, shell=True)
    tim = 'sudo timedatectl set-ntp true'
    timrun = subprocess.call(tim, shell=True)
    print('Success!')

except:
    failed_command = subprocess.call(["false"])
    print("The exit code was: error")
