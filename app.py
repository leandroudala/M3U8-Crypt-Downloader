import os
import time
from urllib.request import urlopen

# link = input('informe o link: ')
"""
m3u8    https://hls2.videos.sproutvideo.com/1c17b7f004cf656622755e966ed6e87d/7cf365e36d8835c8b2aad49cf3a1d8aa/video/1080.m3u8?Policy=eyJTdGF0ZW1lbnQiOlt7IlJlc291cmNlIjoiaHR0cHM6Ly9obHMyLnZpZGVvcy5zcHJvdXR2aWRlby5jb20vMWMxN2I3ZjAwNGNmNjU2NjIyNzU1ZTk2NmVkNmU4N2QvN2NmMzY1ZTM2ZDg4MzVjOGIyYWFkNDljZjNhMWQ4YWEvKi5tM3U4P3Nlc3Npb25JRD1kOWYxODI2MS03YmMxLTQ5MjMtYTAxMy1mOWE0MDU5NDM4OWIiLCJDb25kaXRpb24iOnsiRGF0ZUxlc3NUaGFuIjp7IkFXUzpFcG9jaFRpbWUiOjE1ODUwNDgwOTl9fX1dfQ__&Signature=Pc--MI7YPBuyhL0aGx4Sjd8j3Bj7V6UBOSDvBul-nx19~eeon3aYgE37EXLjUzDYidGn9kdNiiLQkPAME1V1E67JXG1X5Sd16HxTZjKo0vD~yOxf0O2aUdbQdzpx6lplTYCz-uXH~qHLVsWDVJGFDKb0HYS6ywaOoiqnQ6ZUwpAj7C~xdDK1QNVNROf3qzdYKTkqf0PH~caAnnOXpywCxTbwg30CihQY3lloFmH~dOzWlcnhpxbg5V--Jmva1ksN28kfOqXRKv7WubMHxlGCJTRssLgv4RDIjusoXBAif4HhIKT5DJnd8~GxvuOJJX6XZvs2jQoFKBrv3tnsrCtO-g__&Key-Pair-Id=APKAIB5DGCGAQJ4GGIUQ&sessionID=d9f18261-7bc1-4923-a013-f9a40594389b
key     https://hls2.videos.sproutvideo.com/1c17b7f004cf656622755e966ed6e87d/7cf365e36d8835c8b2aad49cf3a1d8aa/video/1080.key?Policy=eyJTdGF0ZW1lbnQiOlt7IlJlc291cmNlIjoiaHR0cHM6Ly9obHMyLnZpZGVvcy5zcHJvdXR2aWRlby5jb20vMWMxN2I3ZjAwNGNmNjU2NjIyNzU1ZTk2NmVkNmU4N2QvN2NmMzY1ZTM2ZDg4MzVjOGIyYWFkNDljZjNhMWQ4YWEvKi5rZXk~c2Vzc2lvbklEPWQ5ZjE4MjYxLTdiYzEtNDkyMy1hMDEzLWY5YTQwNTk0Mzg5YiIsIkNvbmRpdGlvbiI6eyJEYXRlTGVzc1RoYW4iOnsiQVdTOkVwb2NoVGltZSI6MTU4NTA0ODA5OX19fV19&Signature=V0FAW6VrORqrZgy0YawC5HhGLblQF0BRCGikyhZrXFfh0fmQ~sBg7dDpMz9kaaXBPdFuamj5jYvLmFzYh7jONkJWFbHEqlu6GbyZSWvVHt2s1m5BQ-ox1Cm8r~lU3RZJxzCelGcP0t8qJDF5naR3SGMVWSD1pItiDGMb0idi78aKhpbVRUc6Qbyn4ghdW65h2~hqAlDT2rNZLscFvQxL~A4hV9m0N7NN0UJE0Y4EQuKc4x2vIY27z48Pq5SCstVa2XhOM6lPOy9F6kjszVD2DZppWthQukfuv75JBpxBV3scvDz1wSRvx65mCTXKCQDN8Du3Dle3uEj6RJ01Zf8clg__&Key-Pair-Id=APKAIB5DGCGAQJ4GGIUQ&sessionID=d9f18261-7bc1-4923-a013-f9a40594389b
ts      https://hls2.videos.sproutvideo.com/1c17b7f004cf656622755e966ed6e87d/7cf365e36d8835c8b2aad49cf3a1d8aa/video/1080_00000.ts?Policy=eyJTdGF0ZW1lbnQiOlt7IlJlc291cmNlIjoiaHR0cHM6Ly9obHMyLnZpZGVvcy5zcHJvdXR2aWRlby5jb20vMWMxN2I3ZjAwNGNmNjU2NjIyNzU1ZTk2NmVkNmU4N2QvN2NmMzY1ZTM2ZDg4MzVjOGIyYWFkNDljZjNhMWQ4YWEvKi50cz9zZXNzaW9uSUQ9ZDlmMTgyNjEtN2JjMS00OTIzLWEwMTMtZjlhNDA1OTQzODliIiwiQ29uZGl0aW9uIjp7IkRhdGVMZXNzVGhhbiI6eyJBV1M6RXBvY2hUaW1lIjoxNTg1MDQ4MDk5fX19XX0_&Signature=Hvj8hAJWZJUYEXZiDwnefxGTbJB5PEFjXb6e3T9utCGIr02n3bsO12Gl44SUyPLslCJ9YRTfY4x0k2GOIxuoXyxQr-vXyvZ8tfSOVQkt74Y0JbBMjgtAPNzhrimTBAkYl~QUqnp5S5bXdvPtr4YKtX~pICzuL2HzyaWJsfkbvubKGqzE0NBh1SQj5T7rawq4xgH3MKk9NKy1yvJxAbXuWvCYS~EexCKze6PuwTP2IgFCc2kJohDgRC9gs2PE2yirhHaGd~DHBWpd1P5Fes9wLm45xIhvgJGPmY0ORGVS4oIFLB7dzoiG9YkAQBe-RuC2RJNBIau2RQxig21tfrYV1g__&Key-Pair-Id=APKAIB5DGCGAQJ4GGIUQ&sessionID=d9f18261-7bc1-4923-a013-f9a40594389b
"""

