# phhgs
python-based coding language

# update log

## 2022.6.3
bug：
1. in []的优化问题：in []的误输问题，中括号内是否要包括冒号问题，in的value长久保存问题，in的value是否可以自动识别type问题
2. re正则数字问题：正则 或 是否可以连续问题，连续是否有优先问题，连续是否导致非贪婪失败问题，正则是否应该考虑正负号问题，[0-9]?还是[1-9]+[0-9]?

优化：
1. re正则数字问题
2. raise Error语句规范问题
3. pyautogui打包问题
4. def 名称规范性问题

## 2022.6.4
bug：
1. 二次set type会出现type和value对不上的问题：二次set type导致的二次set value失败问题，二次set type导致的输出问题，二次set type导致的不报错问题
2. in []的优化问题：中括号内是否要包括冒号问题，in的value长久保存问题，in的value是否可以自动识别type问题
3. re正则数字问题：正则 或 是否可以连续问题，连续是否有优先问题，连续是否导致非贪婪失败问题，正则是否应该考虑正负号问题，[0-9]?还是[1-9]+[0-9]?

优化：
1. in []的误输问题
2. raise Error语句规范问题
3. windows和mac的ctrl兼容问题
4. pyqt5打包问题

