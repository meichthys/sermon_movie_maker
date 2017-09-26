# Remobe dist directory before building
rm -dr ../dist/

# Run Pyinstaller
pyinstaller \
    --distpath ../dist/ \
    --onefile \
    --specpath ../dist/ \
    --workpath ../dist/work/ \
    --name "SermonMovieMaker" \
    --console \
    --clean \
    ../main.py

# Cleanup uneeded files
rm -dr ../dist/work
rm ../dist/SermonMovieMaker.spec