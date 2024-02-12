FROM redis:latest

COPY redisinit.sh /usr/local/bin/

RUN chmod +x /usr/local/bin/redisinit.sh

ENTRYPOINT ["/usr/local/bin/redisinit.sh"]

CMD ["redis-server", "--appendonly yes"]