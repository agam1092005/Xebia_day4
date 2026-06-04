'use client';
import React, { useState } from 'react';
import Link from 'next/link';
import { useRouter } from 'next/navigation';

export default function RegisterPage() {
  const [form, setForm] = useState({ username: '', password: '' });
  const router = useRouter();

  const handleSubmit = async (e: React.FormEvent) => {
    e.preventDefault();
    const res = await fetch('http://localhost:8000/register', {
      method: 'POST',
      headers: { 'Content-Type': 'application/json' },
      body: JSON.stringify(form),
    });
    if (res.ok) {
      router.push('/login');
    } else {
      alert('Registration failed');
    }
  };

  return (
    <div className="flex flex-col items-center justify-center min-h-screen bg-white text-black p-4">
      <div className="w-full max-w-sm border border-black p-8 rounded-minimal">
        <h1 className="text-2xl font-light mb-6 text-center">Create Account</h1>
        <form onSubmit={handleSubmit} className="flex flex-col gap-4">
          <input 
            type="text" 
            placeholder="Username" 
            className="w-full p-3 border border-black rounded-minimal outline-none focus:ring-1 focus:ring-black"
            value={form.username}
            onChange={(e) => setForm({...form, username: e.target.value})}
            required
          />
          <input 
            type="password" 
            placeholder="Password" 
            className="w-full p-3 border border-black rounded-minimal outline-none focus:ring-1 focus:ring-black"
            value={form.password}
            onChange={(e) => setForm({...form, password: e.target.value})}
            required
          />
          <button type="submit" className="w-full py-3 bg-black text-white rounded-minimal hover:bg-gray-800 transition-colors">
            Register
          </button>
        </form>
        <div className="mt-6 text-center text-sm">
          Already have an account? <Link href="/login" className="underline">Login</Link>
        </div>
      </div>
    </div>
  );
}
