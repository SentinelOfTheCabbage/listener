class Sample:
    def __init__(self, data):
        self.data = data
        sample_glacer()
        get_groups_sep()

    def __glancing__(self, count, delta):
        if count > 0:
            for pos,elem in enumerate(data):
                for i in range(1,delta+1):
                    if (pos > i) and (len(data) - pos > i) and elem < data[pos - i] and elem < data[pos + i]:
                        data[pos] = (data[pos - i] + data[pos + i])/2
            temp_db = glancing(data, count - 1, delta)
        return data

    def sample_glacer(self):
        self.data = self.__glancing__(5, 3)
        self.data = self.__glancing__(5, 2)
        self.data = self.__glancing__(5, 1)
        return self.data

    def get_groups_separators(self, hz_scale):
        self.sep_indexes = [0]
        for pos,elem in enumerate(self.data):
            if (pos>0 and pos < len(data)-1) and (data[pos - 1] >= elem <= data[pos + 1]):
                if self.sep_indexes [-1] == pos - 1:
                    self.sep_indexes [-1] = pos
                else:
                    self.sep_indexes.append(pos)
        return self.sep_indexes

    def get_groups_max_values(self, sep_group = self.sep_indexes):
        self.indexes = []
        self.values = []
        for pos, border in enumerate(sep_group):
            if pos < len(sep_group) - 1:
                self.values.append(max(data[border: sep_group[pos + 1]]))
                self.indexes.append(border + np.where(data[border: sep_group[pos + 1]] == (value[-1]))[0][0])
        return self.values, self.indexes

    def get_risk_db_val(self):
        return 3*self.data.mean()*0.8

    def get_hard_db_val(self):
        return 3*self.data.mean()

    def curr_group(self, index):
        for pos, i in enumerate(self.indexes):
            if index < i:
                return pos