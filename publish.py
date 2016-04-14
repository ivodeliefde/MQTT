import paho.mqtt.client as mqtt

#---------------------------------------------------------------------------------------------------#
#--------------------------Code below is based on the Paho documentation----------------------------#
#---------------------------http://www.eclipse.org/paho/clients/python/-----------------------------#
#---------------------------------------------------------------------------------------------------#

def publish(client):
	for i in range(10):
		client.publish("paho/test/hello", "Hello world! {0}".format(i))
	# multiple(msgs, hostname="localhost", port=1883, client_id="", keepalive=60, will=None, auth=None, tls=None, protocol=mqtt.MQTTv311)

# The callback for when the client receives a CONNACK response from the server.
def on_connect(client, userdata, flags, rc):
    print("Connected with result code "+str(rc))

    # publish data
    publish(client)
    

# The callback for when a PUBLISH message is received from the server.
def on_message(client, userdata, msg):
    print(msg.topic+" : "+str(msg.payload))


client = mqtt.Client()
client.on_connect = on_connect
client.on_message = on_message


client.connect("iot.eclipse.org", 1883, 60)
# for use with a private MQTT broker:
# client.username_pw_set(username, password)
# client.connect(host, port, 60)


# Blocking call that processes network traffic, dispatches callbacks and
# handles reconnecting.
# Other loop*() functions are available that give a threaded interface and a
# manual interface.
client.loop_forever()

