# Send to single device.
from pyfcm import FCMNotification

FCM_API_KEY = "YOUR_KEY"
push_service = FCMNotification(api_key=FCM_API_KEY)

message = "Hellow all devices on neews"

result = push_service.notify_topic_subscribers(topic_name="news", message_body=message)


print result