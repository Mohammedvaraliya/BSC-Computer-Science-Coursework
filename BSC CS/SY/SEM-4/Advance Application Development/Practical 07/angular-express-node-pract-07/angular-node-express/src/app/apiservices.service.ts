import { Injectable } from '@angular/core';
import { HttpClient, HttpErrorResponse  } from '@angular/common/http'
import { catchError } from 'rxjs/operators';
import { throwError } from 'rxjs';

@Injectable({
  providedIn: 'root'
})
export class ApiservicesService {

  constructor(private http : HttpClient) { }

  // Connect frontend to backend

  private apiUrl = 'http://localhost:3000';

  // Create student 
  registerStudent(student: any) {
    return this.http.post(`${this.apiUrl}/student`, student)
    .pipe(
      catchError(err => {
        if (err instanceof HttpErrorResponse) {
          if (err.status === 409) {
            console.log(err.error.message);
            return throwError(err.error.message);
          }
        }
        return throwError(err);
      })
    );
}
  

}