# resgatando a URL
print("Capturando URL")
# link_m3u8 = 'https://hls2.videos.sproutvideo.com/1c17b7f004cf656622755e966ed6e87d/7cf365e36d8835c8b2aad49cf3a1d8aa/video/1080.m3u8?Policy=eyJTdGF0ZW1lbnQiOlt7IlJlc291cmNlIjoiaHR0cHM6Ly9obHMyLnZpZGVvcy5zcHJvdXR2aWRlby5jb20vMWMxN2I3ZjAwNGNmNjU2NjIyNzU1ZTk2NmVkNmU4N2QvN2NmMzY1ZTM2ZDg4MzVjOGIyYWFkNDljZjNhMWQ4YWEvKi5tM3U4P3Nlc3Npb25JRD1kOWYxODI2MS03YmMxLTQ5MjMtYTAxMy1mOWE0MDU5NDM4OWIiLCJDb25kaXRpb24iOnsiRGF0ZUxlc3NUaGFuIjp7IkFXUzpFcG9jaFRpbWUiOjE1ODUwNDgwOTl9fX1dfQ__&Signature=Pc--MI7YPBuyhL0aGx4Sjd8j3Bj7V6UBOSDvBul-nx19~eeon3aYgE37EXLjUzDYidGn9kdNiiLQkPAME1V1E67JXG1X5Sd16HxTZjKo0vD~yOxf0O2aUdbQdzpx6lplTYCz-uXH~qHLVsWDVJGFDKb0HYS6ywaOoiqnQ6ZUwpAj7C~xdDK1QNVNROf3qzdYKTkqf0PH~caAnnOXpywCxTbwg30CihQY3lloFmH~dOzWlcnhpxbg5V--Jmva1ksN28kfOqXRKv7WubMHxlGCJTRssLgv4RDIjusoXBAif4HhIKT5DJnd8~GxvuOJJX6XZvs2jQoFKBrv3tnsrCtO-g__&Key-Pair-Id=APKAIB5DGCGAQJ4GGIUQ&sessionID=d9f18261-7bc1-4923-a013-f9a40594389b'
link_m3u8 = input('m3u8: ')
f = urlopen(link_m3u8)
response = f.read()
response = response.splitlines(True)

