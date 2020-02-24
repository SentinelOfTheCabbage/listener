import Sample

class Processor:
    def __init__(self,hz_scale):
        self.curr_notes = []
        self.risk_notes = []
        self.hz_scale = hz_scale

    def calculate_data(self,sample):
        max_ind, max_val = sample.max_ind, sample.max_val
        risk_br = sample.get_risk_db_val()
        hard_br = sample.get_hard_db_val()

        for elem in curr_notes:
            group_ind = curr_group(elem.hz_history[-1])
            cur_ind   = sample.max_ind[group_ind]
            cur_val   = sample.max_val[group_ind]
            elem.append_story(cur_val, cur_ind)
        
        # Добавить список, хранящий индексы тех групп, которые ещё не 
        # подверглись обходу процессора 


class Note:
    def __init__(self, new_db, new_hz, start_sample):
        self.hz_history = []
        self.db_history = []
        self.start_sample = start_sample
        self.append_story(new_db,new_hz)

    def append_story(self, new_db, new_hz_ind):
        self.hz_ind_history.append(new_hz_ind)
        self.db_history.append(new_db)
