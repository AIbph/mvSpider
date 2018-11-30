import requests
from multiprocessing import Pool


def main(i):
    if i <= 999:
        url = "https://tudou.com-l-tudou.com/20181115/14290_e27463ca/1000k/hls/f93e716d438%03d.ts"%i
    else:
        url = "https://tudou.com-l-tudou.com/20181115/14290_e27463ca/1000k/hls/f93e716d438%d.ts" % i
    header = {"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/68.0.3440.106 Safari/537.36"}
    response = requests.get(url, headers=header)
    if i <= 999:
        fp = open("./mp4/{}".format(url[-9:]), "ab")
    else:
        name = 438000 + i
        fp = open("./mp4/{}".format(str(name) + ".ts"), "ab")
    fp.write(response.content)
    print("开始保存第：%d个视频"%i)
    fp.close()
    print("保存第：%d个视频成功！" % i)


if __name__ == '__main__':
    pool = Pool(20)
    for i in range(1199):
        pool.apply_async(main, (i,))
    print("Down")
    pool.close()
    pool.join()