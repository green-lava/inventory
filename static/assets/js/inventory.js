let btn = document.getElementById("btn");
let sidebar = document.querySelector(".sidebar");
let searchBtn = document.querySelector(".bx-search");

btn.addEventListener("click", myFunction);
function myFunction() {
  sidebar.classList.toggle("active");
}
searchBtn.onclick = function () {
  sidebar.classList.toggle("active");
};

let profilebtn = document.getElementById("profilebtn");
let profile = document.querySelector(".profile_popup");
profilebtn.onclick = function () {
  profile.classList.toggle("profile_active");
};

// Area Chart
var options = {
  stroke: {
    curve: "smooth",
  },
  chart: {
    height: 280,
    type: "area",
  },
  dataLabels: {
    enabled: false,
  },
  series: [
    {
      name: "Series 1",
      data: [45, 52, 38, 45, 19, 23, 2],
    },
  ],
  fill: {
    type: "gradient",
    gradient: {
      shadeIntensity: 1,
      opacityFrom: 0.7,
      opacityTo: 0.9,
      stops: [0, 90, 100],
    },
  },
  xaxis: {
    categories: [
      "01 Jan",
      "02 Jan",
      "03 Jan",
      "04 Jan",
      "05 Jan",
      "06 Jan",
      "07 Jan",
    ],
  },
};

var chart = new ApexCharts(document.querySelector("#chart"), options);

chart.render();
// _________________________________________________________________
// Inventry action
// let prductlist = document.getElementById("prductlist");
// let addproduct = document.getElementById("addproduct");
// let updateproduct = document.getElementById("updateproduct");

// let productlistpg = document.querySelector(".productlistpg");
// let addproductpg = document.querySelector(".addproductpg");
// let updateproductpg = document.querySelector(".updateproductpg");

// prductlist.onclick = function () {
//   prductlist.classList.add("activtab");
//   addproduct.classList.remove("activtab");
//   updateproduct.classList.remove("activtab");
//   productlistpg.classList.remove("d-none");
//   addproductpg.classList.add("d-none");
//   updateproductpg.classList.add("d-none");
// };
// addproduct.onclick = function () {
//   prductlist.classList.remove("activtab");
//   addproduct.classList.add("activtab");
//   updateproduct.classList.remove("activtab");
//   productlistpg.classList.add("d-none");
//   addproductpg.classList.remove("d-none");
//   updateproductpg.classList.add("d-none");
// };
// updateproduct.onclick = function () {
//   prductlist.classList.remove("activtab");
//   addproduct.classList.remove("activtab");
//   updateproduct.classList.add("activtab");
//   productlistpg.classList.add("d-none");
//   addproductpg.classList.add("d-none");
//   updateproductpg.classList.remove("d-none");
// };
