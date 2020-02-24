class Sample:
    def __init__(self, data):
        self.data = data
        self.sample_glacer()
        self.separate_to_groups()
        self.risk_db = self.data.mean()*3*0.8
        self.hard_db = self.data.mean()*3

    def __glancing__(self, count, delta):
        data = self.data
        if count > 0:
            for pos,elem in enumerate(data):
                for i in range(1,delta+1):
                    if ((pos > i) and (len(data) - pos > i) and elem < 
                                    data[pos - i] and elem < data[pos + i]):
                        data[pos] = (data[pos - i] + data[pos + i])/2
            temp_db = glancing(data, count - 1, delta)
        return data

    def sample_glacer(self):
        self.data = self.__glancing__(5, 3)
        self.data = self.__glancing__(5, 2)
        self.data = self.__glancing__(5, 1)

    def separate__to_groups(self, hz_scale):
        self.sep_indexes = [0]
        for pos,elem in enumerate(self.data):
            if (pos>0 and pos < len(data)-1) and 
                                    (data[pos - 1] >= elem <= data[pos + 1]):
                if self.sep_indexes [-1] == pos - 1:
                    self.sep_indexes [-1] = pos
                else:
                    self.sep_indexes.append(pos)
        self.__get_groups_max_values__()
        return self.sep_indexes

    def __get_groups_max_values__(self):
        self.max_ind = []
        self.max_val = []

        for pos, bound in enumerate(self.sep_indexes):
            cur_slice = self.data[bound: sep_indexes[pos + 1]]
            if  pos < len(self.sep_indexes) - 1:
                self.values.append(max(cur_slice))
                self.indexes.append(bound + np.where(cur_slice == (value[-1])
                                                        )[0][0])

        return self.max_val, self.max_ind

    def get_risk_db_val(self):
        return self.risk_db

    def get_hard_db_val(self):
        return self.hard_db

    def curr_group(self, index):
        for pos, i in enumerate(self.max_ind):
            if index < i:
                return pos