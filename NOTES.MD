Converting:
- Converted to asciidoc with kramdoc using the convert.py python script
- Script also generates navigation (only a base, needs manual work for a useful structure)
- All images copied into the images (asset) folder, with each sample getting it's own folder
- Image links fixed
    - Some samples use link:./images/renderdoc_with_labels.jpg[image:./images/renderdoc_with_labels.jpg[\]], which need more manual treatment
- Lots of links manually fixed
- Use auto-generated table of contents in some places

Opens : 
- Still lots of problems like wrong formatting of some chapterr (eg. Fragment Shading Rate dynamic)
- Many samples only have dummy readme files with no real content
- Lots of links need to be fixed (e.g. to other parts of code or samples or within the same document)
- Better nav, maybe move HPP sample variants below non HPP version as sub link
- Some HPP samples duplicate tutorials of non HPP variants
- Some files have manual table of contest, should be remove (use side nav) or auto-generated from doctype

Done:
- Fixed some existing markdown issues on samples repo (indentation, formatting, line breaks, etc.)
