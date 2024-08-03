export CHECK_CONTAINER_TELEGRAM=
export CHECK_CONTAINER_CHATID=
export CHECK_CONTAINER_LIST=

python3 ./scripts/mysistem_check_container.py >> ./logs/mysistem_check_container-$(date +"%F").log
