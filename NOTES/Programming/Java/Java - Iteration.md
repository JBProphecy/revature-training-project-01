
---

# Standard For-Loop vs Enhanced For-Loop

``` java
int[] array = new int[] {12, 24, 36, 48};

System.out.println("Standard For-Loop");
for (int i = 0; i < array.length; i++) {
	System.out.println(array[i]);
}

System.out.println("Enhanced For-Loop");
for (int a : array) {
	System.out.println(a);
}
```

---
