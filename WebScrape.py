{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 35,
   "id": "2a4da6a1",
   "metadata": {},
   "outputs": [],
   "source": [
    "import numpy"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 36,
   "id": "fc78b5e7",
   "metadata": {},
   "outputs": [],
   "source": [
    "import matplotlib as mp\n",
    "from bs4 import BeautifulSoup\n",
    "import requests"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 68,
   "id": "4bf55f36",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "body{margin:0 auto;max-width:736px;padding:0 8px;}a{color:#1967D2;text-decoration:none;tap-highlight-color:rgba(0,0,0,.10)}a:visited{color:#4B11A8}a:hover{text-decoration:underline}img{border:0}html{font-family:Roboto,Helvetica Neue,Arial,sans-serif;font-size:14px;line-height:20px;text-size-adjust:100%;color:#3c4043;word-wrap:break-word;background-color:#fff}.bRsWnc{background-color:#fff;border-top:1px solid #dadce0;height:39px;overflow:hidden}.N6RWV{height:51px;overflow-scrolling:touch;overflow-x:auto;overflow-y:hidden}.Uv67qb{box-pack:justify;font-size:12px;line-height:37px;justify-content:space-between;justify-content:space-between}.Uv67qb a,.Uv67qb span{color:#70757a;display:block;flex:none;padding:0 16px;text-align:center;text-transform:uppercase;}span.OXXup{border-bottom:2px solid #4285f4;color:#4285f4;font-weight:bold}a.eZt8xd:visited{color:#70757a}.FElbsf{border-left:1px solid rgba(0,0,0,.12)}header article{overflow:visible}.Pg70bf{height:39px;display:box;display:flex;display:flex;width:100%}.H0PQec{position:relative;flex:1}.sbc{display:flex;width:100%}.Pg70bf input{margin:2px 4px 2px 8px;}.x{width:26px;color:#70757a;font:27px/38px arial, sans-serif;line-height:40px;}#qdClwb{flex:0 0 auto;width:39px;height:39px;border-bottom:0;padding:0;border-top-right-radius:8px;background-color:#1a73e8;border:1px solid #1558d6;background-image:url(data:image/gif;base64,R0lGODdhJAAjAPIHAODr/nCk+MPZ/FmV96zK+/7+/5K5+kqL9iwAAAAAJAAjAEADani63P4wykmbKcQRXDscQAEMXmmeaLQVLCukzyC09AjfeK7v/MAajACLhPMVAgwjsUcEiZa8xgAYrVqv2Kx2iwsIAAABknfBBAKrTE4IcMyot8ur8datqIbQfJdnAfo2WE6BV05wXIiJigkAOw==);}.sc{font-size:16px;position:absolute;top:39px;left:0;right:0;box-shadow:0px 2px 5px rgba(0,0,0,.2);z-index:2;background-color:#fff}.sc>div{padding:10px 10px;padding-left:16px;padding-left:14px;border-top:1px solid #dfe1e5}.scs{background-color:#f8f9fa;}.noHIxc{display:block;font-size:16px;padding:0 0 0 8px;flex:1;height:35px;outline:none;border:none;width:100%;-webkit-tap-highlight-color:rgba(0,0,0,.00);overflow:hidden;}.sbc input[type=text]{background:none}.sml .cOl4Id{display:none}.l{display:none}.sml header{background:none}.sml .l{display:block;padding:0 8px}.sml .l{letter-spacing:-1px;text-align:center;border-radius:2px 0 0 0;font:22px/36px Futura, Arial, sans-serif;font-smoothing:antialiased}.bz1lBb{background:#fff;border-radius:8px 8px 0 0;box-shadow:0 1px 6px rgba(32, 33, 36, 0.18);margin-top:10px}.KP7LCb{border-radius:0 0 8px 8px;box-shadow:0 2px 3px rgba(32, 33, 36, 0.18);margin-bottom:10px;overflow:hidden}.cOl4Id{letter-spacing:-1px;text-align:center;font:22pt Futura, Arial, sans-serif;height:37px;font-smoothing:antialiased;padding:10px 0 5px 0;}.cOl4Id span{display:inline-block}.V6gwVd{color:#4285f4}.iWkuvd{color:#ea4335}.cDrQ7{color:#fcc934}.ntlR9{color:#34a853}.tJ3Myc{-webkit-transform:rotate(-20deg);position:relative;left:-1px;display:inline-block}footer{text-align:center;margin-top:18px}footer a,footer a:visited,.smiUbb{color:#70757a}.xeDNfc{margin:0 13px}#EOlPnc{margin-top:36px}#EOlPnc>div{margin:20px}.Srfpq{color:#70757a}\n",
      "------\n",
      "table,div,span,p{display:none}\n",
      "------\n",
      ".wEsjbd{background-color:#fff;height:44px;white-space:nowrap}.coPU8c{height:60px;overflow-scrolling:touch;overflow-x:auto;overflow-y:hidden}.Xj2aue{height:44px;overflow:hidden}.RnNGze{margin:11px 16px}.wEsjbd div,.wEsjbd a,.wEsjbd li{outline-width:0;outline:none}\n",
      "------\n",
      ".PA9J5{display:inline-block}.RXaOfd{display:inline-block;height:22px;position:relative;padding-top:0;padding-bottom:0;padding-right:16px;padding-left:0;line-height:22px;cursor:pointer;text-transform:uppercase;font-size:12px;color:#70757a}.sa1toc{display:none;position:absolute;background:#fff;border:1px solid #d6d6d6;box-shadow:0 2px 4px rgba(0,0,0,0.3);margin:0;white-space:nowrap;z-index:103;line-height:17px;padding-top:5px;padding-bottom:5px;padding-left:0}.PA9J5:hover .sa1toc{display:block}.mGSy8d a:active,.RXaOfd:active{color:#4285f4}\n",
      "------\n",
      ".TWMOUc{display:inline-block;padding-right:14px;white-space:nowrap}.vQYuGf{font-weight:bold}.OmTIzf{border-color:#909090 transparent;border-style:solid;border-width:4px 4px 0 4px;width:0;height:0;margin-left:-10px;top:50%;margin-top:-2px;position:absolute}.RXaOfd:active .OmTIzf{border-color:#4285f4 transparent}\n",
      "------\n",
      ".ozatM{font-size:12px;text-transform:uppercase}.ozatM .yNFsl,.ozatM li{list-style-type:none;list-style-position:outside;list-style-image:none}.yNFsl.SkUj4c,.yNFsl a{color:rgba(0,0,0,0.54);text-decoration:none;padding:6px 44px 6px 14px;line-height:17px;display:block}.SkUj4c{background-image:url(//ssl.gstatic.com/ui/v1/menu/checkmark2.png);background-position:right center;background-repeat:no-repeat}.SkUj4c:active{background-color:#f8f9fa}\n",
      "------\n",
      ".ZINbbc{background-color:#fff;margin-bottom:10px;box-shadow:0 1px 6px rgba(32, 33, 36, 0.28);border-radius:8px}.uUPGi{font-size:14px;line-height:20px;}.O9g5cc>*:first-child{border-top-left-radius:8px;border-top-right-radius:8px}.O9g5cc>*:last-child{border-bottom-left-radius:8px;border-bottom-right-radius:8px}.O9g5cc>.qxDOhb>*:first-child{border-top-left-radius:8px;border-top-right-radius:8px}.O9g5cc>.qxDOhb>*:last-child{border-bottom-left-radius:8px;border-bottom-right-radius:8px}.rLshyf,.BmP5tf{padding-top:12px;padding-bottom:12px}.YOx3Ab{padding-left:16px;}.w1C3Le,.BmP5tf,.G5NbBd,.CS4w5b{padding-left:16px;padding-right:16px;}.G5NbBd{padding-bottom:12px}.CS4w5b{padding-top:12px}.MUxGbd{font-size:14px;font-family:Roboto,Helvetica Neue,Arial,sans-serif;line-height:20px;padding-top:1px;margin-bottom:-1px}.MUxGbd.v0nnCb{font-size:16px;line-height:20px;padding-top:1px;margin-bottom:-1px}.lyLwlc{color:#202124}a.fdYsqf{color:#4b11a8}.ZTv9Bb{display:block}.nVTMpe{border-radius:8px}.wVMPHe{margin:0 auto}.kCrYT{padding:12px 16px 12px}.l97dzf{font-weight:400}.zBAuLc{line-height:normal;margin:0;padding:0}.BNeawe{white-space:pre-line;word-wrap:break-word}.deIvCb{font-size:16px;line-height:20px;font-weight:400}.deIvCb.HrGdeb{color:#fff}.deIvCb.AP7Wnd{color:#202124}.tAd8D{font-size:14px;line-height:20px}.tAd8D.HrGdeb{color:rgba(255,255,255,.70)}.tAd8D.AP7Wnd{color:#70757a}.R0jTRc{vertical-align:middle}.x54gtf{height:1px;background-color:#dfe1e5;margin:0 16px}.Q0HXG{height:1px;background-color:#dfe1e5}.X7NTVe{display:table;width:100%;padding-right:16px;box-sizing:border-box}.tHmfQe{display:table-cell;padding:12px 0 12px 16px}.UHtrk{width:72px}.HBTM6d{width:30px}.XS7yGd{display:table-cell;text-align:center;vertical-align:middle;padding:12px 0 12px 8px}.am3QBf{display:table;vertical-align:top}.xUrNXd.VyZZLb{color:rgba(255,255,255,.70)}.xUrNXd.UMOHqf{color:#70757a}.tP9Zud{display:inline-block;}.QzarWc{color:#3c4043}.oqSTJd{color:#70757a}.Hk2yDb,.Hk2yDb span{background-repeat:repeat-x;background-size:14px,14px;height:14px;width:70px}.Hk2yDb{display:inline-block;font-size:0;line-height:0;position:relative;top:1px}.Hk2yDb span{display:block}.Hk2yDb.KsR1A{background-image:url(data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAACgAAAAoBAMAAAB+0KVeAAAAD1BMVEVMaXEAAAAAAAAAAAAAAACF6eB8AAAABXRSTlMAID8OM2w9R7oAAACdSURBVHgBvdGBCcIwEEbhq+kAaXEA+5oBYuoAmnb/mQT5gcMDCoB+AIEA9y7EfmrIFl1uFrXVol4sSFBjB3LsQCzNsMQOlNjhq5S26Qrwmjbdp6PjlKMq4SiXwNOAhrOadDeymoyAPP1zfEUGJJvTNdFOLxFzElLPQqNb0/8F+x39iDTYzR56ucws7pBePtnU/aKomrpbM5sM1f7pDdrTIIXMnb07AAAAAElFTkSuQmCC)}.Hk2yDb.KsR1A span{background-image:url(data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAACgAAAAoBAMAAAB+0KVeAAAAGFBMVEVMaXH0tAD0tAD0tAD0tAD0tAD0tAD0tAB7hoq7AAAACHRSTlMAP6Ib/oXVZJ3/vYgAAADHSURBVHgBnNE1A4JgGARgmtHW0dxtZ+OA0dbRdrX/v+RLmkc/9H3MH2HjEcgVIrA1iMCZEoF7NWwycA6hBKxDmAZ6IawA/aDx0FMLoGjgKIAdA3d0WM89SkfYOZaWl5SOdwSiGe0EMW4/jkIP5vdeU2t2k14sUGugKJ6GKGdfG0aoE/+l509I7y/4azfiL7/l4IDIU4rmHwv0zZUH94AaZ421f4DO1ofVCFmgbGwbQNwzahtrJ4sRoUQvva8JuRo9vcA8RyMAAIXWR1O6HNlyAAAAAElFTkSuQmCC)}.AraNOb{text-decoration:underline}.Icx6Cd{margin:0 auto 8px}.ZAfNud{display:table;width:100%}.naKQFc{display:table-cell;vertical-align:top}.Ne5sAf{vertical-align:middle}.xevp3d{overflow:hidden}.XCaUNd{display:block}.mugnXc{color:#3c4043;font-size:14px}.Q0cixc{display:block;white-space:pre-line;word-wrap:break-word}.mugnXc.Q0cixc{line-height:20px}.mEUgP{font-weight:bold;font-size:16px;color:#000;margin:0;padding:12px 16px 12px}.atOwb{font-weight:bold}.C7GS5b{margin-left:12px;display:table-cell;vertical-align:middle}.rkGIWe{padding:14px}.xpc .hwc,.xpx .hwx{display:none}.iIWm4b{box-sizing:border-box;min-height:48px}.fLtXsc{padding:14px;position:relative}.NtmAdb{width:40px;height:40px;overflow:hidden;margin-top:-10px;margin-bottom:-16px;margin-right:8px;border-radius:4px}.xpc .NtmAdb{display:inline-block}.xpx .NtmAdb{display:none}.Lt3Tzc{display:inline-block;padding-right:26px}.Lym8W{width:14px;height:20px;position:relative;margin:0 auto}.xCgLUe{position:absolute;right:16px;margin-top:-10px;top:50%}.Lym8W div{position:absolute;border-left:7px solid transparent;border-right:7px solid transparent;width:0;height:0;left:0}.IyYaEd{top:7px;border-top:7px solid #70757a}.ECUHQe{top:4px;border-top:7px solid #fff}.AeQQub{bottom:7px;border-bottom:7px solid #70757a}.YCU7eb{bottom:4px;border-bottom:7px solid #fff}.qxDOhb{border-radius:0}.yStFkb .xpd{border-radius:8px;box-shadow:none;border:1px solid #dadce0;margin-bottom:0}.uEec3{font-size:12px;line-height:16px}.uEec3.HrGdeb{color:rgba(255,255,255,.70)}.uEec3.AP7Wnd{color:#70757a}.EDgFbc{color:#1967D2}a:visited .EDgFbc{color:#4B11A8}.EDgFbc.VyZZLb{color:#fff}a:visited .EDgFbc.VyZZLb{color:rgba(255,255,255,.70)}.VbKY9d{color:#006621}.P1NWSe{display:table;width:100%;padding-top:16px;padding-bottom:16px;margin-bottom:-12px}.wOMIed{display:table-cell;vertical-align:top}.nkPlDb{vertical-align:middle}.JhFlyf{color:#3c4043;font-size:14px;text-align:center}.VQFmSd{display:block;white-space:pre-line;word-wrap:break-word}.JhFlyf.VQFmSd{line-height:20px}.f4J0H{padding:18px}.hfgVwf{margin-top:12px}.IxZjcf .hfgVwf{margin-bottom:12px}.OdF8Fd{float:right;padding-left:16px}.p1vimb{border-radius:8px;display:block}.rkvY3c{clear:both}.CgE3Ac{margin:0 16px}.I9mEQ{padding-bottom:12px}.LnMnt{border-collapse:collapse;border-spacing:0;width:100%}.LnMnt td{padding-top:0;padding-bottom:0;padding-right:8px}.LnMnt .s5aIid{padding-right:0}.IxZjcf{border-bottom:1px solid #dfe1e5}.sjsZvd{vertical-align:top}.OE1use{text-align:left}.BSv1qf{text-align:center}.HlHBvc{text-align:right}.IfyLsd{float:left;margin-right:8px}.s3v9rd{font-size:14px;line-height:20px}.s3v9rd.HrGdeb{color:#fff}.s3v9rd.AP7Wnd{color:#202124}.vvjwJb{color:#1967D2;font-size:16px;line-height:20px}a:visited .vvjwJb,.vvjwJb a:visited{color:#4B11A8}.vvjwJb.HrGdeb{color:#fff}a:visited .vvjwJb.HrGdeb,.vvjwJb.HrGdeb a:visited{color:rgba(255,255,255,.70)}.UPmit{font-size:14px;line-height:20px}.UPmit.HrGdeb{color:rgba(255,255,255,.70)}.UPmit.AP7Wnd{color:#0d652d}.oTWEpb{padding-top:12px}.n1Qedd{overflow:hidden;text-align:center}.KMAGC{margin:0 auto;display:block}.ho0sdc{margin:0 -50%;display:inline-block}.Ey4n2{padding-bottom:12px}.rl7ilb{display:block;clear:both}.yRG22b{padding-left:48px;margin:0}.MSiauf{padding-bottom:8px}.XLloXe{color:#1967D2;font-size:14px;line-height:20px}a:visited .XLloXe,.XLloXe a:visited{color:#4B11A8}.XLloXe.HrGdeb{color:#fff}a:visited .XLloXe.HrGdeb,.XLloXe.HrGdeb a:visited{color:rgba(255,255,255,.70)}.gGQDvd{padding:14px;position:relative}.Q71vJc{display:block;position:relative;width:100%}.kjGX2{position:absolute;left:48px;right:0;vertical-align:bottom;display:inline-block;color:#3c4043}.ieB2Dd{width:40px;height:40px;overflow:hidden;margin-top:-10px;margin-bottom:-16px;margin-right:8px;border-radius:4px;display:inline-block;border-radius:50%;}.LsF2v span{color:#fff;mask-image:url(data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAADAAAAAwCAQAAAD9CzEMAAABa0lEQVR4AeyWtUIYQRBAX6yLu0uH08Q9ZfInNHF36UKFlHwHNLi7u2uNN9hgg3PsCVtx753fzOkalgkJieErOXQwsWAHOXwjZjcvXohsYy7xBOYgycwhDs6RzEECcJZyxGA5Z/HJIUoQVAp4z22OL3ibdxs+WgmH8EUqorZzl83cpR1RU/FBDKI2cMrhAzYgaiyeydDUQc7hxDkGNSoDj1xH1CfsxDNEvYEnXmtaNiayNPK1vw+UgIkEfx+pRdOiMRGlkS14YlLTjmHimEZO4IlxTTuCiSMaOYkn2jQtChORGtlr+ycX4YlXrotptkb+wxM3XFa0J4j60E5TMaRRNXgmHlEbOevQ2DUi6gt8kGJorjsQNW23OpxbnOQEt3lPMYLKNJdsdpkjuv5lo9MX/nMBUT/jk3iHYUs9zwGQ4LeAaHTgxTgtpPOLpyj8Dn4LE4l79RbhLV7bvsVnsHmLz1gk0e7lQ0LmRzMAAAU5VLMEuZJZAAAAAElFTkSuQmCC)}.lRVwie{text-overflow:ellipsis;white-space:nowrap;overflow:hidden}.nMymef{display:flex}.G5eFlf{flex:1;display:block}.nMymef span{text-align:center}\n",
      "------\n"
     ]
    }
   ],
   "source": [
    "text= \"knee surgeons chennai\"\n",
    "url = 'https://google.com/search?q=' + text\n",
    "  \n",
    "# Fetch the URL data using requests.get(url),\n",
    "# store it in a variable, request_result.\n",
    "request_result=requests.get( url )\n",
    "  \n",
    "# Creating soup from the fetched request\n",
    "soup = BeautifulSoup(request_result.text,\n",
    "                         \"html.parser\")\n",
    "\n",
    "#print(soup.prettify())\n",
    "# soup.find.all( h3 ) to grab\n",
    "# all major headings of our search result,\n",
    "heading_object=soup.find_all( 'style')\n",
    "\n",
    "# Iterate through the object\n",
    "# and print it as a string.\n",
    "for info in heading_object:\n",
    "\tprint(info.getText())\n",
    "\tprint(\"------\")\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 29,
   "id": "9013f622",
   "metadata": {},
   "outputs": [],
   "source": []
  },
  {
   "cell_type": "code",
   "execution_count": 33,
   "id": "d61bbe80",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "[]\n"
     ]
    }
   ],
   "source": []
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "50487926",
   "metadata": {},
   "outputs": [],
   "source": []
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "d9b8ad71",
   "metadata": {},
   "outputs": [],
   "source": []
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3 (ipykernel)",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.9.7"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}
