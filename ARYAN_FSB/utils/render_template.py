from ARYAN_FSB.vars import Var
from ARYAN_FSB.bot import StreamBot
from ARYAN_FSB.utils.human_readable import humanbytes
from ARYAN_FSB.utils.file_properties import get_file_ids
from ARYAN_FSB.server.exceptions import InvalidHash
import urllib.parse
import aiofiles
import logging
import aiohttp

async def render_page(id, secure_hash):
    file_data = await get_file_ids(StreamBot, int(Var.BIN_CHANNEL), int(id))
    
    # Check if hash is valid
    if file_data.unique_id[:6] != secure_hash:
        logging.debug(f'link hash: {secure_hash} - {file_data.unique_id[:6]}')
        logging.debug(f"Invalid hash for message with - ID {id}")
        raise InvalidHash
    
    src = urllib.parse.urljoin(Var.URL, f'{secure_hash}{str(id)}')

    # Determine type of media (video, audio, or other)
    if str(file_data.mime_type.split('/')[0].strip()) == 'video':
        async with aiofiles.open('ARYAN_FSB/template/req.html') as r:
            html = (await r.read()).format(heading=f'Watch {file_data.file_name}', file_name=file_data.file_name, file_url=src)
    elif str(file_data.mime_type.split('/')[0].strip()) == 'audio':
        async with aiofiles.open('ARYAN_FSB/template/req.html') as r:
            html = (await r.read()).format(heading=f'Listen {file_data.file_name}', file_name=file_data.file_name, file_url=src)
    else:
        async with aiofiles.open('ARYAN_FSB/template/dl.html') as r:
            async with aiohttp.ClientSession() as s:
                async with s.get(src) as u:
                    file_size = humanbytes(int(u.headers.get('Content-Length')))
                    html = (await r.read()).format(heading=f'Download {file_data.file_name}', file_name=file_data.file_name, file_url=src, file_size=file_size)
    
    return html
