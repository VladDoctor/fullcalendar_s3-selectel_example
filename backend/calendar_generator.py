# импорт boto3
import boto3

# ключи генерируем в разделе сервисных пользователей
access_key = "914866b003e94c569f7b5beb19cb0adf"
secret_key = "70232d4de75c4877916d0998db78dbd0"

# указываем типовой ендпоинт, название региона, access_key и aws_secret_access_key
s3 = boto3.client("s3", endpoint_url="https://s3.ru-1.storage.selcloud.ru",
                  region_name="ru-1", aws_access_key_id=access_key, aws_secret_access_key=secret_key,
                  verify=False)

# пользовательские данные (для примера)
users_calendars = {
    'user_1': {
        '09.12.24-13.12.24' : '[{"title":"Lunch","start":"2024-12-09T12:00:00+00:00"}]'
    }
}

# название контейнера
bucket_name = 'fullcalendar3'

# список пользователей и дат
users_list = list(users_calendars.keys())
dates_list = list(users_calendars["user_1"].keys())

# название объекта, в который мы запишем данные (наш json-файл)
key = f'{users_list[0]}/{dates_list[0]}.json'

#  данные, которые запишем внутрь объекта (тело объекта)
body = users_calendars[users_list[0]][dates_list[0]]

# предварительное создание объекта
s3.generate_presigned_post(Bucket=bucket_name, Key=key, Fields={"Access-Control-Allow-Origin": "*"})
s3.put_object(Bucket=bucket_name, Key=key, Body=body)
# запись содержания body в объект