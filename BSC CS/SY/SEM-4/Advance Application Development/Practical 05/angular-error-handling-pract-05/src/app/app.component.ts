import { Component } from '@angular/core';

@Component({
  selector: 'app-root',
  templateUrl: './app.component.html',
  styleUrls: ['./app.component.css']
})
export class AppComponent {
  title = 'angular-error-handling-pract-05';

  ngOnInit(){
    throw new Error("This error is meant to handled by the error handler service.")
  }
  
}
