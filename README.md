## Torrent Tagger

This is a *really* simple script I wrote so I could automatically tag torrents in [qBittorrent](https://github.com/qbittorrent/qBittorrent) based on the name of the torrent. My specific use case for this is there are some torrents I want [qBit Manage](https://github.com/StuffAnThings/qbit_manage) to remove if there are no hardlinks, and some I do NOT. So with this script I can tag the ones I do not want it to remove, and exclude that tag from the share limits. But I'm sure there are plenty of other use cases for something like this, so hopefully this helps!

## Usage

`python torrent_tags.py` *qbit_url* *title_search_regex* *qbit_tag*

- *qbit_url:* The url to your qBittorrent WebUI (example: `http://localhost:10095`)
- *title_search_regex*: The regex you want to search for in the names of your torrents (currently no flags are supported, and `ignorecase` is on by default). For example if you want to tag all releases from CoolGuy35, then you would use `"CoolGuy35"`
- *qbit_tag*: Name of the tag you want to add to all torrents that contain the *title_search_string*. (example: `"CoolGuy"`) **NOTE**: Currently this tag has to exist in qBittorrent before running this script. It will cause an error if the tag you give here doesn't exist.

## How to automate

Currently I just have this script run on a cron job on the same TrueNAS machine I have running qBittorrent on.

## Future Improvements

- ~~Have the *title_search_string* be a regular expression instead of just a string~~
    - Add the abilities to pass flags (currently the `ignorecase` flag is on by default)
- Add the ability to give multiple tags and multiple search expressions 
- Add the ability to give login creds for qBittorrent