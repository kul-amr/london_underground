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
    stations:Station[]=[];
    filteredFromStations:Observable<Station[]>;
    filteredToStations:Observable<Station[]>;
    errMsg:string;
    isDisabled:boolean=true;
    route=[];

    constructor(private stationService:StationService, private routeService:RouteService) { }

    ngOnInit() {
        this.getStations();
    }

    getRoute(){
        console.log("Calling getroute : ", this.fromStationControl , this.toStationControl);
        this.routeService.getRoute(this.fromStationControl.value,this.toStationControl.value).subscribe(
            (res) => {
                this.route = res;
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
                map(value => this._filter(value))
            );
        console.log("filteredFromStations as : ", this.filteredFromStations);
    }

    toStationClick(){
        this.isDisabled=false;
        console.log("in toStationClick : ");
        this.filteredToStations = this.toStationControl.valueChanges
            .pipe(
                startWith(''),
                map(value => this._filter(value))
            );
        console.log("filteredToStations as : ", this.filteredToStations);
    }

    private _filter(value:string){
        console.log("calling filter : ", value, this.stations.length);
        var filterValue = value.toLowerCase();
        return this.stations.filter(station => station.name.toLowerCase().includes(filterValue));
    }

    getStations(){
        console.log("calling getStations")
        this.stationService.getStations().subscribe(
            (res) => {
                this.stations = res;
                console.log(this.stations.length);
            },
            (err) => {
                this.errMsg = "error as : "+ err;
                console.log(this.errMsg);
            },
            () => {}
        )
    }

}
