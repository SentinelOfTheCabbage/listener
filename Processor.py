class Processor:
    def __init__(self,hz_scale):
        self.curr_notes = []
        self.risk_notes = []
        self.hz_scale = hz_scale

    def calculate_data(self,sample):
        max_values, max_indexes = sample.get_groups_max_values()
        risk_br = sample.get_risk_db_val()
        hard_br = sample.get_hard_db_val()

        for elem in curr_notes:
            group_num = curr_group(elem.hz_history[-1])
            elem.append_story(values[group_num], group_num)
            

class Note:
    def __init__(self, new_db, new_hz, start_sample):
        self.hz_history = []
        self.db_history = []
        self.append_story(new_db,new_hz)
        self.start_sample = start_sample

    def append_story(self, new_db, new_hz_ind):
        self.hz_ind_history.append(new_hz_ind)
        self.db_history.append(new_db)