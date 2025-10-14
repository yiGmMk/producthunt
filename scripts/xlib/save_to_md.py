from xlib.time import get_time_now
from xlib.gpt import call_openai


extra_keywork = """
Role: 关键词提取专家
Profile
language: English
description: A specialized AI expert in extracting the most relevant keywords from text documents.

validation: Check that the output is a comma-separated string of English keywords.Don't contain any special characters,like #,if so,remove them.
constraints: The number of keywords must not exceed 8.
error_handling: If the analysis yields fewer than 8 keywords, return all identified keywords.

Example:
Title: Short Text Example
Format Type: text
Description: Keywords extracted from a short paragraph.
Example Content: |
natural language processing, keyword extraction, text analysis, semantic analysis, NLP techniques, information retrieval

Initialization
As a Keyword Extraction Expert, you must adhere to the above Rules, follow the Workflows diligently, and output results according to the defined output format.
仅返回3个关键词,不要其他任何文字,不要携带特殊字符如冒号,括号等
"""


class SaveToMD:
    def __init__(self, workdir):
        self.workdir = workdir

    def save(self, filename, content, imageurl):
        keywords = ""
        try:
            keywords = call_openai(extra_keywork, content)
        except Exception as e:
            print("Error in generating markdown content")
        keywords = keywords.replace("```", "")
        if len(keywords.split(",")) > 3:
            keywords = ",".join(keywords.split(",")[:3])
        # 定义 YAML 头部信息和正文内容
        yaml_header = {
            "title": filename,
            "date": get_time_now(),
            "draft": False,
            "image": imageurl,
            "tags": f"['github',{keywords}]",
            "categories": ["github"],
        }

        # 将字典和正文内容合并为一个字符串
        markdown_text = "---\n"
        for key, value in yaml_header.items():
            markdown_text += f"{key}: {value}\n"
        markdown_text += "---\n\n"
        # Remove relative image paths
        import re

        content = re.sub(r"!\[.*?\]\(\.\/.*?\)|<img.*?src=\"\/(.*?)\".*?>", "", content)
        markdown_text += content

        # 将字符串写入 Markdown 文件
        full_filename = self.workdir + "/" + "github-" + filename + ".md"
        with open(full_filename, "w") as f:
            f.write(markdown_text)
