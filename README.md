# Search_law
The project major provide a searching api of laws. Users can input a searching url and the sever return a result about laws.
# Function
## 1 requestAPI
### __input:__
```
http://127.0.0.1:5000/search/api?info=拐卖妇女
```
### __output__
```
{
  "task": [
    {
      "1": [
        "\u3010\u6536\u4e70\u88ab\u62d0\u5356\u7684\u5987\u5973\u3001\u513f\u7ae5\u7f6a\uff1b\u5f3a\u5978....",
        "\u3010\u6536\u4e70\u88ab\u62d0\u5356\u7684\u5987\u5973\u3001\u513f\u7ae5\u7f6a\uff1b\u5f3a\u5978\u7f6a\uff1b\u975e\u6cd5\u62d8\u7981\u7f6a\uff1b\u6545\u610f\u4f24\u5bb3\u7f6a\uff1b\u4fae\u8fb1\u7f6a\uff1b\u62d0\u5356\u5987\u5973\u3001\u513f\u7ae5\u7f6a\u3011\u6536\u4e70\u88ab\u62d0\u5356\u7684\u5987\u5973\u3001\u513f\u7ae5\u7684\uff0c\u5904\u4e09\u5e74\u4ee5\u4e0b\u6709\u671f\u5f92\u5211\u3001\u62d8\u5f79\u6216\u8005\u7ba1\u5236\u3002;\r\n\t\u6536\u4e70\u88ab\u62d0\u5356\u7684\u5987\u5973\uff0c\u5f3a\u884c\u4e0e\u5176\u53d1\u751f\u6027\u5173\u7cfb\u7684\uff0c\u4f9d\u7167\u672c\u6cd5\u7b2c\u4e8c\u767e\u4e09\u5341\u516d\u6761\u7684\u89c4\u5b9a\u5b9a\u7f6a\u5904\u7f5a\u3002;\r\n\t\u6536\u4e70\u88ab\u62d0\u5356\u7684\u5987\u5973\u3001\u513f\u7ae5\uff0c\u975e\u6cd5\u5265\u593a\u3001\u9650\u5236\u5176\u4eba\u8eab\u81ea\u7531\u6216\u8005\u6709\u4f24\u5bb3\u3001\u4fae\u8fb1\u7b49\u72af\u7f6a\u884c\u4e3a\u7684\uff0c\u4f9d\u7167\u672c\u6cd5\u7684\u6709\u5173\u89c4\u5b9a\u5b9a\u7f6a\u5904\u7f5a\u3002;\r\n\t\u6536\u4e70\u88ab\u62d0\u5356\u7684\u5987\u5973\u3001\u513f\u7ae5\uff0c\u5e76\u6709\u7b2c\u4e8c\u6b3e\u3001\u7b2c\u4e09\u6b3e\u89c4\u5b9a\u7684\u72af\u7f6a\u884c\u4e3a\u7684\uff0c\u4f9d\u7167\u6570\u7f6a\u5e76\u7f5a\u7684\u89c4\u5b9a\u5904\u7f5a\u3002;\r\n\t\u6536\u4e70\u88ab\u62d0\u5356\u7684\u5987\u5973\u3001\u513f\u7ae5\u53c8\u51fa\u5356\u7684\uff0c\u4f9d\u7167\u672c\u6cd5\u7b2c\u4e8c\u767e\u56db\u5341\u6761\u7684\u89c4\u5b9a\u5b9a\u7f6a\u5904\u7f5a\u3002;\r\n\t\u6536\u4e70\u88ab\u62d0\u5356\u7684\u5987\u5973\u3001\u513f\u7ae5\uff0c\u5bf9\u88ab\u4e70\u513f\u7ae5\u6ca1\u6709\u8650\u5f85\u884c\u4e3a\uff0c\u4e0d\u963b\u788d\u5bf9\u5176\u8fdb\u884c\u89e3\u6551\u7684\uff0c\u53ef\u4ee5\u4ece\u8f7b\u5904\u7f5a\uff1b\u6309\u7167\u88ab\u4e70\u5987\u5973\u7684\u610f\u613f\uff0c\u4e0d\u963b\u788d\u5176\u8fd4\u56de\u539f\u5c45\u4f4f\u5730\u7684\uff0c\u53ef\u4ee5\u4ece\u8f7b\u6216\u8005\u51cf\u8f7b\u5904\u7f5a\u3002"
      ]
    },
    {
      "2": [
        "\u3010\u62d0\u5356\u5987\u5973\u3001\u513f\u7ae5\u7f6a\u3011\u62d0\u5356\u5987\u5973\u3001\u513f....",
        "\u3010\u62d0\u5356\u5987\u5973\u3001\u513f\u7ae5\u7f6a\u3011\u62d0\u5356\u5987\u5973\u3001\u513f\u7ae5\u7684\uff0c\u5904\u4e94\u5e74\u4ee5\u4e0a\u5341\u5e74\u4ee5\u4e0b\u6709\u671f\u5f92\u5211\uff0c\u5e76\u5904\u7f5a\u91d1\uff1b\u6709\u4e0b\u5217\u60c5\u5f62\u4e4b\u4e00\u7684\uff0c\u5904\u5341\u5e74\u4ee5\u4e0a\u6709\u671f\u5f92\u5211\u6216\u8005\u65e0\u671f\u5f92\u5211\uff0c\u5e76\u5904\u7f5a\u91d1\u6216\u8005\u6ca1\u6536\u8d22\u4ea7\uff1b\u60c5\u8282\u7279\u522b\u4e25\u91cd\u7684\uff0c\u5904\u6b7b\u5211\uff0c\u5e76\u5904\u6ca1\u6536\u8d22\u4ea7\uff1a;\r\n\t(\u4e00)\u62d0\u5356\u5987\u5973\u3001\u513f\u7ae5\u96c6\u56e2\u7684\u9996\u8981\u5206\u5b50\uff1b;\r\n\t(\u4e8c)\u62d0\u5356\u5987\u5973\u3001\u513f\u7ae5\u4e09\u4eba\u4ee5\u4e0a\u7684\uff1b;\r\n\t(\u4e09)\u5978\u6deb\u88ab\u62d0\u5356\u7684\u5987\u5973\u7684\uff1b;\r\n\t(\u56db)\u8bf1\u9a97\u3001\u5f3a\u8feb\u88ab\u62d0\u5356\u7684\u5987\u5973\u5356\u6deb\u6216\u8005\u5c06\u88ab\u62d0\u5356\u7684\u5987\u5973\u5356\u7ed9\u4ed6\u4eba\u8feb\u4f7f\u5176\u5356\u6deb\u7684\uff1b;\r\n\t(\u4e94)\u4ee5\u51fa\u5356\u4e3a\u76ee\u7684\uff0c\u4f7f\u7528\u66b4\u529b\u3001\u80c1\u8feb\u6216\u8005\u9ebb\u9189\u65b9\u6cd5\u7ed1\u67b6\u5987\u5973\u3001\u513f\u7ae5\u7684\uff1b;\r\n\t(\u516d)\u4ee5\u51fa\u5356\u4e3a\u76ee\u7684\uff0c\u5077\u76d7\u5a74\u5e7c\u513f\u7684\uff1b;\r\n\t(\u4e03)\u9020\u6210\u88ab\u62d0\u5356\u7684\u5987\u5973\u3001\u513f\u7ae5\u6216\u8005\u5176\u4eb2\u5c5e\u91cd\u4f24\u3001\u6b7b\u4ea1\u6216\u8005\u5176\u4ed6\u4e25\u91cd\u540e\u679c\u7684\uff1b;\r\n\t(\u516b)\u5c06\u5987\u5973\u3001\u513f\u7ae5\u5356\u5f80\u5883\u5916\u7684\u3002;\r\n\t\u62d0\u5356\u5987\u5973\u3001\u513f\u7ae5\u662f\u6307\u4ee5\u51fa\u5356\u4e3a\u76ee\u7684\uff0c\u6709\u62d0\u9a97\u3001\u7ed1\u67b6\u3001\u6536\u4e70\u3001\u8d29\u5356\u3001\u63a5\u9001\u3001\u4e2d\u8f6c\u5987\u5973\u3001\u513f\u7ae5\u7684\u884c\u4e3a\u4e4b\u4e00\u7684\u3002"
      ]
    }
  ]
}
```
### The data Structure
```
{task: {the order number: [sketch of laws, complete laws],
	{the order number: [sketch of laws, complete laws],
	....
}
```
## 2 SearchUI

<img src="/search_law_file/static/search_page.jpg" width="80%" height="28%" />

<img src="/search_law_file/static/law_page.png" width="80%" height="28%" />