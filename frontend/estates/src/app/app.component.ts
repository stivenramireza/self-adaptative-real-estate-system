import { Component } from '@angular/core';
import { AngularFirestore, AngularFirestoreCollection } from '@angular/fire/compat/firestore';
import { Observable } from 'rxjs';
import { State } from './interfaces';
import { HttpClient, HttpHeaders } from "@angular/common/http";

@Component({
  selector: 'app-root',
  templateUrl: './app.component.html',
  styleUrls: ['./app.component.css']
})
export class AppComponent {

  private stateCollection: AngularFirestoreCollection<State> | undefined;

  states : State[] = [];

  title = 'estates';

  baseurl = "http://127.0.0.1:5000/api/v1/control/";
  httpHeaders = new HttpHeaders({ "Content-type": "application/json"});


  constructor(private afs: AngularFirestore, private http: HttpClient) {
    this.stateCollection = afs.collection<State>('Inmuebles');
    this.stateCollection.valueChanges().subscribe(data => {
      this.states = data;
    });
  }

  updateVisit(id: string){
    const body = {property_id: id}
    this.http.post(this.baseurl, body, { headers: this.httpHeaders }).toPromise().then((data)=> {
      console.log(data);
    });
  }
}
