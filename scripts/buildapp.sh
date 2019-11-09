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
    --add-binary='/System/Library/Frameworks/Tk.framework/Tk':'tk' \
    --add-binary='/System/Library/Frameworks/Tcl.framework/Tcl':'tcl' \
    ../main.py

# Cleanup uneeded files
rm -dr ../dist/work
rm ../dist/SermonMovieMaker.spec