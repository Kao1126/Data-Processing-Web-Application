import React, { useState } from "react";
import "bootstrap/dist/css/bootstrap.min.css";

function TableGenerator(data) {
  if (data.data === null) {
    return null;
  } else {
    return (
      <div>
        <table class="table">
          <thead>
            <tr>
              <th>Column Name</th>
              {Object.keys(data["data"]).map((key) => (
                <th scope="col">{key}</th>
              ))}
            </tr>
          </thead>

          <tbody>
            <tr>
              <th scope="row">Type</th>
              {Object.values(data["data"]).map((value) => (
                <td>{value}</td>
              ))}
            </tr>
          </tbody>
        </table>
      </div>
    );
  }
}

export default TableGenerator;
