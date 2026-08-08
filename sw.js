/* Mass & Balance — service worker.
   Strategy: cache-first, so the app opens instantly and works with zero connectivity,
   with a silent background refresh whenever a connection happens to be available.
   Bump CACHE_VERSION whenever index.html is updated and redeployed. */
const CACHE_VERSION = 'mb-v1';
const CORE_ASSETS = [
  './',
  './index.html',
  './manifest.json',
  './icon-192.png',
  './icon-512.png',
  './icon-512-maskable.png',
];

self.addEventListener('install', event => {
  event.waitUntil(
    caches.open(CACHE_VERSION)
      .then(cache => cache.addAll(CORE_ASSETS))
      .then(() => self.skipWaiting())
  );
});

self.addEventListener('activate', event => {
  event.waitUntil(
    caches.keys()
      .then(names => Promise.all(
        names.filter(n => n !== CACHE_VERSION).map(n => caches.delete(n))
      ))
      .then(() => self.clients.claim())
  );
});

self.addEventListener('fetch', event => {
  if (event.request.method !== 'GET') return;
  event.respondWith(
    caches.match(event.request).then(cached => {
      const network = fetch(event.request)
        .then(resp => {
          if (resp && resp.ok) {
            const copy = resp.clone();
            caches.open(CACHE_VERSION).then(cache => cache.put(event.request, copy));
          }
          return resp;
        })
        .catch(() => cached); /* offline: fall back to whatever is cached, if anything */
      return cached || network;
    })
  );
});
