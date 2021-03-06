# (C) supun-maduraga my best friend for his project on call-music-plus

from time import time
from datetime import datetime
from pyrogram import Client, filters
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton, Chat, CallbackQuery
from helpers.decorators import authorized_users_only
from config import BOT_NAME, BOT_USERNAME, OWNER_NAME, GROUP_SUPPORT, UPDATES_CHANNEL, ASSISTANT_NAME
from handlers.play import cb_admin_check


START_TIME = datetime.utcnow()
START_TIME_ISO = START_TIME.replace(microsecond=0).isoformat()
TIME_DURATION_UNITS = (
    ('week', 60 * 60 * 24 * 7),
    ('day', 60 * 60 * 24),
    ('hour', 60 * 60),
    ('min', 60),
    ('sec', 1)
)

async def _human_time_duration(seconds):
    if seconds == 0:
        return 'inf'
    parts = []
    for unit, div in TIME_DURATION_UNITS:
        amount, seconds = divmod(int(seconds), div)
        if amount > 0:
            parts.append('{} {}{}'
                         .format(amount, unit, "" if amount == 1 else "s"))
    return ', '.join(parts)


@Client.on_callback_query(filters.regex("cbstart"))
async def cbstart(_, query: CallbackQuery):
    current_time = datetime.utcnow()
    uptime_sec = (current_time - START_TIME).total_seconds()
    uptime = await _human_time_duration(int(uptime_sec))
    await query.edit_message_text(
        f"""<b>๐๐ป **Hallo, saya {query.message.from_user.mention}!**</b>

โ **Saya aktif dan siap memutar musik!
โข Start time: `{START_TIME_ISO}`
โข Klik pada tombol ยป ๐ Perintah dan lihat semua perintah bot!

๐ก Bot By @{UPDATES_CHANNEL}**""",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "๐ฅ Support", url=f"https://t.me/{GROUP_SUPPORT}")
                ],
                [
                    InlineKeyboardButton(
                        "๐ Perintah", callback_data="cbhelp"
                    )
                ]
            ]
        )
    )



@Client.on_callback_query(filters.regex("cbhelp"))
async def cbhelp(_, query: CallbackQuery):
    await query.edit_message_text(
        f"""<b>๐๏ธ Berikut ini adalah menu bantuan !</b>

**Dalam menu ini Anda dapat membuka beberapa menu perintah yang tersedia, di setiap menu perintah ada juga penjelasan singkat dari setiap perintah**

๐ก Bot by @{UPDATES_CHANNEL}""",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "๐ Basic Cmd", callback_data="cbbasic"
                    ),
                    InlineKeyboardButton(
                        "๐ Advanced Cmd", callback_data="cbadvanced"
                    )
                ],
                [
                    InlineKeyboardButton(
                        "๐ Admin Cmd", callback_data="cbadmin"
                    ),
                    InlineKeyboardButton(
                        "๐ Sudo Cmd", callback_data="cbsudo"
                    )
                ],
                [
                    InlineKeyboardButton(
                        "โฅ๏ธ Fun Cmd", callback_data="cbfun"
                    )
                ],
                [
                    InlineKeyboardButton(
                        "BACK", callback_data="cbguide"
                    )
                ]
            ]
        )
    )


@Client.on_callback_query(filters.regex("cbbasic"))
async def cbbasic(_, query: CallbackQuery):
    await query.edit_message_text(
        f"""<b>๐๏ธ command dasar untuk bot</b>

๐ก [ SETTING GRUP ]
/play (judul) - memutar musik melalui youtube
/ytp (judul) - memutar musik secara langsung 
/stream (balas ke audio) - memutar kusik melalui balas ke audio
/playlist - melihat daftar antrian
/song (judul) - mengunduh musik dari youtube
/search (judul) - mencari musik dari youtube secara detail
/video (judul) - mengunduh musik dari youtube secara detail
/lirik - (judul) mencari lirik
๐ก [ SETTING CHANNEL ]
/cplay - memutar musik melalui channel
/cplayer - melihat daftar antrian
/cpause - jeda pemutar musik
/cresume - melanjut pemutaran musik
/cskip - melewati ke lagu berikutnya
/cend - memberhentikan musik
/admincache - menyegarkan cache admin
/ubjoinc - mengundang assisten join ke channel

๐ก Bot by @{UPDATES_CHANNEL}""",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "BACK", callback_data="cbhelp"
                    )
                ]
            ]
        )
    )


@Client.on_callback_query(filters.regex("cbadvanced"))
async def cbadvanced(_, query: CallbackQuery):
    await query.edit_message_text(
        f"""<b>๐๏ธ command lanjutan</b>

/start (di grup) - melihat status bot
/reload - memperbarui bot dan menyegarkan daftar admin
/alive - melihat status alive bot
/ping - cek ping bot

๐ก Bot by @{UPDATES_CHANNEL}""",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "BACK", callback_data="cbhelp"
                    )
                ]
            ]
        )
    )


