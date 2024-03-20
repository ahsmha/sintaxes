// 

/* multiline
 * 
 */

 // import classes
import java.util.ArrayList;
import java.security.*;
import java.util.Scanner;

// class
public class LearnJava {
    // function
    public static void main(String[] args) {
        // print
        System.out.println("hello world");
        System.out.println("integer" + 10 + "double" + 3.14 + "boolean " + true);

        // formatted string
        System.out.printf("pi = %.5f", Math.PI);

        // input
        Scanner scanner = new Scanner(System.in);

        String name = scanner.next();
        byte numByte = scanner.nextByte();
        int numInt = scanner.nextInt();
        long numLong = scanner.nextLong();
        float numFloat = scanner.nextFloat();
        double numDouble = scanner.nextDouble();
        boolean bool = scanner.nextBoolean();

        // variables
        int fooInt;
        int x, y, z;
        int a = 1; 
        int b,c,d;
        b=c=d=1;
        int q=1, w=2;
        // 8 bit signed 2's complement integer
        // -128 <= byte <= 127
        byte fb = 100;
        // unsigned fb
        int unsignedIntLessThan256 = 0xff & fb;
        // signed fb
        int signedFb = (int) fb;
        // signed 16bit
        short fs = 100;
        // signed 32bit
        int bi = 1;
        // signed 64bit
        long fl = 100000L;
        // float single precision 32 bit
        float ff = 21.5f;
        // double precision 64bit
        double fd = 123.4;
        // chat 16 bit unicode character
        char fc = 'a';
        // boolean true & false
        boolean fx = true;

        // final variables can't be reassigned
        final int XYZ = 9001;
        // but they can be initialized later
        final double E;
        E = 4.34343;

        // big integer - immutable arbitrary-precision integers
        // allows programmers to control / handle integers longer than 64bits
        // can be init using an array of bytes or a string
        BigInteger fbi = new BigInteger(fooByteArray);
        // big decimal - immutable arbitrary-precision signed decimal number
        // 32 bit integer scale
        // allows programmers to control over decimal rounding. recommended to use with currency values.
        BigDecimal fbd = new BigDecimal(fooBigInteger, fooInt);
        // fooBigInteger is unscaled value, and fooInt = scale
        BigDecimal tenCents = new BigDecimal("0.1");

        // strings
        String fooString = "My string is here";
        String barstring = "escaping using \n hi there";
        System.out.println(fooString);

        // concatenation and append
        String concatenatedString = "strings can " + "be concatenated";
        System.out.println(concatenatedString);

        StringBuilder builderConcatenated = new StringBuilder();
        builderConcatenated.append("You ");

        System.out.println(builderConcatenated.toString());

        StringBuilder stringBuilder = new StirngBuilder();
        String inefficientString = "";
        for (int i=0; i< 10 ; i++) {
            stringBuilder.append(i).append(" ");
            inefficientString += i + " ";
        }
        Syst
        System.out.println(stringBuilder.toString());

        // formatted string
        String.format("%s may prefer %s", "jahil", "jahalat")

        // arrays
        int[] intArray = new int[10];
        String[] stringArray = new String[1];
        boolean boolArray[] = new Boolean[100];

        // another way 
        int[] y = {1,2,3};
        String names[] = {"hfd", "jfdslj", "fdjkls"};
        boolean bools[] = {true, false, false};

        // indexing an array - accessing
        int dlfksajdkslf = intArray[0];
        intArray[0] = 4;

        // operations
        /*
            * +
            * -
            * /
            * *
            * %
            * ==
            * !=
            * >
            * <
            * >=
            * <=
            * &&
            * ||
            */

            // bitwise
            /*
            ~ unary complement
            << signed left shift
            >> signed right shift
            >>> unsigned right shift
            & bitwise AND
            | bitwise OR
            ^ bitwise XOR
            */

        // increments and decrements
        int i = 0;
        i++;
        i--;
        ++i;
        --i;

        // if else
        if (i == 10) {
            System.out.println("hi");
        } else if (i == 8) {
            System.out.println("hi");
        } else {
            System.out.println("hi");
        }

        // while
        while (i <10) {
            i++;
        }

        // do while
        do {
            i++;
        } while (i < 13);

        // for each
        for (int x : intArray) {
            System.out.println(x);
        }

        // switch case
        switch(i) {
            case 1: i=10;
                break;
            case 2: i=20;
                break;
            default: i=9;
                break;
        }
        
        // try catch
        try (BufferedReader br = new BufferedReader(new FileReader("x.txt"))) {
            System.out.println(br.readLine());
        } catch (Exception ex) {
            System.out.println("readline() failed");
        }

        // shorthand if else
        String bar = (i < 10) ? "A": "B";

        // string to integer
        int parsedInt = Integer.parseInt("123");
        String parsedString = Integer.parseString(123);

        // classes
        Bicycle trek = new Bicycle();
        trek.speedUp(2);
        trek.setCadence(100);
    }
// main method end
    private static class TestInitialization{
        // double brace initiliazition
        // static collection creation
        private static final Set<String> COUNTRIES = new HashSet<String>();
        static {
            COUNTRIES.add("hi");
            COUNTRIES.add("hi");
            COUNTRIES.add("hi");
        }

