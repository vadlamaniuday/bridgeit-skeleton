"use client";

import {
  QueryClient,
  QueryClientProvider,
  useQuery,
} from "@tanstack/react-query";

const queryClient = new QueryClient();

export default function Home() {
  return (
    <>
      <QueryClientProvider client={queryClient}>
        <Example />
      </QueryClientProvider>
    </>
  );
}

function Example() {
  const { isPending, error, data } = useQuery({
    queryKey: ["repoData"],
    queryFn: () =>
      fetch("http://localhost:8000/api/items").then((res) => res.json()),
  });

  if (isPending)
    return (
      <div className="flex justify-center items-center h-screen">
        Loading...
      </div>
    );

  if (error)
    return (
      <div className="flex justify-center items-center h-screen text-red-500">
        An error has occurred: {error.message}
      </div>
    );

  return (
    <div className="p-4">
      {data.items.map((item) => (
        <div key={item.id} className="bg-white p-4 rounded-lg shadow-md mb-4">
          <h1 className="text-xl font-bold mb-2">{item.company}</h1>
          <p className="text-gray-700 mb-1">Model: {item.model}</p>
          <p className="text-gray-700 mb-1">Processor: {item.processor}</p>
          <p className="text-gray-700 mb-1">Camera: {item.camera}</p>
          <p className="text-gray-700 mb-1">RAM: {item.ram} GB</p>
          <p className="text-gray-700 mb-1">ROM: {item.rom} GB</p>
          <p className="text-gray-700 mb-1">Price: {item.price}</p>
        </div>
      ))}
    </div>
  );
}
