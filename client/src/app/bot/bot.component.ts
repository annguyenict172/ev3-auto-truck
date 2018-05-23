import {Component, ElementRef, OnChanges, OnInit, ViewChild} from '@angular/core';
import {BotService} from '../core/service/bot.service';

declare var $: any;

@Component({
  selector: 'app-bot',
  templateUrl: './bot.component.html',
  styleUrls: ['./bot.component.css']
})

export class BotComponent implements OnInit {
  @ViewChild('myCanvas') myCanvas: ElementRef;
  public ctx: CanvasRenderingContext2D;
  data: any;
  constructor(public botService: BotService) {
  }

  bulb = 'assets/images/pic_bulboff.gif';
  srcImage = [this.bulb, this.bulb, this.bulb, this.bulb, this.bulb, this.bulb, this.bulb, this.bulb,
    this.bulb, this.bulb, this.bulb, this.bulb, this.bulb, this.bulb];

  ngOnInit() {
    this.botService.channel.bind('change-position', data => {
      console.log(data);
    });
    this.changeImage(12);
    this.botService.getData().subscribe(res => {
      console.log('tem', res);
      this.data = res;
    });
  }


  changeImage(id) {
    // console.log(id);
    for (let i = 0; i < 14; i++) {
      if (i == id) {
        this.srcImage[id] = 'assets/images/pic_bulbon.gif';
      } else {
        this.srcImage[i] = 'assets/images/pic_bulboff.gif';
      }
    }

  }
}
