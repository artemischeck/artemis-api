from celery import task
import logging


@task
def send_notification(payload):
    try:
        channel = payload.get("channel")
        message = payload.get("message")
        token = payload.get("token")
        account_id = payload.get("account_id")
        webhook_url = payload.get("webhook_url")
        email = payload.get("email")
        phone_number = payload.get("phone_number")

        if channel == "pushover":
            p = get_notifier('pushover')
            p.notify(user=account_id, token=token, message=message)
        if channel == "slack":
            slack = get_notifier('slack')
            slack.notify(message=message, webhook_url=webhook_url)
        if channel == "email":
            email = get_notifier('email')
            email.notify(to=email, message=message)
        if channel == "telegram":
            telegram = get_notifier('telegram')
            telegram.notify(message=message, token=token, chat_id=account_id)
        if channel == "statuspage":
            statuspage = get_notifier('statuspage')
            statuspage.notify(message=message, api_key=token, page_id=chat_id)
        if channel == "twilio":
            twilio = get_notifier('twilio')
            twilio.notify(message=message, to=phone_number,
                          account_sid=account_id, auth_token=token)
    except Exception as ex:
        logging.error(ex, exc_info=True)
