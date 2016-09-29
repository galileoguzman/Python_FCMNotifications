# Send to single device.
from pyfcm import FCMNotification


FCM_API_KEY = "YOUR_KEY"
FCM_DEVICE_ID = "YOUR_DEVICE_TOKEN"



push_service = FCMNotification(api_key=FCM_API_KEY)
registration_id = FCM_DEVICE_ID

message_title = "Python Test"
message_body = "Hellow Android, you are the best"
result = push_service.notify_single_device(registration_id=registration_id, message_title=message_title, message_body=message_body)


print result