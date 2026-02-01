
---

# Hash Map Example

``` java
import java.util.HashMap;
import java.util.Map;

// Create Map
Map<String, Integer> myHashMap = new HashMap<String, Integer>();

// Add Entries to Map
myHashMap.put("a", new Integer(100));
myHashMap.put("b", new Integer(200));
myHashMap.put("c", new Integer(300));
myHashMap.put("d", new Integer(400));

// Display Entries in Map
for (Map.Entry<String, Integer> entry : myHashMap.entrySet()) {
	System.out.println(entry.getKey() + ":" + entry.getValue());
}

// Get Size of Map
System.out.println(myHashMap.size());

// Get Value by Key in Map
myHashMap.get("d");

// Remove Entries from Map
myHashMap.remove("d");
```

---
