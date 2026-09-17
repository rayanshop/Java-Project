import java.util.ArrayList; 
import java.util.Scanner;


// Parent class
class Person {

    private int personCode;
    private String personName;
    private String phoneNumber;

    Person(int personCode, String personName, String phoneNumber) {
        this.personCode = personCode;
        this.personName = personName;
        this.phoneNumber = phoneNumber;
    }

    public int getPersonCode() {
        return personCode;
    }

    public String getPersonName() {
        return personName;
    }

    public String getPhoneNumber() {
        return phoneNumber;
    }
}

// Passenger class
class Rider extends Person {

    Rider(int personCode, String personName, String phoneNumber) {
        super(personCode, personName, phoneNumber);
    }
}

// Driver class
class CabDriver extends Person {

    private double cabDistance;
    private boolean freeCab;

    CabDriver(int personCode, String personName,
              String phoneNumber, double cabDistance) {

        super(personCode, personName, phoneNumber);

        this.cabDistance = cabDistance;
        freeCab = true;
    }

    public double getCabDistance() {
        return cabDistance;
    }

    public boolean isFreeCab() {
        return freeCab;
    }

    public void changeCabStatus(boolean status) {
        freeCab = status;
    }
}

// Ride class
class Trip {

    private int tripNumber;
    private Rider rider;
    private CabDriver cabDriver;
    private double tripDistance;
    private double tripFare;
    private String tripStatus;

    Trip(int tripNumber, Rider rider, CabDriver cabDriver,
         double tripDistance) {

        this.tripNumber = tripNumber;
        this.rider = rider;
        this.cabDriver = cabDriver;
        this.tripDistance = tripDistance;

        tripFare = 50 + (tripDistance * 15);

        tripStatus = "BOOKED";
    }

    public void finishTrip() {
        tripStatus = "COMPLETED";
        cabDriver.changeCabStatus(true);
    }

    public void stopTrip() {
        tripStatus = "CANCELLED";
        cabDriver.changeCabStatus(true);
    }

    public int getTripNumber() {
        return tripNumber;
    }

    public String getTripStatus() {
        return tripStatus;
    }

    public void showTrip() {

        System.out.println("------------------------------");
        System.out.println("Trip Number : " + tripNumber);
        System.out.println("Rider       : " + rider.getPersonName());
        System.out.println("Driver      : " + cabDriver.getPersonName());
        System.out.println("Distance    : " + tripDistance + " km");
        System.out.println("Fare        : Rs. " + tripFare);
        System.out.println("Status      : " + tripStatus);
        System.out.println("------------------------------");
    }
}

// Main class
public class Main {

    static Scanner inputBox = new Scanner(System.in);

    static ArrayList<Rider> riderList = new ArrayList<>();
    static ArrayList<CabDriver> cabList = new ArrayList<>();
    static ArrayList<Trip> tripBox = new ArrayList<>();

    static int nextTripNumber = 1001;

    // Add a passenger
    public static void addRider() {

        System.out.println("\n--- ADD RIDER ---");

        System.out.print("Enter rider code: ");
        int code = inputBox.nextInt();
        inputBox.nextLine();

        System.out.print("Enter rider name: ");
        String name = inputBox.nextLine();

        System.out.print("Enter phone number: ");
        String phone = inputBox.nextLine();

        Rider newRider = new Rider(code, name, phone);

        riderList.add(newRider);

        System.out.println("Rider added successfully.");
    }

    // Add a driver
    public static void addCabDriver() {

        System.out.println("\n--- ADD CAB DRIVER ---");

        System.out.print("Enter driver code: ");
        int code = inputBox.nextInt();
        inputBox.nextLine();

        System.out.print("Enter driver name: ");
        String name = inputBox.nextLine();

        System.out.print("Enter phone number: ");
        String phone = inputBox.nextLine();

        System.out.print("Enter distance from passenger: ");
        double distance = inputBox.nextDouble();

        CabDriver newDriver =
                new CabDriver(code, name, phone, distance);

        cabList.add(newDriver);

        System.out.println("Driver added successfully.");
    }

    // Show drivers
    public static void showCabs() {

        System.out.println("\n--- CAB DRIVERS ---");

        if (cabList.size() == 0) {
            System.out.println("No drivers available.");
            return;
        }

        for (CabDriver cab : cabList) {

            System.out.println(
                    "Code: " + cab.getPersonCode()
                    + " | Name: " + cab.getPersonName()
                    + " | Distance: " + cab.getCabDistance()
                    + " km"
                    + " | Status: "
                    + (cab.isFreeCab() ? "Available" : "Busy")
            );
        }
    }

    // Search rider
    public static Rider findRider(int wantedCode) {

        for (Rider rider : riderList) {

            if (rider.getPersonCode() == wantedCode) {
                return rider;
            }
        }

        return null;
    }

