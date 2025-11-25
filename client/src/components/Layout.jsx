import { Film, Plus, Library, TrendingUp, LogOut, User } from 'lucide-react';

export default function Layout({ children, currentView, onViewChange, currentUser, onLogout }) {
  const navItems = [
    { id: 'library', label: 'Mi Biblioteca', icon: Library },
    { id: 'trending', label: 'Catálogo', icon: TrendingUp },
  ];

  return (
    <div className="min-h-screen bg-gradient-to-br from-slate-50 to-slate-100">
      <nav className="bg-white border-b border-slate-200 sticky top-0 z-50 shadow-sm">
        <div className="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
          <div className="flex justify-between items-center h-16">
            <div className="flex items-center space-x-3">
              <div className="bg-gradient-to-br from-slate-700 to-slate-900 p-2 rounded-lg">
                <Film className="w-6 h-6 text-white" />
              </div>
              <h1 className="text-2xl font-bold bg-gradient-to-r from-slate-700 to-slate-900 bg-clip-text text-transparent">
                Media Diary
              </h1>
            </div>

            <div className="flex items-center space-x-2">
              {navItems.map((item) => {
                const Icon = item.icon;
                const isActive = currentView === item.id;
                return (
                  <button
                    key={item.id}
                    onClick={() => onViewChange(item.id)}
                    className={`flex items-center space-x-2 px-4 py-2 rounded-lg font-medium transition-all duration-200 ${
                      isActive
                        ? 'bg-slate-900 text-white shadow-md'
                        : 'text-slate-600 hover:bg-slate-100 hover:text-slate-900'
                    }`}
                  >
                    <Icon className="w-4 h-4" />
                    <span>{item.label}</span>
                  </button>
                );
              })}
            </div>

            <div className="flex items-center space-x-3">
              <button
                onClick={() => onViewChange('add')}
                className="flex items-center space-x-2 bg-gradient-to-r from-green-600 to-green-700 text-white px-4 py-2 rounded-lg font-medium hover:from-green-700 hover:to-green-800 transition-all duration-200 shadow-md hover:shadow-lg"
              >
                <Plus className="w-4 h-4" />
                <span>Agregar</span>
              </button>

              {currentUser && (
                <div className="flex items-center space-x-2 border-l border-slate-200 pl-3">
                  <div className="flex items-center space-x-2 text-slate-700">
                    <User className="w-4 h-4" />
                    <span className="text-sm font-medium">{currentUser.username}</span>
                  </div>
                  <button
                    onClick={onLogout}
                    className="flex items-center space-x-1 px-3 py-2 text-slate-600 hover:text-red-600 hover:bg-red-50 rounded-lg transition-all duration-200"
                    title="Cerrar sesión"
                  >
                    <LogOut className="w-4 h-4" />
                  </button>
                </div>
              )}
            </div>
          </div>
        </div>
      </nav>

      <main className="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 py-8">
        {children}
      </main>
    </div>
  );
}
