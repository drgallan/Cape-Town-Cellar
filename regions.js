window.REGION_GROUPS=[
{g:"Paarl",lat:-33.72,lon:18.96,m:["Voor Paardeberg","Agter-Paarl","Paarl"]},
{g:"Stellenbosch",lat:-33.94,lon:18.86,m:["Stellenbosch","Polkadraai","Bottelary","Banghoek","Jonkershoek","Devon Valley","Helderberg"]},
{g:"Swartland",lat:-33.3,lon:18.73,m:["Swartland","Malmesbury","Paardeberg","Riebeekberg"]},
{g:"Cape Town & Constantia",lat:-33.98,lon:18.45,m:["Constantia","Durbanville","Cape Town"]},
{g:"Franschhoek",lat:-33.91,lon:19.12,m:["Franschhoek"]},
{g:"Wellington",lat:-33.64,lon:19.01,m:["Wellington","Welington","Bovlei","Limietberg"]},
{g:"Tulbagh",lat:-33.28,lon:19.14,m:["Tulbagh"]},
{g:"Darling",lat:-33.37,lon:18.38,m:["Darling","Groenekloof"]},
{g:"Elgin",lat:-34.15,lon:19.03,m:["Elgin"]},
{g:"Hemel-en-Aarde & Bot River",lat:-34.32,lon:19.22,m:["Hemel-en-Aarde","Walker Bay","Bot River"]},
{g:"Cape South Coast",lat:-34.5,lon:19.85,m:["Cape South Coast","Elim","Klein River","Greyton","Sondagskloof","Shaw","Springfontein","Malgas","Swellendam","Duivenhoks","Duivenshok","Overberg","Plettenberg"]},
{g:"Breedekloof & Worcester",lat:-33.65,lon:19.38,m:["Breedekloof","Slanghoek","Worcester","Nuy","Elandskloof"]},
{g:"Robertson",lat:-33.8,lon:19.88,m:["Robertson","McGregor","Bonnievale"]},
{g:"Klein Karoo",lat:-33.5,lon:21.3,m:["Calitzdorp","Klein Karoo","Montagu","Tradouw","Langeberg","Langkloof","Karoo"]},
{g:"West Coast & Cederberg",lat:-32.6,lon:18.9,m:["Piekenierskloof","Citrusdal","Cederberg","Ceres","Olifants","Koekenaap","Bamboes","Cape West Coast","Nieuwoudtville","Prieska","Sutherland"]}
];
window.REGION_OF=function(r){var L=r.toLowerCase();for(var i=0;i<window.REGION_GROUPS.length;i++){var g=window.REGION_GROUPS[i];for(var j=0;j<g.m.length;j++){if(L.indexOf(g.m[j].toLowerCase())>=0)return g.g}}return "Wider Cape"};
