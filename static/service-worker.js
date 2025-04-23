self.addEventListener('install', e => {
    e.waitUntil(
      caches.open('notas-cache').then(cache => {
        return cache.addAll([
          '/',
          '/static/style.css',
          // outros arquivos se tiver
        ]);
      })
    );
  });
  
  self.addEventListener('fetch', e => {
    e.respondWith(
      caches.match(e.request).then(response => response || fetch(e.request))
    );
  });
  