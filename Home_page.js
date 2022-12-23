const matches = [
  {
    id: 1,
    team1: {
      name: "IND",
      score: "336",
      wickets: "5",
      overs: "50",
      image: "https://www.w3schools.com/images/w3schools_green.jpg",
    },
    team2: {
      name: "PAK",
      score: "336",
      wickets: "5",
      overs: "50",
      image: "https://www.w3schools.com/images/w3schools_green.jpg",
    },
  },
  {
    id: 2,
    team1: {
      name: "IND",
      score: "336",
      wickets: "5",
      overs: "50",
      image: "https://i.imgur.com/717RRSi.png",
    },
    team2: {
      name: "PAK",
      score: "336",
      wickets: "5",
      overs: "50",
      image: "https://i.imgur.com/717RRSi.png",
    },
  },
  {
    id: 3,
    team1: {
      name: "IND",
      score: "336",
      wickets: "5",
      overs: "50",
      image: "https://i.imgur.com/717RRSi.png",
    },
    team2: {
      name: "PAK",
      score: "336",
      wickets: "5",
      overs: "50",
      image: "https://i.imgur.com/717RRSi.png",
    },
  },
  {
    id: 4,
    team1: {
      name: "IND",
      score: "336",
      wickets: "5",
      overs: "50",
      image: "https://i.imgur.com/717RRSi.png",
    },
    team2: {
      name: "PAK",
      score: "336",
      wickets: "5",
      overs: "50",
      image: "https://i.imgur.com/717RRSi.png",
    },
  },
  {
    id: 4,
    team1: {
      name: "IND",
      score: "336",
      wickets: "5",
      overs: "50",
      image: "https://i.imgur.com/717RRSi.png",
    },
    team2: {
      name: "PAK",
      score: "336",
      wickets: "5",
      overs: "50",
      image: "https://i.imgur.com/717RRSi.png",
    },
  },
];

function setNewRow(content) {
  var newRow = "<tr>" + content + "</tr>";
  return newRow;
}

function renderTable() {
  var tbody = document.getElementById("allMatches");

  var content = "";
  var count = 0;
  for (var i = 0; i < matches.length; i++) {
    var td = `
        <td>
      <div class="column">
      <div class="main">
        <p class="head">
          Cricket World Cup 2019 <span class="right day">Yesterday</span>
        </p>
        <br />
        <table style="cursor: pointer;">
                <tr onclick='location.href="index.html"'>
                    <td class="right1">
                    <span>${matches[i].team1.name}</span>
                    &emsp;
                        <img
                            class="flag"
                            src="${matches[i].team1.image}"
                            
                            alt="" 
                        />
                                                
                        <br /><br />
                        <p class="score">${matches[i].team1.score}/${matches[i].team1.wickets}</p>
                        <br />  
                        <p class="overs">(${matches[i].team1.overs})</p>
                    </td>
                    <td class="right1">
                        <span>${matches[i].team2.name}</span>
                        &emsp;
                        <img
                            class="flag"
                            src="${matches[i].team2.image}"
                            alt=""
                        />
                        <br /><br />
                        <p class="score pak">${matches[i].team2.score}/${matches[i].team2.wickets}</p>
                        <br />
                        <p class="overs pak">(${matches[i].team2.overs})</p>
                    </td>
                    </tr>
                </table>
        <center>
          <p class="target"><u>Target 302</u></p>
          <p class="res">India won by 89 runs (DLS method)</p>
          <p class="match">ODI 22 of 38</p>
        </center>
      </div>
    </div>
    </td>
      `;
    content += td;
    if (count % 2 != 0) {
      content = setNewRow(content);
      count++;
    } else {
      count++;
    }
  }

  tbody.innerHTML = content;
}

renderTable();
