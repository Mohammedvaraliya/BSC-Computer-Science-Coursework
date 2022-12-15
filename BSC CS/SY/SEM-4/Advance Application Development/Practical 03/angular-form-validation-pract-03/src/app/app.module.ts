import { NgModule } from '@angular/core';
import { BrowserModule } from '@angular/platform-browser';

import {ReactiveFormsModule} from '@angular/forms';

import { AppComponent } from './app.component';
import { FormBodyComponent } from './form-body/form-body.component';

@NgModule({
  declarations: [
    AppComponent,
    FormBodyComponent
  ],
  imports: [
    BrowserModule,
    ReactiveFormsModule
  ],
  providers: [],
  bootstrap: [AppComponent]
})
export class AppModule { }
