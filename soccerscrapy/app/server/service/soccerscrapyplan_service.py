from apscheduler.events import EVENT_JOB_EXECUTED, EVENT_JOB_ERROR, EVENT_JOB_REMOVED, EVENT_SCHEDULER_SHUTDOWN
from apscheduler.schedulers.background import BackgroundScheduler
from _datetime import datetime

from common.match_constants import MatchConstants
from common.timezone_util import TimezoneUtil
from soccerscrapy.app.server.dao.operationimpl_dao import OperationImplDAO
from soccerscrapy.app.server.model.scrapyplan_model import ScrapyplanModel
import os


class SoccerScrapyPlanService:
    scheduler = BackgroundScheduler()
    data = None
    dateTimeSchedule = None

    def __init__(self, data_model: ScrapyplanModel):
        self.collection = OperationImplDAO("current_match")
        os.environ['COLLECTION_NAME'] = data_model.collection
        self.data = data_model
        self.dateTimeSchedule = TimezoneUtil.convertTimezoneToLocalDateTime(data_model.datetime_start,
                                                                            data_model.datetime_end,
                                                                            data_model.timezones)

    def scrapyPlanFacade(self):
        try:
            # (1) Search schedule in execution/schedule

            # (2) Plan Schedule
            self.scheduler.add_listener(self.listener_job, EVENT_SCHEDULER_SHUTDOWN)
            self.scheduler.add_job(self.scrapy_running, 'interval', seconds=10,
                                   start_date=self.dateTimeSchedule['datetimeStart'],
                                   end_date=self.dateTimeSchedule['datetimeEnd'], id=self.data.scrapy)
            try:
                self.scheduler.start()
            finally:
                print(" - scheduler SCRAPY - ! ")
                # self.scheduler.shutdown(wait=False)
        except Exception as e:
            print("Error 1 ", e)

    def scrapy_running(self):
        try:
            print(" - START SCRAPY - ! ")
            os.system("scrapy crawl placardefutebol")
            self.check_schedule()
        except Exception as e:
            print("[Service-Error] - START SCRAPY :: ", e)

    def check_schedule(self):
        print("Check_schedule")
        dateNow = TimezoneUtil.dateNowUTC()
        dateEnd = self.dateTimeSchedule['datetimeEnd']

        print("DATETIME_NOW", dateNow)
        print("DATETIME_END", dateEnd)
        if dateNow > dateEnd:
            print("Schedule Shutdown ", dateEnd)
            self.scheduler.shutdown(wait=False)

    def listener_job(self, event):
        print('The job worked :)')
