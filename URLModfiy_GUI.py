# coding: utf-8
"""
作者: CreateNULL
版本: v1.0
日期: 2024年9月30日
"""
from PySide6.QtWidgets import QComboBox
import sys
import json
from PySide6.QtWidgets import (
    QApplication, QWidget, QVBoxLayout, QLabel, QTextEdit, QPushButton,
    QTableWidget, QTableWidgetItem, QScrollArea, QHeaderView,
    QGroupBox, QHBoxLayout, QMenu, QGridLayout, QCheckBox
)
from PySide6.QtWidgets import QFileDialog
from PySide6.QtGui import QAction
from PySide6.QtCore import Qt
from modify.urlmodify import ModifyURL
from themes.themes import Pixel_Graph, Fresh_Green
from PySide6.QtWidgets import QRadioButton, QVBoxLayout


# 实例化处理的类
urlmodify = ModifyURL()

class URLProcessorApp(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("URL 处理器 - 版本 1.0  By: CreateNULL")
        self.setGeometry(100, 100, 900, 600)  # 增加窗口宽度
        self.setStyleSheet(Pixel_Graph)

        # 主布局
        main_layout = QHBoxLayout()

        # 左侧布局：输入区域
        left_layout = QVBoxLayout()

        # 输入区域
        self.url_input_label = QLabel("待处理的URL文本")
        self.url_input_area = QTextEdit()
        self.url_input_area.setPlaceholderText("请输入URL，每行一个")

        # 滚动区域
        self.scroll_area = QScrollArea()
        self.scroll_area.setWidgetResizable(True)
        self.scroll_area.setWidget(self.url_input_area)

        # 输出区域
        self.output_label = QLabel("结果输出:")
        self.output_table = QTableWidget()

        # 添加输入和输出组件到左侧布局
        left_layout.addWidget(self.url_input_label)
        left_layout.addWidget(self.scroll_area)
        left_layout.addWidget(self.output_label)
        left_layout.addWidget(self.output_table)


        # 右侧布局：功能按钮
        button_layout = QVBoxLayout()
        self.function_group = QGroupBox("功能按钮")
        button_grid_layout = QGridLayout()  # 使用网格布局

        self.process_button = QPushButton("URL分类")
        self.process_button.clicked.connect(self.filter_url)

        # 其他功能按钮示例
        self.function_button1 = QPushButton("提取URL信息")
        self.function_button1.clicked.connect(self.extract_infos)
        self.function_button2 = QPushButton("添加端口")
        self.function_button2.clicked.connect(self.add_port)
        self.function_button3 = QPushButton("添加协议")
        self.function_button3.clicked.connect(self.add_protocol)
        self.function_button4 = QPushButton("去除空行、空格")
        self.function_button4.clicked.connect(self.remove_blank_space)
        self.function_button5 = QPushButton("去除两边的引号")
        self.function_button5.clicked.connect(self.remove_quotation_marks)
        self.download_button = QPushButton("下载结果为 XLSX")
        self.download_button.clicked.connect(self.download_results)
        # ----------------------------- 单选 --------------------------
        # 新增复选框以控制是否过滤空行
        self.filter_empty_lines_label = QLabel("过滤结果中的空行:")
        self.filter_empty_lines_check = QCheckBox("是")

        # 将复选框添加到左侧布局中
        left_layout.addWidget(self.filter_empty_lines_label)
        left_layout.addWidget(self.filter_empty_lines_check)

        # ---------------------------------- 去重 ---------------------------
        # 添加去重复选框
        self.deduplicate_label = QLabel("去重结果:")
        self.deduplicate_check = QCheckBox("是")

        # 将去重复选框添加到左侧布局中
        left_layout.addWidget(self.deduplicate_label)
        left_layout.addWidget(self.deduplicate_check)
        # ---------------------------------- 下拉 ---------------------------
        # 在左侧布局中添加下拉框选择原始顺序
        self.order_label = QLabel("选择URL处理顺序:")
        self.order_combobox = QComboBox()
        self.order_combobox.addItems(["URL分类-先分类，再输出到对应列", "URL分类-单个，按照列来分类输出",])

        # 设置下拉框的样式
        self.order_combobox.setStyleSheet("padding: 5px; font-size: 14px;")

        # 添加到左侧布局
        left_layout.addWidget(self.order_label)
        left_layout.addWidget(self.order_combobox)

        # 设置按钮样式
        for button in [self.process_button, self.function_button1, self.function_button2, self.function_button3, self.function_button4, self.function_button5, self.download_button]:
            button.setStyleSheet("padding: 10px; font-size: 14px;")

        # 将按钮添加到网格布局（每行两个按钮）
        button_grid_layout.addWidget(self.process_button, 0, 0)
        button_grid_layout.addWidget(self.function_button1, 0, 1)
        button_grid_layout.addWidget(self.function_button2, 1, 0)
        button_grid_layout.addWidget(self.function_button3, 1, 1)
        button_grid_layout.addWidget(self.function_button4, 2, 0)
        button_grid_layout.addWidget(self.function_button5, 2, 1)
        button_grid_layout.addWidget(self.download_button, 3, 0)

        # 添加按钮网格布局到主按钮布局
        button_layout.addLayout(button_grid_layout)

        # 将按钮布局设置到组框
        self.function_group.setLayout(button_layout)

        # 设置右侧组框的宽度
        self.function_group.setFixedWidth(300)  # 设置右侧功能框宽度

        # 将左右布局添加到主布局
        main_layout.addLayout(left_layout)
        main_layout.addWidget(self.function_group)

        self.setLayout(main_layout)

        # 右键菜单支持复制功能
        self.output_table.setContextMenuPolicy(Qt.CustomContextMenu)
        self.output_table.customContextMenuRequested.connect(self.show_context_menu)

    def show_context_menu(self, pos):
        menu = QMenu()
        copy_action = QAction("复制", self)
        copy_action.triggered.connect(self.copy_selection)
        menu.addAction(copy_action)
        menu.exec(self.output_table.mapToGlobal(pos))

    def copy_selection(self):
        selected_range = self.output_table.selectedRanges()[0]
        rows = selected_range.rowCount()
        cols = selected_range.columnCount()
        data = []

        for row in range(rows):
            row_data = []
            for col in range(cols):
                item = self.output_table.item(selected_range.topRow() + row, selected_range.leftColumn() + col)
                row_data.append(item.text() if item else "")
            data.append("\t".join(row_data))

        clipboard = QApplication.clipboard()
        clipboard.setText("\n".join(data))

    def filter_url(self, ):
        urls = self.url_input_area.toPlainText()
        self.output_table.clear()

        if not urls:
            return

        urls = urls.split("\n")
        urls = [_['derivative'] for _ in urlmodify.remove_blank_space(urls=urls, remove_blank_line=False)]

        # 根据下拉框选择设置 original_order
        original_order = self.order_combobox.currentIndex() == 1  # 如果选择 "原始顺序"，则为 True，否则为 False

        # 判断是否需要再次过滤空行
        filter_empty_lines = self.filter_empty_lines_check.isChecked()

        # 判断是否需要去重
        deduplicate = self.deduplicate_check.isChecked()

        result = urlmodify.filter(urls=urls, original_order=original_order, no_empty=filter_empty_lines, deduplicate=deduplicate)

        titles = ['域名-严格模式', '域名-宽松模式', 'IP-严格模式', 'IP-宽松模式', 'URL', '其他字符']
        self.output_table.setColumnCount(len(titles))
        self.output_table.setHorizontalHeaderLabels(titles)

        # 填充数据
        row_count = max(len(result), max([max(len(item) for item in _.values()) for _ in result]))
        self.output_table.setRowCount(row_count)

        if original_order:
            for row in range(row_count):
                row_data = result[row]
                for col, col_data in enumerate(row_data.values()):
                    self.output_table.setItem(row, col, QTableWidgetItem(''.join(col_data)))
        else:
            if result:
                data = result[0]  # 获取第一个字典
                for col, col_key in enumerate(data):
                    col_data = data[col_key]
                    for row in range(len(col_data)):
                        row_data = col_data[row] if row < len(col_data) else ""
                        self.output_table.setItem(row, col, QTableWidgetItem(row_data))

        # 自适应列宽（可选）
        self.output_table.resizeColumnsToContents()

    def extract_infos(self):
        urls = self.url_input_area.toPlainText()
        self.output_table.clear()  # 清空表格内容

        if not urls:
            return

        urls = urls.split("\n")
        # 去除空格, 不去除空行
        urls = [_['derivative'] for _ in urlmodify.remove_blank_space(urls=urls, remove_blank_line=False)]

        # 判断是否需要再次过滤空行
        filter_empty_lines = self.filter_empty_lines_check.isChecked()

        # 判断是否需要去重
        deduplicate = self.deduplicate_check.isChecked()

        # 处理提取信息
        result = urlmodify.extract_infos(urls=urls, no_empty=filter_empty_lines, deduplicate=deduplicate)

        # 设置标题
        titles = ['原始URL', '协议', '域名', 'IP', '端口', '路径', '参数', '非域名/非IP']
        self.output_table.setColumnCount(len(titles))
        self.output_table.setHorizontalHeaderLabels(titles)

        # 设置行数
        row_count = len(result)
        self.output_table.setRowCount(row_count)

        # 填充数据
        for row, data in enumerate(result):
            self.output_table.setItem(row, 0, QTableWidgetItem(data.get('original', '')))
            self.output_table.setItem(row, 1, QTableWidgetItem(data.get('protocol', '')))
            self.output_table.setItem(row, 2, QTableWidgetItem(data.get('domain', '')))
            self.output_table.setItem(row, 3, QTableWidgetItem(data.get('ip', '')))
            self.output_table.setItem(row, 4, QTableWidgetItem(data.get('port', '')))
            self.output_table.setItem(row, 5, QTableWidgetItem(data.get('path', '')))

            # 将参数字典转换为字符串
            params = data.get('params', {})

            params_str = json.dumps(params, ensure_ascii=False) if isinstance(params, dict) else ''
            self.output_table.setItem(row, 6, QTableWidgetItem(params_str))

            self.output_table.setItem(row, 7, QTableWidgetItem(str(data.get('is_other', ''))))

        # 自适应列宽（可选）
        self.output_table.resizeColumnsToContents()

    def add_port(self):
        urls = self.url_input_area.toPlainText()
        self.output_table.clear()  # 清空表格内容

        if not urls:
            return

        urls = urls.split("\n")

        # 去除空格, 不去除空行
        urls = [_['derivative'] for _ in urlmodify.remove_blank_space(urls=urls, remove_blank_line=False)]

        # 判断是否需要再次过滤空行
        filter_empty_lines = self.filter_empty_lines_check.isChecked()

        # 判断是否需要去重
        deduplicate = self.deduplicate_check.isChecked()

        # 添加端口
        result = urlmodify.add_port(urls=urls, no_empty=filter_empty_lines, deduplicate=deduplicate)

        if not result:
            return

        # 设置标题
        titles = ['原始URL', '处理后的URL（添加端口）']
        self.output_table.setColumnCount(len(titles))
        self.output_table.setHorizontalHeaderLabels(titles)

        # 设置行数
        row_count = len(result)
        self.output_table.setRowCount(row_count)

        # 填充数据
        for row, data in enumerate(result):
            # 将 'original' 和 'derivative' 数据填充到表格中
            self.output_table.setItem(row, 0, QTableWidgetItem(data['original']))
            self.output_table.setItem(row, 1, QTableWidgetItem(data['derivative']))

        # 自适应列宽（可选）
        self.output_table.resizeColumnsToContents()

    def add_protocol(self):
        urls = self.url_input_area.toPlainText()  # 获取用户输入的 URL 列表
        self.output_table.clear()  # 清空表格内容

        if not urls:
            return

        urls = urls.split("\n")  # 按换行符拆分输入的 URL

        # 去除空格, 不去除空行
        urls = [_['derivative'] for _ in urlmodify.remove_blank_space(urls=urls, remove_blank_line=False)]

        # 判断是否需要再次过滤空行
        filter_empty_lines = self.filter_empty_lines_check.isChecked()

        # 判断是否需要去重
        deduplicate = self.deduplicate_check.isChecked()

        # 添加协议
        result = urlmodify.add_protocol(urls=urls, no_empty=filter_empty_lines, deduplicate=deduplicate)  # 调用处理方法添加协议

        if not result:
            return

        # 设置标题
        titles = ['原始URL', '处理后URL（添加协议）']
        self.output_table.setColumnCount(len(titles))
        self.output_table.setHorizontalHeaderLabels(titles)

        # 设置行数
        row_count = len(result)
        self.output_table.setRowCount(row_count)

        # 填充数据
        for row, data in enumerate(result):
            # 将 'original' 和 'derivative' 数据填充到表格中
            self.output_table.setItem(row, 0, QTableWidgetItem(data['original']))  # 原始URL
            self.output_table.setItem(row, 1, QTableWidgetItem(data['derivative']))  # 添加协议后的URL

        # 自适应列宽（可选）
        self.output_table.resizeColumnsToContents()

    def remove_quotation_marks(self):
        urls = self.url_input_area.toPlainText()  # 获取用户输入的 URL 列表
        self.output_table.clear()  # 清空表格内容

        if not urls:
            return

        # 判断是否需要再次过滤空行
        filter_empty_lines = self.filter_empty_lines_check.isChecked()
        # 判断是否需要去重
        deduplicate = self.deduplicate_check.isChecked()

        urls = urls.split("\n")  # 按换行符拆分输入的 URL
        result = urlmodify.remove_quotation_marks(urls=urls, no_empty=filter_empty_lines, deduplicate=deduplicate)  # 调用处理方法去除引号

        if not result:
            return

        # 设置标题
        titles = ['原始URL', '去除引号后的URL']
        self.output_table.setColumnCount(len(titles))
        self.output_table.setHorizontalHeaderLabels(titles)

        # 设置行数
        row_count = len(result)
        self.output_table.setRowCount(row_count)

        # 填充数据
        for row, data in enumerate(result):
            # 将 'original' 和 'derivative' 数据填充到表格中
            self.output_table.setItem(row, 0, QTableWidgetItem(data['original']))  # 原始URL
            self.output_table.setItem(row, 1, QTableWidgetItem(data['derivative']))  # 去除引号后的URL

        # 自适应列宽（可选）
        self.output_table.resizeColumnsToContents()

    def remove_blank_space(self):
        urls = self.url_input_area.toPlainText()  # 获取用户输入的 URL 列表
        self.output_table.clear()  # 清空表格内容

        if not urls:
            return

        urls = urls.split("\n")  # 按换行符拆分输入的 URL

        # 判断是否需要去重
        deduplicate = self.deduplicate_check.isChecked()

        result = urlmodify.remove_blank_space(urls=urls, deduplicate=deduplicate)  # 调用处理方法删除空行和空格

        if not result:
            return

        # 设置标题
        titles = ['原始URL', '删除空行和空格后的URL']
        self.output_table.setColumnCount(len(titles))
        self.output_table.setHorizontalHeaderLabels(titles)

        # 设置行数
        row_count = len(result)
        self.output_table.setRowCount(row_count)

        # 填充数据
        for row, data in enumerate(result):
            # 将 'original' 和 'derivative' 数据填充到表格中
            self.output_table.setItem(row, 0, QTableWidgetItem(data['original']))  # 原始URL
            self.output_table.setItem(row, 1, QTableWidgetItem(data['derivative']))  # 删除空行和空格后的URL

        # 自适应列宽（可选）
        self.output_table.resizeColumnsToContents()

    def download_results(self):
        # 获取输出表格的数据
        row_count = self.output_table.rowCount()
        column_count = self.output_table.columnCount()

        if row_count == 0 or column_count == 0:
            return  # 如果没有数据则不执行

        data = []
        headers = []

        # 获取表头
        for col in range(column_count):
            item = self.output_table.horizontalHeaderItem(col)
            headers.append(item.text() if item else '')

        data.append(headers)  # 将表头添加到数据中

        # 获取表格数据
        for row in range(row_count):
            row_data = []
            for col in range(column_count):
                item = self.output_table.item(row, col)
                row_data.append(item.text() if item else '')
            data.append(row_data)

        # 使用 openpyxl 创建 Excel 文件
        from openpyxl import Workbook
        workbook = Workbook()
        sheet = workbook.active

        for r in range(len(data)):
            for c in range(len(data[r])):
                sheet.cell(row=r+1, column=c+1, value=data[r][c])

        # 保存文件
        filename, _ = QFileDialog.getSaveFileName(self, "保存文件", "", "Excel 文件 (*.xlsx);;所有文件 (*)")
        if filename:
            workbook.save(filename)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = URLProcessorApp()
    window.show()
    sys.exit(app.exec())