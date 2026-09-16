PRAGMA foreign_keys = ON;

CREATE TABLE Customers (
    CustomerID INTEGER PRIMARY KEY AUTOINCREMENT,
    Name TEXT NOT NULL,
    HomeAddress TEXT,
    Email TEXT UNIQUE,
    Number TEXT
);

CREATE TABLE Memberships (
    MembershipID INTEGER PRIMARY KEY AUTOINCREMENT,
    CustomerID INTEGER NOT NULL,
    FOREIGN KEY (CustomerID)
        REFERENCES Customers(CustomerID)
        ON DELETE CASCADE
);

CREATE TABLE Items (
    ItemID INTEGER PRIMARY KEY AUTOINCREMENT,
    Name TEXT NOT NULL,
    ProductionPrice REAL NOT NULL,
    SellPrice REAL NOT NULL,
    Quantity INTEGER NOT NULL DEFAULT 0
);

CREATE TABLE Sales (
    SaleID INTEGER PRIMARY KEY AUTOINCREMENT,
    ItemID INTEGER NOT NULL,
    Date TEXT NOT NULL,
    FOREIGN KEY (ItemID)
        REFERENCES Items(ItemID)
        ON DELETE CASCADE
);

CREATE TABLE OrdersHistory (
    OrderHistoryID INTEGER PRIMARY KEY AUTOINCREMENT,
    MembershipID INTEGER NOT NULL,
    FOREIGN KEY (MembershipID)
        REFERENCES Memberships(MembershipID)
        ON DELETE CASCADE
);

CREATE TABLE Orders (
    OrderHistoryID INTEGER NOT NULL,
    ItemID INTEGER NOT NULL,
    QuantityBought INTEGER NOT NULL,
    
    PRIMARY KEY (OrderHistoryID, ItemID),

    FOREIGN KEY (OrderHistoryID)
        REFERENCES OrdersHistory(OrderHistoryID)
        ON DELETE CASCADE,

    FOREIGN KEY (ItemID)
        REFERENCES Items(ItemID)
        ON DELETE CASCADE
);