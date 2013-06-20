routes_in = (
  ('/personas/(?P<alias>[a-zA-Z_]\w*)', '/Poderopedia/personas/conexiones/\g<alias>'),
  ('/personas/(?P<alias>[a-zA-Z_]\w*)/perfil', '/Poderopedia/personas/perfil/\g<alias>'),
  ('/personas/(?P<alias>[a-zA-Z_]\w*)/conexiones', '/Poderopedia/personas/conexiones/\g<alias>'),
  ('/personas/(?P<alias>[a-zA-Z_]\w*)/personasrelacionadas', '/Poderopedia/personas/personasrelacionadas/\g<alias>'),
  ('/personas/(?P<alias>[a-zA-Z_]\w*)/empresasrelacionadas', '/Poderopedia/personas/empresasrelacionadas/\g<alias>'),
  ('/personas/(?P<alias>[a-zA-Z_]\w*)/organizacionesrelacionadas', '/Poderopedia/personas/organizacionesrelacionadas/\g<alias>'),
  ('/personas/(?P<alias>[a-zA-Z_]\w*)/mapa_relaciones', '/Poderopedia/personas/mapa_relaciones/\g<alias>'),
  ('/personas/(?P<alias>[a-zA-Z_]\w*)/documentos/$anything', '/Poderopedia/personas/documentos/\g<alias>/$anything'),
  ('/empresas/(?P<alias>[a-zA-Z_-]+)', '/Poderopedia/empresas/conexiones/\g<alias>'),
  ('/empresas/(?P<alias>[a-zA-Z_-]+)/conexiones', '/Poderopedia/empresas/conexiones/\g<alias>'),
  ('/empresas/(?P<alias>[a-zA-Z_-]+)/personasrelacionadas', '/Poderopedia/empresas/personasrelacionadas/\g<alias>'),
  ('/empresas/(?P<alias>[a-zA-Z_-]+)/empresasrelacionadas', '/Poderopedia/empresas/empresasrelacionadas/\g<alias>'),
  ('/empresas/(?P<alias>[a-zA-Z_-]+)/organizacionesrelacionadas', '/Poderopedia/empresas/organizacionesrelacionadas/\g<alias>'),
  ('/empresas/(?P<alias>[a-zA-Z_-]+)/mapa_relaciones', '/Poderopedia/empresas/mapa_relaciones/\g<alias>'),
  ('/empresas/(?P<alias>[a-zA-Z_-]+)/documentos/$anything', '/Poderopedia/empresas/documentos/\g<alias>/$anything'),
  ('/organizaciones/(?P<alias>[a-zA-Z_-]+)', '/Poderopedia/organizaciones/conexiones/\g<alias>'),
  ('/organizaciones/(?P<alias>[a-zA-Z_-]+)/conexiones', '/Poderopedia/organizaciones/conexiones/\g<alias>'),
  ('/organizaciones/(?P<alias>[a-zA-Z_-]+)/personasrelacionadas', '/Poderopedia/organizaciones/personasrelacionadas/\g<alias>'),
  ('/organizaciones/(?P<alias>[a-zA-Z_-]+)/empresasrelacionadas', '/Poderopedia/organizaciones/empresasrelacionadas/\g<alias>'),
  ('/organizaciones/(?P<alias>[a-zA-Z_-]+)/organizacionesrelacionadas', '/Poderopedia/organizaciones/organizacionesrelacionadas/\g<alias>'),
  ('/organizaciones/(?P<alias>[a-zA-Z_-]+)/mapa_relaciones', '/Poderopedia/organizaciones/mapa_relaciones/\g<alias>'),
  ('/organizaciones/(?P<alias>[a-zA-Z_-]+)/documentos/$anything', '/Poderopedia/organizaciones/documentos/\g<alias>/$anything'),
  ('/','/Poderopedia/default/index'),
  ('/$anything','/Poderopedia/$anything'),
)
routes_out = (
  ('/Poderopedia/personas/conexiones/(?P<alias>[a-zA-Z_]\w*)', '/personas/\g<alias>'),
  ('/Poderopedia/personas/perfil/(?P<alias>[a-zA-Z_]\w*)', '/personas/\g<alias>/perfil'),
  ('/Poderopedia/personas/conexiones/(?P<alias>[a-zA-Z_]\w*)', '/personas/\g<alias>/conexiones'),
  ('/Poderopedia/personas/personasrelacionadas/(?P<alias>[a-zA-Z_]\w*)', '/personas/\g<alias>/personasrelacionadas'),
  ('/Poderopedia/personas/empresasrelacionadas/(?P<alias>[a-zA-Z_]\w*)', '/personas/\g<alias>/empresasrelacionadas'),
  ('/Poderopedia/personas/organizacionesrelacionadas/(?P<alias>[a-zA-Z_]\w*)', '/personas/\g<alias>/organizacionesrelacionadas'),
  ('/Poderopedia/personas/mapa_relaciones/(?P<alias>[a-zA-Z_]\w*)', '/personas/\g<alias>/mapa_relaciones'),
  ('/Poderopedia/personas/documentos/(?P<alias>[a-zA-Z_]\w*)/$anything', '/personas/\g<alias>/documentos/$anything'),
  ('/Poderopedia/empresas/conexiones/(?P<alias>[a-zA-Z_-]+)', '/empresas/\g<alias>'),
  ('/Poderopedia/empresas/conexiones/(?P<alias>[a-zA-Z_-]+)', '/empresas/\g<alias>/conexiones'),
  ('/Poderopedia/empresas/personasrelacionadas/(?P<alias>[a-zA-Z_-]+)', '/empresas/\g<alias>/personasrelacionadas'),
  ('/Poderopedia/empresas/empresasrelacionadas/(?P<alias>[a-zA-Z_-]+)', '/empresas/\g<alias>/empresasrelacionadas'),
  ('/Poderopedia/empresas/organizacionesrelacionadas/(?P<alias>[a-zA-Z_-]+)', '/empresas/\g<alias>/organizacionesrelacionadas'),
  ('/Poderopedia/empresas/mapa_relaciones/(?P<alias>[a-zA-Z_-]+)', '/empresas/\g<alias>/mapa_relaciones'),
  ('/Poderopedia/empresas/documentos/(?P<alias>[a-zA-Z_-]+)/$anything', '/empresas/\g<alias>/documentos/$anything'),
  ('/Poderopedia/organizaciones/conexiones/(?P<alias>[a-zA-Z_-]+)', '/organizaciones/\g<alias>'),
  ('/Poderopedia/organizaciones/conexiones/(?P<alias>[a-zA-Z_-]+)', '/organizaciones/\g<alias>/conexiones'),
  ('/Poderopedia/organizaciones/personasrelacionadas/(?P<alias>[a-zA-Z_-]+)', '/organizaciones/\g<alias>/personasrelacionadas'),
  ('/Poderopedia/organizaciones/empresasrelacionadas/(?P<alias>[a-zA-Z_-]+)', '/organizaciones/\g<alias>/empresasrelacionadas'),
  ('/Poderopedia/organizaciones/organizacionesrelacionadas/(?P<alias>[a-zA-Z_-]+)', '/organizaciones/\g<alias>/organizacionesrelacionadas'),
  ('/Poderopedia/organizaciones/mapa_relaciones/(?P<alias>[a-zA-Z_-]+)', '/organizaciones/\g<alias>/mapa_relaciones'),
  ('/Poderopedia/organizaciones/documentos/(?P<alias>[a-zA-Z_-]+)/$anything', '/organizaciones/\g<alias>/documentos/$anything'),
  ('/Poderopedia/default/index','/'),
  ('/Poderopedia/$anything','/$anything'),
)

routes_onerror = [
  ('*/404', 'error/error404')
]