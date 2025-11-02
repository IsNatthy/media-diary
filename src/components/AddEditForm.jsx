import { useState, useEffect } from 'react';
import { X, Save, Film, Tv } from 'lucide-react';

export default function AddEditForm({ media, onSave, onCancel, catalog }) {
  const [formData, setFormData] = useState({
    title: '',
    year: new Date().getFullYear(),
    type: 'movie',
    status: 'pending',
    poster: '',
    description: '',
    rating: 0,
    currentSeason: 1,
    currentEpisode: 1,
    totalEpisodes: 10,
  });

  const [suggestions, setSuggestions] = useState([]);
  const [showSuggestions, setShowSuggestions] = useState(false);

  useEffect(() => {
    if (media) {
      setFormData(media);
    }
  }, [media]);

  const handleTitleChange = (value) => {
    setFormData({ ...formData, title: value });

    if (value.length > 2 && !media) {
      const filtered = catalog.filter((item) =>
        item.title.toLowerCase().includes(value.toLowerCase())
      );
      setSuggestions(filtered);
      setShowSuggestions(true);
    } else {
      setSuggestions([]);
      setShowSuggestions(false);
    }
  };

  const selectSuggestion = (item) => {
    setFormData({
      ...formData,
      title: item.title,
      year: item.year,
      type: item.type,
      poster: item.poster || '',
      description: item.description || '',
    });
    setShowSuggestions(false);
  };

  const handleSubmit = (e) => {
    e.preventDefault();
    onSave(formData);
  };

  return (
    <div className="fixed inset-0 bg-black/50 backdrop-blur-sm flex items-center justify-center z-50 p-4">
      <div className="bg-white rounded-2xl shadow-2xl max-w-2xl w-full max-h-[90vh] overflow-y-auto">
        <div className="sticky top-0 bg-white border-b border-slate-200 px-6 py-4 flex items-center justify-between z-10">
          <h2 className="text-2xl font-bold text-slate-900">
            {media ? 'Editar Contenido' : 'Agregar Contenido'}
          </h2>
          <button
            onClick={onCancel}
            className="p-2 hover:bg-slate-100 rounded-lg transition-colors"
          >
            <X className="w-5 h-5 text-slate-600" />
          </button>
        </div>

        <form onSubmit={handleSubmit} className="p-6 space-y-6">
          <div className="relative">
            <label className="block text-sm font-medium text-slate-700 mb-2">
              Título *
            </label>
            <input
              type="text"
              required
              value={formData.title}
              onChange={(e) => handleTitleChange(e.target.value)}
              onFocus={() => formData.title.length > 2 && !media && setShowSuggestions(true)}
              className="w-full px-4 py-2.5 border border-slate-300 rounded-lg focus:ring-2 focus:ring-slate-900 focus:border-transparent outline-none"
              placeholder="Nombre de la película o serie"
            />
            {showSuggestions && suggestions.length > 0 && (
              <div className="absolute top-full left-0 right-0 mt-1 bg-white border border-slate-300 rounded-lg shadow-lg max-h-60 overflow-y-auto z-20">
                {suggestions.map((item) => (
                  <button
                    key={item.id}
                    type="button"
                    onClick={() => selectSuggestion(item)}
                    className="w-full px-4 py-3 hover:bg-slate-50 transition-colors text-left flex items-center space-x-3 border-b border-slate-100 last:border-b-0"
                  >
                    <div className="w-12 h-16 flex-shrink-0 bg-slate-200 rounded overflow-hidden">
                      {item.poster ? (
                        <img src={item.poster} alt={item.title} className="w-full h-full object-cover" />
                      ) : (
                        <div className="w-full h-full flex items-center justify-center bg-gradient-to-br from-slate-300 to-slate-400">
                          <span className="text-xl">🎬</span>
                        </div>
                      )}
                    </div>
                    <div>
                      <div className="font-medium text-slate-900">{item.title}</div>
                      <div className="text-sm text-slate-500">{item.year} • {item.type === 'movie' ? 'Película' : 'Serie'}</div>
                    </div>
                  </button>
                ))}
              </div>
            )}
          </div>

          <div className="grid grid-cols-2 gap-4">
            <div>
              <label className="block text-sm font-medium text-slate-700 mb-2">
                Año *
              </label>
              <input
                type="number"
                required
                min="1900"
                max={new Date().getFullYear() + 5}
                value={formData.year}
                onChange={(e) => setFormData({ ...formData, year: parseInt(e.target.value) })}
                className="w-full px-4 py-2.5 border border-slate-300 rounded-lg focus:ring-2 focus:ring-slate-900 focus:border-transparent outline-none"
              />
            </div>

            <div>
              <label className="block text-sm font-medium text-slate-700 mb-2">
                Tipo *
              </label>
              <div className="grid grid-cols-2 gap-2">
                <button
                  type="button"
                  onClick={() => setFormData({ ...formData, type: 'movie' })}
                  className={`flex items-center justify-center space-x-2 px-4 py-2.5 rounded-lg font-medium transition-all ${
                    formData.type === 'movie'
                      ? 'bg-slate-900 text-white'
                      : 'bg-slate-100 text-slate-700 hover:bg-slate-200'
                  }`}
                >
                  <Film className="w-4 h-4" />
                  <span>Película</span>
                </button>
                <button
                  type="button"
                  onClick={() => setFormData({ ...formData, type: 'series' })}
                  className={`flex items-center justify-center space-x-2 px-4 py-2.5 rounded-lg font-medium transition-all ${
                    formData.type === 'series'
                      ? 'bg-slate-900 text-white'
                      : 'bg-slate-100 text-slate-700 hover:bg-slate-200'
                  }`}
                >
                  <Tv className="w-4 h-4" />
                  <span>Serie</span>
                </button>
              </div>
            </div>
          </div>

          <div>
            <label className="block text-sm font-medium text-slate-700 mb-2">
              Estado *
            </label>
            <select
              value={formData.status}
              onChange={(e) => setFormData({ ...formData, status: e.target.value })}
              className="w-full px-4 py-2.5 border border-slate-300 rounded-lg focus:ring-2 focus:ring-slate-900 focus:border-transparent outline-none"
            >
              <option value="pending">Por ver</option>
              <option value="watching">En progreso</option>
              <option value="completed">Completada</option>
            </select>
          </div>

          {formData.type === 'series' && (
            <div className="grid grid-cols-3 gap-4 p-4 bg-blue-50 border border-blue-200 rounded-lg">
              <div>
                <label className="block text-sm font-medium text-slate-700 mb-2">
                  Temporada actual
                </label>
                <input
                  type="number"
                  min="1"
                  value={formData.currentSeason}
                  onChange={(e) => setFormData({ ...formData, currentSeason: parseInt(e.target.value) || 1 })}
                  className="w-full px-3 py-2 border border-slate-300 rounded-lg focus:ring-2 focus:ring-slate-900 focus:border-transparent outline-none"
                />
              </div>
              <div>
                <label className="block text-sm font-medium text-slate-700 mb-2">
                  Episodio actual
                </label>
                <input
                  type="number"
                  min="1"
                  value={formData.currentEpisode}
                  onChange={(e) => setFormData({ ...formData, currentEpisode: parseInt(e.target.value) || 1 })}
                  className="w-full px-3 py-2 border border-slate-300 rounded-lg focus:ring-2 focus:ring-slate-900 focus:border-transparent outline-none"
                />
              </div>
              <div>
                <label className="block text-sm font-medium text-slate-700 mb-2">
                  Total episodios
                </label>
                <input
                  type="number"
                  min="1"
                  value={formData.totalEpisodes}
                  onChange={(e) => setFormData({ ...formData, totalEpisodes: parseInt(e.target.value) || 10 })}
                  className="w-full px-3 py-2 border border-slate-300 rounded-lg focus:ring-2 focus:ring-slate-900 focus:border-transparent outline-none"
                />
              </div>
            </div>
          )}

          <div>
            <label className="block text-sm font-medium text-slate-700 mb-2">
              URL del póster (opcional)
            </label>
            <input
              type="url"
              value={formData.poster}
              onChange={(e) => setFormData({ ...formData, poster: e.target.value })}
              className="w-full px-4 py-2.5 border border-slate-300 rounded-lg focus:ring-2 focus:ring-slate-900 focus:border-transparent outline-none"
              placeholder="https://ejemplo.com/poster.jpg"
            />
          </div>

          <div>
            <label className="block text-sm font-medium text-slate-700 mb-2">
              Descripción (opcional)
            </label>
            <textarea
              value={formData.description}
              onChange={(e) => setFormData({ ...formData, description: e.target.value })}
              rows="3"
              className="w-full px-4 py-2.5 border border-slate-300 rounded-lg focus:ring-2 focus:ring-slate-900 focus:border-transparent outline-none resize-none"
              placeholder="Breve descripción..."
            />
          </div>

          <div className="flex items-center justify-between pt-6 border-t border-slate-200">
            <button
              type="button"
              onClick={onCancel}
              className="px-6 py-2.5 border border-slate-300 text-slate-700 font-medium rounded-lg hover:bg-slate-50 transition-colors"
            >
              Cancelar
            </button>
            <button
              type="submit"
              className="flex items-center space-x-2 bg-gradient-to-r from-green-600 to-green-700 text-white px-6 py-2.5 rounded-lg font-medium hover:from-green-700 hover:to-green-800 transition-all shadow-md hover:shadow-lg"
            >
              <Save className="w-4 h-4" />
              <span>{media ? 'Guardar Cambios' : 'Agregar'}</span>
            </button>
          </div>
        </form>
      </div>
    </div>
  );
}
