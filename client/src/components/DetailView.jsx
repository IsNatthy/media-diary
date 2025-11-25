import { X, Star, Edit2, Trash2, Calendar, Clock, CheckCircle2, Play } from 'lucide-react';

export default function DetailView({ media, onClose, onEdit, onDelete }) {
  const getStatusConfig = (status) => {
    switch (status) {
      case 'completed':
        return { icon: CheckCircle2, label: 'Completada', color: 'text-green-600', bg: 'bg-green-100' };
      case 'watching':
        return { icon: Play, label: 'En progreso', color: 'text-blue-600', bg: 'bg-blue-100' };
      case 'pending':
        return { icon: Clock, label: 'Por ver', color: 'text-slate-600', bg: 'bg-slate-100' };
      default:
        return { icon: Clock, label: 'Sin estado', color: 'text-slate-600', bg: 'bg-slate-100' };
    }
  };

  const statusConfig = getStatusConfig(media.status);
  const StatusIcon = statusConfig.icon;

  return (
    <div className="fixed inset-0 bg-black/50 backdrop-blur-sm flex items-center justify-center z-50 p-4">
      <div className="bg-white rounded-2xl shadow-2xl max-w-4xl w-full max-h-[90vh] overflow-y-auto">
        <div className="sticky top-0 bg-white border-b border-slate-200 px-6 py-4 flex items-center justify-between z-10">
          <h2 className="text-2xl font-bold text-slate-900">Detalles</h2>
          <button
            onClick={onClose}
            className="p-2 hover:bg-slate-100 rounded-lg transition-colors"
          >
            <X className="w-5 h-5 text-slate-600" />
          </button>
        </div>

        <div className="p-6">
          <div className="flex flex-col md:flex-row gap-6 mb-8">
            <div className="w-full md:w-64 flex-shrink-0">
              <div className="aspect-[2/3] rounded-xl overflow-hidden bg-slate-200 shadow-lg">
                {media.poster ? (
                  <img
                    src={media.poster}
                    alt={media.title}
                    className="w-full h-full object-cover"
                  />
                ) : (
                  <div className="w-full h-full flex items-center justify-center bg-gradient-to-br from-slate-300 to-slate-400">
                    <span className="text-6xl">🎬</span>
                  </div>
                )}
              </div>
            </div>

            <div className="flex-1 space-y-4">
              <div>
                <h1 className="text-3xl font-bold text-slate-900 mb-2">{media.title}</h1>
                <div className="flex items-center space-x-4 text-slate-600">
                  <div className="flex items-center space-x-2">
                    <Calendar className="w-4 h-4" />
                    <span>{media.year}</span>
                  </div>
                  <span className="text-xs font-medium px-3 py-1 bg-slate-100 text-slate-700 rounded-full">
                    {media.type === 'movie' ? 'Película' : 'Serie'}
                  </span>
                </div>
              </div>

              {media.description && (
                <p className="text-slate-600 leading-relaxed">{media.description}</p>
              )}

              <div className={`inline-flex items-center space-x-2 px-4 py-2 rounded-lg ${statusConfig.bg}`}>
                <StatusIcon className={`w-5 h-5 ${statusConfig.color}`} />
                <span className={`font-medium ${statusConfig.color}`}>{statusConfig.label}</span>
              </div>

              {media.type === 'series' && (
                <div className="p-4 bg-blue-50 border border-blue-200 rounded-lg space-y-2">
                  <h3 className="font-semibold text-slate-900">Progreso de visualización</h3>
                  <div className="grid grid-cols-3 gap-4 text-sm">
                    <div>
                      <span className="text-slate-600">Temporada:</span>
                      <p className="font-semibold text-slate-900">{media.currentSeason}</p>
                    </div>
                    <div>
                      <span className="text-slate-600">Episodio:</span>
                      <p className="font-semibold text-slate-900">{media.currentEpisode}</p>
                    </div>
                    <div>
                      <span className="text-slate-600">Total episodios:</span>
                      <p className="font-semibold text-slate-900">{media.totalEpisodes}</p>
                    </div>
                  </div>
                  <div className="w-full bg-slate-200 rounded-full h-2 mt-2">
                    <div
                      className="bg-gradient-to-r from-blue-500 to-blue-600 h-2 rounded-full transition-all duration-300"
                      style={{ width: `${(media.currentEpisode / media.totalEpisodes) * 100}%` }}
                    />
                  </div>
                </div>
              )}

              <div className="space-y-2">
                <h3 className="font-semibold text-slate-900">Mi calificación</h3>
                <div className="flex items-center space-x-1">
                  {[1, 2, 3, 4, 5].map((value) => (
                    <div
                      key={value}
                      className="transition-transform"
                    >
                      <Star
                        className={`w-8 h-8 ${
                          value <= media.rating
                            ? 'text-yellow-500 fill-yellow-500'
                            : 'text-slate-300'
                        }`}
                      />
                    </div>
                  ))}
                </div>
              </div>

              {media.review && (
                <div className="space-y-2">
                  <h3 className="font-semibold text-slate-900">Mi Reseña</h3>
                  <div className="bg-slate-50 rounded-lg p-4 border border-slate-200">
                    <p className="text-slate-700 leading-relaxed italic">"{media.review}"</p>
                  </div>
                </div>
              )}

              <div className="flex space-x-3 pt-4">
                <button
                  onClick={() => onEdit(media)}
                  className="flex items-center space-x-2 px-4 py-2 bg-slate-900 text-white rounded-lg font-medium hover:bg-slate-800 transition-colors"
                >
                  <Edit2 className="w-4 h-4" />
                  <span>Editar</span>
                </button>
                <button
                  onClick={() => {
                    if (confirm('¿Estás seguro de que quieres eliminar este contenido?')) {
                      onDelete(media.id);
                      onClose();
                    }
                  }}
                  className="flex items-center space-x-2 px-4 py-2 bg-red-600 text-white rounded-lg font-medium hover:bg-red-700 transition-colors"
                >
                  <Trash2 className="w-4 h-4" />
                  <span>Eliminar</span>
                </button>
              </div>
            </div>
          </div>

          <div className="border-t border-slate-200 pt-6">
          </div>
        </div>
      </div>
    </div>
  );
}
