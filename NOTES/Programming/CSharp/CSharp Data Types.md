
---
# Documentation

https://learn.microsoft.com/en-us/dotnet/csharp/language-reference/language-specification/types

---
# Reference Types

A reference type is a class type, an interface type, an array type, a delegate type, or the `dynamic` type.

---
## Class Types

| C# Alias | .NET Class Type    | Description                                                  |
| -------- | ------------------ | ------------------------------------------------------------ |
| `object` | `System.Object`    | This class serves as the base class for all types.           |
| `string` | `System.String`    | This class serves as the the string type for C#.             |
|          | `System.ValueType` | This class serves as the base class for all value types.     |
|          | `System.Enum`      | This class serves as the base class for all enum types.      |
|          | `System.Array`     | This class serves as the base class for all array types.     |
|          | `System.Delegate`  | This class serves as the base class for all delegate types.  |
|          | `System.Exception` | This class serves as the base class for all exception types. |

---
## Dynamic Type

The `dynamic` type defers type checking from compile-time to runtime.

---
# Value Types

A value type is either a struct type or an enumeration type.

---
## Simple Types

C# provides a set of predefined `struct` types called the simple types. The simple types are identified through keywords, but these keywords are simply aliases for predefined `struct` types in the `System` namespace, as described in the table below.

| C# Alias  | .NET Struct Type | Size     | Description                                     |
| --------- | ---------------- | -------- | ----------------------------------------------- |
| `bool`    | `System.Boolean` | 1 byte   |                                                 |
| `char`    | `System.Char`    | 2 bytes  |                                                 |
| `byte`    | `System.Byte`    | 1 byte   | This type represents an 8-bit unsigned integer. |
| `sbyte`   | `System.SByte`   | 1 byte   | This type represents an 8-bit signed integer.   |
| `short`   | `System.Int16`   | 2 bytes  | This type represents a 16-bit signed integer.   |
| `ushort`  | `System.UInt16`  | 2 bytes  | This type represents a 16-bit unsigned integer. |
| `int`     | `System.Int32`   | 4 bytes  | This type represents a 32-bit signed integer.   |
| `uint`    | `System.UInt32`  | 4 bytes  | This type represents a 32-bit unsigned integer. |
| `long`    | `System.Int64`   | 8 bytes  | This type represents a 64-bit signed integer.   |
| `ulong`   | `System.UInt64`  | 8 bytes  | This type represents a 64-bit unsigned integer. |
| `float`   | `System.Single`  | 4 bytes  |                                                 |
| `double`  | `System.Double`  | 8 bytes  |                                                 |
| `decimal` | `System.Decimal` | 16 bytes |                                                 |

---
## Enumeration Types

``` c#
enum Weekdays : byte
{
	Sunday,
	Monday,
	Tuesday,
	Wednesday,
	Thursday,
	Friday,
	Saturday
}
```

---
## Tuple Types

``` c#
(int, string) myTuple01 = (1, "One");
(int number, string word) myTuple02 = (2, "Two")
```

---
## Nullable Value Types

You can use the **`?`** symbol as shown below to define a nullable type.

``` c#
int? myNullableInteger = null;
```

You can also do it like this, although it's more verbose.

``` c#
Nullable<int> myNullableInteger = null;
```

---
