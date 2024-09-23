# Configuration file for the Sphinx documentation builder.
#
# For the full list of built-in configuration values, see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Project information -----------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#project-information

project = "Chenxi's Blog"
copyright = '2024, Chenxi'
author = 'Chenxi'
release = '1.0'

# -- General configuration ---------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#general-configuration

extensions = []

templates_path = ['_templates']
exclude_patterns = []

language = 'zh_CN'



# -- Options for HTML output -------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#options-for-html-output

#html_theme = 'alabaster'
html_theme = 'default'
# html主题的相关设置
html_theme_options = {"collapse_navigation": False, "navigation_depth": 6}
html_static_path = ['_static']

# 在页面底部显示上一次更新于某某时间
html_last_updated_fmt = "%Y-%m-%d %H:%M:%S"

# 图形、表格、代码块如果有标题，自动添加编号, 默认为False
numfig = True

# 默认的源代码高亮的语言，默认值为default， 类似于python3
highlight_language = 'default'



