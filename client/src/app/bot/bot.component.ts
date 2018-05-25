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
  robotStatus: String = 'Not Ready';

  constructor(public botService: BotService) {
  }

  ngOnInit() {
    this.botService.channel.bind('change-position', data => {
      let locationId = data.location_id;
      if (locationId < 0 || locationId > 13) locationId = 0;
      this.changeImage(locationId);
    });
    this.botService.channel.bind('change-status', data => {
      this.robotStatus = data.status;
    });
    this.botService.getData().subscribe(res => {
      this.data = res;
    });
    this.botService.channel.bind('choose-warehouse', data => {
      this.botService.getData().subscribe(res => {
        this.data = res;
        this.chooseWarehouse(data.warehouse_num);
      });
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
      switch(point) {
        case -2:
          image.src = 'assets/images/white.png';
          break;
        case -1:
          image.src = 'assets/images/black.png';
          break;
        case 5:
        case 7:
          image.src = 'assets/images/blue.png';
          break;
        default:
          image.src = 'assets/images/red.png';
      }
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
      if (i === id) {
        image.src = 'assets/images/yellow.png';
      } else {
        if (i === 5 || i === 7) image.src = 'assets/images/blue.png';
        else image.src = 'assets/images/red.png';
      }
    }
  }

  chooseWarehouse(warehouseNum) {
    let id = warehouseNum === 0 ? 'warehouse1' : 'warehouse2';
    let warehouse = document.getElementById(id);
    warehouse.style.backgroundColor = "yellow";
  }
}
