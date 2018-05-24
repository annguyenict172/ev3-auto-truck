import { Injectable } from '@angular/core';
import Pusher from 'pusher-js';
import {map} from 'rxjs/operators';
import {HttpClient} from '@angular/common/http';
@Injectable({
  providedIn: 'root'
})
export class BotService {
  pusher: any;
  channel: any;
  private url = 'http://localhost:5000/warehouses';
  constructor(private http: HttpClient) {
    this.pusher = new Pusher('bc48ffab0f0d29ebe910', {
      cluster: 'ap1',
      encrypted: true
    });
    this.channel = this.pusher.subscribe('ans-team-887');
    // this.getData();
  }

  getData(){
    return this.http.get(this.url)
      .pipe(map((res: any) => res.warehouses ))
      // .subscribe(res => console.log(res));
  }
}

