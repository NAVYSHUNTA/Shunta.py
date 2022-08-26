# Python 用語集
Pythonの重要用語を忘れがちなのでここにメモする。

- **イテレータ**：イテレータは、求められるたびに要素をひとつずつ返し、データがなくなるとデータの代わりに StopIteration 例外を返すオブジェクトのこと。
なお、iter() 関数を用いれば、range, listなどからイテレータを生成することができる。

- **イテラブル**：イテレータに変換可能なオブジェクトのこと。
Ex:list, tuple, str, range, dict, set, file object

- **ミュータブル**：変更可能なオブジェクトのこと。
Ex:list, dict, set

- **イミュータブル**：変更不可能なオブジェクトのこと。
Ex:int, float, complex, bool, tuple, str, range, file object

- **シーケンス型**：複数の要素を順番に並べたデータ型のこと。
Ex:list, tuple, str, range
listはミュータブルなシーケンスである。
tuple, str, rangeはイミュータブルなシーケンスである。
