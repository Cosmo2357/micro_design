### 
多分userServiceでPostgresにユーザー情報、productServiceでmongoDBに商品情報、redpandaでpinotに商品情報のデータを入れてfeedServiceで取得して表示する。

https://redpanda.com/

https://redpanda.com/blog/streaming-data-apache-pinot-kafka-connect-redpanda

https://github.com/apache/pinot/issues/12155


uvicorn main:app --reload

http://127.0.0.1:8000/docs#