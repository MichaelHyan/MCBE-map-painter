from PIL import Image
material = 'concrete'#wool#concrete_powder
def match(image_path):
    colors = [
    [217,199,199],
    [183,169,166],
    [103,98,89],
    [58,60,44],
    [131,92,58],
    [189,57,48],
    [206,100,27],
    [221,201,0],
    [215,90,121],
    [173,62,202],
    [151,77,197],
    [59,75,187],
    [90,132,198],
    [84,133,163],
    [121,143,48],
    [118,191,0]]
    weight_r, weight_g, weight_b = 0.299, 0.587, 0.114
    try:
        img = Image.open(image_path).convert("RGB")
    except Exception as e:
        print(f"读取图片失败：{e}")
        return
    width, height = img.size
    print(f"\n图片尺寸：{width}x{height} 像素")
    result = []
    for y in range(height):
        for x in range(width):
            pixel_rgb = img.getpixel((x, y))
            min_dist_sq = float('inf')
            closest_idx = 0
            for color_idx, target_rgb in enumerate(colors):
                dr = pixel_rgb[0] - target_rgb[0]
                dg = pixel_rgb[1] - target_rgb[1]
                db = pixel_rgb[2] - target_rgb[2]
                weighted_dist_sq = (
                    (dr * weight_r) ** 2 +
                    (dg * weight_g) ** 2 +
                    (db * weight_b) ** 2
                )
                if weighted_dist_sq < min_dist_sq:
                    min_dist_sq = weighted_dist_sq
                    closest_idx = color_idx
            result.append((x, y, closest_idx))
    return result
def convert(x,y,l):
    color = ['white',
              'light_gray',
              'gray',
              'black',
              'brown',
              'red',
              'orange',
              'yellow',
              'pink',
              'magenta',
              'purple',
              'blue',
              'light_blue',
              'cyan',
              'green',
              'lime',]
    return f'setblock ~{x} ~-1 ~{y} {color[l]}_{material}'
def main():
    print('将图片拖至此处')
    path = input()
    result = match(path)
    r = []
    for x, y, l in result:
        r.append(convert(x,y,l))
    j = 0
    for i in range(0,len(r),9000):
        with open(f'.\\functions\\new{j}.mcfunction', 'w') as f:
            f.write('\n'.join(r[i:i+9000]))
        j += 1
    print(f'生成完毕  共{j+1}个文件')
if __name__ == "__main__":
    main()