    // Find nearest available cab
    public static CabDriver pickCab() {

        CabDriver chosenCab = null;

        for (CabDriver cab : cabList) {

            if (cab.isFreeCab()) {

                if (chosenCab == null) {

                    chosenCab = cab;

                } else if (cab.getCabDistance()
                        < chosenCab.getCabDistance()) {

                    chosenCab = cab;
                }
            }
        }

        return chosenCab;
    }

    // Book a ride
    public static void bookTrip() {

        System.out.println("\n--- BOOK A CAB ---");

        if (riderList.size() == 0) {
            System.out.println("Please add a rider first.");
            return;
        }

        if (cabList.size() == 0) {
            System.out.println("No cabs have been added.");
            return;
        }

        System.out.print("Enter rider code: ");
        int riderCode = inputBox.nextInt();

        Rider selectedRider = findRider(riderCode);

        if (selectedRider == null) {
            System.out.println("Rider not found.");
            return;
        }

        CabDriver chosenCab = pickCab();

        if (chosenCab == null) {
            System.out.println("All cabs are currently busy.");
            return;
        }

        System.out.print("Enter journey distance: ");
        double journeyDistance = inputBox.nextDouble();

        double expectedFare =
                50 + (journeyDistance * 15);

        System.out.println("\n--- BOOKING DETAILS ---");
        System.out.println("Rider    : "
                + selectedRider.getPersonName());
        System.out.println("Driver   : "
                + chosenCab.getPersonName());
        System.out.println("Distance : "
                + journeyDistance + " km");
        System.out.println("Fare     : Rs. " + expectedFare);

        System.out.print("Confirm booking? (Y/N): ");
        char answer = inputBox.next().charAt(0);

        if (answer == 'Y' || answer == 'y') {

            Trip newTrip = new Trip(
                    nextTripNumber,
                    selectedRider,
                    chosenCab,
                    journeyDistance
            );

            nextTripNumber++;

            tripBox.add(newTrip);

            chosenCab.changeCabStatus(false);

            System.out.println("\nCab booked successfully.");
            System.out.println(
                    "Your trip number is "
                    + newTrip.getTripNumber()
            );

        } else {

            System.out.println("Booking was not made.");
        }
    }

    // Complete a ride
    public static void completeTrip() {

        System.out.println("\n--- COMPLETE TRIP ---");

        System.out.print("Enter trip number: ");
        int wantedTrip = inputBox.nextInt();

        for (Trip trip : tripBox) {

            if (trip.getTripNumber() == wantedTrip) {

                if (trip.getTripStatus().equals("BOOKED")) {

                    trip.finishTrip();

                    System.out.println(
                            "Trip completed successfully."
                    );

                } else {

                    System.out.println(
                            "This trip is already "
                            + trip.getTripStatus()
                    );
                }

                return;
            }
        }

        System.out.println("Trip not found.");
    }

    // Cancel a ride
    public static void cancelTrip() {

        System.out.println("\n--- CANCEL TRIP ---");

        System.out.print("Enter trip number: ");
        int wantedTrip = inputBox.nextInt();

        for (Trip trip : tripBox) {

            if (trip.getTripNumber() == wantedTrip) {

                if (trip.getTripStatus().equals("BOOKED")) {

                    trip.stopTrip();

                    System.out.println(
                            "Trip cancelled successfully."
                    );

                } else {

                    System.out.println(
                            "This trip cannot be cancelled."
                    );
                }

                return;
            }
        }

        System.out.println("Trip not found.");
    }

    // Display all trips
    public static void showTrips() {

        System.out.println("\n--- TRIP HISTORY ---");

        if (tripBox.size() == 0) {
            System.out.println("No trips have been booked.");
            return;
        }

        for (Trip trip : tripBox) {
            trip.showTrip();
        }
    }

    // Main method
    public static void main(String[] args) {

        while (true) {

            System.out.println("\n==============================");
            System.out.println("       CAB BOOKING APP");
            System.out.println("==============================");

            System.out.println("1. Add Rider");
            System.out.println("2. Add Cab Driver");
            System.out.println("3. Show Drivers");
            System.out.println("4. Book Cab");
            System.out.println("5. Complete Trip");
            System.out.println("6. Cancel Trip");
            System.out.println("7. Show Trip History");
            System.out.println("8. Exit");

            System.out.print("\nEnter your choice: ");

            try {

                int menuChoice = inputBox.nextInt();

                switch (menuChoice) {

                    case 1:
                        addRider();
                        break;

                    case 2:
                        addCabDriver();
                        break;

                    case 3:
                        showCabs();
                        break;

                    case 4:
                        bookTrip();
                        break;

                    case 5:
                        completeTrip();
                        break;

                    case 6:
                        cancelTrip();
                        break;

                    case 7:
                        showTrips();
                        break;

                    case 8:
                        System.out.println(
                                "Thank you for using the app."
                        );
                        inputBox.close();
                        return;

                    default:
                        System.out.println(
                                "Please select a valid option."
                        );
                }

            } catch (Exception problem) {

                System.out.println(
                        "Invalid input. Please try again."
                );

                inputBox.nextLine();
            }
        }
    }
}
