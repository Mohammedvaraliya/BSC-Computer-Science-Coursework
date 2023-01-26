# Advanced Application Development Practical (6 & 7)

## Initializing a Angular project.

1. Initialize a `angular` project using `ng`.

   ```bash
    npm install -g @angular/cli
   ```

   ```bash
    ng new angular-node-express
   ```

   ```bash
    type y and press ENTER
   ```

   ```bash
    select css and press ENTER
   ```

## Create 4 Components named (create, read, update, delete)

1. To create a `component` using `ng`.

   ```bash
    cd angular-node-express
   ```

   ```bash
    ng g c create
   ```

   ```bash
    ng g c read
   ```

   ```bash
    ng g c update
   ```

   ```bash
    ng g c delete
   ```

1.  Add the following code to your `app-routing.module.ts` file which is located in the `src` `app`.
    ```ts
    import { NgModule } from '@angular/core';
    import { RouterModule, Routes } from '@angular/router';
    import { CreateComponent } from './create/create.component';
    import { DeleteComponent } from './delete/delete.component';
    import { ReadComponent } from './read/read.component';  
    import { UpdateComponent } from './update/update.component';

    const routes: Routes = [
    {path: 'create', component: CreateComponent},
    {path: 'read', component: ReadComponent},
    {path: 'update', component: UpdateComponent},
    {path: 'delete', component: DeleteComponent},
    ];

    @NgModule({
    imports: [RouterModule.forRoot(routes)],
    exports: [RouterModule]
    })
    export class AppRoutingModule { }

    ```

## Create the `router-Link` in the `app.component.html`.

1. Create `router-Link`.

   ```html
   <h1>Students records</h1>
    <div class="container">
        <a routerLink="create">Create</a>
        <a routerLink="read">Read</a>
        <a routerLink="update">Update</a>
        <a routerLink="delete">Delete</a>
    </div>

    <router-outlet></router-outlet>
   ```

1. Take a look on file `app.module.ts`.

   ```ts
    import { NgModule } from '@angular/core';
    import { BrowserModule } from '@angular/platform-browser';

    import { FormsModule } from '@angular/forms';

    import { AppRoutingModule } from './app-routing.module';
    import { AppComponent } from './app.component';
    import { CreateComponent } from './create/create.component';
    import { ReadComponent } from './read/read.component';

    import { HttpClientModule } from '@angular/common/http';
    import { ApiservicesService } from './apiservices.service';
    import { UpdateComponent } from './update/update.component';
    import { DeleteComponent } from './delete/delete.component';

    @NgModule({
    declarations: [
        AppComponent,
        CreateComponent,
        ReadComponent,
        UpdateComponent,
        DeleteComponent
    ],
    imports: [
        BrowserModule,
        AppRoutingModule,
        HttpClientModule,
        FormsModule
    ],
    providers: [ApiservicesService],
    bootstrap: [AppComponent]
    })
    export class AppModule { }
   ```

1. Now create service to interact with API.

    ```In an Angular project, services are used to encapsulate and share logic and data across different components in the application. Services are typically used to handle tasks such as making HTTP requests to an API, handling form validation, or managing application state. By creating a service, you can separate the logic and data management from the component, making the component code cleaner and easier to read, as well as easier to test. Additionally, services can be reused across multiple components, reducing code duplication.```
   ```bash
   ng g s apiservices
   ```

## Create Multiple API call `frontend` to `backend`

