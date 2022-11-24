import json

INPUT_FILE = "input.csv"


def csv_to_list_dict(filename) -> list[dict]:
    with open(filename, 'r') as f:
        results = []
        for line in f:
            a = [x.split('\n')[0] for x in line.split(',')]
            results.append(a)
        a = len(results)
        ans = []
        for x in range(1, a):
            a = {}
            for i in range(len(results[0])):
                a[results[0][i]] = results[x][i]
            ans.append(a)
        return ans


print(json.dumps(csv_to_list_dict(INPUT_FILE), indent=4))
