### Write a program to implement CRUD Update operations on MongoDB.

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

1. In your `app.component.html` file, add the following code:

```html
<h1>This is Global Error Handling</h1>
```

1. Create new file in `app` directory named `GlobalErrorHandler.ts`. And add the following code in that file

    ```tsx
    import { ErrorHandler, Injectable } from '@angular/core';

    @Injectable()
    export class GlobalErrorHandler implements ErrorHandler {

        constructor() {}
        handleError(error: TypeError) {
            // your custom error handling logic
            console.log("error", error);
            this.displayError(error);
        }
        private displayError(error: TypeError): void {
            // call error logging API or display error
            alert(error.message);
        }
    }
    ```


1. In your `app.component.ts` file, add the following code:
    
    ```tsx
    import { Component } from '@angular/core';

    @Component({
    selector: 'app-root',
    templateUrl: './app.component.html',
    styleUrls: ['./app.component.css']
    })
    export class AppComponent {
    title = 'question_8_error_handeling';

    ngOnInit(){
        throw new Error("This error is meant to handled by the error handler service.")
    }

    }

    ```
    
2. In your `app.module.ts` file, import the `FormsModule` module and add it to the imports array:
    
    ```tsx
    import { BrowserModule } from '@angular/platform-browser';

    import { AppRoutingModule } from './app-routing.module';
    import { AppComponent } from './app.component';

    import { GlobalErrorHandler } from './GlobalErrorHandler';
    import { ErrorHandler, NgModule } from '@angular/core';

    @NgModule({
    declarations: [
        AppComponent
    ],
    imports: [
        BrowserModule,
        AppRoutingModule
    ],
    providers: [
        {provide: ErrorHandler, useClass:GlobalErrorHandler}
    ],
    bootstrap: [AppComponent]
    })
    export class AppModule { }

    ```
    

## Run the application

```bash
npm start
```

## Output 

