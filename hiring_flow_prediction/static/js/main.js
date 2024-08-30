$(document).ready(function() {
  $(".menuIcon").click(function() {
    $(".sidebar").toggleClass("close__sidebar");
    $(".main__section .right__section").toggleClass("close__sidebar");
  });

  $(".close__btn").click(function() {
    $(".sidebar").addClass("close__sidebar");
    //$(".main__section .right__section").toggleClass("close__sidebar");
  });

  if ($(window).width() < 767) {
    $(".sidebar").addClass("close__sidebar");
  }

  //Employee Distribution

  const employeeDistribution = document.getElementById("employeeDistribution");

  new Chart(employeeDistribution, {
    type: "pie",
    data: {
      labels: ["Red", "Blue", "Yellow", "Green", "Purple", "Orange"],
      datasets: [
        {
          label: "Distribution Of Employees",
          data: [12, 19, 3, 5, 2, 3],
          borderWidth: 1
        }
      ]
    },
    options: {
      scales: {
        y: {
          beginAtZero: true
        }
      }
    }
  });

  //leaving Reason----------------------------------

  const leavingreason = document.getElementById("leavingreason");

  // Define gradient colors
  const gradientColors = [
    "rgba(255, 99, 132, 0.6)",
    "rgba(54, 162, 235, 0.6)",
    "rgba(255, 206, 86, 0.6)",
    "rgba(75, 192, 192, 0.6)",
    "rgba(153, 102, 255, 0.6)",
    "rgba(255, 159, 64, 0.6)"
  ];

  // Create gradient fill for each color
  const gradients = gradientColors.map(color => {
    const ctx = leavingreason.getContext("2d");
    const gradient = ctx.createLinearGradient(0, 0, 0, 300);
    gradient.addColorStop(0, color);
    gradient.addColorStop(1, "rgba(255, 255, 255, 0)"); // Transparent gradient
    return gradient;
  });

  new Chart(leavingreason, {
    type: "pie",
    data: {
      labels: ["Red", "Blue", "Yellow", "Green", "Purple", "Orange"],
      datasets: [
        {
          label: "leaving Reason",
          data: [12, 19, 3, 5, 2, 3],
          borderWidth: 1,
          backgroundColor: gradients,
          borderColor: gradientColors
        }
      ]
    },
    options: {
      scales: {
        y: {
          beginAtZero: true
        }
      }
    }
  });

  //Employee Count

  const employeeCount = document.getElementById("employeeCount1");

  new Chart(employeeCount, {
    type: "bar",
    data: {
      labels: ["HR", "Microsoft", "System", "Admin", "IT", "DM"],
      datasets: [
        {
          label: "Distribution Of Employees",
          data: [12, 19, 3, 5, 2, 3],
          backgroundColor: [
            "rgba(255, 99, 132, 0.2)",
            "rgba(255, 159, 64, 0.2)",
            "rgba(255, 205, 86, 0.2)",
            "rgba(75, 192, 192, 0.2)",
            "rgba(54, 162, 235, 0.2)",
            "rgba(153, 102, 255, 0.2)",
            "rgba(201, 203, 207, 0.2)"
          ],
          borderWidth: 1
        }
      ]
    },
    options: {
      scales: {
        y: {
          beginAtZero: true
        }
      }
    }
  });

  // Salary Range

  const salaryRange = document.getElementById("salaryRange");

  new Chart(salaryRange, {
    type: "bar",
    data: {
      labels: ["HR", "Microsoft", "System", "Admin", "IT", "DM"],
      datasets: [
        {
          label: "Distribution Of Salary Range",
          data: [12, 19, 3, 5, 2, 3],
          backgroundColor: [
            "rgba(255, 99, 132, 0.2)",
            "rgba(255, 159, 64, 0.2)",
            "rgba(255, 205, 86, 0.2)",
            "rgba(75, 192, 192, 0.2)",
            "rgba(54, 162, 235, 0.2)",
            "rgba(153, 102, 255, 0.2)",
            "rgba(201, 203, 207, 0.2)"
          ],
          borderWidth: 1
        }
      ]
    },
    options: {
      scales: {
        y: {
          beginAtZero: true
        }
      }
    }
  });

  //Growth Insights

  const growthInsights = document.getElementById("growthInsights");

  new Chart(growthInsights, {
    type: "line",
    data: {
      labels: ["Jan", "Feb", "March", "April", "May", "Jun"],
      datasets: [
        {
          label: "Employee Growth Insights",
          data: [15, 19, 3, 5, 2, 3],
          backgroundColor: [
            "rgba(255, 99, 132, 0.2)",
            "rgba(255, 159, 64, 0.2)",
            "rgba(255, 205, 86, 0.2)",
            "rgba(75, 192, 192, 0.2)",
            "rgba(54, 162, 235, 0.2)",
            "rgba(153, 102, 255, 0.2)",
            "rgba(201, 203, 207, 0.2)"
          ],
          borderWidth: 1
        }
      ]
    },
    options: {
      scales: {
        y: {
          beginAtZero: true
        }
      }
    }
  });
});

