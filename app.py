import streamlit as st
import streamlit.components.v1 as components

# --- HTML code for the animated deep-dive document ---
# Paste your entire HTML code into this multi-line string.
html_code = """
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>LLM-Based Recommendation Systems - Technical Deep Dive</title>
    <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.5.2/css/all.min.css" xintegrity="sha512-SnH5WK+bZxgPHs44uWIX+LLJAJ9/2PkPKZ5QiAj6Ta86w+fsb2B0I/2S6JvK/8I9L4g2Gv+6T5F5G6w==" crossorigin="anonymous" referrerpolicy="no-referrer" />
    <style>
        * {
            margin: 0;
            padding: 0;
            box-sizing: border-box;
        }
        
        body {
            font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif;
            background: linear-gradient(135deg, #0a0a0a 0%, #1a1a2e 50%, #16213e 100%);
            min-height: 100vh;
            padding: 20px;
            overflow-x: auto;
        }
        
        .main-container {
            background: white;
            border-radius: 24px;
            box-shadow: 0 30px 80px rgba(0,0,0,0.3);
            padding: 40px;
            min-width: 1600px;
            width: 100%;
            position: relative;
            overflow: hidden;
        }
        
        .header {
            text-align: center;
            margin-bottom: 40px;
            position: relative;
        }
        
        .header h1 {
            font-size: 32px;
            color: #1a1a1a;
            margin-bottom: 12px;
            font-weight: 800;
            background: linear-gradient(135deg, #0077b5, #00a0dc);
            -webkit-background-clip: text;
            -webkit-text-fill-color: transparent;
            background-clip: text;
        }
        
        .header p {
            color: #666;
            font-size: 16px;
            font-weight: 500;
        }
        
        .timeline-container {
            display: flex;
            gap: 30px;
            align-items: stretch;
            justify-content: space-between;
            margin-bottom: 40px;
            position: relative;
            min-height: 700px;
        }
        
        .system-card {
            flex: 1;
            background: #fafafa;
            border-radius: 20px;
            padding: 30px;
            position: relative;
            border: 3px solid transparent;
            transition: all 1s cubic-bezier(0.4, 0, 0.2, 1);
            opacity: 0.25;
            transform: translateY(40px) scale(0.92);
            min-height: 650px;
            display: flex;
            flex-direction: column;
            box-shadow: 0 8px 32px rgba(0,0,0,0.1);
        }
        
        .system-card.active {
            opacity: 1;
            transform: translateY(0) scale(1);
            box-shadow: 0 25px 60px rgba(0,0,0,0.15);
        }
        
        .system-card.amazon.active {
            border-color: #ff6b35;
            background: linear-gradient(135deg, #fff8f5, #ffffff);
        }
        
        .system-card.netflix.active {
            border-color: #e50914;
            background: linear-gradient(135deg, #fef5f5, #ffffff);
        }
        
        .system-card.youtube.active {
            border-color: #ff0000;
            background: linear-gradient(135deg, #fff5f5, #ffffff);
        }
        
        .system-card.microsoft.active {
            border-color: #0078d4;
            background: linear-gradient(135deg, #f5f9ff, #ffffff);
        }
        
        .system-card.deepmind.active {
            border-color: #4285f4;
            background: linear-gradient(135deg, #f0f7ff, #ffffff);
        }
        
        .card-header {
            display: flex;
            align-items: center;
            margin-bottom: 25px;
            position: relative;
        }
        
        .company-badge {
            background: #1a1a1a;
            color: white;
            padding: 8px 16px;
            border-radius: 20px;
            font-size: 12px;
            font-weight: 700;
            position: absolute;
            top: -12px;
            right: 0;
            text-transform: uppercase;
        }
        
        .amazon .company-badge { background: #ff6b35; }
        .netflix .company-badge { background: #e50914; }
        .youtube .company-badge { background: #ff0000; }
        .microsoft .company-badge { background: #0078d4; }
        .deepmind .company-badge { background: #4285f4; }
        
        .system-icon {
            width: 60px;
            height: 60px;
            border-radius: 16px;
            display: flex;
            align-items: center;
            justify-content: center;
            margin-right: 16px;
            font-size: 24px;
            color: white;
            font-weight: 800;
            position: relative;
            overflow: hidden;
        }
        
        .amazon .system-icon { 
            background: linear-gradient(135deg, #ff6b35, #ff8c42);
        }
        .netflix .system-icon { 
            background: linear-gradient(135deg, #e50914, #f40612);
        }
        .youtube .system-icon { 
            background: linear-gradient(135deg, #ff0000, #cc0000);
        }
        .microsoft .system-icon { 
            background: linear-gradient(135deg, #0078d4, #106ebe);
        }
        .deepmind .system-icon { 
            background: linear-gradient(135deg, #4285f4, #1a73e8);
        }
        
        .system-title {
            flex: 1;
        }
        
        .system-title h3 {
            font-size: 22px;
            font-weight: 800;
            color: #1a1a1a;
            margin-bottom: 6px;
        }
        
        .system-title p {
            font-size: 14px;
            color: #666;
            font-weight: 600;
        }
        
        .architecture-section {
            margin-bottom: 25px;
        }
        
        .section-title {
            font-size: 16px;
            font-weight: 700;
            color: #1a1a1a;
            margin-bottom: 15px;
            padding-bottom: 8px;
            border-bottom: 3px solid #f0f0f0;
            display: flex;
            align-items: center;
        }
        
        .section-icon {
            margin-right: 10px;
            font-size: 16px;
            width: 24px;
            height: 24px;
            display: flex;
            align-items: center;
            justify-content: center;
            background: #f0f0f0;
            border-radius: 6px;
        }
        
        .tech-stack {
            display: flex;
            flex-wrap: wrap;
            gap: 10px;
            margin-bottom: 20px;
        }
        
        .tech-item {
            background: white;
            border: 2px solid #e8e8e8;
            border-radius: 20px;
            padding: 8px 16px;
            font-size: 12px;
            font-weight: 600;
            color: #1a1a1a;
            transition: all 0.5s ease;
            position: relative;
            overflow: hidden;
        }
        
        .system-card.active .tech-item {
            border-color: inherit;
            background: rgba(255,255,255,0.95);
            animation: techItemFloat 0.8s ease forwards;
        }
        
        .tech-item:nth-child(1) { animation-delay: 0.1s; }
        .tech-item:nth-child(2) { animation-delay: 0.2s; }
        .tech-item:nth-child(3) { animation-delay: 0.3s; }
        .tech-item:nth-child(4) { animation-delay: 0.4s; }
        .tech-item:nth-child(5) { animation-delay: 0.5s; }
        .tech-item:nth-child(6) { animation-delay: 0.6s; }
        .tech-item:nth-child(7) { animation-delay: 0.7s; }
        .tech-item:nth-child(8) { animation-delay: 0.8s; }
        
        @keyframes techItemFloat {
            from { 
                transform: translateY(20px) scale(0.9);
                opacity: 0;
            }
            to { 
                transform: translateY(0) scale(1);
                opacity: 1;
            }
        }
        
        .architecture-flow {
            display: flex;
            flex-direction: column;
            gap: 12px;
            margin-bottom: 20px;
        }
        
        .flow-step {
            background: white;
            border-radius: 12px;
            padding: 16px 20px;
            border-left: 5px solid #e8e8e8;
            font-size: 14px;
            color: #1a1a1a;
            position: relative;
            transition: all 0.6s ease;
            transform: translateX(-20px);
            opacity: 0;
            font-weight: 600;
        }
        
        .system-card.active .flow-step {
            transform: translateX(0);
            opacity: 1;
            border-left-color: inherit;
        }
        
        .flow-step:nth-child(1) { transition-delay: 0.3s; }
        .flow-step:nth-child(2) { transition-delay: 0.5s; }
        .flow-step:nth-child(3) { transition-delay: 0.7s; }
        .flow-step:nth-child(4) { transition-delay: 0.9s; }
        .flow-step:nth-child(5) { transition-delay: 1.1s; }
        .flow-step:nth-child(6) { transition-delay: 1.3s; }
        
        .step-detail {
            font-size: 12px;
            color: #666;
            margin-top: 6px;
            font-style: italic;
            font-weight: 500;
        }
        
        .technical-specs {
            background: rgba(0,0,0,0.04);
            border-radius: 12px;
            padding: 20px;
            margin-top: auto;
        }
        
        .spec-grid {
            display: grid;
            grid-template-columns: 1fr 1fr;
            gap: 12px;
        }
        
        .spec-item {
            display: flex;
            justify-content: space-between;
            font-size: 13px;
            padding: 8px 0;
            border-bottom: 1px solid #e8e8e8;
        }
        
        .spec-item:last-child {
            border-bottom: none;
        }
        
        .spec-label {
            color: #666;
            font-weight: 600;
        }
        
        .spec-value {
            color: #1a1a1a;
            font-weight: 700;
        }
        
        .performance-metrics {
            background: linear-gradient(135deg, #667eea, #764ba2);
            color: white;
            border-radius: 12px;
            padding: 16px;
            margin-top: 15px;
            text-align: center;
            position: relative;
            overflow: hidden;
        }
        
        .metrics-title {
            font-size: 14px;
            font-weight: 700;
            margin-bottom: 10px;
        }
        
        .metrics-grid {
            display: flex;
            justify-content: space-around;
        }
        
        .metric-item {
            text-align: center;
        }
        
        .metric-value {
            font-size: 18px;
            font-weight: 800;
            margin-bottom: 4px;
        }
        
        .metric-label {
            font-size: 11px;
            opacity: 0.9;
        }
        
        .connection-lines {
            position: absolute;
            top: 50%;
            left: 0;
            right: 0;
            height: 4px;
            z-index: 1;
            pointer-events: none;
        }
        
        .data-flow {
            position: absolute;
            height: 100%;
            background: linear-gradient(90deg, transparent, #0077b5, transparent);
            border-radius: 2px;
            opacity: 0;
            animation: dataFlowAnimation 4s ease-in-out infinite;
        }
        
        .data-flow:nth-child(1) {
            left: 19%;
            width: 12%;
            animation-delay: 0s;
        }
        
        .data-flow:nth-child(2) {
            left: 38%;
            width: 12%;
            animation-delay: 1s;
        }
        
        .data-flow:nth-child(3) {
            left: 57%;
            width: 12%;
            animation-delay: 2s;
        }
        
        .data-flow:nth-child(4) {
            left: 76%;
            width: 12%;
            animation-delay: 3s;
        }
        
        @keyframes dataFlowAnimation {
            0% { opacity: 0; transform: scaleX(0.1); }
            25% { opacity: 0.8; transform: scaleX(1); }
            75% { opacity: 0.8; transform: scaleX(1); }
            100% { opacity: 0; transform: scaleX(0.1); }
        }
        
        .controls {
            position: absolute;
            top: 20px;
            right: 20px;
            display: flex;
            gap: 12px;
            z-index: 10;
        }
        
        .control-btn {
            background: #0077b5;
            color: white;
            border: none;
            padding: 10px 16px;
            border-radius: 8px;
            font-size: 13px;
            cursor: pointer;
            transition: all 0.3s ease;
            font-weight: 600;
        }
        
        .control-btn:hover {
            background: #005885;
            transform: translateY(-2px);
        }
        
        .control-btn.active {
            background: #00a0dc;
            box-shadow: 0 4px 12px rgba(0,160,220,0.3);
        }
        
        .progress-indicator {
            height: 8px;
            background: #f0f0f0;
            border-radius: 4px;
            margin: 25px 0;
            position: relative;
            overflow: hidden;
        }
        
        .progress-fill {
            height: 100%;
            background: linear-gradient(90deg, #0077b5, #00a0dc);
            border-radius: 4px;
            width: 20%;
            transition: width 1.2s cubic-bezier(0.4, 0, 0.2, 1);
            position: relative;
        }
        
        .progress-fill::after {
            content: '';
            position: absolute;
            top: 0;
            right: 0;
            width: 20px;
            height: 100%;
            background: linear-gradient(90deg, transparent, rgba(255,255,255,0.3));
            animation: progressShine 2s ease-in-out infinite;
        }
        
        @keyframes progressShine {
            0% { transform: translateX(-100%); }
            50% { transform: translateX(0); }
            100% { transform: translateX(100%); }
        }
        
        .timer-display {
            position: absolute;
            top: 25px;
            left: 25px;
            background: rgba(0,0,0,0.9);
            color: white;
            padding: 12px 20px;
            border-radius: 25px;
            font-size: 16px;
            font-weight: 700;
            z-index: 10;
            display: flex;
            align-items: center;
            gap: 8px;
        }
        
        .current-system {
            position: absolute;
            bottom: 25px;
            left: 50%;
            transform: translateX(-50%);
            background: rgba(0,0,0,0.95);
            color: white;
            padding: 12px 25px;
            border-radius: 25px;
            font-size: 15px;
            font-weight: 600;
            z-index: 10;
        }
        
        .key-insight {
            background: linear-gradient(135deg, #667eea, #764ba2);
            color: white;
            padding: 25px;
            border-radius: 16px;
            margin-top: 30px;
            text-align: center;
            position: relative;
            overflow: hidden;
        }
        
        .key-insight::before {
            content: '';
            position: absolute;
            top: -50%;
            left: -50%;
            width: 200%;
            height: 200%;
            background: radial-gradient(circle, rgba(255,255,255,0.1) 0%, transparent 70%);
            animation: insightPulse 3s ease-in-out infinite;
        }
        
        @keyframes insightPulse {
            0%, 100% { transform: scale(0.8); opacity: 0; }
            50% { transform: scale(1); opacity: 1; }
        }
        
        .insight-title {
            font-size: 18px;
            font-weight: 800;
            margin-bottom: 12px;
            position: relative;
            z-index: 1;
        }
        
        .insight-text {
            font-size: 15px;
            line-height: 1.6;
            position: relative;
            z-index: 1;
        }
        
        @media (max-width: 1400px) {
            .main-container {
                min-width: 100%;
                padding: 25px;
            }
            
            .timeline-container {
                flex-direction: column;
                gap: 25px;
                min-height: auto;
            }
            
            .system-card {
                min-height: 500px;
            }
            
            .connection-lines {
                display: none;
            }
        }
    </style>
</head>
<body>
    <div class="main-container">
        <div class="timer-display" id="timerDisplay">
            ⏱️ <span id="countdown">6.5</span>
        </div>
        <div class="current-system" id="currentSystem">Amazon M6-Rec - Multimodal E-commerce Recommendations</div>
        
        <div class="header">
            <h1>LLM-Based Recommendation Systems: Technical Architecture Deep Dive</h1>
            <p>Comprehensive analysis of production-scale LLM recommendation architectures from industry leaders</p>
        </div>
        
        <div class="controls">
            <button class="control-btn active" onclick="startAnimation()">▶ Play</button>
            <button class="control-btn" onclick="pauseAnimation()">⏸ Pause</button>
            <button class="control-btn" onclick="resetAnimation()">↻ Reset</button>
        </div>
        
        <div class="progress-indicator">
            <div class="progress-fill" id="progressFill"></div>
        </div>
        
        <div class="timeline-container">
            <div class="connection-lines">
                <div class="data-flow"></div>
                <div class="data-flow"></div>
                <div class="data-flow"></div>
                <div class="data-flow"></div>
            </div>
            
            <!-- Amazon M6-Rec -->
            <div class="system-card amazon active" id="card1">
                <div class="card-header">
                    <div class="system-icon">M6</div>
                    <div class="system-title">
                        <h3>Amazon M6-Rec</h3>
                        <p>Multimodal Unified Architecture</p>
                    </div>
                    <div class="company-badge">Amazon</div>
                </div>
                
                <div class="architecture-section">
                    <div class="section-title">
                        <span class="section-icon">🔧</span>
                        Core Technologies
                    </div>
                    <div class="tech-stack">
                        <div class="tech-item">Mixture of Experts (MoE)</div>
                        <div class="tech-item">Cross-Modal Attention</div>
                        <div class="tech-item">Vision Transformer</div>
                        <div class="tech-item">Multi-Task Learning</div>
                        <div class="tech-item">Contrastive Learning</div>
                        <div class="tech-item">Parameter Sharing</div>
                        <div class="tech-item">Knowledge Distillation</div>
                    </div>
                    
                    <div class="section-title">
                        <span class="section-icon">🏗️</span>
                        Architecture Pipeline
                    </div>
                    <div class="architecture-flow">
                        <div class="flow-step">
                            Multimodal Input Encoder
                            <div class="step-detail">Text (BERT-Large), Images (ViT-B/32), Product metadata, User behavior sequences</div>
                        </div>
                        <div class="flow-step">
                            Cross-Modal Fusion Layer
                            <div class="step-detail">Multi-head cross-attention, modality alignment matrices, joint embedding space (768d)</div>
                        </div>
                        <div class="flow-step">
                            Massive LLM Core (100B+ params)
                            <div class="step-detail">Transformer architecture with MoE routing, 48 layers, 128 attention heads</div>
                        </div>
                        <div class="flow-step">
                            Multi-Task Output Heads
                            <div class="step-detail">Search ranking, sponsored ads, product recommendations, personalization scores</div>
                        </div>
                        <div class="flow-step">
                            Real-time Contextual Adaptation
                            <div class="step-detail">Session context integration, dynamic user profiling, A/B testing infrastructure</div>
                        </div>
                    </div>
                </div>
                
                <div class="technical-specs">
                    <div class="spec-grid">
                        <div class="spec-item">
                            <span class="spec-label">Model Size:</span>
                            <span class="spec-value">100B+ params</span>
                        </div>
                        <div class="spec-item">
                            <span class="spec-label">Training Data:</span>
                            <span class="spec-value">10TB+ multimodal</span>
                        </div>
                        <div class="spec-item">
                            <span class="spec-label">Inference Latency:</span>
                            <span class="spec-value">< 50ms</span>
                        </div>
                        <div class="spec-item">
                            <span class="spec-label">Supported Modalities:</span>
                            <span class="spec-value">Text + Image + Meta</span>
                        </div>
                    </div>
                    <div class="performance-metrics">
                        <div class="metrics-title">Production Performance</div>
                        <div class="metrics-grid">
                            <div class="metric-item">
                                <div class="metric-value">15.2%</div>
                                <div class="metric-label">CTR Improvement</div>
                            </div>
                            <div class="metric-item">
                                <div class="metric-value">28%</div>
                                <div class="metric-label">Cold Start Lift</div>
                            </div>
                            <div class="metric-item">
                                <div class="metric-value">12.8%</div>
                                <div class="metric-label">Revenue Impact</div>
                            </div>
                        </div>
                    </div>
                </div>
            </div>
            
            <!-- Netflix RecLLM -->
            <div class="system-card netflix" id="card2">
                <div class="card-header">
                    <div class="system-icon">REC</div>
                    <div class="system-title">
                        <h3>Netflix RecLLM</h3>
                        <p>Streaming-Optimized LLM Architecture</p>
                    </div>
                    <div class="company-badge">Netflix</div>
                </div>
                
                <div class="architecture-section">
                    <div class="section-title">
                        <span class="section-icon">🔧</span>
                        Core Technologies
                    </div>
                    <div class="tech-stack">
                        <div class="tech-item">GPT-4 Base Model</div>
                        <div class="tech-item">LoRA Fine-tuning</div>
                        <div class="tech-item">Prompt Engineering</div>
                        <div class="tech-item">Streaming Context</div>
                        <div class="tech-item">Real-time Learning</div>
                        <div class="tech-item">Latency Optimization</div>
                        <div class="tech-item">Domain Adaptation</div>
                    </div>
                    
                    <div class="section-title">
                        <span class="section-icon">🏗️</span>
                        Architecture Pipeline
                    </div>
                    <div class="architecture-flow">
                        <div class="flow-step">
                            User Context Aggregation
                            <div class="step-detail">Viewing history, ratings, search queries, session behavior, demographic data</div>
                        </div>
                        <div class="flow-step">
                            Streaming-Specific Prompt Templates
                            <div class="step-detail">Genre preferences, watch time patterns, device context, time-of-day signals</div>
                        </div>
                        <div class="flow-step">
                            LLM Inference Engine
                            <div class="step-detail">GPT-4 with Netflix-specific LoRA adapters, streaming domain knowledge base</div>
                        </div>
                        <div class="flow-step">
                            Real-time Ranking and Filtering
                            <div class="step-detail">Content availability, licensing constraints, quality scores, freshness signals</div>
                        </div>
                        <div class="flow-step">
                            Personalized Response Generation
                            <div class="step-detail">Contextual recommendations, explanation generation, confidence scoring</div>
                        </div>
                    </div>
                </div>
                
                <div class="technical-specs">
                    <div class="spec-grid">
                        <div class="spec-item">
                            <span class="spec-label">Base Model:</span>
                            <span class="spec-value">GPT-4 (70B)</span>
                        </div>
                        <div class="spec-item">
                            <span class="spec-label">Fine-tuning:</span>
                            <span class="spec-value">LoRA Adapters</span>
                        </div>
                        <div class="spec-item">
                            <span class="spec-label">Inference Latency:</span>
                            <span class="spec-value">< 100ms</span>
                        </div>
                        <div class="spec-item">
                            <span class="spec-label">Update Frequency:</span>
                            <span class="spec-value">Real-time</span>
                        </div>
                    </div>
                    <div class="performance-metrics">
                        <div class="metrics-title">Streaming Performance</div>
                        <div class="metrics-grid">
                            <div class="metric-item">
                                <div class="metric-value">22%</div>
                                <div class="metric-label">Engagement Lift</div>
                            </div>
                            <div class="metric-item">
                                <div class="metric-value">18%</div>
                                <div class="metric-label">Watch Time ↑</div>
                            </div>
                            <div class="metric-item">
                                <div class="metric-value">31%</div>
                                <div class="metric-label">New Content Discovery</div>
                            </div>
                        </div>
                    </div>
                </div>
            </div>
            
            <!-- YouTube PaLM RecSys -->
            <div class="system-card youtube" id="card3">
                <div class="card-header">
                    <div class="system-icon">YT</div>
                    <div class="system-title">
                        <h3>YouTube PaLM-Rec</h3>
                        <p>Two-Stage Video Recommendation</p>
                    </div>
                    <div class="company-badge">Google</div>
                </div>
                
                <div class="architecture-section">
                    <div class="section-title">
                        <span class="section-icon">🔧</span>
                        Core Technologies
                    </div>
                    <div class="tech-stack">
                        <div class="tech-item">PaLM-2 (540B)</div>
                        <div class="tech-item">Two-Stage Pipeline</div>
                        <div class="tech-item">Video Understanding</div>
                        <div class="tech-item">Few-Shot Learning</div>
                        <div class="tech-item">Contextual Embeddings</div>
                        <div class="tech-item">Massive Retrieval</div>
                        <div class="tech-item">Neural Ranking</div>
                    </div>
                    
                    <div class="section-title">
                        <span class="section-icon">🏗️</span>
                        Architecture Pipeline
                    </div>
                    <div class="architecture-flow">
                        <div class="flow-step">
                            Candidate Recall Stage
                            <div class="step-detail">Video corpus scanning (100M+ videos), semantic similarity, collaborative signals</div>
                        </div>
                        <div class="flow-step">
                            Content Understanding Module
                            <div class="step-detail">Video transcription, thumbnail analysis, metadata extraction, topic modeling</div>
                        </div>
                        <div class="flow-step">
                            PaLM-2 LLM Reranking
                            <div class="step-detail">Scores candidates based on user history and real-time context using a few-shot approach</div>
                        </div>
                        <div class="flow-step">
                            Final Ranking & Diversification
                            <div class="step-detail">Applies business logic and diversity filters before presenting to the user</div>
                        </div>
                        <div class="flow-step">
                            Clickstream & Feedback Loop
                            <div class="step-detail">User interactions are captured and fed back to fine-tune the ranking model</div>
                        </div>
                    </div>
                </div>
                
                <div class="technical-specs">
                    <div class="spec-grid">
                        <div class="spec-item">
                            <span class="spec-label">Base Model:</span>
                            <span class="spec-value">PaLM-2</span>
                        </div>
                        <div class="spec-item">
                            <span class="spec-label">Pipeline:</span>
                            <span class="spec-value">Recall + Rerank</span>
                        </div>
                        <div class="spec-item">
                            <span class="spec-label">Inference Latency:</span>
                            <span class="spec-value">< 200ms</span>
                        </div>
                        <div class="spec-item">
                            <span class="spec-label">Update Frequency:</span>
                            <span class="spec-value">Daily Batches</span>
                        </div>
                    </div>
                    <div class="performance-metrics">
                        <div class="metrics-title">Video Performance</div>
                        <div class="metrics-grid">
                            <div class="metric-item">
                                <div class="metric-value">11%</div>
                                <div class="metric-label">Click-through Rate</div>
                            </div>
                            <div class="metric-item">
                                <div class="metric-value">3.2%</div>
                                <div class="metric-label">Watch Time ↑</div>
                            </div>
                            <div class="metric-item">
                                <div class="metric-value">High</div>
                                <div class="metric-label">Scalability</div>
                            </div>
                        </div>
                    </div>
                </div>
            </div>

            <!-- Microsoft ChatRec -->
            <div class="system-card microsoft" id="card4">
                <div class="card-header">
                    <div class="system-icon">CHAT</div>
                    <div class="system-title">
                        <h3>Microsoft ChatRec</h3>
                        <p>Conversational Recommender Systems</p>
                    </div>
                    <div class="company-badge">Microsoft</div>
                </div>
                
                <div class="architecture-section">
                    <div class="section-title">
                        <span class="section-icon">🔧</span>
                        Core Technologies
                    </div>
                    <div class="tech-stack">
                        <div class="tech-item">Dialogue LLM</div>
                        <div class="tech-item">Session Context</div>
                        <div class="tech-item">Knowledge Graph</div>
                        <div class="tech-item">Retrieval-Augmented Generation (RAG)</div>
                        <div class="tech-item">Multi-turn Conversation</div>
                        <div class="tech-item">User Intent Modeling</div>
                        <div class="tech-item">Dynamic Prompting</div>
                    </div>
                    
                    <div class="section-title">
                        <span class="section-icon">🏗️</span>
                        Architecture Pipeline
                    </div>
                    <div class="architecture-flow">
                        <div class="flow-step">
                            Conversational Intent Parsing
                            <div class="step-detail">Extracts user intent (e.g., "find a sci-fi movie"), entities, and constraints from dialogue</div>
                        </div>
                        <div class="flow-step">
                            Real-time Context & State Tracking
                            <div class="step-detail">Maintains user's conversational state, preferences, and implicit feedback</div>
                        </div>
                        <div class="flow-step">
                            Knowledge Base & Retrieval
                            <div class="step-detail">Queries a product knowledge graph or vector database for relevant items</div>
                        </div>
                        <div class="flow-step">
                            Dialogue LLM Generation
                            <div class="step-detail">Generates a conversational and personalized response, providing recommendations and explanations</div>
                        </div>
                        <div class="flow-step">
                            Feedback & Refinement Loop
                            <div class="step-detail">Processes user responses (e.g., "I don't like that") to refine future recommendations</div>
                        </div>
                    </div>
                </div>
                
                <div class="technical-specs">
                    <div class="spec-grid">
                        <div class="spec-item">
                            <span class="spec-label">Base Model:</span>
                            <span class="spec-value">Proprietary LLM</span>
                        </div>
                        <div class="spec-item">
                            <span class="spec-label">Interactivity:</span>
                            <span class="spec-value">Multi-turn dialogue</span>
                        </div>
                        <div class="spec-item">
                            <span class="spec-label">Ideal Use Case:</span>
                            <span class="spec-value">Chatbots, Q&A</span>
                        </div>
                        <div class="spec-item">
                            <span class="spec-label">Latency:</span>
                            <span class="spec-value">Variable (1-2s)</span>
                        </div>
                    </div>
                    <div class="performance-metrics">
                        <div class="metrics-title">Conversational Performance</div>
                        <div class="metrics-grid">
                            <div class="metric-item">
                                <div class="metric-value">95%</div>
                                <div class="metric-label">User Satisfaction</div>
                            </div>
                            <div class="metric-item">
                                <div class="metric-value">88%</div>
                                <div class="metric-label">Recommendation Accuracy</div>
                            </div>
                            <div class="metric-item">
                                <div class="metric-value">High</div>
                                <div class="metric-label">Personalization</div>
                            </div>
                        </div>
                    </div>
                </div>
            </div>

            <!-- DeepMind RETRO -->
            <div class="system-card deepmind" id="card5">
                <div class="card-header">
                    <div class="system-icon">RETRO</div>
                    <div class="system-title">
                        <h3>DeepMind RETRO</h3>
                        <p>Retrieval-Enhanced Transformer Architecture</p>
                    </div>
                    <div class="company-badge">DeepMind</div>
                </div>
                
                <div class="architecture-section">
                    <div class="section-title">
                        <span class="section-icon">🔧</span>
                        Core Technologies
                    </div>
                    <div class="tech-stack">
                        <div class="tech-item">Retrieval-Augmented LLM</div>
                        <div class="tech-item">k-nearest neighbor (k-NN)</div>
                        <div class="tech-item">Vector Search</div>
                        <div class="tech-item">Massive Corpus Indexing</div>
                        <div class="tech-item">Frozen LLM</div>
                        <div class="tech-item">Causal Attention</div>
                        <div class="tech-item">Contrastive Learning</div>
                    </div>
                    
                    <div class="section-title">
                        <span class="section-icon">🏗️</span>
                        Architecture Pipeline
                    </div>
                    <div class="architecture-flow">
                        <div class="flow-step">
                            Pre-trained Model (Frozen)
                            <div class="step-detail">Uses a large pre-trained LLM (e.g., 7.5B parameters) with frozen weights</div>
                        </div>
                        <div class="flow-step">
                            Massive Retrieval Database
                            <div class="step-detail">A large, indexed corpus (e.g., 2T tokens from Wikipedia, books, web pages) is segmented into chunks</div>
                        </div>
                        <div class="flow-step">
                            K-NN Retrieval at Inference
                            <div class="step-detail">For each generated token, the model queries the database for the k-nearest text chunks</div>
                        </div>
                        <div class="flow-step">
                            Contextualized Token Generation
                            <div class="step-detail">The retrieved chunks are used as additional context in the attention mechanism to generate the next token</div>
                        </div>
                        <div class="flow-step">
                            Continuous Learning Loop
                            <div class="step-detail">New information can be added to the retrieval database without retraining the entire LLM</div>
                        </div>
                    </div>
                </div>
                
                <div class="technical-specs">
                    <div class="spec-grid">
                        <div class="spec-item">
                            <span class="spec-label">Base Model:</span>
                            <span class="spec-value">7.5B params</span>
                        </div>
                        <div class="spec-item">
                            <span class="spec-label">Knowledge Base:</span>
                            <span class="spec-value">2T token corpus</span>
                        </div>
                        <div class="spec-item">
                            <span class="spec-label">Update Cost:</span>
                            <span class="spec-value">Low (Index Update)</span>
                        </div>
                        <div class="spec-item">
                            <span class="spec-label">Freshness:</span>
                            <span class="spec-value">Very High</span>
                        </div>
                    </div>
                    <div class="performance-metrics">
                        <div class="metrics-title">Research Performance</div>
                        <div class="metrics-grid">
                            <div class="metric-item">
                                <div class="metric-value">SOTA</div>
                                <div class="metric-label">Factual Accuracy</div>
                            </div>
                            <div class="metric-item">
                                <div class="metric-value">Low</div>
                                <div class="metric-label">Hallucination Rate</div>
                            </div>
                            <div class="metric-item">
                                <div class="metric-value">High</div>
                                <div class="metric-label">Scalability</div>
                            </div>
                        </div>
                    </div>
                </div>
            </div>
        </div>
        
        <div class="key-insight">
            <div class="insight-title">The Evolution of LLM-Based RecSys: Key Technical Insights</div>
            <div class="insight-text">
                The shift towards LLM-based systems is driven by their ability to handle **unstructured, multimodal data** and perform **complex, nuanced reasoning**. Architectures like Amazon's M6-Rec unify multiple recommendation tasks, while retrieval-focused models like DeepMind's RETRO solve the challenge of **knowledge freshness and scalability**. The choice of architecture depends on the domain, with a clear trade-off between the complexity and a model's ability to offer real-time, personalized experiences.
            </div>
        </div>
    </div>
    
    <script>
        let currentCard = 1;
        let animationInterval;
        let countdownInterval;
        let isPlaying = true;
        let timeLeft = 6.5; // Changed from 12 to 6.5
        
        const cardSystems = [
            "Amazon M6-Rec - Multimodal E-commerce Recommendations",
            "Netflix RecLLM - Streaming-Optimized Architecture", 
            "YouTube PaLM-Rec - Two-Stage Video Recommendation",
            "Microsoft ChatRec - Conversational Recommender Systems",
            "DeepMind RETRO - Retrieval-Enhanced Transformer Architecture"
        ];
        const totalCards = cardSystems.length;
        
        function updateTimer() {
            document.getElementById('countdown').textContent = timeLeft.toFixed(1); // Added .toFixed(1)
            if (timeLeft > 0) {
                timeLeft -= 0.5; // Changed from timeLeft-- to timeLeft -= 0.5
            } else {
                currentCard++;
                if (currentCard > totalCards) {
                    currentCard = 1;
                }
                showCard(currentCard);
                timeLeft = 6.5; // Changed from 12 to 6.5
            }
        }
        
        function showCard(cardNumber) {
            // Update progress bar
            const progressFill = document.getElementById('progressFill');
            progressFill.style.width = `${(cardNumber / totalCards) * 100}%`;
            
            // Update current system text
            document.getElementById('currentSystem').textContent = cardSystems[cardNumber - 1];
            
            // Hide all cards
            for (let i = 1; i <= totalCards; i++) {
                document.getElementById(`card${i}`).classList.remove('active');
            }
            
            // Show current card
            document.getElementById(`card${cardNumber}`).classList.add('active');
            
            // Reset timer
            timeLeft = 6.5; // Changed from 12 to 6.5
        }
        
        function startAnimation() {
            if (isPlaying) return;
            
            isPlaying = true;
            document.querySelector('.control-btn.active').classList.remove('active');
            document.querySelector('.control-btn:first-child').classList.add('active');
            
            countdownInterval = setInterval(updateTimer, 500); // Changed from 1000 to 500
        }
        
        function pauseAnimation() {
            isPlaying = false;
            clearInterval(countdownInterval);
            document.querySelector('.control-btn.active').classList.remove('active');
            document.querySelector('.control-btn:nth-child(2)').classList.add('active');
        }
        
        function resetAnimation() {
            pauseAnimation();
            currentCard = 1;
            timeLeft = 6.5; // Changed from 12 to 6.5
            showCard(1);
            document.querySelector('.control-btn.active').classList.remove('active');
            document.querySelector('.control-btn:last-child').classList.add('active');
        }
        
        // Auto-start animation on load
        document.addEventListener('DOMContentLoaded', function() {
            showCard(1);
            setTimeout(startAnimation, 1000);
        });
        
        // Click on cards to navigate
        document.getElementById('card1').addEventListener('click', function() { pauseAnimation(); currentCard = 1; showCard(1); });
        document.getElementById('card2').addEventListener('click', function() { pauseAnimation(); currentCard = 2; showCard(2); });
        document.getElementById('card3').addEventListener('click', function() { pauseAnimation(); currentCard = 3; showCard(3); });
        document.getElementById('card4').addEventListener('click', function() { pauseAnimation(); currentCard = 4; showCard(4); });
        document.getElementById('card5').addEventListener('click', function() { pauseAnimation(); currentCard = 5; showCard(5); });
    </script>
</body>
</html>
"""

st.set_page_config(layout="wide")
st.title("LLM Recommendation Systems: A Technical Deep Dive")
st.write("This interactive document provides a detailed comparison of modern LLM-based recommendation architectures.")

# Embed the HTML content in the Streamlit app
components.html(html_code, height=900, scrolling=True)