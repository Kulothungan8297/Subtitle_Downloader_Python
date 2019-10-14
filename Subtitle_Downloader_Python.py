from datetime import timedelta

from babelfish import Language
from subliminal import download_best_subtitles, region, save_subtitles, scan_videos

# configure the cache
region.configure('dogpile.cache.dbm', arguments={'filename': 'cachefile.dbm'})

# scan for videos newer than 2 weeks and their existing subtitles in a folder
videos = scan_videos('D:\TV Series\Westworld\[TorrentCouch.com].Westworld.S02.Complete.720p.WEB-DL.x264.[MP4].[5.3GB].[Season.2.Full]')

# download best subtitles
subtitles = download_best_subtitles(videos, {Language('eng')})

# save them to disk, next to the video
for v in videos:
    save_subtitles(v, subtitles[v])
