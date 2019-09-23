import { BrowserModule } from '@angular/platform-browser';
import { NgModule } from '@angular/core';
import { HttpClientModule } from '@angular/common/http';
import { MatToolbarModule } from '@angular/material/toolbar';

import { AppRoutingModule } from './app-routing.module';
import { AppComponent } from './app.component';
import { StationComponent } from './station/station.component';
import { LineComponent } from './line/line.component';
import { RouteComponent } from './route/route.component';
import { StationService } from './services/station.service';
import { LineService } from './services/line.service';
import { RouteService } from './services/route.service';
import { HomeComponent } from './home/home.component';
import { HeaderComponent } from './header/header.component';
import { FooterComponent } from './footer/footer.component';


@NgModule({
  declarations: [
    AppComponent,
    StationComponent,
    LineComponent,
    RouteComponent,
    HomeComponent,
    HeaderComponent,
    FooterComponent
  ],
  imports: [
    BrowserModule,
    AppRoutingModule,
    HttpClientModule,
    MatToolbarModule
  ],
  providers: [
    StationService,
    LineService,
    RouteService
  ],
  bootstrap: [AppComponent]
})
export class AppModule { }
