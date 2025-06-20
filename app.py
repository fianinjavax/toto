import streamlit as st
from datetime import datetime, timedelta
import time
from optimized_bbfs_system import get_optimized_system

# Configure for production deployment
@st.cache_resource
def load_system():
    """Load system with caching for better performance"""
    try:
        # Allow URL to be customized via environment variable or use default
        import os
        custom_url = os.getenv('DATA_SOURCE_URL', None)
        return get_optimized_system(custom_url)
    except Exception as e:
        st.error(f"Error loading system: {str(e)}")
        return None

def main():
    st.set_page_config(
        page_title="BBFS Mobile Pro", 
        page_icon="📱",
        layout="centered",
        initial_sidebar_state="collapsed"
    )
    
    # Ultra-Premium Mobile App Theme
    st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Inter:wght@100;200;300;400;500;600;700;800;900&family=JetBrains+Mono:wght@400;500;600;700&display=swap');
    
    /* Remove Streamlit elements */
    header[data-testid="stHeader"] {
        height: 0rem !important;
        display: none !important;
    }
    
    .stApp > header {
        height: 0rem !important;
        display: none !important;
    }
    
    #MainMenu {
        visibility: hidden !important;
    }
    
    footer {
        visibility: hidden !important;
    }
    
    .viewerBadge_container__1QSob {
        display: none !important;
    }
    
    /* Optimized Mobile Container */
    .main .block-container {
        padding: 70px 0 0 0 !important;
        max-width: 375px !important;
        margin: 0 auto !important;
        background: #000000;
        min-height: 100vh;
    }
    
    .stApp {
        background: linear-gradient(180deg, #000000 0%, #1a1a1a 100%);
        min-height: 100vh;
        position: relative;
        overflow-x: hidden;
    }
    
    .main {
        background: transparent;
        font-family: 'Inter', -apple-system, BlinkMacSystemFont, sans-serif;
        color: #ffffff;
        padding: 0;
        margin: 0;
        position: relative;
        z-index: 2;
    }
    
    /* Optimized Mobile Header */
    .mobile-header {
        background: rgba(0, 0, 0, 0.95);
        backdrop-filter: blur(20px);
        -webkit-backdrop-filter: blur(20px);
        border-bottom: 1px solid rgba(255, 255, 255, 0.1);
        padding: 16px 20px 12px 20px;
        margin: 0;
        position: fixed;
        top: 0;
        left: 0;
        right: 0;
        z-index: 1000;
        box-shadow: 0 2px 20px rgba(0, 0, 0, 0.3);
    }
    
    .app-title {
        font-family: 'Inter', sans-serif;
        font-size: 22px;
        font-weight: 600;
        color: #ffffff;
        text-align: center;
        margin: 0;
        letter-spacing: -0.5px;
    }
    
    .app-subtitle {
        font-size: 11px;
        font-weight: 400;
        color: rgba(255, 255, 255, 0.7);
        text-align: center;
        margin: 2px 0 0 0;
        letter-spacing: 0.5px;
        text-transform: uppercase;
    }
    
    /* Premium Status Bar */
    .status-bar {
        background: linear-gradient(135deg, rgba(255, 255, 255, 0.08) 0%, rgba(255, 255, 255, 0.04) 100%);
        backdrop-filter: blur(20px);
        -webkit-backdrop-filter: blur(20px);
        border: 1px solid rgba(255, 255, 255, 0.1);
        border-radius: 20px;
        padding: 16px 24px;
        margin: 16px 12px;
        text-align: center;
        box-shadow: 
            0 8px 32px rgba(0, 0, 0, 0.3),
            inset 0 1px 0 rgba(255, 255, 255, 0.1),
            0 0 0 1px rgba(255, 255, 255, 0.05);
        position: relative;
        overflow: hidden;
    }
    

    
    .status-text {
        font-size: 13px;
        font-weight: 500;
        color: rgba(255, 255, 255, 0.9);
        margin: 0;
        position: relative;
        z-index: 1;
        letter-spacing: 0.2px;
    }
    
    /* Optimized Card Components */
    .mobile-card {
        background: rgba(255, 255, 255, 0.08);
        backdrop-filter: blur(15px);
        -webkit-backdrop-filter: blur(15px);
        border: 1px solid rgba(255, 255, 255, 0.12);
        border-radius: 20px;
        margin: 12px;
        padding: 18px;
        box-shadow: 0 8px 24px rgba(0, 0, 0, 0.3);
        transition: transform 0.2s ease;
    }
    
    .mobile-card:hover {
        transform: translateY(-1px);
    }
    
    .prediction-card {
        background: rgba(26, 26, 46, 0.9);
        backdrop-filter: blur(20px);
        -webkit-backdrop-filter: blur(20px);
        border: 1px solid rgba(233, 69, 96, 0.2);
        border-radius: 20px;
        margin: 16px 12px;
        padding: 24px;
        text-align: center;
        box-shadow: 0 12px 32px rgba(233, 69, 96, 0.2);
    }
    

    
    .analytics-card {
        background: rgba(255, 255, 255, 0.08);
        backdrop-filter: blur(15px);
        border-radius: 16px;
        padding: 1.5rem;
        margin: 1rem 0;
        border: 1px solid rgba(255, 255, 255, 0.15);
        transition: all 0.3s ease;
    }
    
    .analytics-card:hover {
        background: rgba(255, 255, 255, 0.12);
        border: 1px solid rgba(255, 255, 255, 0.25);
    }
    
    /* Optimized BBFS Display */
    .bbfs-display {
        background: linear-gradient(135deg, #1a1a2e 0%, #16213e 50%, #e94560 100%);
        color: #ffffff;
        font-family: 'JetBrains Mono', monospace;
        font-size: 30px;
        font-weight: 700;
        text-align: center;
        padding: 20px;
        border-radius: 16px;
        margin: 0;
        letter-spacing: 4px;
        box-shadow: 0 8px 24px rgba(233, 69, 96, 0.3);
        border: 1px solid rgba(233, 69, 96, 0.4);
        position: relative;
        z-index: 1;
    }
    
    /* Premium Section Headers */
    .section-header {
        font-family: 'Inter', sans-serif;
        font-size: 18px;
        font-weight: 600;
        color: rgba(255, 255, 255, 0.95);
        margin: 32px 16px 16px 16px;
        letter-spacing: -0.4px;
        position: relative;
        padding-left: 12px;
    }
    
    .section-header::before {
        content: '';
        position: absolute;
        left: 0;
        top: 50%;
        transform: translateY(-50%);
        width: 4px;
        height: 20px;
        background: linear-gradient(135deg, #e94560, #0f3460);
        border-radius: 2px;
    }
    
    /* Optimized Metrics Grid */
    .metrics-grid {
        display: grid;
        grid-template-columns: 1fr 1fr;
        gap: 10px;
        margin: 16px 12px;
    }
    
    .metric-item {
        background: rgba(255, 255, 255, 0.06);
        backdrop-filter: blur(15px);
        -webkit-backdrop-filter: blur(15px);
        border: 1px solid rgba(255, 255, 255, 0.1);
        border-radius: 16px;
        padding: 16px 12px;
        text-align: center;
        transition: transform 0.2s ease;
        box-shadow: 0 4px 16px rgba(0, 0, 0, 0.2);
    }
    
    .metric-item:active {
        transform: scale(0.98);
    }
    
    .metric-value {
        font-family: 'Inter', sans-serif;
        font-size: 22px;
        font-weight: 700;
        color: #e94560;
        margin: 0 0 4px 0;
        text-shadow: 0 0 20px rgba(233, 69, 96, 0.3);
    }
    
    .metric-label {
        font-size: 11px;
        font-weight: 500;
        color: rgba(255, 255, 255, 0.7);
        margin: 0;
        letter-spacing: 0.5px;
        text-transform: uppercase;
    }
    
    /* Current Streak */
    .current-streak {
        background: linear-gradient(135deg, #FF3B30 0%, #FF6B35 100%);
        border-radius: 20px;
        padding: 20px;
        margin: 16px;
        text-align: center;
        box-shadow: 0 8px 32px rgba(255, 59, 48, 0.3);
        border: 1px solid rgba(255, 255, 255, 0.2);
    }
    
    .current-streak.success {
        background: linear-gradient(135deg, #30D158 0%, #00D4AA 100%);
        box-shadow: 0 8px 32px rgba(48, 209, 88, 0.3);
    }
    
    .streak-number {
        font-family: 'SF Pro Display', sans-serif;
        font-size: 40px;
        font-weight: 900;
        color: #ffffff;
        margin: 0;
    }
    
    .streak-label {
        font-size: 16px;
        font-weight: 600;
        color: rgba(255, 255, 255, 0.9);
        margin: 4px 0 0 0;
    }
    
    /* Optimized Results List */
    .results-list {
        background: rgba(255, 255, 255, 0.05);
        backdrop-filter: blur(15px);
        -webkit-backdrop-filter: blur(15px);
        border-radius: 20px;
        margin: 16px 12px;
        overflow: hidden;
        border: 1px solid rgba(255, 255, 255, 0.08);
        box-shadow: 0 8px 24px rgba(0, 0, 0, 0.3);
    }
    
    .result-item {
        padding: 18px 20px;
        border-bottom: 1px solid rgba(255, 255, 255, 0.05);
        display: flex;
        justify-content: space-between;
        align-items: center;
        transition: all 0.3s cubic-bezier(0.25, 0.46, 0.45, 0.94);
        position: relative;
        overflow: hidden;
    }
    

    
    .result-item:last-child {
        border-bottom: none;
    }
    
    .result-item:active {
        background: rgba(255, 255, 255, 0.08);
        transform: scale(0.99);
    }
    
    .result-left {
        flex: 1;
        padding-left: 8px;
    }
    
    .result-date {
        font-size: 12px;
        font-weight: 500;
        color: rgba(255, 255, 255, 0.6);
        margin: 0 0 4px 0;
        text-transform: uppercase;
        letter-spacing: 0.5px;
    }
    
    .result-numbers {
        font-size: 15px;
        font-weight: 600;
        color: #ffffff;
        margin: 0;
        font-family: 'JetBrains Mono', monospace;
        letter-spacing: 1px;
    }
    
    .result-status {
        font-size: 12px;
        font-weight: 700;
        padding: 8px 16px;
        border-radius: 16px;
        text-transform: uppercase;
        letter-spacing: 1px;
        backdrop-filter: blur(10px);
        -webkit-backdrop-filter: blur(10px);
        box-shadow: 0 4px 16px rgba(0, 0, 0, 0.2);
    }
    
    .win {
        background: rgba(48, 209, 88, 0.2);
        color: #30D158;
    }
    
    .loss {
        background: rgba(255, 59, 48, 0.2);
        color: #FF3B30;
    }
    
    /* Optimized Buttons */
    .stButton > button {
        background: linear-gradient(135deg, #e94560 0%, #0f3460 100%);
        color: #ffffff;
        border: 1px solid rgba(255, 255, 255, 0.2);
        border-radius: 14px;
        padding: 14px 20px;
        font-family: 'Inter', sans-serif;
        font-size: 14px;
        font-weight: 600;
        width: calc(100% - 24px);
        margin: 8px 12px;
        transition: all 0.2s ease;
        box-shadow: 0 4px 16px rgba(233, 69, 96, 0.3);
        text-transform: uppercase;
        letter-spacing: 0.5px;
    }
    
    .stButton > button:hover {
        background: linear-gradient(135deg, #ff5577 0%, #1e5aa0 100%);
        transform: translateY(-1px);
        box-shadow: 0 6px 20px rgba(233, 69, 96, 0.4);
    }
    
    .stButton > button:active {
        transform: translateY(0);
        box-shadow: 0 2px 8px rgba(233, 69, 96, 0.3);
    }
    
    /* Input Fields */
    .stTextInput > div > div > input {
        background: rgba(255, 255, 255, 0.08);
        border: 1px solid rgba(255, 255, 255, 0.2);
        border-radius: 12px;
        color: #ffffff;
        font-size: 16px;
        padding: 12px 16px;
    }
    
    .stTextInput > div > div > input:focus {
        border-color: #007AFF;
        box-shadow: 0 0 0 3px rgba(0, 122, 255, 0.2);
    }
    
    /* Loading Animation */
    .stSpinner > div {
        border-color: #007AFF !important;
    }
    
    /* Bottom Safe Area */
    .bottom-safe-area {
        height: 34px;
        background: transparent;
    }
    
    /* Input Fields Premium Styling */
    .stTextInput > div > div > input {
        background: linear-gradient(145deg, rgba(255, 255, 255, 0.08) 0%, rgba(255, 255, 255, 0.02) 100%);
        backdrop-filter: blur(20px);
        -webkit-backdrop-filter: blur(20px);
        border: 1px solid rgba(255, 255, 255, 0.15);
        border-radius: 16px;
        color: #ffffff;
        font-size: 15px;
        font-family: 'Inter', sans-serif;
        padding: 16px 20px;
        transition: all 0.3s cubic-bezier(0.25, 0.46, 0.45, 0.94);
        box-shadow: 
            0 8px 32px rgba(0, 0, 0, 0.2),
            inset 0 1px 0 rgba(255, 255, 255, 0.1);
    }
    
    .stTextInput > div > div > input:focus {
        border-color: rgba(233, 69, 96, 0.5);
        box-shadow: 
            0 0 0 3px rgba(233, 69, 96, 0.2),
            0 12px 40px rgba(0, 0, 0, 0.3),
            inset 0 1px 0 rgba(255, 255, 255, 0.15);
        background: linear-gradient(145deg, rgba(255, 255, 255, 0.12) 0%, rgba(255, 255, 255, 0.06) 100%);
    }
    
    /* Loading Animation Premium */
    .stSpinner > div {
        border-color: rgba(233, 69, 96, 0.3) !important;
        border-top-color: #e94560 !important;
    }
    
    /* Sidebar Premium Styling */
    .css-1d391kg {
        background: linear-gradient(145deg, rgba(0, 0, 0, 0.8) 0%, rgba(20, 20, 40, 0.9) 100%);
        backdrop-filter: blur(40px);
        -webkit-backdrop-filter: blur(40px);
        border-right: 1px solid rgba(255, 255, 255, 0.1);
    }
    
    /* Ultra-Responsive Design */
    @media (max-width: 380px) {
        .main .block-container {
            max-width: 100% !important;
            padding: 0 8px !important;
        }
        
        .bbfs-display {
            font-size: 26px;
            letter-spacing: 4px;
            padding: 20px 16px;
        }
        
        .app-title {
            font-size: 20px;
        }
        
        .mobile-card {
            margin: 8px 4px;
            padding: 16px;
            border-radius: 20px;
        }
        
        .prediction-card {
            margin: 12px 4px;
            padding: 24px 16px;
        }
        
        .metrics-grid {
            gap: 8px;
            margin: 12px 4px;
        }
        
        .metric-item {
            padding: 16px 12px;
        }
        
        .section-header {
            margin: 24px 8px 12px 8px;
            font-size: 16px;
        }
        
        .results-list {
            margin: 12px 4px;
        }
        
        .status-bar {
            margin: 12px 4px;
            padding: 14px 20px;
        }
    }
    
    @media (max-width: 320px) {
        .bbfs-display {
            font-size: 22px;
            letter-spacing: 3px;
        }
        
        .app-title {
            font-size: 18px;
        }
        
        .metric-value {
            font-size: 18px;
        }
        
        .metric-label {
            font-size: 10px;
        }
    }
    
    /* Premium Touch Interactions */
    .mobile-card:active,
    .metric-item:active,
    .result-item:active {
        transform: scale(0.98);
    }
    
    /* Bottom Safe Area */
    .bottom-safe-area {
        height: 40px;
        background: transparent;
        margin-top: 20px;
    }
    
    /* Premium Scrollbar */
    ::-webkit-scrollbar {
        width: 6px;
    }
    
    ::-webkit-scrollbar-track {
        background: rgba(255, 255, 255, 0.1);
        border-radius: 3px;
    }
    
    ::-webkit-scrollbar-thumb {
        background: linear-gradient(135deg, #e94560, #0f3460);
        border-radius: 3px;
    }
    
    ::-webkit-scrollbar-thumb:hover {
        background: linear-gradient(135deg, #ff5577, #1e5aa0);
    }
    </style>
    """, unsafe_allow_html=True)
    
    # Initialize system
    system = load_system()
    
    if system is None:
        st.error("Gagal memuat sistem. Silakan refresh halaman.")
        st.stop()
    
    # Mobile App Header
    st.markdown("""
    <div class="mobile-header">
        <div class="app-title">BBFS Mobile Pro</div>
        <div class="app-subtitle">Prediksi Angka Cerdas</div>
    </div>
    """, unsafe_allow_html=True)
    
    # Auto-load data with better error handling
    if 'data_loaded' not in st.session_state:
        st.session_state.data_loaded = False
    
    if not st.session_state.data_loaded:
        try:
            if system.fetch_complete_data():
                system.run_performance_test()
                st.session_state.data_loaded = True
            else:
                st.error("Gagal memuat data. Menggunakan mode demo.")
                st.session_state.data_loaded = True
        except Exception as e:
            st.error(f"Error memuat data: {str(e)}")
            st.session_state.data_loaded = True
    
    # Status - selalu tampilkan sesuatu
    if system.data and len(system.data) > 0:
        performance = system.get_performance_summary()
        if performance:
            status_color = "#00d2d3" if performance['max_consecutive_loss'] <= 10 else "#ff6b6b"
            status_icon = "●" if performance['max_consecutive_loss'] <= 10 else "●"
            st.markdown(f"""
            <div class="status-bar">
                <div class="status-text">
                    <span style="color: {status_color};">{status_icon}</span> Max {performance['max_consecutive_loss']} Loss | 
                    Win {performance['win_rate']:.1f}% | {performance['total_tests']:,} Data
                </div>
            </div>
            """, unsafe_allow_html=True)
        else:
            st.markdown('<div class="status-bar"><div class="status-text">MEMPROSES DATA...</div></div>', unsafe_allow_html=True)
    else:
        st.markdown('<div class="status-bar"><div class="status-text">MEMUAT SISTEM...</div></div>', unsafe_allow_html=True)
    
    # Auto Refresh Button
    if st.button("Auto Refresh Data", type="primary", use_container_width=True):
        with st.spinner("Memperbarui data real-time..."):
            try:
                # Clear all caches first
                system.data = []
                system.performance_cache = {}
                system.loss_analysis = {}
                system.optimization_cache = {}
                system.last_updated = None
                
                # Force reload data
                if system.fetch_complete_data():
                    if system.run_performance_test(force_refresh=True):
                        st.success("Data berhasil diperbarui!")
                        st.session_state.data_loaded = True
                        time.sleep(1)
                        st.rerun()
                    else:
                        st.error("Gagal memproses data setelah refresh")
                else:
                    st.error("Gagal mengambil data dari server")
            except Exception as e:
                st.error(f"Error saat refresh: {str(e)}")

    # URL Configuration Section
    with st.expander("⚙️ Konfigurasi URL Data", expanded=False):
        st.markdown(f"""
        <div class="mobile-card">
            <div style="font-size: 14px; color: rgba(255,255,255,0.8); margin-bottom: 12px;">
                URL Sumber Data Saat Ini: <br>
                <span style="color: #e94560; font-family: monospace;">{system.url}</span>
            </div>
        </div>
        """, unsafe_allow_html=True)
        
        new_url = st.text_input(
            "Ubah URL Sumber Data",
            value=system.url,
            placeholder="http://example.com/data-source",
            key="main_url_config"
        )
        
        col1, col2 = st.columns([1, 1])
        with col1:
            if st.button("Update URL", type="primary", use_container_width=True):
                if new_url and new_url.strip() and new_url != system.url:
                    with st.spinner("Mengupdate URL dan memuat data..."):
                        try:
                            # Update system URL directly
                            system.url = new_url.strip()
                            # Clear cache and reload data
                            system.data = []
                            system.performance_cache = {}
                            system.loss_analysis = {}
                            system.optimization_cache = {}
                            
                            if system.fetch_complete_data():
                                system.run_performance_test(force_refresh=True)
                                st.success(f"URL berhasil diupdate dan data dimuat! Total: {len(system.data)} records")
                                st.rerun()
                            else:
                                st.error("Gagal memuat data dari URL baru")
                        except Exception as e:
                            st.error(f"Error: {str(e)}")
                else:
                    st.warning("Masukkan URL yang valid dan berbeda")
        
        with col2:
            if st.button("Reset Default", type="secondary", use_container_width=True):
                default_url = "http://178.128.121.191/"
                if system.url != default_url:
                    with st.spinner("Reset ke URL default..."):
                        system.url = default_url
                        system.data = []
                        system.performance_cache = {}
                        system.loss_analysis = {}
                        system.optimization_cache = {}
                        
                        if system.fetch_complete_data():
                            system.run_performance_test(force_refresh=True)
                            st.success("URL direset ke default!")
                            st.rerun()
                        else:
                            st.error("Gagal memuat data default")
                else:
                    st.info("Sudah menggunakan URL default")


    
    # Sidebar - Data info
    with st.sidebar:
        data_info = system.get_data_info()
        if data_info:
            st.markdown("### Dataset")
            st.metric("Records", f"{data_info['total_records']:,}")
            st.text(f"{data_info['date_range']['start']} - {data_info['date_range']['end']}")
            
            # Performance metrics
            performance = system.get_performance_summary()
            if performance:
                st.markdown("### Performance")
                st.metric("Max Loss Streak", performance['max_consecutive_loss'])
                st.metric("Win Rate", f"{performance['win_rate']:.1f}%")
                target_status = "Tercapai" if performance['max_consecutive_loss'] <= 10 else "Belum Tercapai"
                st.metric("Target ≤10 Loss", target_status)
    
    # Main Content - Mobile Cards
    st.markdown('<div class="section-header">📊 Prediksi BBFS Optimal</div>', unsafe_allow_html=True)
    
    # Selalu tampilkan konten dasar
    if system.data and len(system.data) >= 2:
        latest_results = system.get_latest_results(1)
        if latest_results and len(latest_results) > 0:
            latest = latest_results[0]
            
            # Use actual data date for accurate display
            try:
                if hasattr(latest['date'], 'strftime'):
                    current_date_display = latest['date'].strftime('%d/%m/%Y')
                else:
                    current_date_display = str(latest['date'])[:10]
                current_day_indo = latest['day']
            except:
                current_date_display = "N/A"
                current_day_indo = "N/A"
            
            try:
                # Generate BBFS untuk latest result
                input_2d = latest['result'][-2:]
                bbfs = system.generate_optimized_bbfs(input_2d, current_day_indo)
                
                st.markdown(f"""
                <div class="mobile-card">
                    <div style="font-size: 14px; color: rgba(255,255,255,0.8); margin-bottom: 8px;">
                        <strong>Data Terakhir:</strong> {latest['result']} | <strong>Tanggal:</strong> {current_date_display}
                    </div>
                    <div style="font-size: 14px; color: rgba(255,255,255,0.8);">
                        <strong>Hari:</strong> {current_day_indo} | <strong>Input 2D:</strong> {input_2d}
                    </div>
                </div>
                """, unsafe_allow_html=True)
                
                # BBFS Display in Prediction Card
                bbfs_display = ' '.join(bbfs)
                st.markdown(f"""
                <div class="prediction-card">
                    <div class="bbfs-display">{bbfs_display}</div>
                </div>
                """, unsafe_allow_html=True)
                
                # Quick metrics dengan validasi data
                performance = system.get_performance_summary()
                if performance and performance.get('total_tests', 0) > 0:
                    # Validasi ulang perhitungan untuk memastikan akurasi
                    total_tests = performance.get('total_tests', 0)
                    total_wins = performance.get('wins', 0)
                    total_losses = total_tests - total_wins
                    calculated_win_rate = (total_wins / total_tests * 100) if total_tests > 0 else 0
                    
                    st.markdown(f"""
                    <div class="metrics-grid">
                        <div class="metric-item">
                            <div class="metric-value">{calculated_win_rate:.1f}%</div>
                            <div class="metric-label">Win Rate</div>
                        </div>
                        <div class="metric-item">
                            <div class="metric-value">{performance["max_consecutive_loss"]}</div>
                            <div class="metric-label">Max Loss</div>
                        </div>
                        <div class="metric-item">
                            <div class="metric-value">{total_wins:,}</div>
                            <div class="metric-label">Total Wins</div>
                        </div>
                        <div class="metric-item">
                            <div class="metric-value">{total_tests:,}</div>
                            <div class="metric-label">Total Tests</div>
                        </div>
                    </div>
                    """, unsafe_allow_html=True)
                    
                    # Tampilkan informasi validasi dalam mobile card
                    st.markdown(f"""
                    <div class="mobile-card" style="text-align: center; font-size: 13px; color: rgba(255,255,255,0.7);">
                        ✓ Validasi: {total_wins} WIN + {total_losses} LOSS = {total_tests} Total Tests
                    </div>
                    """, unsafe_allow_html=True)
                    
            except Exception as e:
                st.warning(f"Memproses prediksi... ({str(e)})")
        else:
            st.info("Data tidak tersedia")
    else:
        # Tampilkan konten default jika tidak ada data
        st.markdown("""
        <div style="text-align: center; padding: 2rem;">
            <h3>Sistem Sedang Memuat Data</h3>
            <p>Silakan tunggu beberapa saat...</p>
        </div>
        """, unsafe_allow_html=True)
    
    st.markdown('</div>', unsafe_allow_html=True)
    
    # Current Loss Streak Analysis
    st.markdown('<div class="section-title">Loss Streak Aktif</div>', unsafe_allow_html=True)
    
    # Calculate current loss streak
    current_loss_streak, streak_details = system.get_current_loss_streak_analysis(10)
    
    # Display current streak
    col1, col2 = st.columns([1, 1])
    
    with col1:
        if current_loss_streak > 0:
            st.markdown(f"""
            <div class="current-streak">
                <h3 style="margin: 0 0 1rem 0; font-weight: 700;">LOSS STREAK AKTIF</h3>
                <div class="streak-number">{current_loss_streak}</div>
                <p style="margin: 0.5rem 0 0 0; opacity: 0.9;">Memerlukan strategi khusus</p>
            </div>
            """, unsafe_allow_html=True)
        else:
            st.markdown(f"""
            <div class="current-streak success">
                <h3 style="margin: 0 0 1rem 0; font-weight: 700;">TIDAK ADA STREAK</h3>
                <div class="streak-number">0</div>
                <p style="margin: 0.5rem 0 0 0; opacity: 0.9;">Kondisi operasional normal</p>
            </div>
            """, unsafe_allow_html=True)
    
    with col2:
        if streak_details:
            st.markdown('<div class="analytics-card">', unsafe_allow_html=True)
            st.markdown("**Detail Loss Streak Aktif:**")
            
            for detail in streak_details[:6]:
                # Format date - use actual date from data
                try:
                    if hasattr(detail['date'], 'strftime'):
                        date_display = detail['date'].strftime('%d/%m/%Y')
                    else:
                        # Try to parse string date
                        try:
                            if isinstance(detail['date'], str):
                                if len(detail['date']) >= 10:  # YYYY-MM-DD format
                                    parsed_date = datetime.strptime(detail['date'][:10], '%Y-%m-%d')
                                    date_display = parsed_date.strftime('%d/%m/%Y')
                                else:
                                    date_display = detail['date'][:10]
                            else:
                                date_display = str(detail['date'])[:10]
                        except:
                            date_display = str(detail['date'])[:10]
                except:
                    date_display = "N/A"
                
                # Extract 2D from the correct keys
                input_2d = detail['input_2d']
                actual_2d = detail['actual_2d']
                
                st.markdown(f"""
                <div style="padding: 0.3rem 0; border-bottom: 1px solid rgba(255,255,255,0.1);">
                    <span style="font-size: 0.85rem;">{date_display}</span><br>
                    <span><strong>{detail['input_result']}</strong> ({input_2d}) → {detail['actual_result']} ({actual_2d})</span>
                    <span style="color: #ff6b6b; font-weight: 600; float: right;">LOSS #{detail['loss_number']}</span>
                </div>
                """, unsafe_allow_html=True)
            
            st.markdown('</div>', unsafe_allow_html=True)
        else:
            st.markdown('<div class="analytics-card">', unsafe_allow_html=True)
            st.markdown("""
            <div style="text-align: center; padding: 2rem;">
                <div style="font-size: 1.2rem; font-weight: 600; color: #00d2d3; margin-bottom: 0.5rem;">
                    Tidak Ada Loss Streak Aktif
                </div>
                <div style="font-size: 0.9rem; color: #ccc; opacity: 0.8;">
                    Sistem beroperasi dalam kondisi normal
                </div>
            </div>
            """, unsafe_allow_html=True)
            st.markdown('</div>', unsafe_allow_html=True)
    
    # Loss Streak Statistics
    st.markdown('<div class="section-title">Statistik Loss Streak</div>', unsafe_allow_html=True)
    loss_stats = system.get_consecutive_loss_breakdown()
    if loss_stats and len(loss_stats) > 0:
        st.markdown('<div class="analytics-card">', unsafe_allow_html=True)
        
        # Show summary first if available
        if '_summary' in loss_stats:
            summary = loss_stats['_summary']
            st.markdown(f"""
            **Ringkasan Distribusi Loss Streak:**
            - Total Streak: {summary['total_streaks']}
            - Max Streak: {summary['max_streak']}x  
            - Rata-rata: {summary['avg_streak']:.1f}x
            """)
            st.markdown("---")
        
        st.markdown("**Distribusi Historis Lengkap:**")
        
        # Create more detailed table with all streaks
        st.markdown("""
        <div style="background: rgba(255,255,255,0.05); border-radius: 12px; padding: 16px; margin: 12px 0;">
            <div style="display: grid; grid-template-columns: 1fr 1fr 1fr 1fr; gap: 8px; font-weight: 600; margin-bottom: 8px; padding-bottom: 8px; border-bottom: 1px solid rgba(255,255,255,0.2);">
                <span>Streak</span>
                <span>Jumlah</span>
                <span>Persentase</span>
                <span>Status</span>
            </div>
        """, unsafe_allow_html=True)
        
        # Filter out summary and sort by streak length
        streak_items = [(k, v) for k, v in loss_stats.items() if k != '_summary']
        streak_items.sort(key=lambda x: x[1].get('streak_length', 0))
        
        for streak_length, stats in streak_items:
            status = stats.get('status', 'Normal')
            
            # Color coding based on status
            status_colors = {
                'Normal': '#00d2d3',
                'Perhatian': '#ffa500', 
                'Tinggi': '#ff6b6b',
                'Kritis': '#ff3030',
                'Berbahaya': '#ff0000'
            }
            color = status_colors.get(status, '#ffffff')
            
            st.markdown(f"""
            <div style="display: grid; grid-template-columns: 1fr 1fr 1fr 1fr; gap: 8px; padding: 6px 0; border-bottom: 1px solid rgba(255,255,255,0.1);">
                <span style="font-weight: 600;">{streak_length}</span>
                <span>{stats["count"]}</span>
                <span>{stats["percentage"]:.1f}%</span>
                <span style="color: {color}; font-weight: 600;">{status}</span>
            </div>
            """, unsafe_allow_html=True)
        
        st.markdown('</div>', unsafe_allow_html=True)
        st.markdown('</div>', unsafe_allow_html=True)
    
    # Latest Results with Win/Loss Analysis
    st.markdown('<div class="section-title">Data Real-Time Terbaru</div>', unsafe_allow_html=True)
    
    # Refresh button
    if st.button("Refresh Data Terbaru", key="refresh_realtime", use_container_width=True, type="primary"):
        with st.spinner("Mengambil data real-time..."):
            try:
                # Clear cache for fresh data
                system.data = []
                system.performance_cache = {}
                system.loss_analysis = {}
                system.optimization_cache = {}
                
                if system.fetch_complete_data():
                    system.run_performance_test(force_refresh=True)
                    st.success("Data terbaru berhasil dimuat!")
                    time.sleep(0.8)
                    st.rerun()
                else:
                    st.error("Gagal mengambil data terbaru")
            except Exception as e:
                st.error(f"Error saat refresh: {str(e)}")
    
    # Get real-time analysis data
    realtime_analysis = system.get_real_time_analysis(8)
    if realtime_analysis:
        # Current result info dari data terbaru
        latest = realtime_analysis[0]
        
        # Format tanggal
        try:
            if hasattr(latest['date'], 'strftime'):
                date_display = latest['date'].strftime('%d/%m/%Y')
            else:
                date_display = str(latest['date'])[:10]
        except:
            date_display = str(latest['date'])
        
        # Use actual data date for accurate display
        try:
            if hasattr(latest['date'], 'strftime'):
                current_date_display = latest['date'].strftime('%d/%m/%Y')
            else:
                current_date_display = str(latest['date'])[:10]
            current_day_indo = latest['day']
        except:
            current_date_display = "N/A"
            current_day_indo = "N/A"
        
        st.markdown(f"""
        **Data Terakhir:** {latest['input_result']} | **Tanggal:** {current_date_display} | 
        **Hari:** {current_day_indo} | **Input 2D:** {latest['input_2d']} | **Hasil Aktual:** {latest['actual_result']} ({latest['actual_2d']})
        """)
        
        # Mobile Results List
        st.markdown('<div class="section-header">📈 Analisis Terbaru</div>', unsafe_allow_html=True)
        st.markdown('<div class="results-list">', unsafe_allow_html=True)
        
        wins_count = 0
        for analysis in realtime_analysis:
            if analysis['is_win']:
                wins_count += 1
            
            # Format date - use actual date from data
            try:
                if hasattr(analysis['date'], 'strftime'):
                    date_str = analysis['date'].strftime('%d/%m/%Y')
                else:
                    # Try to parse string date
                    try:
                        if isinstance(analysis['date'], str) and len(analysis['date']) >= 10:
                            parsed_date = datetime.strptime(analysis['date'][:10], '%Y-%m-%d')
                            date_str = parsed_date.strftime('%d/%m/%Y')
                        else:
                            date_str = str(analysis['date'])[:10]
                    except:
                        date_str = str(analysis['date'])[:10]
            except:
                date_str = "N/A"
            
            status_color = "#00d2d3" if analysis['is_win'] else "#ff6b6b"
            status_text = "WIN" if analysis['is_win'] else "LOSS"
            
            # Tampilkan digit yang covered dan missing untuk transparency
            if analysis['is_win']:
                detail_info = f"Covered: {analysis['actual_2d']}"
            else:
                missing = ', '.join(analysis['missing_digits']) if analysis['missing_digits'] else "None"
                detail_info = f"Missing: {missing}"
            
            st.markdown(f"""
            <div class="result-item">
                <div class="result-left">
                    <div class="result-date">{date_str} - {analysis['input_2d']}→{analysis['actual_2d']}</div>
                    <div class="result-numbers">{analysis['bbfs_string']}</div>
                </div>
                <div class="result-status {status_text.lower()}">{status_text}</div>
            </div>
            """, unsafe_allow_html=True)
        
        st.markdown('</div>', unsafe_allow_html=True)
        
        # Summary dalam mobile card
        total_analyzed = len(realtime_analysis)
        recent_win_rate = (wins_count / total_analyzed * 100) if total_analyzed > 0 else 0
        st.markdown(f"""
        <div class="mobile-card" style="text-align: center;">
            <div style="font-size: 16px; font-weight: 600; margin-bottom: 8px;">Analisis Real-Time</div>
            <div style="font-size: 14px; color: rgba(255,255,255,0.8);">
                {wins_count} WIN dari {total_analyzed} test ({recent_win_rate:.1f}% win rate)
            </div>
        </div>
        """, unsafe_allow_html=True)
        
        # Bottom safe area untuk mobile app
        st.markdown('<div class="bottom-safe-area"></div>', unsafe_allow_html=True)

if __name__ == "__main__":
    main()