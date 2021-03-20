from pathlib import Path
import requests

problems = []
classes = ['algorithms', 'shell', 'database', 'concurrency']

for cls in classes:
    LEETCODE_PROBLEMS = f"https://leetcode.com/api/problems/{cls}/"

    req = requests.get(LEETCODE_PROBLEMS)
    problems += req.json()['stat_status_pairs']

keys = ['frontend_question_id', 'question__title']

v_id_title = [[p['stat'][k] for k in keys] for p in problems]
max_id = max(p[0] for p in v_id_title)

files = list(Path("leetcode").glob("leetcode_*md"))


for f in files:
    try:
        _, pid = f.name.split('_')
        pid = int(pid.rstrip(".md"))
        if pid <= max_id:
            continue
        with open(f, 'r') as oldf:
            contents = oldf.readlines()
        if contents[0] != '---\n':
            continue
        candidates = [[nid, title]
                      for nid, title in v_id_title if title.strip() in contents[1]]
        if len(candidates) != 1:
            continue
        nid, title = candidates[0]
        prob = f"{nid}. {title}"
        # change title
        contents[1] = f"title: {prob}\n"
        # change or add title line
        title_line = [i for i in range(
            len(contents)) if contents[i].startswith("# ")]
        new_title = f"# {prob}\n"
        if title_line:
            contents[title_line[0]] = new_title
        else:
            contents.insert(4, new_title)

        fname = f"leetcode/leetcode_{nid}.md"
        with open(fname, 'w') as newf:
            newf.writelines(contents)
        f.unlink()
    except Exception as e:
        print(f, e)
        pass
