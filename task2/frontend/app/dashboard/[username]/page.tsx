'use client';
import React, { useEffect, useState } from 'react';
import { useParams, useRouter } from 'next/navigation';

export default function DashboardPage() {
  const params = useParams();
  const router = useRouter();
  const [message, setMessage] = useState('');

  useEffect(() => {
    async function fetchDashboard() {
      const res = await fetch(`http://localhost:8000/dashboard/${params.username}`);
      if (res.ok) {
        const data = await res.json();
        setMessage(data.message);
      } else {
        router.push('/login');
      }
    }
    fetchDashboard();
  }, [params.username, router]);

  return (
    <div className="flex flex-col items-center justify-center min-h-screen bg-white text-black p-4">
      <div className="w-full max-w-2xl border border-black p-12 rounded-minimal text-center">
        <h1 className="text-3xl font-light mb-4">Dashboard</h1>
        <p className="text-lg mb-8">{message || 'Loading...'}</p>
        <button 
          onClick={() => router.push('/login')} 
          className="px-6 py-2 border border-black rounded-minimal hover:bg-black hover:text-white transition-colors"
        >
          Logout
        </button>
      </div>
    </div>
  );
}
