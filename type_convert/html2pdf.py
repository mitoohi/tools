"""
将HTML文件转换成PDF
"""

import pdfkit

if __name__ == '__main__':
    pdfkit.from_url('http://www.baidu.com', 'out.pdf')
