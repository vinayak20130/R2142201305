﻿# Repository Title
 to create
curl -X POST -H "Content-Type: application/json" -d '{"key":"one", "value":1}' http://127.0.0.1:3000/number
to retrieve 
curl http://127.0.0.1:3000/number/one
to update
curl -X PUT -H "Content-Type: application/json" -d '{"value":10}' http://127.0.0.1:3000/number/one
to delete
curl -X DELETE http://127.0.0.1:3000/number/one
