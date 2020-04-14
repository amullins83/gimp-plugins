from gimpfu import *

def zoom_in_gif(img, num_frames, max_zoom_percent):
    n = int(num_frames)
    pdb.gimp_image_undo_group_start(img)
    max_zoom = 1.0 * max_zoom_percent / 100.0
    zoom_step = pow(max_zoom, 1.0/n)
    w = img.width
    h = img.height
    for _ in range(n):
        new_layer = pdb.gimp_layer_copy(img.layers[0], False)
        img.add_layer(new_layer)
        w *= zoom_step
        h *= zoom_step
        pdb.gimp_layer_scale(new_layer, w, h, True)
        pdb.gimp_layer_resize_to_image_size(new_layer)

    pdb.gimp_image_undo_group_end(img)

register(
    proc_name=("python_fu_zoom_in_gif"),
    blurb=("Creates a 'zoom in' animation"),
    help=("Adds layers that can be exported as an animated GIF that zooms in to the center of the existing top layer."),
    author=("Austin Mullins"),
    copyright=("GPLv3, Austin Mullins"),
    date=("2020"),
    label=("Zoom-in GIF"),
    imagetypes=("*"),
    params=[
        (PF_IMAGE, "img", "Image", None),
        (PF_SPINNER, "num_frames", "Frames:", 5, (2, 120, 1)),
        (PF_SPINNER, "max_zoom_percent", "Zoom %:", 200, (50, 1600, 5)),
    ],
    results=[],
    function=(zoom_in_gif),
    menu=("<Image>/Filters/Animation"),
    domain=("gimp20-python", gimp.locale_directory),
)

main()
