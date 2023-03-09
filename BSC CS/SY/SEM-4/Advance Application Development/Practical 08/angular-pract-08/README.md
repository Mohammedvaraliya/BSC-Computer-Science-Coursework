# Angular, ng-controller, ng-model and expressions

## Initializing a Angular project.

1. Initialize a `angular` project using `ng`.

   ```bash
    npm install -g @angular/cli
   ```

   ```bash
    ng new angular-pract-08
   ```

   ```bash
    type y and press ENTER
   ```

   ```bash
    select css and press ENTER
   ```

## To apply ng-controller, ng-model and expressions

`AngularJS syntax (ng-controller, ng-model, and expressions) in an Angular application. However, these are not supported in Angular.`
`In Angular, you should use components instead of controllers, and bindings instead of ng-model`

1. In your `app.component.html` file, add the following code:

   ```html
    <input type="text" [(ngModel)]="name">
    <p>Hello, {{ name }}!</p>
   ```

   ```This code defines an input field with two-way data binding using the [(ngModel)] syntax, which binds the value of the input field to the name property in the component. The expression {{ name }} displays the value of the name property.```

1.  In your `app.component.ts` file, add the following code:

    ```ts
    import { Component } from '@angular/core';

    @Component({
    selector: 'app-root',
    templateUrl: './app.component.html',
    styleUrls: ['./app.component.css']
    })
    export class AppComponent {
    title = 'angular-pract-08';
    name =  "";
    }

    ```

    ```This code defines a component named AppComponent with a title property and a name property. The name property is of type string.```

1. In your `app.module.ts` file, import the `FormsModule` module and add it to the imports array:

   ```ts
   import { NgModule } from '@angular/core';
    import { BrowserModule } from '@angular/platform-browser';
    import { FormsModule } from '@angular/forms';

    import { AppComponent } from './app.component';

    @NgModule({
    declarations: [
        AppComponent
    ],
    imports: [
        BrowserModule,
        FormsModule
    ],
    providers: [],
    bootstrap: [AppComponent]
    })
    export class AppModule { }

   ```

   ```This code imports the FormsModule module and adds it to the imports array, which is necessary for using data binding in your Angular application.```

    ```With these changes, you should now have a working Angular application that uses data binding. When you type a new value into the input field, the value of the name property will be updated, and the text "Hello, " will be updated to reflect the new value.```

## Run the application

    npm start


## Output



