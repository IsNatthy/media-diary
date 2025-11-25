import { useState } from 'react';
import { X, LogIn, UserPlus } from 'lucide-react';

export default function LoginForm({ onLogin, onClose }) {
  const [isRegistering, setIsRegistering] = useState(false);
  const [formData, setFormData] = useState({
    username: '',
    email: '',
    password: '',
  });
  const [error, setError] = useState('');
  const [isLoading, setIsLoading] = useState(false);

  const validateForm = () => {
    if (!formData.email || !/\S+@\S+\.\S+/.test(formData.email)) {
      setError('Por favor ingresa un email válido');
      return false;
    }

    if (isRegistering) {
      if (!formData.username || formData.username.length < 3) {
        setError('El nombre de usuario debe tener al menos 3 caracteres');
        return false;
      }
      if (!formData.password || formData.password.length < 6) {
        setError('La contraseña debe tener al menos 6 caracteres');
        return false;
      }
    } else {
      if (!formData.password) {
        setError('Por favor ingresa tu contraseña');
        return false;
      }
    }
    return true;
  };

  const handleSubmit = async (e) => {
    e.preventDefault();
    setError('');
    
    if (!validateForm()) {
      return;
    }

    setIsLoading(true);

    try {
      if (isRegistering) {
        await onLogin(formData.username, formData.email, formData.password, true);
      } else {
        await onLogin(formData.email, formData.password, false);
      }
      setFormData({ username: '', email: '', password: '' });
    } catch (err) {
      setError(err.message || 'Error al procesar la solicitud');
    } finally {
      setIsLoading(false);
    }
  };

  const toggleMode = () => {
    setIsRegistering(!isRegistering);
    setError('');
    setFormData({ username: '', email: '', password: '' });
  };

  const handleChange = (field, value) => {
    setFormData({ ...formData, [field]: value });
    if (error) setError('');
  };

  return (
    <div className="fixed inset-0 bg-gradient-to-br from-slate-900 via-slate-800 to-slate-900 flex items-center justify-center z-50 p-4">
      <div className="bg-white rounded-2xl shadow-2xl max-w-md w-full overflow-hidden">
        <div className="bg-gradient-to-r from-slate-900 to-slate-800 px-6 py-8 text-center">
          <div className="inline-flex items-center justify-center w-16 h-16 bg-white/10 backdrop-blur-sm rounded-full mb-4">
            <span className="text-4xl">🎬</span>
          </div>
          <h2 className="text-3xl font-bold text-white mb-2">
            Media Diary
          </h2>
          <p className="text-slate-300 text-sm">
            {isRegistering ? 'Crea tu cuenta para comenzar' : 'Bienvenido de vuelta'}
          </p>
        </div>

        <form onSubmit={handleSubmit} className="p-6 space-y-5">
          {error && (
            <div className="bg-red-50 border border-red-200 text-red-700 px-4 py-3 rounded-lg text-sm animate-pulse">
              {error}
            </div>
          )}

          {isRegistering && (
            <div>
              <label className="block text-sm font-medium text-slate-700 mb-2">
                Nombre de usuario
              </label>
              <input
                type="text"
                required
                value={formData.username}
                onChange={(e) => handleChange('username', e.target.value)}
                className="w-full px-4 py-2.5 border border-slate-300 rounded-lg focus:ring-2 focus:ring-slate-900 focus:border-transparent outline-none transition-all"
                placeholder="Tu nombre de usuario"
                disabled={isLoading}
              />
            </div>
          )}

          <div>
            <label className="block text-sm font-medium text-slate-700 mb-2">
              Email
            </label>
            <input
              type="email"
              required
              value={formData.email}
              onChange={(e) => handleChange('email', e.target.value)}
              className="w-full px-4 py-2.5 border border-slate-300 rounded-lg focus:ring-2 focus:ring-slate-900 focus:border-transparent outline-none transition-all"
              placeholder="tu@email.com"
              disabled={isLoading}
            />
          </div>

          <div>
            <label className="block text-sm font-medium text-slate-700 mb-2">
              Contraseña
            </label>
            <input
              type="password"
              required
              value={formData.password}
              onChange={(e) => handleChange('password', e.target.value)}
              className="w-full px-4 py-2.5 border border-slate-300 rounded-lg focus:ring-2 focus:ring-slate-900 focus:border-transparent outline-none transition-all"
              placeholder="Tu contraseña"
              disabled={isLoading}
            />
          </div>

          <button
            type="submit"
            disabled={isLoading}
            className="w-full flex items-center justify-center space-x-2 bg-gradient-to-r from-slate-900 to-slate-800 text-white px-6 py-3 rounded-lg font-medium hover:from-slate-800 hover:to-slate-700 transition-all shadow-md hover:shadow-lg disabled:opacity-50 disabled:cursor-not-allowed"
          >
            {isLoading ? (
              <>
                <div className="w-5 h-5 border-2 border-white/30 border-t-white rounded-full animate-spin" />
                <span>Procesando...</span>
              </>
            ) : (
              <>
                {isRegistering ? (
                  <>
                    <UserPlus className="w-5 h-5" />
                    <span>Crear cuenta</span>
                  </>
                ) : (
                  <>
                    <LogIn className="w-5 h-5" />
                    <span>Iniciar sesión</span>
                  </>
                )}
              </>
            )}
          </button>

          <div className="text-center pt-4 border-t border-slate-200">
            <p className="text-slate-600 text-sm mb-3">
              {isRegistering ? '¿Ya tienes una cuenta?' : '¿No tienes una cuenta?'}
            </p>
            <button
              type="button"
              onClick={toggleMode}
              disabled={isLoading}
              className="text-slate-900 font-medium hover:text-slate-700 transition-colors disabled:opacity-50"
            >
              {isRegistering ? 'Inicia sesión aquí' : 'Regístrate aquí'}
            </button>
          </div>
        </form>
      </div>
    </div>
  );
}
