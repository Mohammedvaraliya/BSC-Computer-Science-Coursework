import { ComponentFixture, TestBed } from '@angular/core/testing';

import { FormBodyComponent } from './form-body.component';

describe('FormBodyComponent', () => {
  let component: FormBodyComponent;
  let fixture: ComponentFixture<FormBodyComponent>;

  beforeEach(async () => {
    await TestBed.configureTestingModule({
      declarations: [ FormBodyComponent ]
    })
    .compileComponents();

    fixture = TestBed.createComponent(FormBodyComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
