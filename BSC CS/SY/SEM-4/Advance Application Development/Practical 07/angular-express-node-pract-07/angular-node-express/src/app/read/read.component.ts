import { Component, OnInit } from '@angular/core';
import { ApiservicesService } from '../apiservices.service'

@Component({
  selector: 'app-read',
  templateUrl: './read.component.html',
  styleUrls: ['./read.component.css']
})
export class ReadComponent {

  constructor (private service : ApiservicesService) { }

}
