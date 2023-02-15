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
  updateStudent(rollNo: any, password: any, newPassword: any, userData: any): Observable<any> {
    const headers = new HttpHeaders({ 'Content-Type': 'application/json' });
    const url = `${this.apiUrl}/student?rollNo=${rollNo}`;
    return this.http.put(url, { password, newPassword, ...userData }, { headers }).pipe(
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

  // Delete student
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
