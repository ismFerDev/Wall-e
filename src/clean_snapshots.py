import logging
from datetime import datetime
from datetime import timedelta

logger = logging.getLogger('Wall-e')


class CleanerSnapshots(object):

    def __init__(self, connection_snapshots):
        self.connection_snapshots = connection_snapshots

    def get_all_snapshots(self):
        print("lol")
        return self.connection_snapshots.describe_snapshots()

    def delete_snapshot(self, snapshotId):
        try:
            print("deleting snapshot "+snapshotId)
            '''
            #result = self.connection_snapshots.delete_snapshot(SnapshotId = snapshotId)
            '''
        except:
            '''
            check if we have to retry due to AWS throttling, fail otherwise
            '''
            print("muerte")
        else:
            return result

    def cleaner_snapshots_older_than(self, days):
        snapshots = self.get_all_snapshots()['Snapshots']
        print("days:" + str(days))
        for snapshot in snapshots:
            snapshot_date = snapshot['StartTime']
            tz_info = snapshot_date.tzinfo
            if (datetime.now(tz_info)) > (snapshot_date + timedelta(days=int(days[0]))):
                print("delete! - " + snapshot['SnapshotId'] + " - " + str(snapshot_date))
                '''
                If the snapshot date is greater than the number of days specified, delete it
                # delete_snapshot(snapshot['SnapshotId']
                '''