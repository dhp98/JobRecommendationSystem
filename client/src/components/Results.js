import React from 'react'

const Results = ({jobsData}) => {
  const jobs = jobsData.data;
  return (
    <div>
      {
        jobs.map((job)=>(
          <div className='resultsItem' key={job.title+job.company+Date.now()}>

            <h3>{job.company}</h3>
            <h4>{job.title}</h4>
            <span>{job.location}</span>
            <br/>
            <a href={job.link}> Click her to know more</a>
            <p>
              {job.desc}
            </p>
          </div>
        ))
      }
    </div>
  )
}

export default Results