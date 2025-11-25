import { useState, useEffect } from 'react';
import Layout from './components/Layout';
import LibraryView from './components/LibraryView';
import CatalogView from './components/CatalogView';
import AddEditForm from './components/AddEditForm';
import DetailView from './components/DetailView';
import LoginForm from './components/LoginForm';
import { getCatalog } from './api/catalog';
import { login, register, logout, checkAuth } from './api/auth';
import { getLibrary, addContent, updateContent, deleteContent } from './api/library';

function App() {
  // Estado de autenticación
  const [currentUser, setCurrentUser] = useState(null);
  const [isLoading, setIsLoading] = useState(true);

  // Estados existentes
  const [currentView, setCurrentView] = useState('library');
  const [userMedia, setUserMedia] = useState([]);
  const [catalog, setCatalog] = useState([]);
  const [selectedMedia, setSelectedMedia] = useState(null);
  const [showForm, setShowForm] = useState(false);
  const [showDetail, setShowDetail] = useState(false);
  const [editingMedia, setEditingMedia] = useState(null);

  // Verificar sesión al cargar
  useEffect(() => {
    const initAuth = async () => {
      try {
        const user = await checkAuth();
        if (user) {
          setCurrentUser(user);
          fetchLibrary();
        }
      } catch (error) {
        console.log("No session found");
      } finally {
        setIsLoading(false);
      }
    };
    initAuth();
    fetchCatalog();
  }, []);

  const fetchLibrary = async () => {
    try {
      const library = await getLibrary();
      setUserMedia(library);
    } catch (error) {
      console.error("Error fetching library:", error);
    }
  };

  const fetchCatalog = async () => {
    try {
      const data = await getCatalog();
      setCatalog(data);
    } catch (error) {
      console.error("Error fetching catalog:", error);
    }
  };

  const handleViewChange = (view) => {
    if (view === 'add') {
      setEditingMedia(null);
      setShowForm(true);
    } else {
      setCurrentView(view);
    }
  };

  const handleAddFromCatalog = async (catalogItem) => {
    try {
      const newMediaData = {
        ...catalogItem,
        status: 'pending',
        rating: 0,
        current_season: 1,
        current_episode: 1,
        total_episodes: catalogItem.totalEpisodes || 10, // Adjust based on catalog data
      };
      const newMedia = await addContent(newMediaData);
      setUserMedia([...userMedia, newMedia]);
    } catch (error) {
      console.error("Error adding from catalog:", error);
    }
  };

  const handleSaveMedia = async (formData) => {
    try {
      if (editingMedia) {
        const updatedMedia = await updateContent(editingMedia.id, formData);
        setUserMedia(
          userMedia.map((m) =>
            m.id === editingMedia.id ? updatedMedia : m
          )
        );
      } else {
        const newMedia = await addContent(formData);
        setUserMedia([...userMedia, newMedia]);
      }
      setShowForm(false);
      setEditingMedia(null);
    } catch (error) {
      console.error("Error saving media:", error);
      const message = error.response?.data?.message || error.message;
      throw new Error(message);
    }
  };

  const handleEdit = (media) => {
    setEditingMedia(media);
    setShowForm(true);
    setShowDetail(false);
  };

  const handleDelete = async (id) => {
    try {
      await deleteContent(id);
      setUserMedia(userMedia.filter((m) => m.id !== id));
      if (selectedMedia && selectedMedia.id === id) {
        setShowDetail(false);
        setSelectedMedia(null);
      }
    } catch (error) {
      console.error("Error deleting media:", error);
    }
  };

  const handleView = (media) => {
    setSelectedMedia(media);
    setShowDetail(true);
  };

  const userMediaIds = userMedia.map((m) => m.id);

  // Funciones de autenticación
  const handleLogin = async (usernameOrEmail, emailOrPassword, passwordOrUndefined, isRegistering) => {
    setIsLoading(true);
    
    try {
      if (isRegistering) {
        // Registering: username, email, password, true
        const username = usernameOrEmail;
        const email = emailOrPassword;
        const password = passwordOrUndefined;
        
        if (username && email && password) {
          await register(username, email, password);
          await login(email, password);
          const user = await checkAuth();
          setCurrentUser(user);
          fetchLibrary();
          console.log('Usuario registrado exitosamente');
        } else {
          throw new Error('Todos los campos son requeridos');
        }
      } else {
        // Login: email, password, false
        const email = usernameOrEmail;
        const password = emailOrPassword;
        
        if (email && password) {
          await login(email, password);
          const user = await checkAuth();
          setCurrentUser(user);
          fetchLibrary();
          console.log('Login exitoso');
        } else {
          throw new Error('Email o contraseña inválidos');
        }
      }
    } catch (error) {
      console.error('Error de autenticación:', error);
      const message = error.response?.data?.message || error.message;
      throw new Error(message);
    } finally {
      setIsLoading(false);
    }
  };

  const handleLogout = async () => {
    try {
      await logout();
      setCurrentUser(null);
      setUserMedia([]);
      setCurrentView('library');
    } catch (error) {
      console.error("Error logging out", error);
    }
  };

  if (isLoading) {
    return <div className="flex items-center justify-center h-screen">Cargando...</div>;
  }

  // Si no hay usuario autenticado, mostrar LoginForm
  if (!currentUser) {
    return <LoginForm onLogin={handleLogin} />;
  }

  // Si hay usuario autenticado, mostrar la aplicación normal
  return (
    <Layout 
      currentView={currentView} 
      onViewChange={handleViewChange}
      currentUser={currentUser}
      onLogout={handleLogout}
    >
      {currentView === 'library' && (
        <LibraryView
          mediaList={userMedia}
          onEdit={handleEdit}
          onDelete={handleDelete}
          onView={handleView}
        />
      )}

      {currentView === 'trending' && (
        <CatalogView
          catalog={catalog}
          onAddFromCatalog={handleAddFromCatalog}
          userMedia={userMedia}
        />
      )}

      {showForm && (
        <AddEditForm
          media={editingMedia}
          onSave={handleSaveMedia}
          onCancel={() => {
            setShowForm(false);
            setEditingMedia(null);
          }}
          catalog={catalog}
        />
      )}

      {showDetail && selectedMedia && (
        <DetailView
          media={selectedMedia}
          onClose={() => {
            setShowDetail(false);
            setSelectedMedia(null);
          }}
          onEdit={handleEdit}
          onDelete={handleDelete}
        />
      )}
    </Layout>
  );
}

export default App;