1. Now add the following code in `apiservices.service.ts`

   ```ts
    import { Injectable } from '@angular/core';
    import { HttpClient, HttpErrorResponse, HttpHeaders } from '@angular/common/http';
    import { catchError } from 'rxjs/operators';
    import { throwError, Observable } from 'rxjs';

    @Injectable({
    providedIn: 'root',
    })
    export class ApiservicesService {
    constructor(private http: HttpClient) {}

    // Connect frontend to backend

    private apiUrl = 'http://localhost:3000';

    // Create student
    registerStudent(student: any) {
        return this.http.post(`${this.apiUrl}/student`, student).pipe(
        catchError((err) => {
            if (err instanceof HttpErrorResponse) {
            if (err.status === 409) {
                console.log(err.error.message);
                alert(err.error.message);
                return throwError(err.error.message);
            }
            }
            return throwError(err);
        })
        );
    }

    // Read student
    readStudent(rollNo: string) {
        return this.http.get(`${this.apiUrl}/student?rollNo=${rollNo}`).pipe(
        catchError((err) => {
            if (err instanceof HttpErrorResponse) {
            if (err.status === 409) {
                console.log(err.error.message);
                alert(err.error.message);
                return throwError(err.error.message);
            }
            }
            return throwError(err);
        })
        );
    }

    // Update student
    updateStudent(rollNo: any, password: any, userData: any): Observable<any> {
        const headers = new HttpHeaders({ 'Content-Type': 'application/json' });
        const url = `${this.apiUrl}/student?rollNo=${rollNo}`;
        return this.http.put(url, { password, ...userData }, { headers }).pipe(
        catchError((err) => {
            if (err instanceof HttpErrorResponse) {
            if (err.status === 409) {
                console.log(err.error.message);
                alert(err.error.message);
                return throwError(err.error.message);
            }
            }
            return throwError(err);
        })
        );
    }

    // Update student
    deleteStudent(rollNo: any, password: any): Observable<any> {
        const bodyData = {
        body: { password },
        };
        return this.http.delete(`${this.apiUrl}/student?rollNo=${rollNo}`, bodyData).pipe(
        catchError((err) => {
            if (err instanceof HttpErrorResponse) {
            if (err.status === 409) {
                console.log(err.error.message);
                alert(err.error.message);
                return throwError(err.error.message);
            }
            }
            return throwError(err);
        })
        );
    }
    }

   ```

1. Now to create a student record take all input field from user from `create` component.

    1. `create.component.html`
   ```html
    <form (submit)="onSubmit()">
        <h2>Create Student Record</h2>
        <label for="rollNo">Roll No:</label>
        <input [(ngModel)]="student.rollNo" name="rollNo" id="rollNo" placeholder="Roll No">
        <br>
        <label for="name">Name:</label>
        <input [(ngModel)]="student.name" name="name" id="name" placeholder="Name">
        <br>
        <label for="password">Password:</label>
        <input type="password" [(ngModel)]="student.password" name="password" id="password" placeholder="Password">
        <br>
        <button type="submit">Register</button>
    </form>  
   ```

   2. `create.component.ts`

    `This is an Angular component class for a "create" feature. It creates a student object with properties for rollNo, name, and password. The component has a constructor that injects an instance of the ApiservicesService, which is a service that makes API calls to a server.`

    `The component also has a method called onSubmit() which is bound to the form's submit event. When the form is submitted, it calls the registerStudent() method on the ApiservicesService, passing in the student object as an argument.`

    `The registerStudent() method makes an API call to register a new student on the server. The subscribe() method is used to listen to the response from the server. If the response is successful, it will log the response to the console and display an alert message saying "Student record added successfully!". If an error occurs, it will log the error to the console and display an alert with the error message.`
    

   ```ts
    import { Component } from '@angular/core';
    import { ApiservicesService } from '../apiservices.service';

    @Component({
    selector: 'app-create',
    templateUrl: './create.component.html',
    styleUrls: ['./create.component.css']
    })
    export class CreateComponent {

    student = { rollNo: '', name: '', password: '' };

    constructor(private createService: ApiservicesService) { }

    onSubmit() {
        this.createService.registerStudent(this.student)
        .subscribe(
            (response) => { 
            console.log(response);
            alert("Student record added successfully!");
            },
            (error) => { 
            console.log(error);
            alert((error.error.message));
            }
        );
    }

    }
   ```

