import { Component, OnInit } from '@angular/core';
import { LineService } from '../services/line.service';
import { Line } from '../models/line.model';
import { StationService } from '../services/station.service';
import { Station } from '../models/station.model';
import { FormControl } from '@angular/forms';
import { Observable } from 'rxjs';
import { startWith, map } from 'rxjs/operators';

@Component({
  selector: 'app-station',
  templateUrl: './station.component.html',
  styleUrls: ['./station.component.css']
})
export class StationComponent implements OnInit {

    lines:Line[];
    stations:Station[]=[];
    errMsg:string;
    isStationSelDisabled:boolean=true;
    allStations:Station[] = [];
    passingLines:Line[] = [];

    stationControl = new FormControl();
    filteredStations:Observable<Station[]>;
    selectedStation:Station=new Station('');

    constructor(private lineService:LineService, private stationService:StationService) { }

    ngOnInit() {
        
        this.getLines();
    }

    getLines(){
        this.lineService.getLines().subscribe(
            (res) => {
                this.lines = res;
            },
            (err) => {
                this.errMsg = "error as : "+ err;
                console.log(this.errMsg);
            },
            () => {}
        )
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

    getStationsByLine(lineName:string){
        this.lineService.getStationsByLine(lineName).subscribe(
            (res) => {
                this.stations = res;
            },
            (err) => {
                this.errMsg = "error as : "+ err;
                console.log(this.errMsg);
            },
            () => {}
        )
    }

    onLineSelect(event){
        console.log("onLineSelect : ",event);
        this.isStationSelDisabled = false;
        this.getStationsByLine(event);
    }

    onStationSelect(event){
        console.log("onStationSelect : ",event);
        this.selectedStation = event;
        this.getPassingLines(event.name);
    }

    getPassingLines(stationName:string){
        this.stationService.getPassingLines(stationName).subscribe(
            (res) => {
                this.passingLines = res;
            },
            (err) => {
                this.errMsg = "error as : "+ err;
                console.log(this.errMsg);
            },
            () => {}
        )
    }

    onStationClick(){
        console.log("in onStationClick : ");
        this.getStations();
        this.filteredStations = this.stationControl.valueChanges
            .pipe(
                startWith(''),
                map(value => this._filter(value))
            );
    }

    private _filter(value:string){
        const filterValue = value.toLowerCase();
        return this.stations.filter(station => station.name.toLowerCase().includes(filterValue));
    }
}
