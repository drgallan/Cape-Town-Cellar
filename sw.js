const C='cc-v3';
self.addEventListener('install',e=>{self.skipWaiting()});
self.addEventListener('activate',e=>{e.waitUntil(caches.keys().then(k=>Promise.all(k.filter(x=>x!==C).map(x=>caches.delete(x)))).then(()=>self.clients.claim()))});
self.addEventListener('fetch',e=>{
  if(e.request.method!=='GET'||!e.request.url.startsWith(self.location.origin))return;
  e.respondWith(caches.open(C).then(c=>fetch(e.request).then(r=>{if(r.ok)c.put(e.request,r.clone());return r}).catch(()=>c.match(e.request))));
});