1. Similarly to `read` a student record take user input `rollNo` from `read` component.

    1. `read.component.html`
   ```html
    <div class="center">
    <form (submit)="onSubmit()">
        <h2>Read Student Record</h2>
        <label for="rollNo">Roll No:</label>
        <input [(ngModel)]="student.rollNo" name="rollNo" id="rollNo" placeholder="Roll No">
        <br>
        <button type="submit">Search</button>
        </form>
        <br>

        <table>
            
            <div *ngIf="student.name.length > 2">
                <tr>
                <div>
                    <td><label>Roll No:</label></td>
                    <td>{{student.rollNo}}</td>
                </div>
                </tr>
                <tr>
                <div>
                    <td><label>Name:</label></td>
                    <td>{{student.name}}</td>
                </div>
                </tr>
                <tr>
                <div>
                    <td><label>Password:</label></td>
                    <td>{{student.password}}</td>
                </div>
                </tr>
            </div>
            
        </table>
    </div>
   ```

   2. `read.component.ts`

    `The onSubmit() method calls the readStudent() method of the ApiservicesService, passing in the student's roll number as an argument. The method returns an observable that the component subscribes to.`

    `If the API call is successful, the response body is logged to the console and the student object is populated with the roll number, name, and password of the student returned by the API. If there is an error, the error message is logged to the console and an alert is displayed to the user, and the student object is reset to its original state.`
    

   ```ts
    import { Component, OnInit } from '@angular/core';
    import { ApiservicesService } from '../apiservices.service'

    @Component({
    selector: 'app-read',
    templateUrl: './read.component.html',
    styleUrls: ['./read.component.css']
    })

    export class ReadComponent {

    student = { rollNo: '', name: '', password: ''};

    constructor (private readService : ApiservicesService) { }

    onSubmit() {
        this.readService.readStudent(this.student.rollNo)
        .subscribe(
            (response: any) => { 
            console.log(response);
            this.student = { rollNo: response.body.rollNo, name: response.body.name, password: response.body.password };
            },
            (error) => { 
            console.log(error);
            alert((error.error.message));
            this.student = { rollNo: '', name: '', password: ''};
            }
        );
    }

    }

   ```

1. Similarly to `update` a student record take user input `rollNo` and `password` from `update` component.

    1. `update.component.html`
   ```html
    <form (submit)="onSubmit()">
        <h2>Update Student Record</h2>
        <label for="rollNo">Roll No:</label>
        <input [(ngModel)]="student.rollNo" name="rollNo" id="rollNo" placeholder="Roll No">
        <label for="password">Password:</label>
        <input type="password" [(ngModel)]="student.password" name="password" id="password" placeholder="Password">
        <br>
        <label for="name">Name:</label>
        <input [(ngModel)]="student.name" name="name" id="name" placeholder="Name">
        <br>
        <br>
        <button type="submit">Update</button>
    </form>
  
   ```

   2. `update.component.ts`

    `The component defines a student object that contains properties for the student's roll number, name, and password.`

    `In the constructor, an instance of the ApiservicesService is injected, and the component creates a method called onSubmit() that is called when the user submits the form.`

    `The onSubmit() method calls the updateStudent() method of the ApiservicesService, passing in the student's roll number, password and student object as an arguments. The method returns an observable that the component subscribes to.`

    `If the API call is successful, the response is logged to the console and an alert message is displayed to the user to confirm that the student record has been updated successfully. If there is an error, the error message is logged to the console and an alert is displayed to the user with the error message.`
    

   ```ts
    import { Component } from '@angular/core';
    import { ApiservicesService } from '../apiservices.service';

    @Component({
    selector: 'app-update',
    templateUrl: './update.component.html',
    styleUrls: ['./update.component.css']
    })
    export class UpdateComponent {
    student = { rollNo: '', name: '', password: '' };

    constructor(private updateService: ApiservicesService) { }

    onSubmit() {
        this.updateService.updateStudent(this.student.rollNo, this.student.password, this.student)
        .subscribe(
            (response) => { 
            console.log(response);
            alert("Student record updated successfully!");
            },
            (error) => { 
            console.log(error);
            alert((error.error.message));
            }
        );
    }

    }
   ```

