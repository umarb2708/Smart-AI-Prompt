from flask import Flask, jsonify
import pytest

def test_home_page(client):
    response = client.get('/')
    assert response.status_code == 200
    assert b'Welcome to the Smart AI Prompting Assistant' in response.data

def test_optimize_page(client):
    response = client.get('/optimize')
    assert response.status_code == 200
    assert b'Optimize Your Prompts' in response.data

def test_evaluate_page(client):
    response = client.get('/evaluate')
    assert response.status_code == 200
    assert b'Evaluate Prompt Strategies' in response.data

def test_interact_page(client):
    response = client.get('/interact')
    assert response.status_code == 200
    assert b'Interact with AI' in response.data