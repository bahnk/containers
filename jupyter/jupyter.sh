#!/bin/sh

unset XDG_RUNTIME_DIR
jupyter-notebook \
	--ip=$(hostname -I | awk '{print $3}') \
	--port=8787

