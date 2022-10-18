import './style.css'

interface Prop{
    tableObj: object[]
}

export const CreateTable: React.FC<Prop> = ({tableObj}) => {
    console.log(tableObj)
    const keys = Object.keys(tableObj[0])
    return(
      <div className="table">
        <div 
          className="table__title"
        >
          { keys &&
            keys.map((key:string, i:number)=>{
              return <p key={i} style={{"display":"grid"}}>
                {key}
                </p>
            } )
          }
        </div>

        <div 
          className="table__row"
        >
          {tableObj.map( (row:object, i:number) =>
            <div 
              className="table__row__cell"
              key={i} 
            >
              { 
                Object.values(row).map(
                  (value: string, i:number)=>
                  <p key={i} style={{"display":"grid"}}>{value}</p>
                )
              }
            </div>
          )}
        </div>

      </div>
    )
  }