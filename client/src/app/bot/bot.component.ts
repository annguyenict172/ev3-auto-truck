import {AfterViewInit, Component, ElementRef, OnChanges, OnInit, ViewChild} from '@angular/core';
import {BotService} from '../core/service/bot.service';

@Component({
  selector: 'app-bot',
  templateUrl: './bot.component.html',
  styleUrls: ['./bot.component.css']
})

export class BotComponent implements OnInit, AfterViewInit {
  @ViewChild('myCanvas') myCanvas: ElementRef;
  public ctx: CanvasRenderingContext2D;

  constructor(public botService: BotService) {
  }

  message: any;

  ngOnInit(){
    this.botService.channel.bind('change-position', data => {
      console.log(data.location_id);
    });
  }

  ngAfterViewInit(): void {
    this.ctx = (<HTMLCanvasElement>this.myCanvas.nativeElement).getContext('2d');
    this.ctx.moveTo(200, 10);
    this.ctx.lineTo(0, 0);
    this.ctx.stroke();
  }
}
