DEBUG = True


def debug_log(where,mess):
    if DEBUG:
        print(where)
        print(mess)
    return


class Spliter:
    def __init__(self):
        self.final_set_nums = []

    def keeper(self, part_of_list):
        if len(self.final_set_nums) > 0:
            if self.final_set_nums[len(self.final_set_nums)-1] != part_of_list:
                    self.final_set_nums.append(list(part_of_list))
        else:
            self.final_set_nums.append(list(part_of_list))
        return

    def spliter(self, number):
        assert isinstance(number, int), "%r is not a int" % number

        set_of_nums = [1] * number  # fill array init stats
        while len(set_of_nums) > 1:
            changed = True
            while changed:
                changed = False
                for i in reversed(range(0, len(set_of_nums))):
                    last = set_of_nums[len(set_of_nums)-1]
                    if last - set_of_nums[i] >= 2:
                        temp = set_of_nums[i]
                        for j in range(i, len(set_of_nums)-1):
                             set_of_nums[j] = temp+1
                        set_of_nums[len(set_of_nums)-1] = last + number - sum(set_of_nums)
                        debug_log('IN 1 for', set_of_nums)
                        self.keeper(set_of_nums)
                        changed = True
                        break
                    else:
                        continue
                self.keeper(set_of_nums)
                debug_log('after for', set_of_nums)

            set_of_nums.pop()
            loa = len(set_of_nums)-1
            set_of_nums = [1] * loa
            set_of_nums.append( number - loa)
            debug_log('after pop', set_of_nums)
            self.keeper(set_of_nums)

        debug_log('result of spliter',self.final_set_nums)
        return

    def optimizer(self,probabilities):
        qk = probabilities[0]
        pk = 1 - qk
        qo = probabilities[1]
        po = 1 - qo
        result = []
        fsn = self.final_set_nums
        for i in range(len(fsn)):
            csm = fsn[i]
            short_circuit = 1
            precipice = 1
            for k in range(len(csm)):
                short_circuit *= 1 - pow(qk, csm[k])
                precipice *= 1 - pow(1-qo, csm[k])
            result.append(short_circuit - precipice)
        return result.index(max(result))

    def show_best(self, index):
        print('Best distribution is:')
        print(self.final_set_nums[index])
        return


def main():
    number = 10
    probability = [0.1, 0.4]

    s = Spliter();
    s.spliter(number)
    s.show_best(s.optimizer(probability))

    return

if __name__ == "__main__":
    main()









# def task(test_number):
#
#     with open('input.txt') as src:
#         n = [int(x) for x in src.readline().split(' ')]
#         data = [int(x) for x in src.readline().split(' ')]
#
#     outputfile = open('output.txt', 'w')
#     for i in xrange(0, n[0]):
#         if i == n[0]-2:
#             outputfile.write(str(data.pop()))
#         else:
#             outputfile.write(str(data.pop())+' ')
#     return
#
# def tas():
#     n = int(input())
#     data = [int(x) for x in raw_input().split(' ')]
#     res = ""
#     for i in range(0, n):
#         res += str(data.pop())+' '
#     print (res[0:-1])