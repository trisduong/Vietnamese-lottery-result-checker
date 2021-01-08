def get_prize():
    result = {}
    url = "http://ketqua.net"
    import requests
    from bs4 import BeautifulSoup

    ses = requests.Session()
    resp = ses.get(url, timeout=5)
    tree = BeautifulSoup(resp.text, "html.parser")
    node = tree.find(name="div", attrs={"id": "rs_0_0"})
    result["Special Prize"] = [node.text]
    node = tree.find(name="div", attrs={"id": "rs_1_0"})
    result["First Prize"] = [node.text]
    node = tree.find_all(
        name="div",
        attrs={"style": "width:50%; position: relative; float: left;"},
    )
    result["Second Prize"] = [num.text for num in node]
    node = tree.find_all(
        name="div",
        attrs={
            "style": "width:33.333333333333%;position: relative; float: left;",
            "data-pattern": "[0-9]{5}",
        },
    )
    result["Third Prize"] = [num.text for num in node]
    node = tree.find_all(
        name="div",
        attrs={
            "style": "width:25%; position: relative; float: left;",
            "data-pattern": "[0-9]{4}",
        },
    )
    result["Four Prize"] = [num.text for num in node]
    node = tree.find_all(
        name="div",
        attrs={
            "style": "width:33.333333333333%;position: relative; float: left;",
            "data-pattern": "[0-9]{4}",
        },
    )
    result["Five Prize"] = [num.text for num in node]
    node = tree.find_all(
        name="div",
        attrs={
            "style": "width:33.333333333333%;position: relative; float: left;",
            "data-pattern": "[0-9]{3}",
        },
    )
    result["Six Prize"] = [num.text for num in node]
    node = tree.find_all(
        name="div",
        attrs={
            "style": "width:25%; position: relative; float: left;",
            "data-pattern": "[0-9]{2}",
        },
    )
    result["Seven Prize"] = [num.text for num in node]
    return result


def solve(input_data):
    result = get_prize()
    for prize, win_numbers in result.items():
        for win_number in win_numbers:
            for test_number in input_data:
                if test_number[-2:] == win_number[-2:]:
                    print("You win", prize, "with number", test_number)


def main():
    import sys
    num_list = sys.argv[1:]
    if num_list == []:
        prize_list = get_prize()
        for prize, win_numbers in prize_list.items():
            print(prize, *win_numbers)
    else:
        solve(num_list)


if __name__ == "__main__":
    main()
