import { HttpClient } from '@angular/common/http';
import { Injectable } from '@angular/core';

@Injectable({
  providedIn: 'root',
})
export class ApiService {
  constructor(private http: HttpClient) {}
  private apiUrl = 'https://your-api-url.com/api';

  getItems() {
    return this.http.get(`${this.apiUrl}/items`).toPromise();
  }
}