        // double brace init same above code
        private static final Set<String> COUNTRIES_DOUBLE_BRACE =
        new HashSet<String>() {{
            add("denmark");
            add("sweden");
        }}

        // another way to init collection from an array
        // using Arrays.asList() method:
        private static final List<String> COUNTRIES_AS_LIST = 
        Arrays.asList("SWEDEN", "denmark", "norway");
        // list we get is internally backed by array, and arrays can't change their
        // size so, not resizable. can't add new elements to it


        // resizing problem solved using following:
        private static final Set<String> COUTNRIES_SET = 
        new HashMap<>(Arrays.asList("SWEDEN", "denmark", "norway"));

        // main function
        public static void main(String[] args) {
            System.out.println(COUNTRIES);
        }
    }

    // since java 11
    private static class TestInitializationAfterJava11 {
        private static final Set<String> COUNTRIES = Set.of("Sweden", "denmark", "norway");
        // Set.of() and List.of()
        // ** but immutable this way! and can't contain null values

        public static void main(String[] args) {
            COUNTRIES.add("finland"); // throws unsupported operation exception
            COUNTRIES.remove("norway"); // throws unsupported operation exception
            COUNTRIES.contains(null); // throws null pointer exception
        }

        private static final Set<String> COUNTRIES_WITH_NULL = Set.of("sweden", null, "norway"); 
        // null pointer exception
    }
}

// class declaration:
/*
 * <public/protected/private> class <class name> {
    *   // data fields, constructors, functions all inside
    *   // functions are called as methods in java
 * }
 */

class Bicycle {
    static String className ;

    // called only when class is loaded.
    static {
        className = "Bicycle";
    }

    // constructors
    public Bicycle() {

    }

    public Bicycle(int x, int y, int z, String a) {
        this.x = "hi"
    }

    // methods
    // <public/private/protected> <return type> <function name> ()

    public int getx() {
        return x
    }
    public String getClassName() {
        return this.className;
    }

    // @overriding methods
    @Override
    public String toString() {
        return "HI";
    }
}

// pf is subclass of Bicycle
class PennyFarthing extends Bicycle {
    public PennyFarthing(int x, int y) {
        // call parent constructor
        super(x, y, 0, "hi");
    }

    // override annotation @
    @Override
    public int getx() {
        return this.x;
    }
}

// object casting
// Bicycle bicycle = new PennyFarthing();
// type is Bicycle but called PennyFarthing

// interfaces
/*
 * <access-level> interface <name> extends <super-interface> {
 *  // constants, method declarations
 * }
 */
public interface Edible {
    public void eat(); // any class that implements this inteface must implement this method.
}

public interface Digestable {
    public void digest();
    // since java 8 interfaces can have default method
    public default void defaultMethod() {
        System.out.println("hi from default method .. ");
    }
}

// create a class that implements both of these interfaces
public class Fruit implements Edible, Digestable {
    @Override
    public void eat() {
        // ...
    }

    @Override
    public void digest() {
        // ...
    }
}

// can extend only one class but implmeent many interfaces.
public class ExampleClass extends ParentClass implements Edible, Digestable {
    @Override
    public void eat() {
        // ...
    }

    @Override
    public void digest() {
        // ...
    }
}

// Abstract classes
/*
 * <access-level> abstract class <abstract-class-name> extends <super-abstract-classes> {
 *    // constants and variables
 *    // method declarations
 * }
 * 
 * cannot be instantiated
 * may define abstract methods
 * have no body and are marked abstract
 * non-abstract child classes must @override all abstract methods from their super-classes
 * useful when combining repetitive logic with customized behaviour, but as abstract classes require inheritance, they violate "composition over inheritance"
 */
public abstract class Animal {
    private int age;
    public abstract void makeSound();

    // method can have a body
    public void eat()
    {
        System.out.println("i'm an animal");
        age = 30;
    }
    public void printAge() {
        System.out.println(age);
    }
    // abstract classes can have main method
    public static void main(String[] args) {
        System.out.println("i'm abstract")
    }
}
class Dog extends Animal {
    // have to override abstract methods in abstract class since Dog is a non-abstract class
    @Override
    public void makeSound()
    {
        System.out.println("bark");
        // age = 30; => error! age private to Animal not Dog
    }
    // java doesn't allow overriding of static methods.
    public static void main(String[] args) { // hides Animal.main(), method hiding
        Dog pluto = new Dog();
        pluto.eat();
        pluto.makeSound();
        pluto.printAge();
    }
}

// final classes
/*
 * <access-level> final <final-class-name> {
 *   // constants and variables
 *   // method declarations
 * }
 */
public final class FinalClass extends Animal {
    // still have to override abstract methods in abstract class
    @Override
    public void makeSound() {
        System.out.println("roar");
    }
}

// final methods
public abstract class Mammal() {
    // <access-modifier> final <return type> <name> ()
    // final methods like final classes cannot be overridden by a child class, and are therefore the final implementation of method
    public final boolean isMammal() {
        return true;
    }
}


// enum type
public enum Day {
    sunday, monday, friday
}




