$(document).ready(function() {
  var employeeLeaving = document.getElementById("employeeLeaving");

  new Chart(employeeLeaving, {
    type: "bar",
    data: {
      labels: ["HR", "Microsoft", "System", "Admin", "IT", "DM"],
      datasets: [
        {
          label: "Department Wise Leaving Employees",
          data: [12, 19, 3, 5, 2, 3],
          backgroundColor: [
            "rgba(255, 99, 132, 0.2)",
            "rgba(255, 159, 64, 0.2)",
            "rgba(255, 205, 86, 0.2)",
            "rgba(75, 192, 192, 0.2)",
            "rgba(54, 162, 235, 0.2)",
            "rgba(153, 102, 255, 0.2)",
            "rgba(201, 203, 207, 0.2)"
          ],
          borderWidth: 1
        }
      ]
    }
  });

  const TerminationType = document.getElementById("TerminationType");

  new Chart(TerminationType, {
    type: "doughnut",
    data: {
      labels: ["Voluntory", "Involuntory"],
      datasets: [
        {
          label: "Distribution Of Employees",
          data: [1, 4],
          borderWidth: 1
        }
      ]
    },
    options: {
      scales: {
        y: {
          beginAtZero: true
        }
      }
    }
  });

  const byGender = document.getElementById("byGender");

  new Chart(byGender, {
    type: "doughnut",
    data: {
      labels: ["Female", "Male"],
      datasets: [
        {
          label: "Distribution Of Employees",
          data: [10, 20],
          borderWidth: 1
        }
      ]
    },
    options: {
      scales: {
        y: {
          beginAtZero: true
        }
      }
    }
  });
});

$(document).ready(function() {
  const timeHire = document.getElementById("timeHire");

  new Chart(timeHire, {
    type: "bar",
    data: {
      labels: ["HR", "Microsoft", "System", "Admin", "IT", "DM"],
      datasets: [
        {
          label: "Time to hire (Days) per Department",
          data: [12, 19, 3, 5, 2, 3],
          backgroundColor: [
            "rgba(255, 99, 132, 0.2)",
            "rgba(255, 159, 64, 0.2)",
            "rgba(255, 205, 86, 0.2)",
            "rgba(75, 192, 192, 0.2)",
            "rgba(54, 162, 235, 0.2)",
            "rgba(153, 102, 255, 0.2)",
            "rgba(201, 203, 207, 0.2)"
          ],
          borderWidth: 1
        }
      ]
    },
    options: {
      scales: {
        y: {
          beginAtZero: true
        }
      }
    }
  });

  const salaryPredict = document.getElementById("salaryPredict");

  new Chart(salaryPredict, {
    type: "line",
    data: {
      labels: ["HR", "Microsoft", "System", "Admin", "IT", "DM"],
      datasets: [
        {
          label: "Predicted Salary Can Be Offered",
          data: [12, 19, 3, 5, 2, 3],
          backgroundColor: [
            "rgba(255, 99, 132, 0.2)",
            "rgba(255, 159, 64, 0.2)",
            "rgba(255, 205, 86, 0.2)",
            "rgba(75, 192, 192, 0.2)",
            "rgba(54, 162, 235, 0.2)",
            "rgba(153, 102, 255, 0.2)",
            "rgba(201, 203, 207, 0.2)"
          ],
          borderWidth: 1
        }
      ]
    },
    options: {
      scales: {
        y: {
          beginAtZero: true
        }
      }
    }
  });
});

//datatable jquery

$(document).ready(function() {
  var table = $("#example").DataTable({});
});