# pegando URL
url_end = link_m3u8.find('.m3u8?')
url_start = link_m3u8[:url_end].rfind('/') + 1
url = link_m3u8[:url_start]
# print(url)

# pegando a chave do TS
print("Capturando parâmetros do TS")
#link_ts = 'https://hls2.videos.sproutvideo.com/1c17b7f004cf656622755e966ed6e87d/7cf365e36d8835c8b2aad49cf3a1d8aa/video/1080_00000.ts?Policy=eyJTdGF0ZW1lbnQiOlt7IlJlc291cmNlIjoiaHR0cHM6Ly9obHMyLnZpZGVvcy5zcHJvdXR2aWRlby5jb20vMWMxN2I3ZjAwNGNmNjU2NjIyNzU1ZTk2NmVkNmU4N2QvN2NmMzY1ZTM2ZDg4MzVjOGIyYWFkNDljZjNhMWQ4YWEvKi50cz9zZXNzaW9uSUQ9ZDlmMTgyNjEtN2JjMS00OTIzLWEwMTMtZjlhNDA1OTQzODliIiwiQ29uZGl0aW9uIjp7IkRhdGVMZXNzVGhhbiI6eyJBV1M6RXBvY2hUaW1lIjoxNTg1MDQ4MDk5fX19XX0_&Signature=Hvj8hAJWZJUYEXZiDwnefxGTbJB5PEFjXb6e3T9utCGIr02n3bsO12Gl44SUyPLslCJ9YRTfY4x0k2GOIxuoXyxQr-vXyvZ8tfSOVQkt74Y0JbBMjgtAPNzhrimTBAkYl~QUqnp5S5bXdvPtr4YKtX~pICzuL2HzyaWJsfkbvubKGqzE0NBh1SQj5T7rawq4xgH3MKk9NKy1yvJxAbXuWvCYS~EexCKze6PuwTP2IgFCc2kJohDgRC9gs2PE2yirhHaGd~DHBWpd1P5Fes9wLm45xIhvgJGPmY0ORGVS4oIFLB7dzoiG9YkAQBe-RuC2RJNBIau2RQxig21tfrYV1g__&Key-Pair-Id=APKAIB5DGCGAQJ4GGIUQ&sessionID=d9f18261-7bc1-4923-a013-f9a40594389b'
link_ts = input('ts: ')
ts_start = link_ts.find('?') + 1
ts_key = link_ts[ts_start:]
# print(ts_key)


link_key = input('key: ')
number = ''
trocou_key = False


temp_filename = 'temp.m3u8'
f = open(temp_filename,'w')

# gerando m3u8 corrigido
for line in response:
    line = line.decode('utf-8').strip()

    if trocou_key == False:
        # verificando se é a linha da key
        end = line.find('.key')
        if end >= 0:
            start = line[:end].find('"') + 1
            old = line[start:end + 4]
            number = old[:old.find('.')]
            line = line.replace(old, link_key)
            trocou_key = True
    
    # depois que trocou a key
    if trocou_key == True:
        if line.find(number + '_') == 0:
            line = "{}{}?{}".format(url, line, ts_key)

    f.write(line + "\n")

f.close()

# rodando ffmpeg
saida_filename = input('Nome do arquivo: ')
if len(saida_filename.strip()) < 1:
    saida_filename = "{}.mp4".format(int(round(time.time() * 1000)))
elif saida_filename.find('.mp4') < 0:
    saida_filename = "{}.mp4".format(saida_filename)

os.system('title {}'.format(saida_filename))

comando = 'ffmpeg -y -protocol_whitelist "file,http,https,tcp,tls,crypto" -i "{}" -c copy -bsf:a aac_adtstoasc "{}"'.format(temp_filename, saida_filename)

print("Rodando o comando: {}".format(comando))
os.system(comando)
