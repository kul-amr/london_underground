import { NgModule } from '@angular/core';
import { Routes, RouterModule } from '@angular/router';
import { HomeComponent } from './home/home.component';
import { StationComponent } from './station/station.component';
import { LinesComponent } from './lines/lines.component';
import { RouteComponent } from './route/route.component';
import { LineComponent } from './line/line.component';


const routes: Routes = [
  {
    path:'',
    component:HomeComponent
  },
  {
    path:'station',
    component:StationComponent
  },
  {
    path:'lines',
    component:LinesComponent
  },
  {
    path:'route',
    component:RouteComponent
  },
  {
    path:'line/:lineName',
    component:LineComponent
  },
  {
    path:'**',
    redirectTo:''
  }
];

@NgModule({
  imports: [RouterModule.forRoot(routes)],
  exports: [RouterModule]
})
export class AppRoutingModule { }
