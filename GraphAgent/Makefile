default: help

##@ Utility
help:  ## Display this help
	@awk 'BEGIN {FS = ":.*##"; printf "\nUsage:\n  make \033[36m\033[0m\n"} /^[a-zA-Z_-]+:.*?##/ { printf "  \033[36m%-15s\033[0m %s\n", $$1, $$2 } /^##@/ { printf "\n\033[1m%s\033[0m\n", substr($$0, 5) } ' $(MAKEFILE_LIST)

getmcplinux: ## Download Linux MCP
	@echo "Downloading MCP for Linux"
	@rm -rf toolbox
	@wget https://storage.googleapis.com/genai-toolbox/v0.5.0/linux/amd64/toolbox
	@chmod +x toolbox

getmcpmac: ## Download Mac MCP
	@echo "Downloading MCP for Mac"
	@rm -rf toolbox
	@wget https://storage.googleapis.com/genai-toolbox/v0.5.0/darwin/arm64/toolbox
	@chmod +x toolbox

genmcpconfig: ## Generate MCP config
	@echo "Generating MCP config"
	@python3 ./generate_config.py 

runtoolbox:
	@./toolbox --tools-file tools.yaml
