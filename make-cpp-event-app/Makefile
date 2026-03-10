CXX = g++
CXXFLAGS = -Wall -Wextra -std=c++17

SRC_DIR = src
BIN_DIR = bin

TARGET = $(BIN_DIR)/ticket_validator

SOURCES = $(SRC_DIR)/main.cpp $(SRC_DIR)/ticket.cpp $(SRC_DIR)/validator.cpp

OBJECTS = $(BIN_DIR)/main.o $(BIN_DIR)/ticket.o $(BIN_DIR)/validator.o


all: $(TARGET)


$(BIN_DIR):
	mkdir -p $(BIN_DIR)


$(BIN_DIR)/main.o: $(SRC_DIR)/main.cpp $(SRC_DIR)/ticket.h $(SRC_DIR)/validator.h | $(BIN_DIR)
	$(CXX) $(CXXFLAGS) -c $(SRC_DIR)/main.cpp -o $(BIN_DIR)/main.o


$(BIN_DIR)/ticket.o: $(SRC_DIR)/ticket.cpp $(SRC_DIR)/ticket.h | $(BIN_DIR)
	$(CXX) $(CXXFLAGS) -c $(SRC_DIR)/ticket.cpp -o $(BIN_DIR)/ticket.o


$(BIN_DIR)/validator.o: $(SRC_DIR)/validator.cpp $(SRC_DIR)/validator.h $(SRC_DIR)/ticket.h | $(BIN_DIR)
	$(CXX) $(CXXFLAGS) -c $(SRC_DIR)/validator.cpp -o $(BIN_DIR)/validator.o


$(TARGET): $(OBJECTS)
	$(CXX) $(CXXFLAGS) $(OBJECTS) -o $(TARGET)


run: $(TARGET)
	./$(TARGET)


report: $(TARGET)
	./$(TARGET) > $(BIN_DIR)/report.txt


stats:
	@total=$$(tail -n +2 data/tickets.csv | wc -l); \
	active=$$(tail -n +2 data/tickets.csv | grep -c ',active$$'); \
	echo "Total tickets: $$total"; \
	echo "Active tickets: $$active"


clean:
	rm -rf $(BIN_DIR)
	

rebuild: clean all