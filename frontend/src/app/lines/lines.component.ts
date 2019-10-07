import { Component, OnInit } from '@angular/core';
import { Router, NavigationExtras } from '@angular/router';

import { LineService } from '../services/line.service';
import { Line } from '../models/line.model';
import { Station } from '../models/station.model';

@Component({
  selector: 'app-lines',
  templateUrl: './lines.component.html',
  styleUrls: ['./lines.component.css']
})
export class LinesComponent implements OnInit {

    lines:Line[];
    errMsg:string;
    stations:Station[]=[];

    constructor(private lineService:LineService, private router:Router) { }

    ngOnInit() {

        console.log("calling onint : ");

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

    onLineSelect(line:Line){
        console.log("passed in line as : ", line);

        let navigationExtras:NavigationExtras = {queryParams:{'lineName':line.name}};

        this.router.navigate(['/line'],navigationExtras);

    }

}
