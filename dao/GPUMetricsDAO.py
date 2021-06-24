from datetime import time

from models.GPU import GPUModel

SQL_INSERT_METRIC = 'INSERT INTO ' \
                    'gpu_metrics ' \
                    '(gpu_core, gpu_memory, gpu_vrm_core, ' \
                    'gpu_hot_spot, pc_id, created_at, updated_at) ' \
                    'VALUES (%s, %s, %s, %s, %s, now(), now())'


class GPUMetricsDAO:
    def __init__(self, db):
        self.db = db

    def insert_gpu_metric(self, obj):
        if isinstance(obj, GPUModel):
            cursor = self.db.cursor()
            cursor.execute(SQL_INSERT_METRIC, (obj.gpu_core, obj.gpu_memory,
                                               obj.gpu_vrm_core, obj.gpu_hot_spot,
                                               obj.pc_id))
            cursor.close()
        else:
            print('Não é instancia')

