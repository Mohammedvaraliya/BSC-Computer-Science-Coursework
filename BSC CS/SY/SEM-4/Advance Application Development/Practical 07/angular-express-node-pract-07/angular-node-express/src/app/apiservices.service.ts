import { Injectable } from '@angular/core';
import { HttpClient } from '@angular/common/http'
import { Observable } from 'rxjs';

@Injectable({
  providedIn: 'root'
})
export class ApiservicesService {

  constructor(private _http : HttpClient) { }

  // Connect frontend to backend

  apiUrl = 'http://localhost:3000/student';

  // get all data

  getAllData():Observable<any> 
  {
    return this._http.get(`${this.apiUrl}`);
  }

}
