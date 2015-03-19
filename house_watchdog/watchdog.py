# TODO Use proper logger

import time
import paho.mqtt.client as paho
import paramiko
from paramiko import (AuthenticationException, BadHostKeyException,
                      SSHException)
import socket


KEEPALIVE = 20
QOS = 1
RETAIN = False

MQTT_USER = 'watchdog'
MQTT_PASSWORD = 'watchdog'
MQTT_SERVER = 'normandie.ubismart.org'
MQTT_PORT = 1883

SSH_USERNAME = 'pi'
SSH_PASSWORD = 'raspberry'
SSH_SERVER = 'normandie.ubismart.org'

RETRIES = 1
SSH_TIMEOUT = 10


def init_mqtt():
    client = paho.Client('house_watchdog')
    client.username_pw_set(MQTT_USER, MQTT_PASSWORD)
    client.connect_async(MQTT_SERVER,
                         MQTT_PORT, KEEPALIVE)
    client.loop_start()
    return client


def send_mqtt_message(client, house, status):
    topic = "watchdog/%s" % (house)
    client.publish(topic, ('on' if status else 'off'), QOS, retain=RETAIN)


def check_online(house_port):
    ssh = paramiko.SSHClient()
    ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())

    for x in range(RETRIES):
        try:
            ssh.connect(SSH_SERVER, port=house_port, username=SSH_USERNAME,
                        password=SSH_PASSWORD, timeout=SSH_TIMEOUT)
            print('SSH proxy at %d is online' % house_port)
            return True
        except (BadHostKeyException, AuthenticationException,
                SSHException, socket.error):
            print('SSH proxy at %d is offline' % house_port)
    return False


def run(houses, every_min=10):
    client = init_mqtt()
    while True:
        for house, port in houses.items():
            print("Testing whether house %d is up or down (port: %d)" %
                  (house, port))
            is_online = check_online(port)
            send_mqtt_message(client, house, is_online)
        time.sleep(every_min * 60)


def main():
    houses = {
        3: 5900,
        4: 5900,
        5: 5900,
        6: 5900,
        7: 5900,
        8: 5808,
        9: 5909,
        10: 5910
    }
    run(houses)


if __name__ == '__main__':
    main()
