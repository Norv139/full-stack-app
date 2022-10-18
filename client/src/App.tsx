import React, {useEffect, useState } from 'react';
import './App.css';
import { CreateTable } from './components/createTable';



function App() {
  

  const [tables, setTables] = useState<string[]>()
  const [tableObj, setTableObj] = useState<object[]>()

  useEffect(()=>{

    fetch('/tables')
    .then(res=>res.json())
    .then(date=>{
      setTables(date.tables)
    })

  },[])

  const fnOnChange =( e: {target: {value: string}} )=>{
    if (e.target.value === 'Null'){
      setTableObj(undefined);
      return
    }
    fetch(`/tables/${e.target.value}`)
    .then(res=>res.json())
    .then(date=>{
      setTableObj(date.table)
    });
  }

  return (
    <div className="App">

      <select className='list' name="list" onChange={fnOnChange}>
        <option>Null</option>
        { tables && 
          tables.map(
            (name:string, i:number)=>
              <option key={i}>{name}</option>
          )
        }
      </select>

      { tableObj && 
        <CreateTable tableObj={tableObj} />
      }
      
    </div>
  );
}


export default App;


