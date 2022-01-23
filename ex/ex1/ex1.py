#DateTimeで日付を取得
import datetime

#dateTimeに日付と時刻を代入
dateTime = datetime.datetime.today();
#dateに日付のみを代入
date = dateTime.date();

#日付の表示
print("今日の日付: %s" % (date));
#print("今日の日付：" + str(date));
