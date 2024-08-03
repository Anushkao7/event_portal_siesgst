import React, { useState, useEffect } from 'react';
import { GoogleGenerativeAI } from "@google/generative-ai";

const Feedback = () => {
    const [eventName, setEventName] = useState('');
    const [questions, setQuestions] = useState([]);
    const [rating, setRating] = useState(0);

    const handleStarClick = (starIndex) => {
      setRating(starIndex + 1);
    };
    useEffect(() => {
        // Fetch event name from backend
        // For now, setting a sample event name
        setEventName("Technical Event");

        // Generate questions
        async function generateQuestions() {
            const genAI = new GoogleGenerativeAI('AIzaSyDYecx7ZQUfrUOksHRU1JHLFPxJuHyfy5Y');
            const model = genAI.getGenerativeModel({ model: "gemini-pro" });
            const prompt = `Write me 5 meaningful questions for the feedback form of ${eventName} in proper format only question no other thing`;

            const result = await model.generateContent(prompt);
            const response = await result.response;
            const text = await response.text();

            // Split the text into individual questions
            const generatedQuestions = text.split("\n");
            setQuestions(generatedQuestions);
        }

        generateQuestions();
    }, [eventName]);

    return (
        <div>
            <h2>Feedback form for {eventName}</h2>
            {questions.map((question, index) => (
                <div key={index}>
                    <p>{question}</p>
                    <input type="text" placeholder="Your answer" />
                </div>
            ))}
            <p>pleace rate the event</p>
            {[...Array(5)].map((_, index) => (
        <span
          key={index}
          style={{ cursor: 'pointer', fontSize: '24px' }}
          onClick={() => handleStarClick(index)}
        >
          {index < rating ? '★' : '☆'}
        </span>
      ))}
      <p>Selected Rating: {rating}</p>
            
        </div>
    );
};

export default Feedback;
