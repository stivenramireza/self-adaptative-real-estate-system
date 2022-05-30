import { Component } from '@angular/core';
import { AngularFirestore, AngularFirestoreCollection } from '@angular/fire/compat/firestore';
import { Observable } from 'rxjs';
import { State } from './interfaces';


@Component({
  selector: 'app-root',
  templateUrl: './app.component.html',
  styleUrls: ['./app.component.css']
})
export class AppComponent {

  private stateCollection: AngularFirestoreCollection<State> | undefined;

  states : State[] = [];

  title = 'estates';


  constructor(private afs: AngularFirestore) {
    this.stateCollection = afs.collection<State>('Inmuebles');
    this.stateCollection.valueChanges().subscribe(data => {
      this.states = data;
    });
  }
}
