-- Create the database if it doesn't exist
CREATE DATABASE IF NOT EXISTS Tourism2;

-- Use the database
USE Tourism2;

-- Create the Tourist table
CREATE TABLE Tourist (
    TouristID INT PRIMARY KEY,
    Name VARCHAR(255),
    DOB DATE,
    Age INT,
    PhoneNo VARCHAR(15)
);

-- Create the Package table
CREATE TABLE Package (
    PackageID INT PRIMARY KEY,
    PackageName VARCHAR(255),
    Duration INT,
    Price DECIMAL(10, 2),
    Rating DECIMAL(3, 2),
    HotelName VARCHAR(255),
    HotelAddress VARCHAR(255)
);

-- Create the Reservation table
CREATE TABLE Reservation (
    ReservationID INT PRIMARY KEY,
    BookingDate DATE,
    NumberOfPeople INT,
    TouristID INT,
    PackageID INT,
    FOREIGN KEY (TouristID) REFERENCES Tourist(TouristID),
    FOREIGN KEY (PackageID) REFERENCES Package(PackageID)
);

-- Create the Payment table
CREATE TABLE Payment (
    PaymentID INT PRIMARY KEY,
    Amount DECIMAL(10, 2),
    PaymentDate DATE,
    Status VARCHAR(50),
    Method VARCHAR(50),
    ReservationID INT,
    FOREIGN KEY (ReservationID) REFERENCES Reservation(ReservationID)
);

-- Create the Modes table (Note: Created before the ConsistsOf table)
CREATE TABLE Modes (
    ModesID INT PRIMARY KEY,
    TransportationType VARCHAR(255),
    DepartureDate DATE,
    ArrivalDate DATE
);

-- Create the ConsistsOf table (Junction table for many-to-many relationship between Package and Modes)
CREATE TABLE ConsistsOf (
    PackageID INT,
    ModesID INT,
    PRIMARY KEY (PackageID, ModesID),
    FOREIGN KEY (PackageID) REFERENCES Package(PackageID),
    FOREIGN KEY (ModesID) REFERENCES Modes(ModesID)
);

-- Create the Includes table (Junction table for many-to-many relationship between Reservation and Package)
CREATE TABLE Includes (
    ReservationID INT,
    PackageID INT,
    PRIMARY KEY (ReservationID, PackageID),
    FOREIGN KEY (ReservationID) REFERENCES Reservation(ReservationID),
    FOREIGN KEY (PackageID) REFERENCES Package(PackageID)
);

-- Create the Hotel table
CREATE TABLE Hotel (
    HotelID INT PRIMARY KEY,
    HotelName VARCHAR(255),
    HotelAddress VARCHAR(255)
);
