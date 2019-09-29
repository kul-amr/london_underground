import { Injectable } from '@angular/core';
import { HttpClient } from '@angular/common/http';
import { throwError, Observable } from 'rxjs';

import { Station } from '../models/station.model';
import { API_URL } from '../env';
import { map, catchError } from 'rxjs/operators';
import { Line } from '../models/line.model';

@Injectable({
  providedIn: 'root'
})
export class StationService {

    constructor(private http:HttpClient) { }

    handleError(err){
        console.log("in handleerror : ", err);
        return throwError(err.message || "Error in execution");
    }

    getStations():Observable<Station[]>{
        let url = API_URL+'/stations/';

        return this.http.get(url).pipe(
            map((res:Response)=>{
                console.log("res['data']")
                return res['data'];
            }),
            catchError(this.handleError)
        );
    }

    getPassingLines(stationName:string):Observable<Line[]>{
        let url = API_URL+'/stations/'+stationName+'/lines';

        return this.http.get(url).pipe(
            map((res:Response)=>{
                res['data'].forEach(element => {
                    element['colour'] = "#"+element['colour'];
                });
                return res['data'];

            }),
            catchError(this.handleError)
        );
    }

}
