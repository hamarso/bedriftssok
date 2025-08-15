# 🏢 Bedriftssøk - Enhetsregisteret Explorer

En moderne, elegant web-applikasjon for å utforske norske bedrifter basert på data fra Enhetsregisteret.

## ✨ Funksjoner

### 🔍 Avanserte Søkefiltre
- **Bransje & Størrelse**: NACE-koder og antall ansatte
- **Bedriftsinfo**: Søk på bedriftsnavn og lokasjon
- **Organisasjon**: Filtrer på organisasjonsform
- **Geografi**: Søk på fylke og postnummer
- **Tid**: Registreringsdato fra/til

### 📊 Visualiseringer
- **Ansatte-fordeling**: Logiske intervaller (1-10, 11-25, 26-50, etc.)
- **Fylke-fordeling**: Interaktiv pie-chart
- **Detaljerte resultater**: Komplett bedriftsinformasjon

### 💾 Eksport
- **Excel**: Strukturert data med formatering
- **CSV**: Enkel tekstbasert eksport
- **Søkehistorikk**: Gjenbruk tidligere søk

## 🚀 Kom i Gang

### Lokal Utvikling

1. **Klon repository**
```bash
git clone https://github.com/dittbrukernavn/bedriftssok.git
cd bedriftssok
```

2. **Opprett virtuelt miljø**
```bash
python -m venv .venv
source .venv/bin/activate  # Linux/Mac
# eller
.venv\Scripts\activate     # Windows
```

3. **Installer avhengigheter**
```bash
pip install -r requirements.txt
```

4. **Kjør applikasjonen**
```bash
streamlit run app.py
```

### Vercel Deployment

1. **Push til GitHub**
```bash
git add .
git commit -m "Initial commit"
git push origin main
```

2. **Deploy på Vercel**
- Koble til GitHub repository
- Vercel vil automatisk oppdage Python-applikasjonen
- Deploy med `vercel.json` konfigurasjon

## 🛠️ Teknisk Stack

- **Frontend**: Streamlit
- **Backend**: Python 3.8+
- **Data**: Enhetsregisteret API (Brønnøysundregistrene)
- **Visualisering**: Plotly Express
- **Data Manipulation**: Pandas
- **Deployment**: Vercel

## 📁 Prosjektstruktur

```
bedriftssok/
├── app.py              # Hovedapplikasjon
├── requirements.txt    # Python avhengigheter
├── vercel.json        # Vercel konfigurasjon
├── README.md          # Prosjektdokumentasjon
├── CHANGELOG.md       # Endringslogg
├── install.ps1        # Windows installasjon
├── run.ps1           # Windows kjøring
├── backup.ps1        # Windows backup
└── restore.ps1       # Windows gjenoppretting
```

## 🔧 Konfigurasjon

### Enhetsregisteret API
- **Base URL**: `https://data.brreg.no/enhetsregisteret/api/enheter`
- **Rate Limiting**: Ingen kjente begrensninger
- **Data Format**: JSON med HATEOAS links

### Søkeparametere
- **NACE-kode**: Bransje-standard (f.eks. 70.220)
- **Antall ansatte**: Minimum krav
- **Lokasjon**: Poststed eller postnummer
- **Organisasjonsform**: AS, ANS, ENK, KS, NUF

## 📊 Datafelter

Hver bedrift inkluderer:
- Organisasjonsnummer og navn
- Adresse og kontaktinformasjon
- Antall ansatte og bransje
- Registreringsdato og status
- Telefon, e-post og nettside

## 🎨 Design

- **Moderne glassmorfisme** med glass-effekter
- **Responsivt design** for alle enheter
- **Lys bakgrunn** med høy kontrast
- **Smooth animasjoner** og hover-effekter
- **Konsistent fargepalett** og typografi

## 🤝 Bidrag

1. Fork repository
2. Opprett feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit endringer (`git commit -m 'Add some AmazingFeature'`)
4. Push til branch (`git push origin feature/AmazingFeature`)
5. Opprett Pull Request

## 📝 Lisens

Dette prosjektet er lisensiert under MIT License - se [LICENSE](LICENSE) filen for detaljer.

## 🙏 Takk

- **Brønnøysundregistrene** for tilgang til Enhetsregisteret API
- **Streamlit** for det fantastiske rammeverket
- **Vercel** for gratis hosting og deployment

## 📞 Kontakt

- **Prosjekt**: [Bedriftssøk](https://github.com/dittbrukernavn/bedriftssok)
- **Issues**: [GitHub Issues](https://github.com/dittbrukernavn/bedriftssok/issues)
- **Discussions**: [GitHub Discussions](https://github.com/dittbrukernavn/bedriftssok/discussions)

---

⭐ **Stjern prosjektet hvis du liker det!**
