import { Injectable } from '@angular/core';
// declare var Pusher: any;
import Pusher from 'pusher-js';

@Injectable({
  providedIn: 'root'
})
export class BotService {
  pusher: any;
  channel: any;
  constructor() {
    this.pusher = new Pusher('bc48ffab0f0d29ebe910', {
      // app_id: '524891',
      cluster: 'ap1',
      // secret: '4ccbafa61f0ddd0abf08',
      encrypted: true
    });
    this.channel = this.pusher.subscribe('ans-team-887');
    console.log(this.channel);
  }
}

