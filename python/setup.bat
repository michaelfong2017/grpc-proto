SETLOCAL
set env_name=windows-env
python -m venv %env_name%
%env_name%\Scripts\python -m pip install --upgrade pip
%env_name%\Scripts\pip install grpcio
%env_name%\Scripts\pip install grpcio-tools
ENDLOCAL
