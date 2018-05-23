import {Component, ElementRef, OnChanges, OnInit, ViewChild} from '@angular/core';
import {BotService} from '../core/service/bot.service';

declare var $: any;

@Component({
  selector: 'app-bot',
  templateUrl: './bot.component.html',
  styleUrls: ['./bot.component.css']
})

export class BotComponent implements OnInit {
  data: any;

  constructor(public botService: BotService) {
  }

  ngOnInit() {
    this.botService.channel.bind('change-position', data => {
      this.changeImage(data.location_id);
    });
    this.botService.getData().subscribe(res => {
      this.data = res;
    });

    var mapDiv;

    mapDiv = document.getElementById('map');

    var map = [0,-1,-1,-1,-1,-1,-1,1,-1,-1,-1,-1,-1,-1,2,-1,-1,-1,-1,-1,-1,3,
            -1,-2,-2,-2,-2,-2,-2,-2,-2,-2,-2,-2,-2,-2,-2,-2,-2,-2,-2,-2,-2,-1,
            -1,-2,-2,-2,-2,-2,-2,-2,-2,-2,-2,-2,-2,-2,-2,-2,-2,-2,-2,-2,-2,-1,
            -1,-2,-2,-2,-2,-2,-2,-2,-2,-2,-2,-2,-2,-2,-2,-2,-2,-2,-2,-2,-2,-1,
            -1,-2,-2,-2,-2,-2,-2,-2,-2,-2,-2,-2,-2,-2,-2,-2,-2,-2,-2,-2,-2,-1,
            13,-2,-2,-2,-2,-2,-2,-2,-2,-2,-2,-2,-2,-2,-2,5,-1,-1,-1,-1,-1,4,
            -1,-2,-2,-2,-2,-2,-2,-2,-2,-2,-2,-2,-2,-2,-2,-2,-2,-2,-2,-2,-2,-1,
            -1,-2,-2,-2,-2,-2,-2,-2,-2,-2,-2,-2,-2,-2,-2,-2,-2,-2,-2,-2,-2,-1,
            -1,-2,-2,-2,-2,-2,-2,-2,-2,-2,-2,-2,-2,-2,-2,-2,-2,-2,-2,-2,-2,-1,
            -1,-2,-2,-2,-2,-2,-2,-2,-2,-2,-2,-2,-2,-2,-2,-2,-2,-2,-2,-2,-2,-1,
            12,-2,-2,-2,-2,-2,-2,-2,-2,-2,-2,-2,-2,-2,-2,7,-1,-1,-1,-1,-1,6,
            -1,-2,-2,-2,-2,-2,-2,-2,-2,-2,-2,-2,-2,-2,-2,-2,-2,-2,-2,-2,-2,-1,
            -1,-2,-2,-2,-2,-2,-2,-2,-2,-2,-2,-2,-2,-2,-2,-2,-2,-2,-2,-2,-2,-1,
            -1,-2,-2,-2,-2,-2,-2,-2,-2,-2,-2,-2,-2,-2,-2,-2,-2,-2,-2,-2,-2,-1,
            -1,-2,-2,-2,-2,-2,-2,-2,-2,-2,-2,-2,-2,-2,-2,-2,-2,-2,-2,-2,-2,-1,
            11,-1,-1,-1,-1,-1,-1,10,-1,-1,-1,-1,-1,-1,9,-1,-1,-1,-1,-1,-1,8];

    map.forEach((point, index) => {
      let image = document.createElement('img');
      let anotherDiv = document.createElement('br');
      image.src = point === -2 ? 'assets/images/white.png' : point === -1 ? 'assets/images/black.png' : 'assets/images/red.png';
      if (point !== -2 && point !== -1) image.id = `point-${point}`
      mapDiv.appendChild(image);
      if (index > 0 && (index + 1) % 22 === 0) mapDiv.appendChild(anotherDiv);
    });
    this.changeImage(0);
  }


  changeImage(id) {
    for (let i = 0; i < 14; i++) {
      let image;
      image = document.getElementById(`point-${i}`) as HTMLImageElement;
      if (i == id) {
        image.src = 'assets/images/yellow.png';
      } else {
        image.src = 'assets/images/red.png';
      }
    }

  }
}
