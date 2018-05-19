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
      cluster: 'ap1',
      encrypted: true
    });
    this.channel = this.pusher.subscribe('ans-team-887');
  }
}

