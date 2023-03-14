## Practical No 8

### There is no such modules and controllers in Angular JS

Angular (formerly known as Angular 2+) does have the concepts of modules and controllers, but they are called differently and work differently from AngularJS.

In Angular, modules are used to group related components, directives, pipes, and services together into a cohesive block of functionality. Modules are created using the @NgModule decorator and can be imported and exported to be used in other modules.

`Controllers, on the other hand, have been deprecated in Angular` in favor of components. Components are the building blocks of Angular applications and are responsible for the view and the behavior of a specific part of the application. Components are created using the @Component decorator and can communicate with other components and services using input and output properties.

The reason controllers were deprecated in Angular is that they are tightly coupled to the view, which can lead to code that is difficult to maintain and test. Components, on the other hand, are more modular and can be easily tested in isolation.