// src/layouts/AdminLayout.jsx
import React from 'react';
import AdminSidebar from '../components/AdminSidebar';
import '../styles/AdminLayout.module.css';

function AdminLayout({ children }) {
  return (
    <div className="admin-layout">
      <aside className="admin-layout__sidebar">
        <AdminSidebar />
      </aside>

      <section className="admin-layout__content">
        {children}
      </section>
    </div>
  );
}

export default AdminLayout;
