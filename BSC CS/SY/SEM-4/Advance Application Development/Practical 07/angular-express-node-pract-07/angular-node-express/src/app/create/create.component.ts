import { Component } from '@angular/core';
import { ApiservicesService } from '../apiservices.service';

@Component({
  selector: 'app-create',
  templateUrl: './create.component.html',
  styleUrls: ['./create.component.css']
})
export class CreateComponent {

  student = { rollNo: '', name: '', password: '' };

  constructor(private createService: ApiservicesService) { }

  onSubmit() {
    this.createService.registerStudent(this.student)
      .subscribe(
        (response) => { console.log(response); },
        (error) => { console.log(error); }
      );
  }

}
