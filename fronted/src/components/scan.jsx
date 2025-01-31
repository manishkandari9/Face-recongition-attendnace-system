import React, { useState, useRef } from 'react';
import Webcam from "react-webcam";
import axios from 'axios';
import { Button, TextField, List, ListItem, Typography } from '@mui/material';

const API_URL = "http://localhost:8000";

function Scan() {
  const webcamRef = useRef(null);
  const [name, setName] = useState('');
  const [attendance, setAttendance] = useState([]);
  const [loading, setLoading] = useState(false);

  const captureAndSend = async (endpoint) => {
    const imageSrc = webcamRef.current.getScreenshot();
    const formData = new FormData();
    const blob = await fetch(imageSrc).then(res => res.blob());
    formData.append('file', blob, 'face.jpg');

    try {
      const response = await axios.post(`${API_URL}/${endpoint}`, formData, {
        headers: { 'Content-Type': 'multipart/form-data' },
        params: endpoint === 'register' ? { name } : {}
      });
      return response.data;
    } catch (error) {
      console.error('Error:', error);
      return null;
    }
  };

  const handleRegister = async () => {
    setLoading(true);
    const result = await captureAndSend('register');
    if (result?.success) {
      setName('');
      alert('Registration Successful!');
    }
    setLoading(false);
  };

  const handleRecognize = async () => {
    setLoading(true);
    const result = await captureAndSend('recognize');
    if (result?.name) {
      setAttendance(prev => [...prev, {
        name: result.name,
        timestamp: new Date().toLocaleString()
      }]);
    }
    setLoading(false);
  };

  return (
    <div style={{ padding: '20px' }}>
      <Typography variant="h3" gutterBottom>
        Face Recognition Attendance
      </Typography>

      <Webcam
        audio={false}
        ref={webcamRef}
        screenshotFormat="image/jpeg"
        style={{ width: '640px', height: '480px' }}
      />

      <div style={{ margin: '20px 0' }}>
        <TextField
          label="Enter Name"
          value={name}
          onChange={(e) => setName(e.target.value)}
          disabled={loading}
        />
        <Button
          variant="contained"
          color="primary"
          onClick={handleRegister}
          disabled={!name || loading}
          style={{ marginLeft: '10px' }}
        >
          {loading ? 'Registering...' : 'Register Face'}
        </Button>

        <Button
          variant="contained"
          color="secondary"
          onClick={handleRecognize}
          disabled={loading}
          style={{ marginLeft: '10px' }}
        >
          {loading ? 'Recognizing...' : 'Take Attendance'}
        </Button>
      </div>

      <Typography variant="h5">Attendance Records:</Typography>
      <List>
        {attendance.map((entry, index) => (
          <ListItem key={index}>
            {entry.name} - {entry.timestamp}
          </ListItem>
        ))}
      </List>
    </div>
  );
}

export default Scan;