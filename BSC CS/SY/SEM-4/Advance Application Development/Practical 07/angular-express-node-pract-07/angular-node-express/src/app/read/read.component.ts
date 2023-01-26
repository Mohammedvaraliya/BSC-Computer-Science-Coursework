import { Component, OnInit } from '@angular/core';
import { ApiservicesService } from '../apiservices.service'

@Component({
  selector: 'app-read',
  templateUrl: './read.component.html',
  styleUrls: ['./read.component.css']
})

export class ReadComponent {

  student = { rollNo: '', name: '', password: ''};

  constructor (private readService : ApiservicesService) { }

  onSubmit() {
    this.readService.readStudent(this.student.rollNo)
      .subscribe(
        (response: any) => { 
          console.log(response);
          this.student = { rollNo: response.body.rollNo, name: response.body.name, password: response.body.password };
        },
        (error) => { 
          console.log(error);
          alert((error.error.message));
          this.student = { rollNo: '', name: '', password: ''};
        }
      );
  }

}
