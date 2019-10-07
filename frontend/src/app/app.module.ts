import { BrowserModule } from '@angular/platform-browser';
import { BrowserAnimationsModule } from '@angular/platform-browser/animations';
import { NgModule } from '@angular/core';
import { HttpClientModule } from '@angular/common/http';
import { MatToolbarModule } from '@angular/material/toolbar';
import { MatAutocompleteModule, MatInputModule, MatListModule, MatIconModule } from '@angular/material';
import { FormControl, FormsModule, ReactiveFormsModule } from '@angular/forms';
import { MatCardModule, MatSelectModule, MatFormFieldModule, MatGridListModule } from '@angular/material';

import { AppRoutingModule } from './app-routing.module';
import { AppComponent } from './app.component';
import { StationComponent } from './station/station.component';
import { LinesComponent } from './lines/lines.component';
import { RouteComponent } from './route/route.component';
import { StationService } from './services/station.service';
import { LineService } from './services/line.service';
import { RouteService } from './services/route.service';
import { HomeComponent } from './home/home.component';
import { HeaderComponent } from './header/header.component';
import { FooterComponent } from './footer/footer.component';
import { StationsComponent } from './stations/stations.component';
import { LineComponent } from './line/line.component';


@NgModule({
  declarations: [
    AppComponent,
    StationComponent,
    LinesComponent,
    RouteComponent,
    HomeComponent,
    HeaderComponent,
    FooterComponent,
    StationsComponent,
    LineComponent
  ],
  imports: [
    BrowserModule,
    AppRoutingModule,
    HttpClientModule,
    MatToolbarModule,
    MatCardModule,
    MatSelectModule,
    MatFormFieldModule,
    BrowserAnimationsModule,
    MatGridListModule,
    FormsModule,
    ReactiveFormsModule,
    MatAutocompleteModule,
    MatInputModule,
    MatListModule,
    MatIconModule
  ],
  providers: [
    StationService,
    LineService,
    RouteService
  ],
  bootstrap: [AppComponent]
})
export class AppModule { }
