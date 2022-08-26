from pytube import YouTube
import os
os.system('cls')

print('</// late18coder\'s YouTube Video Downloader ///>\n\n')
print('+> Enter the link of the video you wish to download;\n')
link = input('-> ')

yt = YouTube(link)

print('\n')
print("=> Title:", yt.title)
print("=> Author:", yt.author)
print("=> Views:", yt.views)
print("=> Upload Date:", yt.publish_date)
print('\n')
print('+> Select your Download Preference\n')
print('  1) High Quality Video (Progressive)')
print('  2) Low Quality Video (Progressive)\n')

quality = int(input('-> '))

if quality == 1:
    selected_res = yt.streams.filter(file_extension='mp4', progressive=True).order_by('resolution').desc().first()
    print("\n=> Stream Data:", selected_res,'\n')

elif quality == 2:
    selected_res = yt.streams.filter(file_extension='mp4', progressive=True).order_by('resolution').asc().first()
    print("\n=> Stream Data:", selected_res,'\n')

else:
    print('=> Invalid Input!')
    input('=> Press any key to exit\n')
    exit()

downdir = os.getcwd()
dir_cd_choice = 'n'

print('=> The current download directory is set to',str(downdir)+'.')
print('+> Do you wish to change the download directory? ( y / default = n )')
dir_cd_choice = input('-> ').lower()

if dir_cd_choice == 'y':
    print('\n+> Enter a new download path; (ex: '+str(downdir)+' )')
    downdir = input('-> ')
    print('\n=> New download path saved and selected.\n')

elif dir_cd_choice == 'n':
    print('=> Default download path selected.\n')

print('=> Please wait a moment for the download to complete...')

selected_res.download(downdir)
print('=> Video successfully downloaded to',downdir,'\n')
input('=> Press any key to exit\n')
exit()
