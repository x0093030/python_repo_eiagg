import os
from pytube import YouTube
import sys

CURRENT_DIR = os.getcwd()
DOWNLOAD_FOLDER = CURRENT_DIR
#video_url = "https://www.youtube.com/watch?v=sPNI8fpWklg"
#video_url = "https://www.youtube.com/watch?v=GUf81ofAZV0"
#video_url =  "https://www.youtube.com/watch?v=3ZQ4p3Xgilo"
#video_url =  "https://www.youtube.com/watch?v=YKAfKprBXQc"
#video_url =  "https://www.youtube.com/watch?v=2Y6Nne8RvaA&list=PLF76WIcTxWvvROCGIxxeKZDF32srWm6mt&index=6"
#video_url =  "https://www.youtube.com/watch?v=WcIcVapfqXw&list=PLF76WIcTxWvvROCGIxxeKZDF32srWm6mt&index=8"
#video_url =  "https://www.youtube.com/watch?v=2Y6Nne8RvaA&list=PLF76WIcTxWvvROCGIxxeKZDF32srWm6mt&index=7"
#video_url = "https://www.youtube.com/watch?v=HCq1OcAEAm0&list=PLF76WIcTxWvvROCGIxxeKZDF32srWm6mt&index=2"
video_url = "https://www.youtube.com/watch?v=BuyFhOIA-bE&list=WL&index=1"

# Seminario Fenix
#video_url = "https://www.youtube.com/watch?v=62wDYoPC4Sg&list=PLVCAyfXUAsByGdNHLdAU9HuuAuTY9gspS"
#video_url = "https://www.youtube.com/watch?v=6uDZJ4gytno&list=PLVCAyfXUAsByGdNHLdAU9HuuAuTY9gspS&index=2"
#video_url = "https://www.youtube.com/watch?v=9Em-dDfkdHQ&list=PLVCAyfXUAsByGdNHLdAU9HuuAuTY9gspS&index=3"
#video_url = "https://www.youtube.com/watch?v=fAEJ5HC76f0&list=PLVCAyfXUAsByGdNHLdAU9HuuAuTY9gspS&index=4"
#video_url = "https://www.youtube.com/watch?v=NBDqBUU-uq4&list=PLVCAyfXUAsByGdNHLdAU9HuuAuTY9gspS&index=5"
#video_url = "https://www.youtube.com/watch?v=gr2YhEbzWmc&list=PLVCAyfXUAsByGdNHLdAU9HuuAuTY9gspS&index=6"
#video_url = "https://www.youtube.com/watch?v=pvyxJt0NopQ&list=PLVCAyfXUAsByGdNHLdAU9HuuAuTY9gspS&index=7"
#video_url = "https://www.youtube.com/watch?v=6fsDrjnsjI4&list=PLVCAyfXUAsByGdNHLdAU9HuuAuTY9gspS&index=8"
#video_url = "https://www.youtube.com/watch?v=xWxz1s6NpY8&list=PLVCAyfXUAsByGdNHLdAU9HuuAuTY9gspS&index=9"
#video_url = "https://www.youtube.com/watch?v=vJ8dwloUHcw&list=PLVCAyfXUAsByGdNHLdAU9HuuAuTY9gspS&index=10"
#video_url = "https://www.youtube.com/watch?v=WtZtFgC3uKc&list=PLVCAyfXUAsByGdNHLdAU9HuuAuTY9gspS&index=11"
#video_url = "https://www.youtube.com/watch?v=ZS4joTwoCqQ&list=PLVCAyfXUAsByGdNHLdAU9HuuAuTY9gspS&index=12"
#video_url = "https://www.youtube.com/watch?v=n3msCDD0fws&list=PLVCAyfXUAsByGdNHLdAU9HuuAuTY9gspS&index=13"
#video_url = "https://www.youtube.com/watch?v=WsBiieE1uuI&list=PLVCAyfXUAsByGdNHLdAU9HuuAuTY9gspS&index=14"
#video_url = "https://www.youtube.com/watch?v=Omc4uAglRpE&list=PLVCAyfXUAsByGdNHLdAU9HuuAuTY9gspS&index=15"
#video_url = "https://www.youtube.com/watch?v=8o3fiUHWlaI&list=PLVCAyfXUAsByGdNHLdAU9HuuAuTY9gspS&index=16"
#video_url = "https://www.youtube.com/watch?v=5vsSUG6Dq4g&list=PLVCAyfXUAsByGdNHLdAU9HuuAuTY9gspS&index=17"
#video_url = "https://www.youtube.com/watch?v=m5sJS2j6aRM&list=PLVCAyfXUAsByGdNHLdAU9HuuAuTY9gspS&index=18"
#video_url = "https://www.youtube.com/watch?v=P6gqEqaONYI&list=PLVCAyfXUAsByGdNHLdAU9HuuAuTY9gspS&index=19"
#video_url = "https://www.youtube.com/watch?v=9feWbvAl7xs&list=PLVCAyfXUAsByGdNHLdAU9HuuAuTY9gspS&index=20"
#video_url = "https://www.youtube.com/watch?v=SBgBvzZaujw&list=PLVCAyfXUAsByGdNHLdAU9HuuAuTY9gspS&index=21"
#video_url = "https://www.youtube.com/watch?v=tBXtLWJ8Ckc&list=PLVCAyfXUAsByGdNHLdAU9HuuAuTY9gspS&index=22"
#video_url = "https://www.youtube.com/watch?v=FIleBBS124Y&list=PLVCAyfXUAsByGdNHLdAU9HuuAuTY9gspS&index=23"
#video_url = "https://www.youtube.com/watch?v=PbwxgBW14LU&list=PLVCAyfXUAsByGdNHLdAU9HuuAuTY9gspS&index=24"
#video_url = "https://www.youtube.com/watch?v=23x5ZfrV7CI&list=PLVCAyfXUAsByGdNHLdAU9HuuAuTY9gspS&index=25"
#video_url = "https://www.youtube.com/watch?v=Hx93Y63TSJQ&list=PLVCAyfXUAsByGdNHLdAU9HuuAuTY9gspS&index=26"
#video_url = "https://www.youtube.com/watch?v=JXtVZF7T32I&list=PLVCAyfXUAsByGdNHLdAU9HuuAuTY9gspS&index=27"

