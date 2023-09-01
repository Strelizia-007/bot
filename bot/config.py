#    Copyright (c) 2021 Danish_00
#    Improved By @Zylern

from decouple import config

try:
    APP_ID = 6620972
    DEV = 1664850827
    OWNER = "1745047302"
    API_HASH = "3f6835286b03e000ab6d71b37cc35b92"
    BOT_TOKEN = config("BOT_TOKEN") 
    ffmpegcode = ["-hide_banner -preset veryfast -c:v libx265 -hide_banner -vf scale=1280:-2 -x265-params no-info=1:loglevel=2:bframes=10:range=limited:aq-mode=3:psy-rd=2 -pix_fmt yuv420p10le  -dst_range 1 -colorspace:v bt709 -color_primaries:v bt709 -color_trc:v bt709 -b:v 850k -maxrate 1900k -bufsize 19000k  -r 23.976 -map 0:v -c:a libopus -b:a 64k -ac 2 -vbr on -map 0:a -c:s copy  -map 0:s? -metadata "title=STARLEY RIPS" -metadata:s:a:0 "title=@LioNriPs - STARLEY" -metadata:s:a:1 "title=@LioNriPs - STARLEY" -metadata:s:a:2 "title=@LioNriPs - STARLEY" -metadata:s:t:0 "title=@LioNriPs - STARLEY" -metadata:s:s:0 title="@LioNriPs - STARLEY" -metadata:s:s:1 title="@LioNriPs - STARLEY" -metadata:s:s:2 title="@LioNriPs - STARLEY" -metadata:s:s:3 title="STRELIZIA - @LioNriPs" -metadata:s:s:4 title="STRELIZIA - @LioNriPs" -metadata:s:s:5 title="STRELIZIA - @LioNriPs" -metadata:s:s:6 title="STRELIZIA - @LioNriPs" -metadata:s:a:3 title="STRELIZIA - @LioNriPs" -metadata:s:a:4 title="STRELIZIA - @LioNriPs" -metadata:s:a:5 title="STRELIZIA - @LioNriPs" -metadata:s:v:0 "title=STARLEY x STRELIZIA""]
    THUMBNAIL = "https://telegra.ph/file/711777fbb7317a73c211a.jpg"
except Exception as e:
    print("Environment vars Missing! Exiting App.")
    print(str(e))
    exit(1)
