import {BrowserModule} from '@angular/platform-browser';
import {NgModule} from '@angular/core';

import {AppComponent} from './app.component';
import {BotComponent} from './bot/bot.component';
import {CoreModule} from './core/core.module';

@NgModule({
  declarations: [
    AppComponent,
    BotComponent
  ],
  imports: [
    BrowserModule,
    CoreModule
  ],
  providers: [],
  bootstrap: [AppComponent]
})
export class AppModule {
}
