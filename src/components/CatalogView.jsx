import { useState } from 'react';
import { Search, Plus } from 'lucide-react';

export default function CatalogView({ catalog, onAddFromCatalog, userMediaIds }) {
  const [searchTerm, setSearchTerm] = useState('');

  const filteredCatalog = catalog.filter((item) =>
    item.title.toLowerCase().includes(searchTerm.toLowerCase())
  );

  const isAdded = (id) => userMediaIds.includes(id);

  return (
    <div className="space-y-6">
      <div className="bg-white rounded-xl shadow-sm border border-slate-200 p-6">
        <div className="relative">
          <Search className="absolute left-3 top-1/2 transform -translate-y-1/2 w-5 h-5 text-slate-400" />
          <input
            type="text"
            placeholder="Buscar en el catálogo..."
            value={searchTerm}
            onChange={(e) => setSearchTerm(e.target.value)}
            className="w-full pl-10 pr-4 py-2.5 border border-slate-300 rounded-lg focus:ring-2 focus:ring-slate-900 focus:border-transparent outline-none transition-all"
          />
        </div>
      </div>

      {filteredCatalog.length === 0 ? (
        <div className="text-center py-16">
          <div className="inline-flex items-center justify-center w-16 h-16 bg-slate-100 rounded-full mb-4">
            <span className="text-3xl">🔍</span>
          </div>
          <h3 className="text-xl font-semibold text-slate-900 mb-2">
            No se encontraron resultados
          </h3>
          <p className="text-slate-600">
            Intenta con otro término de búsqueda
          </p>
        </div>
      ) : (
        <>
          <h2 className="text-2xl font-bold text-slate-900">
            Catálogo Disponible
            <span className="ml-3 text-lg font-normal text-slate-500">
              ({filteredCatalog.length} {filteredCatalog.length === 1 ? 'título' : 'títulos'})
            </span>
          </h2>

          <div className="grid grid-cols-1 md:grid-cols-2 gap-4">
            {filteredCatalog.map((item) => {
              const added = isAdded(item.id);
              return (
                <div
                  key={item.id}
                  className="bg-white rounded-xl shadow-sm hover:shadow-md transition-all duration-200 overflow-hidden border border-slate-200 flex"
                >
                  <div className="w-24 flex-shrink-0 bg-slate-200">
                    {item.poster ? (
                      <img
                        src={item.poster}
                        alt={item.title}
                        className="w-full h-full object-cover"
                      />
                    ) : (
                      <div className="w-full h-full flex items-center justify-center bg-gradient-to-br from-slate-300 to-slate-400">
                        <span className="text-3xl">🎬</span>
                      </div>
                    )}
                  </div>

                  <div className="flex-1 p-4 flex flex-col justify-between">
                    <div>
                      <h3 className="font-semibold text-slate-900 text-lg mb-1">
                        {item.title}
                      </h3>
                      <div className="flex items-center space-x-3 mb-2">
                        <span className="text-sm text-slate-500">{item.year}</span>
                        <span className="text-xs font-medium px-2 py-1 bg-slate-100 text-slate-700 rounded">
                          {item.type === 'movie' ? 'Película' : 'Serie'}
                        </span>
                      </div>
                      {item.description && (
                        <p className="text-sm text-slate-600 line-clamp-2">
                          {item.description}
                        </p>
                      )}
                    </div>

                    <div className="mt-3">
                      {added ? (
                        <button
                          disabled
                          className="w-full px-4 py-2 bg-slate-100 text-slate-500 rounded-lg font-medium cursor-not-allowed"
                        >
                          Ya agregado
                        </button>
                      ) : (
                        <button
                          onClick={() => onAddFromCatalog(item)}
                          className="w-full flex items-center justify-center space-x-2 bg-gradient-to-r from-green-600 to-green-700 text-white px-4 py-2 rounded-lg font-medium hover:from-green-700 hover:to-green-800 transition-all duration-200"
                        >
                          <Plus className="w-4 h-4" />
                          <span>Agregar a mi biblioteca</span>
                        </button>
                      )}
                    </div>
                  </div>
                </div>
              );
            })}
          </div>
        </>
      )}
    </div>
  );
}
