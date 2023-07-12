from apscheduler.schedulers.background import BackgroundScheduler
from .assync_tasks import verify_if_user_can_loan


def start():
    scheduler = BackgroundScheduler()
    scheduler.add_job(verify_if_user_can_loan, "interval", hours=24)
    scheduler.start()
