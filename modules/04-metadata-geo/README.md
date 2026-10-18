# Module 04 — Metadata & Geolocation OSINT

Practice target: photos **you** took with your own phone.

## Concepts
- EXIF: GPS coords, device, timestamps embedded in images
- Metadata in PDFs and Office docs (author names, edit history)
- Visual geolocation: landmarks, shadows, vegetation, signage (Bellingcat style)

## Commands
```bash
exiftool IMG_0001.jpg          # full metadata dump
exiftool -gps:all= -a -b -overwrite_original *.jpg   # strip GPS from a folder
```

## Exercise
1. Dump EXIF on 10 of your own photos — how many carry GPS?
2. Take a photo, strip its metadata, verify with exiftool again.
3. Pick a photo you took outdoors (with metadata removed) and try to geolocate
   it from visuals only: skyline, road signs, sun angle.
4. Check a PDF you made for hidden author metadata.

**Done when:** your photo library is metadata-clean and you can geolocate one of your own photos from visuals alone.
