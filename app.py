from flask import Flask, render_template
import json

"""
A example for creating a Table that is sortable by its header
"""

app = Flask(__name__,static_url_path='')
data = [{
  "来源": "bootstrdap-table",
  "标题": "11",
  "发布日期": "2020-04-17",
},
 {
  "来源": "fxcvbootstrap-tacvxczvble",
  "标题": "10",
  "发布日期": "2020-04-19",
}, {
  "来源": "adsfasdbasfootszxvtrap-table",
  "标题": "12",
  "发布日期": "2020-04-18",
}]
# other column settings -> http://bootstrap-table.wenzhixin.net.cn/documentation/#column-options
columns = [
  {
    "field": "来源", # which is the field's name of data key 
    "title": "来源", # display as the table header's name
    "sortable": True,
  },
  {
    "field": "标题",
    "title": "标题",
    "sortable": True,
  },
  {
    "field": "发布日期",
    "title": "发布日期",
    "sortable": True,
  }
]

#jdata=json.dumps(data)

@app.route('/')
def index():
    return render_template("table.html",
      data=data,
      columns=columns,
      title='Flask Bootstrap Table')


if __name__ == '__main__':
	#print jdata
  app.run(debug=True)