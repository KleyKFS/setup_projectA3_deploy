import { useEffect, useState } from 'react';

export default function Dashboard() {
    const [message, setMessage] = useState("");

    useEffect(() => {
        const socket = new WebSocket("wss://a3-deploy.onrender.com/ws");
        socket.onmessage = (event) => setMessage(event.data);

        return () => socket.close();
 }, []);

 return <div>Mensagem em tempo real: {message}</div>;
}
