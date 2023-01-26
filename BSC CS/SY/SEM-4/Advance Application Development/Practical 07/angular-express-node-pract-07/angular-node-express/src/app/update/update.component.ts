import { Component } from '@angular/core';
import { ApiservicesService } from '../apiservices.service';

@Component({
  selector: 'app-update',
  templateUrl: './update.component.html',
  styleUrls: ['./update.component.css']
})
export class UpdateComponent {
  student = { rollNo: '', name: '', password: '' };

  constructor(private updateService: ApiservicesService) { }

  onSubmit() {
    this.updateService.updateStudent(this.student.rollNo, this.student.password, this.student)
      .subscribe(
        (response) => { 
          console.log(response);
          alert("Student record updated successfully!");
        },
        (error) => { 
          console.log(error);
          alert((error.error.message));
        }
      );
  }

}