def single_video():
    video_obj = YouTube(video_url)
    #stream = video_obj.streams.get_audio_only()
    stream = video_obj.streams.get_audio_only('mp4')
    #stream = video_obj.streams.get_highest_resolution()
    #stream = video_obj.streams.get_lowest_resolution()
    stream.download(DOWNLOAD_FOLDER)
    print('='*77)
    print (DOWNLOAD_FOLDER)
    
def multiple_video():
# Seminario Fenix
    list = ["https://www.youtube.com/watch?v=62wDYoPC4Sg&list=PLVCAyfXUAsByGdNHLdAU9HuuAuTY9gspS",
        "https://www.youtube.com/watch?v=6uDZJ4gytno&list=PLVCAyfXUAsByGdNHLdAU9HuuAuTY9gspS&index=2",
        "https://www.youtube.com/watch?v=9Em-dDfkdHQ&list=PLVCAyfXUAsByGdNHLdAU9HuuAuTY9gspS&index=3",
        "https://www.youtube.com/watch?v=fAEJ5HC76f0&list=PLVCAyfXUAsByGdNHLdAU9HuuAuTY9gspS&index=4",
        "https://www.youtube.com/watch?v=NBDqBUU-uq4&list=PLVCAyfXUAsByGdNHLdAU9HuuAuTY9gspS&index=5",
        "https://www.youtube.com/watch?v=gr2YhEbzWmc&list=PLVCAyfXUAsByGdNHLdAU9HuuAuTY9gspS&index=6",
        "https://www.youtube.com/watch?v=pvyxJt0NopQ&list=PLVCAyfXUAsByGdNHLdAU9HuuAuTY9gspS&index=7",
        "https://www.youtube.com/watch?v=6fsDrjnsjI4&list=PLVCAyfXUAsByGdNHLdAU9HuuAuTY9gspS&index=8",
        "https://www.youtube.com/watch?v=xWxz1s6NpY8&list=PLVCAyfXUAsByGdNHLdAU9HuuAuTY9gspS&index=9",
        "https://www.youtube.com/watch?v=vJ8dwloUHcw&list=PLVCAyfXUAsByGdNHLdAU9HuuAuTY9gspS&index=10",
        "https://www.youtube.com/watch?v=WtZtFgC3uKc&list=PLVCAyfXUAsByGdNHLdAU9HuuAuTY9gspS&index=11",
        "https://www.youtube.com/watch?v=ZS4joTwoCqQ&list=PLVCAyfXUAsByGdNHLdAU9HuuAuTY9gspS&index=12",
        "https://www.youtube.com/watch?v=n3msCDD0fws&list=PLVCAyfXUAsByGdNHLdAU9HuuAuTY9gspS&index=13",
        "https://www.youtube.com/watch?v=WsBiieE1uuI&list=PLVCAyfXUAsByGdNHLdAU9HuuAuTY9gspS&index=14",
        "https://www.youtube.com/watch?v=Omc4uAglRpE&list=PLVCAyfXUAsByGdNHLdAU9HuuAuTY9gspS&index=15",
        "https://www.youtube.com/watch?v=8o3fiUHWlaI&list=PLVCAyfXUAsByGdNHLdAU9HuuAuTY9gspS&index=16",
        "https://www.youtube.com/watch?v=5vsSUG6Dq4g&list=PLVCAyfXUAsByGdNHLdAU9HuuAuTY9gspS&index=17",
        "https://www.youtube.com/watch?v=m5sJS2j6aRM&list=PLVCAyfXUAsByGdNHLdAU9HuuAuTY9gspS&index=18",
        "https://www.youtube.com/watch?v=P6gqEqaONYI&list=PLVCAyfXUAsByGdNHLdAU9HuuAuTY9gspS&index=19",
        "https://www.youtube.com/watch?v=9feWbvAl7xs&list=PLVCAyfXUAsByGdNHLdAU9HuuAuTY9gspS&index=20",
        "https://www.youtube.com/watch?v=SBgBvzZaujw&list=PLVCAyfXUAsByGdNHLdAU9HuuAuTY9gspS&index=21",
        "https://www.youtube.com/watch?v=tBXtLWJ8Ckc&list=PLVCAyfXUAsByGdNHLdAU9HuuAuTY9gspS&index=22",
        "https://www.youtube.com/watch?v=FIleBBS124Y&list=PLVCAyfXUAsByGdNHLdAU9HuuAuTY9gspS&index=23",
        "https://www.youtube.com/watch?v=PbwxgBW14LU&list=PLVCAyfXUAsByGdNHLdAU9HuuAuTY9gspS&index=24",
        "https://www.youtube.com/watch?v=23x5ZfrV7CI&list=PLVCAyfXUAsByGdNHLdAU9HuuAuTY9gspS&index=25",
        "https://www.youtube.com/watch?v=Hx93Y63TSJQ&list=PLVCAyfXUAsByGdNHLdAU9HuuAuTY9gspS&index=26",
        "https://www.youtube.com/watch?v=JXtVZF7T32I&list=PLVCAyfXUAsByGdNHLdAU9HuuAuTY9gspS&index=27"]

    for video in list:
        video_obj = YouTube(video)
        stream = video_obj.streams.get_audio_only('mp4')
        stream.download(DOWNLOAD_FOLDER)
        #print(video)
        print('#'*77)
        print (DOWNLOAD_FOLDER)

def main():
    single_video()
	#multiple_video()
    #C:\Users\admin\ffmpeg\bin\ffmpeg.exe -i "file.mp4" "file.mp3"

if __name__=="__main__":
    sys.exit( main() )