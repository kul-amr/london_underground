import { Injectable } from '@angular/core';
import { HttpClient, HttpErrorResponse, HttpHeaders } from '@angular/common/http'
import { Observable, throwError } from 'rxjs';
import { map, catchError, tap } from 'rxjs/operators';
import { Line } from '../models/line.model';
import { API_URL } from '../env';
import { Station } from '../models/station.model';


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
        console.log("in handleerror : ", err);
        return throwError(err.message || "Error in execution");
    }

    getLines():Observable<Line[]>{
        let url = API_URL+'/lines/';

        return this.http.get(url).pipe(
            map((res:Response)=>{
                res['data'].forEach(element => {
                    element['colour'] = "#"+element['colour'];
                });
                console.log("res['data']")
                return res['data'];
            }),
            catchError(this.handleError)
        );
    }

    getStationsByLine(lineName:string):Observable<Station[]>{
        let url = API_URL+'/lines/'+lineName+'/stations';

        return this.http.get(url).pipe(
            map((res:Response)=>{
                return res['data'];
            }),
            catchError(this.handleError)
        );
    }

}
