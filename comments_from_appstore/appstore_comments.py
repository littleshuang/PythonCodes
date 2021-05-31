#!/bin/python3
# -*- coding: UTF-8 -*-
import os
import shutil
import urllib.request
import json
import logging
import xlsxwriter


class Comment(object):
    def __init__(self):
        self.author = ""
        self.title = ""
        self.rate = 0
        self.content = ""


def write_sheet(workbook, sheet_name, comments):
    if not workbook or not sheet_name or not comments:
        print("One of the parameters is None")
        return

    format = workbook.add_format()
    format.set_border(1)
    format.set_border(1)
    format_title = workbook.add_format()
    format_title.set_border(1)
    format_title.set_bg_color('#cccccc')
    format_title.set_align('center')
    format_title.set_bold()

    sheet = workbook.add_worksheet(sheet_name)
    sheet_title = ['Author', 'Title', 'Rate', 'Content']
    sheet.write_row('A1', sheet_title, format_title)

    print('Author: ' + comments[0].author + "\tTitle: " + comments[0].title + '\tRate: ' + comments[0].rate +
          '\tContent: ' + comments[0].content)

    for row in range(len(comments)):
        sheet.write(row+1, 0, comments[row].author, format)
        sheet.write(row+1, 1, comments[row].title, format)
        sheet.write(row+1, 2, comments[row].rate, format)
        sheet.write(row+1, 3, comments[row].content, format)


def write_workbook(app_comments, output_file):
    if not app_comments or not output_file:
        print("app_comments or output_file is None or empty")
        return

    workbook = xlsxwriter.Workbook(output_file)
    for name, comments in app_comments.items():
        write_sheet(workbook, name, comments)
    workbook.close()


def write_workbook_app(name, comments):
    if not name or not comments:
        print("name or comments is None or empty")
        return

    workbook = xlsxwriter.Workbook(name + '.xlsx')
    write_sheet(workbook, name, comments)
    workbook.close()


def read_comments_from_appstore(pagenum, appid):
    """
    Read the comments related to the appid from appstore.
    :param pagenum: the number of comment pages to read
    :param appid: which app's comment to read
    :return: the comment list
    """
    comment_list = []
    if not pagenum or not appid:
        print("One of the parameters is None")
        return comment_list

    page = 0
    while page < pagenum:
        page = page + 1
        print("read page: %d" % page)
        url = "https://itunes.apple.com/rss/customerreviews/page=%s/id=%s/sortby=mostrecent/json?l=en&&cc=cn" % (page, appid)
        response = urllib.request.urlopen(url)
        json_response = json.loads(response.read().decode())

        if 'entry' in json_response['feed']:
            contents = json_response['feed']['entry']
            # get all comments in this page
            for content in contents:
                comment = Comment()
                comment.author = content['author']['name']['label']
                comment.title = content['title']['label']
                comment.rate = content['im:rating']['label']
                comment.content = content['content']['label']
                comment_list.append(comment)
        else:
            break
    return comment_list


def read_all_comments(app_dict, pagenum):
    """
    Read the first pagenum page comments related to the app in app_dict.
    :param app_dict: {appName: appID}
    :param pagenum: the number of comment pages to read
    :return: {appName: comments}
    """
    app_comment_dict = {}
    if not app_dict or not pagenum:
        print("One of the parameters is None")
        return app_comment_dict

    if pagenum < 0:
        print("Page num should bigger than zero")
        return app_comment_dict

    for name, appid in app_dict.items():
        logging.info('Begin read %s %s' % (name, appid))
        print('Begin read %s %s' % (name, appid))
        comments = read_comments_from_appstore(pagenum, appid)
        if len(comments) > 0:
            app_comment_dict[name] = comments
    return app_comment_dict


def main():
    # appID_dict = {"我的物品": 1423132930, "Find it": 1439383955, "Quick": 1360613074,
    #               "有物-我的东西": 1504418690, "Itemio": 1472869127, "在那儿": 1084364767,
    #               "东西在那儿": 1317482460, "红线": 1447884996, "简衣橱": 1344153452,
    #               "口袋存量": 1440455104, "收哪儿": 1131007446, "收纳盒子": 1049768353,
    #               "整理猫儿": 1341593455, "Stocked": 1206725227, "明查的物品收纳": 1499955805,
    #               "where": 1273937491}
    appID_dict = {"我的物品": 1423132930}

    # The result path
    cur_dir = os.getcwd()
    result_dir = os.path.join(cur_dir, 'result')
    if os.path.exists(result_dir):
        shutil.rmtree(result_dir)
    os.mkdir(result_dir)

    all_comments = read_all_comments(appID_dict, 10)
    print('Begin write comments to the excel file.')
    write_workbook(all_comments, os.path.join(result_dir, 'comments.xlsx'))


if __name__ == '__main__':
    main()
