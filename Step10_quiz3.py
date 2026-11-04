

from jinja2 import Template

# DB에서 읽어온 글 목록
posts:list = [
    {"id":1, "writer":"작성자1", "title":"제목1"},
    {"id":2, "writer":"작성자2", "title":"제목2"},
    {"id":3, "writer":"작성자3", "title":"제목3"}
]

sample =''' 글목록 입니다
   {%- for p in posts %}
    - 글번호: {{p.id}} 작성자: {{p.writer}} 제목: {{p.title}}
    {%- endfor %}
'''



t = Template(sample)
result: str =t.render(posts=posts)

print(result)
