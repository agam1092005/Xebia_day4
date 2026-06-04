import React from 'react';
import Link from 'next/link';

export default function Page() {
  return (
    <div className="flex flex-col items-center justify-center min-h-screen bg-white text-black p-4">
      <h1 className="text-4xl font-light mb-8 tracking-tight">Welcome</h1>
      <div className="flex flex-col gap-4 w-full max-w-xs">
        <Link href="/login" className="w-full py-3 px-6 border border-black text-center rounded-minimal hover:bg-black hover:text-white transition-colors duration-200">
          Login
        </Link>
        <Link href="/register" className="w-full py-3 px-6 bg-black text-white text-center rounded-minimal hover:bg-gray-800 transition-colors duration-200">
          Register
        </Link>
      </div>
    </div>
  );
}
