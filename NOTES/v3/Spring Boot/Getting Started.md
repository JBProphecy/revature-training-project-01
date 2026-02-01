
## **Create Project**

[[Spring Initializer]]

---

## **Initialize Git Repository**

The first thing you should do is initialize a `Git` repository and make the initial commit.

I used to configure everything to the point when I was ready to start coding and then make the initial commit, but I think it would be nice to have the option to switch to the initial commit and see what `Spring Initializer` generated.

---

## **Configure Git Ignore**

I like to modify/organize `.gitignore`.

---

## **Temporarily Disable Docker**

I like to comment everything out of `compose.yaml` until I configure those services.

You may not be able to run your application with an empty `compose.yaml` file.

If you don't want to configure `Docker` yet, disable it in `application.yaml`.

``` yaml
spring:
  docker:
    compose:
      enabled: false
```

---

## **Temporarily Disable Database**

You may not be able to run your application without defining a data source.

If you don't want to configure your data source yet, exclude these three things.

``` java
@SpringBootApplication(exclude = {
  DataSourceAutoConfiguration.class,
  DataSourceTransactionManagerAutoConfiguration.class,
  HibernateJpaAutoConfiguration.class
})
```

---