1. Similarly to `delete` a student record take user input `rollNo` and `password` from `update` component.

    1. `delete.component.html`
   ```html
    <form (submit)="onSubmit()">
        <h2>Delete Student Record</h2>
        <label for="rollNo">Roll No:</label>
        <input [(ngModel)]="student.rollNo" name="rollNo" id="rollNo" placeholder="Roll No">
        <label for="password">Password:</label>
        <input type="password" [(ngModel)]="student.password" name="password" id="password" placeholder="Password">
        <br>
        <button type="submit">Delete</button>
    </form>
   ```

   2. `delete.component.ts`

    `The component defines a student object that contains properties for the student's roll number, name, and password.`

    `In the constructor, an instance of the ApiservicesService is injected, and the component creates a method called onSubmit() that is called when the user submits the form.`

    `The onSubmit() method calls the updateStudent() method of the ApiservicesService, passing in the student's roll number, password and student object as an arguments. The method returns an observable that the component subscribes to.`

    `If the API call is successful, the response is logged to the console and an alert message is displayed to the user to confirm that the student record has been updated successfully. If there is an error, the error message is logged to the console and an alert is displayed to the user with the error message.`
    

   ```ts
    import { Component } from '@angular/core';
    import { ApiservicesService } from '../apiservices.service';

    @Component({
    selector: 'app-delete',
    templateUrl: './delete.component.html',
    styleUrls: ['./delete.component.css']
    })
    export class DeleteComponent {
    student = { rollNo: '', password: '' };

    constructor(private deleteService: ApiservicesService) { }

    onSubmit() {
        this.deleteService.deleteStudent(this.student.rollNo, this.student.password)
        .subscribe(
            (response) => { 
            console.log(response);
            alert("Student record deleted successfully!");
            },
            (error) => { 
            console.log(error);
            alert((error.error.message));
            }
        );
    }

    }
   ```

1. Now add the common `css` on all the component for styling frontend.

    ```css
    form {
        width: 50%;
        margin: 0 auto;
        padding: 20px;
        border: 1px solid #ccc;
        border-radius: 5px;
    }

    h2 {
        text-align: center;
        color: #5e5e5e;
        margin-top: 20px;
    }
    
    label {
        display: block;
        margin-bottom: 10px;
        font-weight: bold;
    }
    
    input {
        width: 100%;
        padding: 12px 20px;
        margin: 8px 0;
        box-sizing: border-box;
        border: 1px solid #ccc;
        border-radius: 4px;
    }
    
    button {
        width: 100%;
        padding: 14px 20px;
        margin: 8px 0;
        border: none;
        border-radius: 4px;
        background-color: #4CAF50;
        color: white;
        cursor: pointer;
    }
    
    button:hover {
        background-color: #45a049;
    }
    ```

## Starting the application

1. We have to run both the server concurrently

    `The concurrently package is a utility for running multiple npm commands concurrently. It allows you to run multiple npm scripts at the same time, which can be useful for running multiple development servers or other background tasks in a single command.`

    `For example, you can use it to run both a client-side development server and a server-side development server at the same time, so that you can test your application in a development environment without having to manually start and stop each server separately. It also allows you to specify a custom command to run if any of the commands fail.`

    `It can be installed by running npm i concurrently and then you can use it by running npx concurrently <command1> <command2> <command3> in your terminal.`

    `It is commonly used to run multiple commands in parallel during development, such as starting a webpack dev server and a backend server at the same time.`

    ```bash
    npm i concurrently
    ```

    `Now add the script in the package.json file`

    ```bash
    "scripts": {
    "ng": "ng",
    "start": "ng serve",
    "build": "ng build",
    "watch": "ng build --watch --configuration development",
    "test": "ng test",
    "both": "concurrently \"npm run start\" \"nodemon backend/index.js\""
    },
    ```

To start the application run `npm run both` start in development mode.
