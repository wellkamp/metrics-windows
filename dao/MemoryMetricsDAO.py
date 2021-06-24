from models.MemoryMetrics import MemoryMetrics

SQL_INSERT_METRIC = 'INSERT INTO ' \
                    'memory_metrics (used, available, ' \
                    'pc_id, created_at, updated_at) ' \
                    'VALUES (%s, %s, %s, now(), now())'


class MemoryMetricDAO:
    def __init__(self, db):
        self.db = db

    def insert_memory_metric(self, obj):
        if isinstance(obj, MemoryMetrics):
            cursor = self.db.cursor()
            cursor.execute(SQL_INSERT_METRIC, (obj.percent, obj.available,
                                               obj.pc_id))
            self.db.commit()
        else:
            print('Não é instancia')


