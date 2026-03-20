[app]
title = Khazna Dr Monem
package.name = khaznamonem
package.domain = org.test
source.dir = .
source.include_exts = py,png,jpg,kv,atlas,sqlite3,ttf
version = 1.0

# المكتبات التي تمنع الانهيار وتصلح الخط العربي
requirements = python3,kivy,cryptography,sqlite3,arabic-reshaper,python-bidi,openssl,hostpython3

orientation = portrait
android.permissions = WRITE_EXTERNAL_STORAGE, READ_EXTERNAL_STORAGE, MANAGE_EXTERNAL_STORAGE
android.api = 31
android.minapi = 21
android.sdk = 31
android.ndk = 25b
android.archs = armeabi-v7a, arm64-v8a
