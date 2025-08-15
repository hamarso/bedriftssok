import streamlit as st
import requests
import pandas as pd
import plotly.express as px
from datetime import datetime
import io

# Page configuration
st.set_page_config(
    page_title="Bedriftssøk",
    page_icon="🏢",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Modern Glassmorphic CSS
st.markdown("""
<style>
/* Modern CSS Variables */
:root {
    --primary: #6366f1;
    --primary-dark: #4f46e5;
    --secondary: #8b5cf6;
    --accent: #06b6d4;
    --success: #10b981;
    --warning: #f59e0b;
    --error: #ef4444;
    
    --bg-primary: #f8fafc;
    --bg-secondary: #f1f5f9;
    --bg-tertiary: #e2e8f0;
    --bg-glass: rgba(255, 255, 255, 0.8);
    --bg-glass-hover: rgba(255, 255, 255, 0.9);
    
    --text-primary: #0f172a;
    --text-secondary: #334155;
    --text-muted: #64748b;
    
    --border: rgba(0, 0, 0, 0.1);
    --border-hover: rgba(0, 0, 0, 0.2);
    
    --shadow: 0 4px 16px rgba(0, 0, 0, 0.1);
    --shadow-hover: 0 8px 24px rgba(0, 0, 0, 0.15);
    --shadow-inset: inset 0 1px 0 rgba(0, 0, 0, 0.05);
}

/* Global Styles */
* {
    box-sizing: border-box;
}

.main {
    background: var(--bg-primary);
    color: var(--text-primary);
    min-height: 100vh;
    padding: 0;
    margin: 0;
}

/* Glassmorphic Cards */
.glass-card {
    background: white;
    border: 1px solid var(--border);
    border-radius: 24px;
    padding: 2rem;
    box-shadow: var(--shadow);
    transition: all 0.3s cubic-bezier(0.4, 0, 0.2, 1);
}

.glass-card:hover {
    background: white;
    border-color: var(--border-hover);
    box-shadow: var(--shadow-hover);
    transform: translateY(-4px);
}

/* Modern Header */
.main-header {
    background: transparent;
    padding: 2rem 0;
    margin: 1rem 0 2rem 0;
    text-align: center;
    border: none;
    box-shadow: none;
}

.main-header h1 {
    font-size: 3.5rem;
    font-weight: 700;
    color: var(--text-primary);
    margin: 0;
    letter-spacing: -0.02em;
}

.main-header p {
    font-size: 1.25rem;
    color: rgba(255, 255, 255, 0.9);
    margin: 1rem 0 0 0;
    font-weight: 400;
    position: relative;
    z-index: 1;
}

/* Modern Buttons */
.stButton > button {
    background: linear-gradient(135deg, var(--primary) 0%, var(--secondary) 100%) !important;
    color: white !important;
    border: none !important;
    border-radius: 16px !important;
    padding: 1rem 2.5rem !important;
    font-weight: 600 !important;
    font-size: 1.1rem !important;
    transition: all 0.3s cubic-bezier(0.4, 0, 0.2, 1) !important;
    box-shadow: var(--shadow) !important;
    text-transform: none !important;
    letter-spacing: 0.5px !important;
    position: relative;
    overflow: hidden;
}

.stButton > button::before {
    content: '';
    position: absolute;
    top: 0;
    left: -100%;
    width: 100%;
    height: 100%;
    background: linear-gradient(90deg, transparent, rgba(255, 255, 255, 0.2), transparent);
    transition: left 0.5s;
}

.stButton > button:hover::before {
    left: 100%;
}

.stButton > button:hover {
    transform: translateY(-2px) !important;
    box-shadow: var(--shadow-hover) !important;
    background: linear-gradient(135deg, var(--primary-dark) 0%, var(--primary) 100%) !important;
}

/* Modern Inputs */
.stTextInput > div > div > input,
.stNumberInput > div > div > input,
.stSelectbox > div > div > div {
    background: white !important;
    border: 1px solid var(--border) !important;
    border-radius: 16px !important;
    color: var(--text-primary) !important;
    padding: 1rem 1.5rem !important;
    font-size: 1rem !important;
    transition: all 0.3s ease !important;
    box-shadow: var(--shadow-inset) !important;
}

.stTextInput > div > div > input:focus,
.stNumberInput > div > div > input:focus,
.stSelectbox > div > div > div:focus {
    border-color: var(--primary) !important;
    box-shadow: 0 0 0 3px rgba(99, 102, 241, 0.1) !important;
    background: white !important;
}

.stTextInput > div > div > input::placeholder {
    color: var(--text-muted) !important;
}

/* Modern Date Inputs */
.stDateInput > div > div > input {
    background: white !important;
    border: 1px solid var(--border) !important;
    border-radius: 16px !important;
    color: var(--text-primary) !important;
    padding: 1rem 1.5rem !important;
}

/* Section Headers */
.section-header {
    background: white;
    padding: 1.5rem 2rem;
    border-radius: 20px;
    margin: 2rem 0 1rem 0;
    border: 1px solid var(--border);
    box-shadow: var(--shadow);
}

.section-header h3 {
    margin: 0;
    color: var(--text-primary);
    font-weight: 600;
    font-size: 1.5rem;
    display: flex;
    align-items: center;
    gap: 0.75rem;
}

/* Metric Cards */
.metric-card {
    background: white;
    border: 1px solid var(--border);
    border-radius: 20px;
    padding: 1.5rem;
    text-align: center;
    transition: all 0.3s ease;
    box-shadow: var(--shadow);
}

.metric-card:hover {
    transform: translateY(-2px);
    box-shadow: var(--shadow-hover);
    border-color: var(--border-hover);
}

.metric-value {
    font-size: 2.5rem;
    font-weight: 800;
    color: var(--primary);
    margin: 0.5rem 0;
}

.metric-label {
    color: var(--text-secondary);
    font-size: 0.9rem;
    font-weight: 500;
    text-transform: uppercase;
    letter-spacing: 0.5px;
}

/* Results Section */
.results-section {
    background: var(--bg-glass);
    backdrop-filter: blur(20px);
    border: 1px solid var(--border);
    border-radius: 24px;
    padding: 2rem;
    margin: 2rem 0;
    box-shadow: var(--shadow);
}

/* Dataframe Styling */
.dataframe {
    background: var(--bg-glass) !important;
    color: var(--text-primary) !important;
}

/* Sidebar Styling */
.sidebar .sidebar-content {
    background: var(--bg-secondary) !important;
    color: var(--text-primary) !important;
}

/* Streamlit Container Overrides */
.block-container {
    padding-top: 0 !important;
    padding-bottom: 1rem !important;
    padding-left: 1rem !important;
    padding-right: 1rem !important;
    max-width: none !important;
}

.stApp {
    background: var(--bg-primary) !important;
}

/* Responsive Design */
@media (max-width: 768px) {
    .main-header h1 {
        font-size: 2.5rem;
    }
    
    .glass-card {
        padding: 1.5rem;
        margin: 1rem 0;
    }
}

/* Custom Scrollbar */
::-webkit-scrollbar {
    width: 8px;
}

::-webkit-scrollbar-track {
    background: var(--bg-secondary);
}

::-webkit-scrollbar-thumb {
    background: var(--primary);
    border-radius: 4px;
}

::-webkit-scrollbar-thumb:hover {
    background: var(--primary-dark);
}

/* Animation Classes */
.fade-in {
    animation: fadeIn 0.6s ease-out;
}

@keyframes fadeIn {
    from { opacity: 0; transform: translateY(20px); }
    to { opacity: 1; transform: translateY(0); }
}

.slide-up {
    animation: slideUp 0.5s ease-out;
}

@keyframes slideUp {
    from { opacity: 0; transform: translateY(30px); }
    to { opacity: 1; transform: translateY(0); }
}
</style>
""", unsafe_allow_html=True)

# Initialize session state
if 'search_history' not in st.session_state:
    st.session_state.search_history = []
if 'current_results' not in st.session_state:
    st.session_state.current_results = None

def clear_results():
    st.session_state.current_results = None

def get_county_from_postal(postal_code: str) -> str:
    """Map Norwegian postal code to county"""
    if not postal_code:
        return "Ukjent"
    
    postal_int = int(postal_code) if postal_code.isdigit() else 0
    
    # Norwegian postal code ranges by county
    if 1 <= postal_int <= 1295:
        return "Oslo"
    elif 1300 <= postal_int <= 2390:
        return "Viken"
    elif 2400 <= postal_int <= 2599:
        return "Innlandet"
    elif 2600 <= postal_int <= 3999:
        return "Vestfold og Telemark"
    elif 4000 <= postal_int <= 5999:
        return "Vestland"
    elif 6000 <= postal_int <= 6999:
        return "Rogaland"
    elif 7000 <= postal_int <= 7999:
        return "Agder"
    elif 8000 <= postal_int <= 8999:
        return "Trøndelag"
    elif 9000 <= postal_int <= 9999:
        return "Nordland"
    elif 10000 <= postal_int <= 99999:
        return "Troms og Finnmark"
    else:
        return "Ukjent"

def fetch_companies(nace_code: str, min_employees: int, company_name: str = None, location: str = None, org_form: str = None, 
                   postal_code: str = None, county: str = None, date_from: str = None, date_to: str = None) -> list[dict]:
    """Fetch companies with enhanced filtering including geographic and date filters"""
    url = "https://data.brreg.no/enhetsregisteret/api/enheter"
    params = {
        "naeringskode": nace_code,
        "fraAntallAnsatte": min_employees,
        "size": 1000,
    }
    
    # Add optional filters
    if company_name:
        params['navn'] = company_name
    if location:
        params['poststed'] = location
    if org_form:
        params['organisasjonsform'] = org_form
    if postal_code:
        params['postnummer'] = postal_code
    
    companies: list[dict] = []
    
    try:
        # Fetch all pages of results
        page_count = 0
        while True:
            page_count += 1
            response = requests.get(url, params=params, timeout=30)
            response.raise_for_status()
            data = response.json()
            
            # Get companies from current page
            page_companies = data.get("_embedded", {}).get("enheter", [])
            companies.extend(page_companies)
            
            # Check if there's a next page
            next_link = data.get("_links", {}).get("next", {}).get("href")
            if next_link:
                # Update URL for next page
                url = next_link
                params = {}  # Clear params for subsequent requests
            else:
                break
        
        # Apply date filtering if specified
        if date_from or date_to:
            filtered_companies = []
            for company in companies:
                reg_date = company.get("registreringsdatoEnhetsregisteret")
                if reg_date:
                    try:
                        company_date = datetime.strptime(reg_date, "%Y-%m-%d").date()
                        if date_from and company_date < datetime.strptime(date_from, "%Y-%m-%d").date():
                            continue
                        if date_to and company_date > datetime.strptime(date_to, "%Y-%m-%d").date():
                            continue
                        filtered_companies.append(company)
                    except ValueError:
                        filtered_companies.append(company)
                else:
                    filtered_companies.append(company)
            companies = filtered_companies
        
        # Apply county filtering if specified
        if county:
            filtered_companies = []
            for company in companies:
                address = company.get("forretningsadresse", {})
                postal = address.get("postnummer", "")
                company_county = get_county_from_postal(postal)
                if company_county == county:
                    filtered_companies.append(company)
            companies = filtered_companies
            
    except requests.RequestException as e:
        st.error(f"Feil ved henting av data: {e}")
        return []
    
    return companies

def to_dataframe(raw: list[dict]) -> pd.DataFrame:
    """Convert raw data to enhanced DataFrame"""
    def map_row(x: dict) -> dict:
        address = x.get("forretningsadresse") or {}
        nace1 = x.get("naeringskode1") or {}
        
        # Map county based on postal code
        postal_code = address.get("postnummer", "")
        county = get_county_from_postal(postal_code)
        
        return {
            "Organisasjonsnummer": x.get("organisasjonsnummer"),
            "Navn": x.get("navn"),
            "Postadresse": address.get("poststed"),
            "Postnummer": address.get("postnummer"),
            "Kommunenummer": address.get("kommunenummer"),
            "Fylke": county,
            "Antall ansatte": x.get("antallAnsatte"),
            "NACE-kode": nace1.get("kode"),
            "NACE-beskrivelse": nace1.get("beskrivelse"),
            "Organisasjonsform": x.get("organisasjonsform", {}).get("kode"),
            "Registreringsdato": x.get("registreringsdatoEnhetsregisteret"),
            "Status": x.get("slettedato") and "Slettet" or "Aktiv",
            "Telefon": x.get("mobil") or x.get("telefon") or "Ikke oppgitt",
            "E-post": x.get("epostadresse") or "Ikke oppgitt",
            "Nettside": x.get("hjemmeside") or "Ikke oppgitt"
        }
    
    if not raw:
        return pd.DataFrame()
    
    df = pd.DataFrame([map_row(x) for x in raw])
    return df

# Main App
st.markdown('<div class="main-header fade-in">', unsafe_allow_html=True)
st.markdown('<h1>🏢 Bedriftssøk</h1>', unsafe_allow_html=True)
st.markdown('<p>Utforsk norske bedrifter med avanserte søkefunksjoner</p>', unsafe_allow_html=True)
st.markdown('</div>', unsafe_allow_html=True)



# Search Section
st.markdown('<div class="section-header slide-up">', unsafe_allow_html=True)
st.markdown('<h3>🔍 Avanserte Søkefiltre</h3>', unsafe_allow_html=True)
st.markdown('</div>', unsafe_allow_html=True)

# Check if we should reuse a previous search
if 'reuse_search' in st.session_state:
    search_params = st.session_state.reuse_search
    del st.session_state.reuse_search
else:
    search_params = {
        'nace_code': '70.220',
        'min_employees': 100,
        'company_name': '',
        'location': '',
        'org_form': '',
        'date_from': '',
        'date_to': '',
        'postal_code': '',
        'county': ''
    }

# Advanced search filters
col1, col2, col3, col4 = st.columns(4)

with col1:
    st.markdown("**📊 Bransje & Størrelse**")
    nace_code = st.text_input(
        "NACE-kode", 
        value=search_params['nace_code'],
        help="F.eks. 70.220 for konsulentvirksomhet",
        placeholder="70.220"
    )
    min_employees = st.number_input(
        "Minimum antall ansatte", 
        min_value=0, 
        value=search_params['min_employees'], 
        step=1,
        help="Filtrer på bedriftsstørrelse"
    )

with col2:
    st.markdown("**🏢 Bedriftsinfo**")
    company_name = st.text_input(
        "Bedriftsnavn (valgfritt)", 
        value=search_params['company_name'],
        help="Søk på del av bedriftsnavn",
        placeholder="Søk på navn..."
    )
    location = st.text_input(
        "Lokasjon (valgfritt)", 
        value=search_params['location'],
        help="F.eks. Oslo, Bergen, Trondheim",
        placeholder="Oslo, Bergen..."
    )

with col3:
    st.markdown("**⚖️ Organisasjon**")
    org_form = st.selectbox(
        "Organisasjonsform (valgfritt)",
        options=['', 'AS', 'ANS', 'ENK', 'KS', 'NUF'],
        index=0 if not search_params['org_form'] else ['', 'AS', 'ANS', 'ENK', 'KS', 'NUF'].index(search_params['org_form']),
        help="Filtrer på organisasjonsform"
    )
    postal_code = st.text_input(
        "Postnummer (valgfritt)",
        value=search_params['postal_code'],
        help="Søk på spesifikt postnummer",
        placeholder="0001, 5000..."
    )

with col4:
    st.markdown("**📍 Geografi & Tid**")
    county = st.selectbox(
        "Fylke (valgfritt)",
        options=['', 'Oslo', 'Viken', 'Innlandet', 'Vestfold og Telemark', 'Vestland', 'Rogaland', 'Agder', 'Trøndelag', 'Nordland', 'Troms og Finnmark'],
        index=0 if not search_params['county'] else ['', 'Oslo', 'Viken', 'Innlandet', 'Vestfold og Telemark', 'Vestland', 'Rogaland', 'Agder', 'Trøndelag', 'Nordland', 'Troms og Finnmark'].index(search_params['county']),
        help="Filtrer på fylke"
    )
    
    # Date filters
    col_date1, col_date2 = st.columns(2)
    with col_date1:
        date_from = st.date_input(
            "Fra dato (valgfritt)",
            value=None,
            help="Søk på bedrifter registrert fra denne datoen"
        )
    with col_date2:
        date_to = st.date_input(
            "Til dato (valgfritt)",
            value=None,
            help="Søk på bedrifter registrert til denne datoen"
        )

# Search Button
st.markdown('<div style="text-align: center; margin: 2rem 0;">', unsafe_allow_html=True)
if st.button("🚀 Start Søk", use_container_width=True):
    with st.spinner("🔍 Søker etter bedrifter..."):
        companies = fetch_companies(
            nace_code.strip(),
            min_employees,
            company_name.strip() if company_name else None,
            location.strip() if location else None,
            org_form if org_form else None,
            postal_code.strip() if postal_code else None,
            county if county else None,
            date_from.strftime('%Y-%m-%d') if date_from else None,
            date_to.strftime('%Y-%m-%d') if date_to else None
        )
        
        if companies:
            st.session_state.current_results = companies
            st.success(f"✅ Fant {len(companies)} bedrifter!")
            st.rerun()
        else:
            st.warning("⚠️ Ingen bedrifter funnet med disse kriteriene.")
else:
    st.markdown('<p style="text-align: center; color: var(--text-muted); margin: 1rem 0;">Fyll ut søkekriteriene og klikk "Start Søk"</p>', unsafe_allow_html=True)
st.markdown('</div>', unsafe_allow_html=True)

# Results Section
if st.session_state.current_results:
    st.markdown('<div class="section-header slide-up">', unsafe_allow_html=True)
    st.markdown('<h3>📊 Søkeresultater</h3>', unsafe_allow_html=True)
    st.markdown('</div>', unsafe_allow_html=True)
    
    companies = st.session_state.current_results
    df = to_dataframe(companies)
    
    if not df.empty:
        # Store current search parameters
        current_search = {
            'nace_code': nace_code.strip(),
            'min_employees': min_employees,
            'company_name': company_name.strip() if company_name else None,
            'location': location.strip() if location else None,
            'org_form': org_form if org_form else None,
            'postal_code': postal_code.strip() if postal_code else None,
            'county': county if county else None,
            'date_from': date_from.strftime('%Y-%m-%d') if date_from else None,
            'date_to': date_to.strftime('%Y-%m-%d') if date_to else None
        }
        
        # Add to search history
        if current_search not in st.session_state.search_history:
            st.session_state.search_history.append(current_search)
        
        # Results summary
        col1, col2, col3 = st.columns(3)
        with col1:
            st.metric("📊 Antall bedrifter", len(df))
        with col2:
            avg_employees = df['Antall ansatte'].mean()
            st.metric("👥 Gjennomsnitt ansatte", f"{avg_employees:.0f}")
        with col3:
            active_companies = len(df[df['Status'] == 'Aktiv'])
            st.metric("✅ Aktive bedrifter", active_companies)
        
        # Data visualization
        st.markdown('<div class="glass-card slide-up">', unsafe_allow_html=True)
        st.markdown("### 📈 Visualiseringer")
        
        col1, col2 = st.columns(2)
        
        with col1:
            # Employee distribution
            if not df.empty and 'Antall ansatte' in df.columns:
                # Create employee size categories
                def categorize_employees(employees):
                    if pd.isna(employees) or employees == 0:
                        return 'Ukjent'
                    elif employees <= 10:
                        return '1-10'
                    elif employees <= 25:
                        return '11-25'
                    elif employees <= 50:
                        return '26-50'
                    elif employees <= 100:
                        return '51-100'
                    elif employees <= 250:
                        return '101-250'
                    elif employees <= 500:
                        return '251-500'
                    elif employees <= 1000:
                        return '501-1000'
                    else:
                        return '1000+'
                
                # Add employee category column
                df_with_categories = df.copy()
                df_with_categories['Ansatte-kategori'] = df_with_categories['Antall ansatte'].apply(categorize_employees)
                
                # Count companies in each category
                category_counts = df_with_categories['Ansatte-kategori'].value_counts()
                
                # Sort categories logically
                category_order = ['1-10', '11-25', '26-50', '51-100', '101-250', '251-500', '501-1000', '1000+', 'Ukjent']
                category_counts = category_counts.reindex(category_order, fill_value=0)
                
                fig_employees = px.bar(
                    x=category_counts.index,
                    y=category_counts.values,
                    title="Fordeling av antall ansatte",
                    labels={'x': 'Antall ansatte', 'y': 'Antall bedrifter'},
                    color_discrete_sequence=[st.get_option("theme.primaryColor")]
                )
                fig_employees.update_layout(
                    plot_bgcolor='rgba(0,0,0,0)',
                    paper_bgcolor='rgba(0,0,0,0)',
                    font=dict(color='#0f172a'),
                    xaxis=dict(gridcolor='rgba(0,0,0,0.1)'),
                    yaxis=dict(gridcolor='rgba(0,0,0,0.1)'),
                    xaxis_title="Antall ansatte",
                    yaxis_title="Antall bedrifter"
                )
                fig_employees.update_traces(marker_color='#6366f1')
                st.plotly_chart(fig_employees, use_container_width=True)
        
        with col2:
            # County distribution
            if not df.empty and 'Fylke' in df.columns:
                county_counts = df['Fylke'].value_counts()
                fig_county = px.pie(
                    values=county_counts.values,
                    names=county_counts.index,
                    title="Fordeling på fylke",
                    color_discrete_sequence=px.colors.qualitative.Set3
                )
                fig_county.update_layout(
                    plot_bgcolor='rgba(0,0,0,0)',
                    paper_bgcolor='rgba(0,0,0,0)',
                    font=dict(color='#0f172a')
                )
                st.plotly_chart(fig_county, use_container_width=True)
        
        st.markdown('</div>', unsafe_allow_html=True)
        
        # Data table
        st.markdown('<div class="glass-card slide-up">', unsafe_allow_html=True)
        st.markdown("### 📋 Detaljerte Resultater")
        
        # Export options
        col1, col2, col3 = st.columns(3)
        with col1:
            if st.button("📊 Eksporter til Excel", use_container_width=True):
                buffer = io.BytesIO()
                with pd.ExcelWriter(buffer, engine='openpyxl') as writer:
                    df.to_excel(writer, sheet_name='Bedrifter', index=False)
                buffer.seek(0)
                st.download_button(
                    label="💾 Last ned Excel-fil",
                    data=buffer.getvalue(),
                    file_name=f"bedrifter_{datetime.now().strftime('%Y%m%d_%H%M%S')}.xlsx",
                    mime="application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
                )
        
        with col2:
            if st.button("📄 Eksporter til CSV", use_container_width=True):
                csv = df.to_csv(index=False)
                st.download_button(
                    label="💾 Last ned CSV-fil",
                    data=csv,
                    file_name=f"bedrifter_{datetime.now().strftime('%Y%m%d_%H%M%S')}.csv",
                    mime="text/csv"
                )
        
        with col3:
            if st.button("🗑️ Tøm resultater", use_container_width=True):
                clear_results()
                st.rerun()
        
        # Display dataframe
        st.dataframe(
            df,
            column_config={
                "Organisasjonsnummer": st.column_config.TextColumn("Org.nr", width="medium"),
                "Navn": st.column_config.TextColumn("Bedriftsnavn", width="large"),
                "Postadresse": st.column_config.TextColumn("Sted", width="medium"),
                "Fylke": st.column_config.TextColumn("📍 Fylke", width="small"),
                "Antall ansatte": st.column_config.NumberColumn("Ansatte", width="small"),
                "NACE-kode": st.column_config.TextColumn("NACE", width="small"),
                "Status": st.column_config.TextColumn("Status", width="small"),
                "Telefon": st.column_config.TextColumn("📞 Telefon", width="medium"),
                "E-post": st.column_config.TextColumn("📧 E-post", width="medium"),
                "Nettside": st.column_config.TextColumn("🌐 Nettside", width="medium")
            },
            use_container_width=True
        )
        
        st.markdown('</div>', unsafe_allow_html=True)
        
        # Search history
        if st.session_state.search_history:
            st.markdown('<div class="glass-card slide-up">', unsafe_allow_html=True)
            st.markdown("### 📚 Søkehistorikk")
            
            for i, search in enumerate(reversed(st.session_state.search_history[-5:]), 1):
                with st.expander(f"🔍 Søk #{len(st.session_state.search_history) - i + 1}"):
                    st.json(search)
                    if st.button(f"🔄 Gjenbruk søk #{len(st.session_state.search_history) - i + 1}", key=f"reuse_{i}"):
                        st.session_state.reuse_search = search
                        st.rerun()
            
            st.markdown('</div>', unsafe_allow_html=True)

# Sidebar
with st.sidebar:
    st.markdown('<div class="glass-card">', unsafe_allow_html=True)
    st.markdown("### 🚀 Rask Start")
    st.markdown("""
    **Populære NACE-koder:**
    - 70.220: Konsulentvirksomhet
    - 62.010: Programvareutvikling
    - 43.210: Elektrisk installasjon
    
    **Nye avanserte filtre:**
    - 📍 **Fylke** - søk på spesifikt fylke
    - 📮 **Postnummer** - presis lokasjon
    - 📅 **Dato** - registreringsperiode
    
    **Tips:**
    - Bruk punktum i NACE-kode (70.220)
    - Bedriftsnavn: Søk på del av navn
    - Kombiner filtre for presise resultater
    """)
    st.markdown('</div>', unsafe_allow_html=True)
    
    st.markdown('<div class="glass-card">', unsafe_allow_html=True)
    st.markdown("### ℹ️ Om Enhetsregisteret")
    st.markdown("""
    Enhetsregisteret inneholder informasjon om alle norske bedrifter og organisasjoner.
    
    **Hva kan du finne:**
    - Bedriftsnavn og organisasjonsnummer
    - Adresse og kontaktinformasjon
    - Antall ansatte og bransje
    - Registreringsdato og status
    - Telefon, e-post og nettside
    """)
    st.markdown('</div>', unsafe_allow_html=True)
