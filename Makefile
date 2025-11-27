ANTLR_JAR = lib/antlr-4.13.2-complete.jar

SRC_DIR = src
OUT_DIR = tests

NAME = KobraV2
GRAMMAR = $(SRC_DIR)/$(NAME).g4

all: generate

generate:
	antlr4 -o $(OUT_DIR) -Dlanguage=Python3 -visitor $(GRAMMAR)

