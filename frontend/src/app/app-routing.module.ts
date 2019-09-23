import { NgModule } from '@angular/core';
import { Routes, RouterModule } from '@angular/router';
import { HomeComponent } from './home/home.component';
import { StationComponent } from './station/station.component';
import { LineComponent } from './line/line.component';
import { RouteComponent } from './route/route.component';


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
    path:'line',
    component:LineComponent
  },
  {
    path:'route',
    component:RouteComponent
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
