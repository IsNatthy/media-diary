import { useState } from 'react';
import { Search, Filter } from 'lucide-react';
import MediaCard from './MediaCard';

export default function LibraryView({ mediaList, onEdit, onDelete, onView }) {
  const [searchTerm, setSearchTerm] = useState('');
  const [filterStatus, setFilterStatus] = useState('all');
  const [filterType, setFilterType] = useState('all');

  const filteredMedia = mediaList.filter((media) => {
    const matchesSearch = media.title.toLowerCase().includes(searchTerm.toLowerCase());
    const matchesStatus = filterStatus === 'all' || media.status === filterStatus;
    const matchesType = filterType === 'all' || media.type === filterType;
    return matchesSearch && matchesStatus && matchesType;
  });

  return (
    <div className="space-y-6">
      <div className="bg-white rounded-xl shadow-sm border border-slate-200 p-6">
        <div className="flex flex-col md:flex-row md:items-center md:justify-between space-y-4 md:space-y-0 md:space-x-4">
          <div className="flex-1 relative">
            <Search className="absolute left-3 top-1/2 transform -translate-y-1/2 w-5 h-5 text-slate-400" />
            <input
              type="text"
              placeholder="Buscar por título..."
              value={searchTerm}
              onChange={(e) => setSearchTerm(e.target.value)}
              className="w-full pl-10 pr-4 py-2.5 border border-slate-300 rounded-lg focus:ring-2 focus:ring-slate-900 focus:border-transparent outline-none transition-all"
            />
          </div>

          <div className="flex items-center space-x-3">
            <div className="flex items-center space-x-2">
              <Filter className="w-4 h-4 text-slate-600" />
              <select
                value={filterStatus}
                onChange={(e) => setFilterStatus(e.target.value)}
                className="px-3 py-2 border border-slate-300 rounded-lg focus:ring-2 focus:ring-slate-900 focus:border-transparent outline-none bg-white text-sm font-medium text-slate-700"
              >
                <option value="all">Todos los estados</option>
                <option value="completed">Completadas</option>
                <option value="watching">En progreso</option>
                <option value="pending">Por ver</option>
              </select>
            </div>

            <select
              value={filterType}
              onChange={(e) => setFilterType(e.target.value)}
              className="px-3 py-2 border border-slate-300 rounded-lg focus:ring-2 focus:ring-slate-900 focus:border-transparent outline-none bg-white text-sm font-medium text-slate-700"
            >
              <option value="all">Todos los tipos</option>
              <option value="movie">Películas</option>
              <option value="series">Series</option>
            </select>
          </div>
        </div>
      </div>

      {filteredMedia.length === 0 ? (
        <div className="text-center py-16">
          <div className="inline-flex items-center justify-center w-16 h-16 bg-slate-100 rounded-full mb-4">
            <span className="text-3xl">🎬</span>
          </div>
          <h3 className="text-xl font-semibold text-slate-900 mb-2">
            No se encontraron resultados
          </h3>
          <p className="text-slate-600">
            {searchTerm || filterStatus !== 'all' || filterType !== 'all'
              ? 'Intenta ajustar los filtros de búsqueda'
              : 'Comienza agregando películas o series a tu biblioteca'}
          </p>
        </div>
      ) : (
        <>
          <div className="flex items-center justify-between">
            <h2 className="text-2xl font-bold text-slate-900">
              Mi Biblioteca
              <span className="ml-3 text-lg font-normal text-slate-500">
                ({filteredMedia.length} {filteredMedia.length === 1 ? 'título' : 'títulos'})
              </span>
            </h2>
          </div>

          <div className="grid grid-cols-2 sm:grid-cols-3 md:grid-cols-4 lg:grid-cols-5 gap-6">
            {filteredMedia.map((media) => (
              <MediaCard
                key={media.id}
                media={media}
                onEdit={onEdit}
                onDelete={onDelete}
                onView={onView}
              />
            ))}
          </div>
        </>
      )}
    </div>
  );
}
