import { Injectable } from '@angular/core';
import { HttpClient, HttpErrorResponse, HttpHeaders } from '@angular/common/http'
import { Observable, throwError } from 'rxjs';
import { map, catchError, tap } from 'rxjs/operators';
import { Line } from '../models/line.model';
import { API_URL } from '../env';


@Injectable({
  providedIn: 'root'
})
export class LineService {

  httpOptions = {
    headers: new HttpHeaders({
      'Content-Type': 'application/json'
    })
  };

  constructor(private http:HttpClient) { }

  handleError(err){
    return throwError(err.message || "Error in execution");
  }

  getLines():Observable<Line[]>{
    return this.http.get<Line[]>(API_URL+'/lines',this.httpOptions).pipe(
      tap((resp) => {
        console.log(resp);
      }),
      catchError(this.handleError));
  }
}
