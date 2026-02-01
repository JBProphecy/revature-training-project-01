
---

# Intermediate Operations / Methods

| Method     | Description |
| ---------- | ----------- |
| `filter`   |             |
| `map`      |             |
| `flatMap`  |             |
| `distinct` |             |
| `sorted`   |             |
| `limit`    |             |
| `skip`     |             |

---

# Terminal Operations / Methods

| Method      | Description |
| ----------- | ----------- |
| `collect`   |             |
| `reduce`    |             |
| `forEach`   |             |
| `count`     |             |
| `anyMatch`  |             |
| `allMatch`  |             |
| `noneMatch` |             |
| `findFirst` |             |
| `findAny`   |             |

---

# Sample of the Source Code

``` java
public interface Stream<T> extends BaseStream<T, Stream<T>> {
	Stream<T> filter(Predicate<? super T> predicate);
	<R> Stream<R> map(Function<? super T, ? extends R> mapper);
	
	T reduce(T identity, BinaryOperator<T> accumulator);
	Optional<T> reduce(BinaryOperator<T> accumulator);
	<U> U reduce(
		U identity,
		BiFunction<U, ? super T, U> accumulator,
		BinaryOperator<U> combiner
	);
		
	<R> R collect(Supplier<R> supplier,
		BiConsumer<R, ? super T> accumulator,
		BiConsumer<R, R> combiner
	);
	<R, A> R collect(Collector<? super T, A, R> collector);
}
```

---
