
---

# Methods

| Method Name      | Description                               |
| ---------------- | ----------------------------------------- |
| `size`           | returns the size of the collection        |
| `isEmpty`        | returns true if the collection is empty   |
| `contains`       |                                           |
| `toArray`        |                                           |
| `add`            |                                           |
| `remove`         |                                           |
| `containsAll`    |                                           |
| `addAll`         |                                           |
| `removeAll`      |                                           |
| `removeIf`       |                                           |
| `retainAll`      |                                           |
| `clear`          |                                           |
| `equals`         | returns true if two collections are equal |
| `hashCode`       | returns the hashcode of the collection    |
| `spliterator`    |                                           |
| `stream`         |                                           |
| `parallelStream` |                                           |

---

# Sample of the Source Code

``` java
public interface Collection<E> extends Iterable<E> {
	int size();
	boolean isEmpty();
	boolean contains(Object o);
	Iterator<E> iterator();
	
	Object[] toArray();
	<T> T[] toArray(T[] a);
	default <T> T[] toArray(IntFunction<T[]> generator)
	{ return toArray(generator.apply(0)); }
	
	boolean add(E e);
	boolean remove(Object o);
	boolean containsAll(Collection<?> c);
	boolean addAll(Collection<? extends E> c);
	boolean removeAll(Collection<?> c);
	
	default boolean removeIf(Predicate<? super E> filter) {
		Objects.requireNonNull(filter);
		boolean removed = false;
		final Iterator<E> each = iterator();
		while (each.hasNext()) {
			if (filter.test(each.next())) {
				each.remove();
				removed = true;
			}
		}
		return removed;
	}
	
	boolean retainAll(Collection<?> c);
	void clear();
	boolean equals(Object o);
	int hashCode();
	@Override
	default Spliterator<E> spliterator()
	{ return Spliterators.spliterator(this, 0); }
	
	default Stream<E> stream()
	{ return StreamSupport.stream(spliterator(), false); }
	
	default Stream<E> parallelStream()
	{ return StreamSupport.stream(spliterator(), true); }
}
```

---
