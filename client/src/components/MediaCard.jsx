import { Star, Clock, CheckCircle2, Play, Edit2, Trash2 } from 'lucide-react';

export default function MediaCard({ media, onEdit, onDelete, onView }) {
  const getStatusConfig = (status) => {
    switch (status) {
      case 'completed':
        return {
          icon: CheckCircle2,
          label: 'Completada',
          bgColor: 'bg-green-100',
          textColor: 'text-green-700',
          borderColor: 'border-green-200',
        };
      case 'watching':
        return {
          icon: Play,
          label: 'En progreso',
          bgColor: 'bg-blue-100',
          textColor: 'text-blue-700',
          borderColor: 'border-blue-200',
        };
      case 'pending':
        return {
          icon: Clock,
          label: 'Por ver',
          bgColor: 'bg-slate-100',
          textColor: 'text-slate-700',
          borderColor: 'border-slate-200',
        };
      default:
        return {
          icon: Clock,
          label: 'Sin estado',
          bgColor: 'bg-slate-100',
          textColor: 'text-slate-700',
          borderColor: 'border-slate-200',
        };
    }
  };

  const statusConfig = getStatusConfig(media.status);
  const StatusIcon = statusConfig.icon;

  return (
    <div className="bg-white rounded-xl shadow-sm hover:shadow-xl transition-all duration-300 overflow-hidden border border-slate-200 group">
      <div className="relative aspect-[2/3] overflow-hidden bg-slate-200">
        {media.poster ? (
          <img
            src={media.poster}
            alt={media.title}
            className="w-full h-full object-cover group-hover:scale-105 transition-transform duration-300"
          />
        ) : (
          <div className="w-full h-full flex items-center justify-center bg-gradient-to-br from-slate-300 to-slate-400">
            <span className="text-6xl text-slate-500">🎬</span>
          </div>
        )}
        <div className="absolute top-3 right-3 flex flex-col space-y-2 opacity-0 group-hover:opacity-100 transition-opacity duration-200">
          <button
            onClick={() => onEdit(media)}
            className="p-2 bg-white/90 backdrop-blur-sm rounded-lg hover:bg-white transition-colors shadow-lg"
          >
            <Edit2 className="w-4 h-4 text-slate-700" />
          </button>
          <button
            onClick={() => onDelete(media.id)}
            className="p-2 bg-white/90 backdrop-blur-sm rounded-lg hover:bg-red-50 transition-colors shadow-lg"
          >
            <Trash2 className="w-4 h-4 text-red-600" />
          </button>
        </div>
      </div>

      <div className="p-4">
        <div className="flex items-start justify-between mb-2">
          <h3
            className="font-semibold text-slate-900 text-lg leading-tight cursor-pointer hover:text-slate-600 transition-colors flex-1"
            onClick={() => onView(media)}
          >
            {media.title}
          </h3>
        </div>

        <div className="flex items-center justify-between mb-3">
          <span className="text-sm text-slate-500">{media.year}</span>
          <span className="text-xs font-medium px-2 py-1 bg-slate-100 text-slate-700 rounded">
            {media.type === 'movie' ? 'Película' : 'Serie'}
          </span>
        </div>

        <div className={`flex items-center space-x-2 px-3 py-2 rounded-lg border ${statusConfig.bgColor} ${statusConfig.borderColor} mb-3`}>
          <StatusIcon className={`w-4 h-4 ${statusConfig.textColor}`} />
          <span className={`text-sm font-medium ${statusConfig.textColor}`}>
            {statusConfig.label}
          </span>
        </div>

        {media.type === 'series' && media.status === 'watching' && (
          <div className="mb-3">
            <div className="flex justify-between text-xs text-slate-600 mb-1">
              <span>Temporada {media.currentSeason}</span>
              <span>Episodio {media.currentEpisode}</span>
            </div>
            <div className="w-full bg-slate-200 rounded-full h-1.5">
              <div
                className="bg-gradient-to-r from-blue-500 to-blue-600 h-1.5 rounded-full transition-all duration-300"
                style={{ width: `${(media.currentEpisode / media.totalEpisodes) * 100}%` }}
              />
            </div>
          </div>
        )}

        {media.rating && (
          <div className="flex items-center space-x-1">
            {[...Array(5)].map((_, i) => (
              <Star
                key={i}
                className={`w-4 h-4 ${
                  i < media.rating
                    ? 'text-yellow-500 fill-yellow-500'
                    : 'text-slate-300'
                }`}
              />
            ))}
          </div>
        )}
      </div>
    </div>
  );
}
