class day_8:
    def __init__(self, file_name):
        self.input_signals, self.output_signals = self.getInput(file_name)
        print(self.input_signals[0])
        print(self.output_signals[0])

    def getInput(self, file_name):
        with open(file_name) as f:
            inputs = list(map(lambda x: x.split(' | '), f.readlines()))
            input_sigs, output_sigs = list(map(lambda x: x[0], inputs)), list(map(lambda x: x[1], inputs))
            input_sigs = list(map(lambda x: x.strip().split(' '), input_sigs))
            output_sigs = list(map(lambda x: x.strip().split(' '), output_sigs))
            return input_sigs, output_sigs

    def check_len(self, signal):
        return (2 <= len(signal) <= 4) or (len(signal) == 7)

    def part_1(self):
        s = 0
        for output_sig in self.output_signals:
            s += sum(map(self.check_len, output_sig))
        return s

    def part_2(self):
        result = 0
        for signal, output in zip(self.input_signals, self.output_signals):
            signal_map = ['' for _ in range(10)]
            signal = sorted(signal, key=len)
            for sig in signal:
                if len(sig) == 2:
                    signal_map[1] = sig
                elif len(sig) == 3:
                    signal_map[7] = sig
                elif len(sig) == 4:
                    signal_map[4] = sig
                elif len(sig) == 7:
                    signal_map[8] = sig
                elif len(sig) == 5:
                    if all([c in sig for c in signal_map[1]]):
                        signal_map[3] = sig
                    elif sum([c in sig for c in signal_map[4]]) == 3:
                        signal_map[5] = sig
                    else:
                        signal_map[2] = sig
                elif len(sig) == 6:
                    if all([c in sig for c in signal_map[4]]):
                        signal_map[9] = sig
                    elif all([c in sig for c in signal_map[7]]):
                        signal_map[0] = sig
                    else:
                        signal_map[6] = sig
                else:
                    signal_map[8] = sig
            print(signal_map)
            out_num = ""
            for output_num in output:
                #print(output_num)
                for i in range(10):
                    if (len(signal_map[i]) == len(output_num)) and all([c in output_num for c in signal_map[i]]):
                        #print(i)
                        out_num += str(i)
                        break
            result+=int(out_num)
        return result


if __name__ == '__main__':
    day_8 = day_8('input.txt')
    print(day_8.part_1())
    print(day_8.part_2())
