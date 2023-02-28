# mongodb
brew services start mongodb-community
sleep 2

# mysql 
mysql.server start
sleep 2

#db_con_test
/usr/local/bin/python3 /Users/ah000151/tmpdev/pythonTest/dbconnect_test.py

#streamlit 
# streamlit run /Users/ah000151/tmpdev/pythonTest/frontend/user_controller.py

#FastAPI
# cd /Users/ah000151/tmpdev/pythonTest/backend/
# uvicorn fmain:app --reload
