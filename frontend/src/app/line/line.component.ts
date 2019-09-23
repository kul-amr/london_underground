import { Component, OnInit } from '@angular/core';
import { LineService } from '../services/line.service';
import { Line } from '../models/line.model';

@Component({
  selector: 'app-line',
  templateUrl: './line.component.html',
  styleUrls: ['./line.component.css']
})
export class LineComponent implements OnInit {

  lines:Line[];
  errMsg:string;

  constructor(private lineService:LineService) { }

  ngOnInit() {

    this.lineService.getLines().subscribe(
        (res) => {
            this.lines = res;
            console.log(this.lines);
        },
        (err) => {
            this.errMsg = "error as : "+ err;
            console.log(this.errMsg);
        },
        () => {}
    )

  }

}
