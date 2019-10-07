import { Component, OnInit } from '@angular/core';
import { FormControl } from '@angular/forms';
import { StationService } from '../services/station.service';
import { Station } from '../models/station.model';
import { Observable } from 'rxjs';
import { startWith, map } from 'rxjs/operators';
import { RouteService } from '../services/route.service';

@Component({
  selector: 'app-route',
  templateUrl: './route.component.html',
  styleUrls: ['./route.component.css']
})
export class RouteComponent implements OnInit {

    fromStationControl = new FormControl();
    toStationControl = new FormControl();
    fromStations:Station[]=[];
    toStations:Station[]=[];
    filteredFromStations:Observable<Station[]>;
    filteredToStations:Observable<Station[]>;
    errMsg:string;
    isDisabled:boolean=true;
    route=[];
    totalTime:number=0;

    constructor(private stationService:StationService, private routeService:RouteService) { }

    ngOnInit() {
        this.getStations();
    }

    getRoute(){
        console.log("Calling getroute : ", this.fromStationControl , this.toStationControl);
        this.routeService.getRoute(this.fromStationControl.value,this.toStationControl.value).subscribe(
            (res) => {
                this.route = res;
                this.totalTime = res.reduce((out,currElm) => out+currElm.via.time, 0);
                console.log("total time is : ",this.totalTime);
            },
            (err) => {
                this.errMsg = "error as : "+ err;
                console.log(this.errMsg);
            },
            () => {}
        )
    }

    fromStationClick(){
        console.log("in fromStationClick : ");
        this.filteredFromStations = this.fromStationControl.valueChanges
            .pipe(
                startWith(''),
                map(value => this._filter(value,this.fromStations))
            );
        console.log("filteredFromStations as : ", this.filteredFromStations);
    }

    toStationClick(){
        this.isDisabled=false;
        console.log("in toStationClick : ");
        this.filteredToStations = this.toStationControl.valueChanges
            .pipe(
                startWith(''),
                map(value => this._filter(value,this.toStations))
            );
        console.log("filteredToStations as : ", this.filteredToStations);
    }

    private _filter(value:string, stations){
        console.log("calling filter : ", value, stations.length);
        var filterValue = value.toLowerCase();
        return stations.filter(station => station.name.toLowerCase().includes(filterValue));
    }

    getStations(){
        console.log("calling getStations")
        this.stationService.getStations().subscribe(
            (res) => {
                this.fromStations = res;
                this.toStations = res;
                console.log(this.fromStations.length);
            },
            (err) => {
                this.errMsg = "error as : "+ err;
                console.log(this.errMsg);
            },
            () => {}
        )
    }

}
