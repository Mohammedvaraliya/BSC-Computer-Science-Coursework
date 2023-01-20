import { ErrorHandler, NgModule } from '@angular/core';
import { BrowserModule } from '@angular/platform-browser';

import { AppComponent } from './app.component';

import { GlobalErrorHandler } from './GlobalErrorHandler';

@NgModule({
  declarations: [
    AppComponent
  ],
  imports: [
    BrowserModule
  ],
  providers: [
    {provide: ErrorHandler, useClass:GlobalErrorHandler}
  ],
  bootstrap: [AppComponent]
})
export class AppModule { }
