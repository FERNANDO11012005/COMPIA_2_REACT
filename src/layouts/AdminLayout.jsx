import React, { useState } from 'react';
import { Link } from 'react-router-dom';
import "../styles/AdminLayout.module.css";

function AdminLayout() {
  const [collapsed, setCollapsed] = useState(false);

  return (
    <div className="admin-layout">
      <aside className={`sidebar ${collapsed ? 'collapsed' : ''}`}>
        <button className="toggle-btn" onClick={() => setCollapsed(!collapsed)}>
          ☰
        </button>
        <h2 className="sidebar-title">{!collapsed && 'Panel Admin'}</h2>
        <nav className="sidebar-nav">
          <Link to="#" className="nav-link">
            <span className="icon">🏠</span>
            {!collapsed && 'Inicio'}
          </Link>
          <Link to="#" className="nav-link">
            <span className="icon">📦</span>
            {!collapsed && 'Productos'}
          </Link>
          <Link to="#" className="nav-link">
            <span className="icon">📊</span>
            {!collapsed && 'Reportes'}
          </Link>
          <Link to="#" className="nav-link">
            <span className="icon">⭐</span>
            {!collapsed && 'Favoritos'}
          </Link>
        </nav>
      </aside>

      <main className="admin-content">
        <div className="admin-welcome">
          <h2>Bienvenido al panel de administración</h2>
          <p>Selecciona una opción del menú lateral para comenzar.</p>
        </div>
      </main>
    </div>
  );
}

export default AdminLayout;
