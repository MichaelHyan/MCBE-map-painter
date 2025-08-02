from PIL import Image
material = ['glass','concrete','wool','planks','nether','sea','structure','terracotta','glazed_terracotta','glowable','special']
name = ['玻璃','混凝土','羊毛','木板','下界方块','海洋神殿方块','建筑方块','陶瓦','带釉陶瓦','发光方块','不可名状方块']
m_list = []
c_list = []
weight = True
def match(image_path,color):
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
            for color_idx, target_rgb in enumerate(color):
                dr = pixel_rgb[0] - target_rgb[0]
                dg = pixel_rgb[1] - target_rgb[1]
                db = pixel_rgb[2] - target_rgb[2]
                if weight:
                    dist_sq = (
                        (dr * weight_r) ** 2 +
                        (dg * weight_g) ** 2 +
                        (db * weight_b) ** 2
                    )
                else:
                    dist_sq = (
                        dr ** 2 +
                        dg ** 2 +
                        db ** 2
                    )
                if dist_sq < min_dist_sq:
                    min_dist_sq = dist_sq
                    closest_idx = color_idx
            result.append((x, y, closest_idx))
    return result
def convert(x,y,l,block):
    return f'setblock ~{x} ~-1 ~{y} {block[l]}'
def main():
    global m_list,c_list,weight
    print('将图片拖至此处')
    path = input()
    print('选取材料类型，序号使用空格分开')
    for i in range(len(material)):
        print(f'{i} {name[i]} {material[i]}')
    b_list = list(map(int,input().split()))
    print('是否使用视觉增强算法，y/n')
    if input() == 'y':
        weight = True
    else:
        weight = False
    for i in b_list:
        with open(f'.\\material\\map_{material[i]}_b.txt','r') as f:
            b = f.read().split('\n')
            m_list.append(b)
        with open(f'.\\material\\map_{material[i]}_c.txt','r') as f:
            c = f.read().split('\n')
            for j in c:
                c_list.append(list(map(int,j.split(','))))
    result = match(path,c_list)
    r = []
    mt_list = []
    for i in m_list:
        for j in i:
            mt_list.append(j)
    for x, y, l in result:
        r.append(convert(x,y,l,mt_list))
    j = 0
    for i in range(0,len(r),9000):
        with open(f'.\\functions\\new{j}.mcfunction', 'w') as f:
            f.write('\n'.join(r[i:i+9000]))
        j += 1
    print(f'生成完毕  共{j}个文件')
    print('是否生成预览图，y/n')
    if input() == 'y':
        pix = []
        for x,y,l in result:
            pix.append((x,y,(c_list[l][0],c_list[l][1],c_list[l][2])))
        width = max(x for x, y, rgb in pix) + 1
        height = max(y for x, y, rgb in pix) + 1
        image = Image.new("RGB", (width, height))
        for x, y, rgb in pix:
            image.putpixel((x, y), rgb)
        image.save("output_image.png")

if __name__ == "__main__":
    main()