import { Component, OnInit } from '@angular/core';
import { ActivatedRoute } from '@angular/router';

import { LineService } from '../services/line.service';
import { Station } from '../models/station.model';

@Component({
  selector: 'app-line',
  templateUrl: './line.component.html',
  styleUrls: ['./line.component.css']
})
export class LineComponent implements OnInit {

    stations:Station[] = [];
    errMsg:string;
    lineName:string;


    constructor(private lineService:LineService, private route:ActivatedRoute) { 
        console.log(this.route.queryParams);

        this.route.params.subscribe(params => {
            console.log("params as : ", params);
            this.lineName = params['lineName'];
        })
    }

    ngOnInit() {

        console.log("linename is : ", this.lineName);

        this.lineService.getStationsByLine(this.lineName).subscribe(
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

}
