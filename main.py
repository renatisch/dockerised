import datetime, time, schedule, os, dotenv
import requests

dotenv.load_dotenv()


def export_data():
    print("running")
    host = os.environ.get("commas_api_key")
    print(host)
    response = requests.get("https://www.idnes.cz/")
    print(response.status_code)


while True:
    schedule.every(5).seconds.do(export_data)
    schedule.run_pending()
    time.sleep(1)
