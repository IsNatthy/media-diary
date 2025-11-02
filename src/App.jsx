import { useState } from 'react';
import Layout from './components/Layout';
import LibraryView from './components/LibraryView';
import CatalogView from './components/CatalogView';
import AddEditForm from './components/AddEditForm';
import DetailView from './components/DetailView';
import { mockCatalog, initialUserMedia } from './data/mockData';

function App() {
  const [currentView, setCurrentView] = useState('library');
  const [userMedia, setUserMedia] = useState(initialUserMedia);
  const [selectedMedia, setSelectedMedia] = useState(null);
  const [showForm, setShowForm] = useState(false);
  const [showDetail, setShowDetail] = useState(false);
  const [editingMedia, setEditingMedia] = useState(null);

  const handleViewChange = (view) => {
    if (view === 'add') {
      setEditingMedia(null);
      setShowForm(true);
    } else {
      setCurrentView(view);
    }
  };

  const handleAddFromCatalog = (catalogItem) => {
    const newMedia = {
      ...catalogItem,
      id: `user-${Date.now()}`,
      status: 'pending',
      rating: 0,
      comments: [],
      currentSeason: 1,
      currentEpisode: 1,
      totalEpisodes: 10,
    };
    setUserMedia([...userMedia, newMedia]);
  };

  const handleSaveMedia = (formData) => {
    if (editingMedia) {
      setUserMedia(
        userMedia.map((m) =>
          m.id === editingMedia.id ? { ...formData, id: editingMedia.id } : m
        )
      );
    } else {
      const newMedia = {
        ...formData,
        id: `user-${Date.now()}`,
        comments: [],
      };
      setUserMedia([...userMedia, newMedia]);
    }
    setShowForm(false);
    setEditingMedia(null);
  };

  const handleEdit = (media) => {
    setEditingMedia(media);
    setShowForm(true);
    setShowDetail(false);
  };

  const handleDelete = (id) => {
    setUserMedia(userMedia.filter((m) => m.id !== id));
  };

  const handleView = (media) => {
    setSelectedMedia(media);
    setShowDetail(true);
  };

  const handleUpdateRating = (id, rating) => {
    setUserMedia(
      userMedia.map((m) => (m.id === id ? { ...m, rating } : m))
    );
    if (selectedMedia && selectedMedia.id === id) {
      setSelectedMedia({ ...selectedMedia, rating });
    }
  };

  const handleAddComment = (id, text) => {
    const newComment = {
      id: `comment-${Date.now()}`,
      text,
      date: new Date().toISOString(),
    };
    setUserMedia(
      userMedia.map((m) =>
        m.id === id
          ? { ...m, comments: [...(m.comments || []), newComment] }
          : m
      )
    );
    if (selectedMedia && selectedMedia.id === id) {
      setSelectedMedia({
        ...selectedMedia,
        comments: [...(selectedMedia.comments || []), newComment],
      });
    }
  };

  const handleDeleteComment = (mediaId, commentId) => {
    setUserMedia(
      userMedia.map((m) =>
        m.id === mediaId
          ? { ...m, comments: m.comments.filter((c) => c.id !== commentId) }
          : m
      )
    );
    if (selectedMedia && selectedMedia.id === mediaId) {
      setSelectedMedia({
        ...selectedMedia,
        comments: selectedMedia.comments.filter((c) => c.id !== commentId),
      });
    }
  };

  const userMediaIds = userMedia.map((m) => m.id.replace('user-', 'cat-'));

  return (
    <Layout currentView={currentView} onViewChange={handleViewChange}>
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
          catalog={mockCatalog}
          onAddFromCatalog={handleAddFromCatalog}
          userMediaIds={userMediaIds}
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
          catalog={mockCatalog}
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
          onUpdateRating={handleUpdateRating}
          onAddComment={handleAddComment}
          onDeleteComment={handleDeleteComment}
        />
      )}
    </Layout>
  );
}

export default App;