@Client.on_callback_query(filters.regex("cbadmin"))
async def cbadmin(_, query: CallbackQuery):
    await query.edit_message_text(
        f"""<b>๐๏ธ command untuk admin grup</b>

/player - melihat status pemutaran
/pause - jeda musik yang diputar
/resume - melanjutkan musik yang di jeda
/skip - melewati ke lagu berikutnya
/end - mematikan musik
/userbotjoin - mengundang assistant untuk bergabung ke grup
/musicplayer (on / off) - mematikan / menghidupkan pemutar musik di grupmu

๐ก Bot by @{UPDATES_CHANNEL}""",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "BACK", callback_data="cbhelp"
                    )
                ]
            ]
        )
    )


@Client.on_callback_query(filters.regex("cbsudo"))
async def cbsudo(_, query: CallbackQuery):
    await query.edit_message_text(
        f"""<b>๐๏ธ **command untuk sudo**</b>

**/userbotleaveall - mengeluarkan asisten dari semua grup
/gcast - mengirim pesan global melalui asisten
/rmd - menghapus file downloadan
/rmr - menghapus file raw terdownload

๐ก Bot by @{UPDATES_CHANNEL}**""",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "BACK", callback_data="cbhelp"
                    )
                ]
            ]
        )
    )


@Client.on_callback_query(filters.regex("cbfun"))
async def cbfun(_, query: CallbackQuery):
    await query.edit_message_text(
        f"""<b>๐๏ธ **Command fun**</b>

**/chika - cek sendiri
/wibu - cek sendiri
/asupan - cek sendiri
/truth - cek sendiri
/dare - cek sendiri

๐ก Bot by @{UPDATES_CHANNEL}**""",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "BACK", callback_data="cbhelp"
                    )
                ]
            ]
        )
    )


@Client.on_callback_query(filters.regex("cbguide"))
async def cbguide(_, query: CallbackQuery):
    await query.edit_message_text(
        f"""**CARA MENGGUNAKAN BOT INI :**

**1.) Pertama, tambahkan ke grupmu.
2.) Kemudian jadikan admin dengan semua izin kecuali admin anonim.
3.) Tambahkan @{ASSISTANT_NAME} ke grupmu atau bisa ketik `/userbotjoin` untuk mengundang assistant.
4.) Nyalakan obrolan suara terlebih dahulu sebelum memutar musik.

๐ก Bot by @{UPDATES_CHANNEL}**""",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "๐ Command List", callback_data="cbhelp"
                    )
                ],
                [
                    InlineKeyboardButton(
                        "๐ Close", callback_data="close"
                    )
                ]
            ]
        )
    )


@Client.on_callback_query(filters.regex("close"))
async def close(_, query: CallbackQuery):
    await query.message.delete()


@Client.on_callback_query(filters.regex("cbcmds"))
async def cbhelps(_, query: CallbackQuery):
    await query.edit_message_text(
        f"""<b>๐๏ธ **Hallo ini adalah menu bantuan !**</b>

**Dalam menu ini Anda dapat membuka beberapa menu perintah yang tersedia, di setiap menu perintah ada juga penjelasan singkat dari setiap perintah

๐ก Bot by @{UPDATES_CHANNEL}**""",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "๐ Basic Cmd", callback_data="cbbasic"
                    ),
                    InlineKeyboardButton(
                        "๐ Advanced Cmd", callback_data="cbadvanced"
                    )
                ],
                [
                    InlineKeyboardButton(
                        "๐ Admin Cmd", callback_data="cbadmin"
                    ),
                    InlineKeyboardButton(
                        "๐ Sudo Cmd", callback_data="cbsudo"
                    )
                ],
                [
                    InlineKeyboardButton(
                        "โฅ๏ธ Fun Cmd", callback_data="cbfun"
                    )
                ],
                [
                    InlineKeyboardButton(
                        "BACK", callback_data="cbstart"
                    )
                ]
            ]
        )
    )


@Client.on_callback_query(filters.regex("cbhowtouse"))
async def cbguides(_, query: CallbackQuery):
    await query.edit_message_text(
        f"""๐๏ธ** CARA MENGGUNAKAN BOT ๐๏ธ :

1.) Pertama, tambahkan ke grupmu.
2.) Kemudian jadikan admin dengan semua izin kecuali admin anonim.
3.) Tambahkan @{ASSISTANT_NAME} ke grupmu atau bisa ketik `/userbotjoin` untuk mengundang assistant.
4.) Nyalakan obrolan suara terlebih dahulu sebelum memutar musik.

๐ก Bot by @{UPDATES_CHANNEL}**""",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "BACK", callback_data="cbstart"
                    )
                ]
            ]
        )
    )
