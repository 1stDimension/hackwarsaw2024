import{r as d,_,c as l,t as s,a as f,b as t,F as h,d as m,o as c}from"./index-CnKrj_Aj.js";const p=()=>{const r=d([]),o=d(null);return{voters:r,error:o,load:async()=>{try{let e=await fetch("http://localhost:8000/voter",{method:"GET",redirect:"follow"});if(!e.ok)throw Error("ERROR: fetching voters");r.value=await e.json()}catch(e){o.value=e.message}}}},g={name:"voters",setup(){const{voters:r,error:o,load:a}=p();return a(),{voters:r,error:o}},data(){return{}},methods:{async presentChange(r,o){console.log(r,o);let a="http://localhost:8000/voter/"+r;o?a+="/present":a+="/absent";try{let e=await fetch(a,{method:"POST",redirect:"follow"});if(!e.ok)throw Error("ERROR: fetching voters");voters.value=await e.json()}catch(e){error.value=e.message}}}},v={key:0},w=t("div",{class:"about"},[t("h1",null,"Voters List")],-1),k=t("tr",null,[t("th",null,"present"),t("th",null,"first name"),t("th",null,"last name"),t("th",null,"local number")],-1),y=["value","onChange"];function b(r,o,a,e,C,u){return c(),l(h,null,[e.error?(c(),l("div",v,s(e.error),1)):f("",!0),w,t("table",null,[k,(c(!0),l(h,null,m(e.voters.voters,n=>(c(),l("tr",{key:n.id},[t("td",null,[t("input",{type:"checkbox",value:n.id,onChange:i=>u.presentChange(n.id,i.target.checked)},null,40,y)]),t("td",null,s(n.first_name),1),t("td",null,s(n.last_name),1),t("td",null,s(n.local),1)]))),128))])],64)}const R=_(g,[["render",b]]);export{R as default};