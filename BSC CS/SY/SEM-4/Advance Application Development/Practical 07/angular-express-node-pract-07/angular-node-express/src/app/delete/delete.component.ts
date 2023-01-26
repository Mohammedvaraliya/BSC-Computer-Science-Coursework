import { Component } from '@angular/core';
import { ApiservicesService } from '../apiservices.service';

@Component({
  selector: 'app-delete',
  templateUrl: './delete.component.html',
  styleUrls: ['./delete.component.css']
})
export class DeleteComponent {
  student = { rollNo: '', password: '' };

  constructor(private deleteService: ApiservicesService) { }

  onSubmit() {
    this.deleteService.deleteStudent(this.student.rollNo, this.student.password)
      .subscribe(
        (response) => { 
          console.log(response);
          alert("Student record deleted successfully!");
        },
        (error) => { 
          console.log(error);
          alert((error.error.message));
        }
      );
  }

}
