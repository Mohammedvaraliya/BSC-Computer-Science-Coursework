import { ErrorHandler, Injectable } from '@angular/core';

@Injectable()
export class GlobalErrorHandler implements ErrorHandler {

    constructor() {}
    handleError(error: TypeError) {
        // your custom error handling logic
        console.log("error", error);
        this.displayError(error);
    }
    private displayError(error: TypeError): void {
        // call error logging API or display error
        alert(error.message);
    }
}