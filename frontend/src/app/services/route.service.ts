import { Injectable } from '@angular/core';
import { HttpClient } from '@angular/common/http';
import { throwError, Observable } from 'rxjs';

import { API_URL } from '../env';
import { map,catchError } from 'rxjs/operators';

@Injectable({
  providedIn: 'root'
})
export class RouteService {

    constructor(private http:HttpClient) { }

    handleError(err){
        console.log("in handleerror : ", err);
        return throwError(err.message || "Error in execution");
    }

    getRoute(fromStation:string,toStation:string):Observable<any>{
        let url = API_URL+'/route/'+fromStation+'/'+toStation;

        return this.http.get(url).pipe(
            map((res:Response) => {
                console.log(res);
                return res;
            }),
            catchError(this.handleError)
        );

    }

}
