import streamlit as st
import pandas as pd
import joblib

# Custom CSS for professional styling
st.markdown("""
<style>
    /* Import Google Fonts */
    @import url('https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600;700&display=swap');
    
    /* Global Styles */
    .main {
        font-family: 'Inter', sans-serif;
    }
    
    /* Header Styling */
    .header-container {
        background: linear-gradient(135deg, #1e3a8a 0%, #3b82f6 50%, #f59e0b 100%);
        padding: 2rem 0;
        border-radius: 12px;
        margin-bottom: 2rem;
        text-align: center;
        color: white;
        box-shadow: 0 10px 30px rgba(0,0,0,0.1);
    }
    
    .header-title {
        font-size: 3rem;
        font-weight: 700;
        margin-bottom: 0.5rem;
        text-shadow: 2px 2px 4px rgba(0,0,0,0.3);
    }
    
    .header-subtitle {
        font-size: 1.2rem;
        font-weight: 300;
        opacity: 0.9;
    }
    
    /* Section Styling */
    .section-container {
        background: white;
        padding: 1.5rem;
        border-radius: 12px;
        box-shadow: 0 4px 20px rgba(0,0,0,0.08);
        margin-bottom: 1.5rem;
        border: 1px solid #e5e7eb;
    }
    
    .section-title {
        color: #1e3a8a !important;
        font-size: 1.3rem;
        font-weight: 600;
        margin-bottom: 1rem;
        padding-bottom: 0.5rem;
        border-bottom: 2px solid #f59e0b;
        display: flex;
        align-items: center;
    }
    
    /* Input Styling */
    .stNumberInput > div > div > input {
        border: 2px solid #e5e7eb;
        border-radius: 8px;
        padding: 0.5rem;
        transition: all 0.3s ease;
        font-family: 'Inter', sans-serif;
    }
    
    .stNumberInput > div > div > input:focus {
        border-color: #f59e0b;
        box-shadow: 0 0 0 3px rgba(245, 158, 11, 0.1);
    }
    
    .stSelectbox > div > div > div {
        border: 2px solid #e5e7eb;
        border-radius: 8px;
        transition: all 0.3s ease;
    }
    
    .stSelectbox > div > div > div:focus-within {
        border-color: #f59e0b;
        box-shadow: 0 0 0 3px rgba(245, 158, 11, 0.1);
    }
    
    /* Button Styling */
    .predict-button {
        background: linear-gradient(135deg, #f59e0b 0%, #d97706 100%);
        color: white;
        border: none;
        padding: 1rem 2rem;
        border-radius: 10px;
        font-size: 1.1rem;
        font-weight: 600;
        cursor: pointer;
        width: 100%;
        margin: 1rem 0;
        box-shadow: 0 4px 15px rgba(245, 158, 11, 0.3);
        transition: all 0.3s ease;
        font-family: 'Inter', sans-serif;
    }
    
    .predict-button:hover {
        transform: translateY(-2px);
        box-shadow: 0 6px 20px rgba(245, 158, 11, 0.4);
    }
    
    /* Results Styling */
    .result-container {
        background: linear-gradient(135deg, #f59e0b 0%, #d97706 100%);
        color: white;
        padding: 2rem;
        border-radius: 12px;
        text-align: center;
        margin: 1rem 0;
        box-shadow: 0 8px 25px rgba(245, 158, 11, 0.3);
    }
    
    .result-price {
        font-size: 2.5rem;
        font-weight: 700;
        margin-bottom: 0.5rem;
    }
    
    .result-label {
        font-size: 1rem;
        opacity: 0.9;
        font-weight: 300;
    }
    
    /* Icon Styling */
    .icon {
        margin-right: 0.5rem;
        font-size: 1.2rem;
    }
    
    /* Responsive Design */
    @media (max-width: 768px) {
        .header-title {
            font-size: 2rem;
        }
        .header-subtitle {
            font-size: 1rem;
        }
    }
    
    /* Hide Streamlit branding */
    #MainMenu {visibility: hidden;}
    footer {visibility: hidden;}
    header {visibility: hidden;}
</style>
""", unsafe_allow_html=True)

# Load  trained model
model = joblib.load('best_gradient_boosting_model.joblib')






# Professional Header
st.markdown("""
<div class="header-container">
    <h1 class="header-title">🏠 Melbourne Property Predictor</h1>
    <p class="header-subtitle">Professional property valuation powered by advanced machine learning</p>
</div>
""", unsafe_allow_html=True)

# Main content in columns for better layout
col1, col2 = st.columns([2, 1])

with col1:
    # Property Details Section
    st.markdown("""
    <div class="section-container">
        <h3 class="section-title">🏘️ Property Information</h3>
    """, unsafe_allow_html=True)
    
    # Basic property details in columns
    prop_col1, prop_col2, prop_col3 = st.columns(3)
    
    with prop_col1:
        rooms = st.number_input("🛏️ Total Rooms", min_value=1, max_value=10, value=3, help="Total number of rooms in the property")
        bathroom = st.number_input("🛁 Bathrooms", min_value=0, max_value=10, value=1, help="Number of bathrooms")
        yearbuilt = st.number_input("📅 Year Built", min_value=1800, max_value=2025, value=1990, help="Year the property was built")
    
    with prop_col2:
        bedroom2 = st.number_input("🛌 Bedrooms", min_value=0, max_value=10, value=2, help="Number of bedrooms")
        car = st.number_input("🚗 Car Spaces", min_value=0, max_value=10, value=1, help="Number of car parking spaces")
        landsize = st.number_input("📏 Land Size (sqm)", min_value=0.0, max_value=10000.0, value=500.0, format="%.2f", help="Land size in square meters")
    
    with prop_col3:
        distance = st.number_input("🏙️ Distance from CBD (km)", min_value=0.0, max_value=100.0, value=10.0, help="Distance from Melbourne CBD")
        
    st.markdown("</div>", unsafe_allow_html=True)
    
    # Location Details Section
    st.markdown("""
    <div class="section-container">
        <h3 class="section-title">📍 Location Details</h3>
    """, unsafe_allow_html=True)
    
    loc_col1, loc_col2 = st.columns(2)
    
    with loc_col1:
        latitude = st.number_input("🌐 Latitude", min_value=-90.0, max_value=90.0, value=-37.8, format="%.6f", help="Property latitude coordinate")
        suburbs = ['Abbotsford', 'Airport West', 'Albert Park', 'Alphington', 'Altona', 'Altona North', 'Armadale', 'Ascot Vale', 'Ashburton', 'Ashwood', 'Avondale Heights', 'Balaclava', 'Balwyn', 'Balwyn North', 'Bentleigh', 'Bentleigh East', 'Box Hill', 'Braybrook', 'Brighton', 'Brighton East', 'Brunswick', 'Brunswick West', 'Bulleen', 'Burwood', 'Camberwell', 'Canterbury', 'Carlton North', 'Carnegie', 'Caulfield', 'Caulfield North', 'Caulfield South', 'Chadstone', 'Clifton Hill', 'Coburg', 'Coburg North', 'Collingwood', 'Doncaster', 'Eaglemont', 'Elsternwick', 'Elwood', 'Essendon', 'Essendon North', 'Fairfield', 'Fitzroy', 'Fitzroy North', 'Flemington', 'Footscray', 'Glen Iris', 'Glenroy', 'Gowanbrae', 'Hadfield', 'Hampton', 'Hampton East', 'Hawthorn', 'Heidelberg Heights', 'Heidelberg West', 'Hughesdale', 'Ivanhoe', 'Kealba', 'Keilor East', 'Kensington', 'Kew', 'Kew East', 'Kooyong', 'Maidstone', 'Malvern', 'Malvern East', 'Maribyrnong', 'Melbourne', 'Middle Park', 'Mont Albert', 'Moonee Ponds', 'Moorabbin', 'Newport', 'Niddrie', 'North Melbourne', 'Northcote', 'Oak Park', 'Oakleigh South', 'Parkville', 'Pascoe Vale', 'Port Melbourne', 'Prahran', 'Preston', 'Reservoir', 'Richmond', 'Rosanna', 'Seddon', 'South Melbourne', 'South Yarra', 'Southbank', 'Spotswood', 'St Kilda', 'Strathmore', 'Sunshine', 'Sunshine North', 'Sunshine West', 'Surrey Hills', 'Templestowe Lower', 'Thornbury', 'Toorak', 'Viewbank', 'Watsonia', 'West Melbourne', 'Williamstown', 'Williamstown North', 'Windsor', 'Yallambie', 'Yarraville', 'Aberfeldie', 'Bellfield', 'Brunswick East', 'Burnley', 'Campbellfield', 'Carlton', 'East Melbourne', 'Essendon West', 'Fawkner', 'Hawthorn East', 'Heidelberg', 'Ivanhoe East', 'Jacana', 'Kingsbury', 'Kingsville', 'Murrumbeena', 'Ormond', 'West Footscray', 'Albion', 'Brooklyn', 'Glen Huntly', 'Oakleigh', 'Ripponlea', 'Cremorne', 'Docklands', 'South Kingsville', 'Strathmore Heights', 'Travancore', 'Caulfield East', 'Seaholme', 'Keilor Park', 'Gardenvale', 'Princes Hill', 'Bayswater', 'Bayswater North', 'Beaumaris', 'Berwick', 'Boronia', 'Briar Hill', 'Broadmeadows', 'Bundoora', 'Burnside Heights', 'Burwood East', 'Cairnlea', 'Caroline Springs', 'Cheltenham', 'Craigieburn', 'Cranbourne', 'Croydon', 'Dandenong', 'Dandenong North', 'Diamond Creek', 'Dingley Village', 'Doncaster East', 'Donvale', 'Doreen', 'Eltham', 'Epping', 'Forest Hill', 'Frankston', 'Frankston North', 'Frankston South', 'Gisborne', 'Gladstone Park', 'Greensborough', 'Hallam', 'Healesville', 'Highett', 'Hillside', 'Huntingdale', 'Keilor Downs', 'Keilor Lodge', 'Keysborough', 'Kings Park', 'Lalor', 'Lower Plenty', 'Melton', 'Mernda', 'Mill Park', 'Mitcham', 'Montmorency', 'Mordialloc', 'Mount Waverley', 'Narre Warren', 'Nunawading', 'Oakleigh East', 'Parkdale', 'Point Cook', 'Ringwood East', 'Rockbank', 'Rowville', 'Sandringham', 'Seaford', 'Skye', 'South Morang', 'Springvale', 'St Albans', 'Sunbury', 'Tarneit', 'Taylors Hill', 'Taylors Lakes', 'The Basin', 'Thomastown', 'Truganina', 'Tullamarine', 'Vermont', 'Wantirna', 'Wantirna South', 'Werribee', 'Westmeadows', 'Williams Landing', 'Wollert', 'Wyndham Vale', 'Black Rock', 'Blackburn', 'Blackburn North', 'Bonbeach', 'Carrum', 'Chelsea', 'Clayton', 'Doveton', 'Ferntree Gully', 'Glen Waverley', 'Greenvale', 'Heathmont', 'Hoppers Crossing', 'McKinnon', 'Melton South', 'Melton West', 'Mentone', 'Mooroolbark', 'Mulgrave', 'Ringwood', 'Roxburgh Park', 'Seabrook', 'Templestowe', 'Vermont South', 'Warrandyte', 'Watsonia North', 'Wheelers Hill', 'Altona Meadows', 'Blackburn South', 'Carrum Downs', 'Clayton South', 'Croydon North', 'Langwarrin', 'Noble Park', 'Notting Hill', 'Ringwood North', 'Sydenham', 'Albanvale', 'Beaconsfield Upper', 'Chelsea Heights', 'Dallas', 'Deer Park', 'Eltham North', 'Keilor', 'Meadow Heights', 'Mount Evelyn', 'North Warrandyte', 'Pakenham', 'Riddells Creek', 'Sandhurst', 'Scoresby', 'Silvan', 'Aspendale', 'Chirnside Park', 'Croydon Hills', 'Croydon South', 'Derrimut', 'Diggers Rest', 'Edithvale', 'Hampton Park', 'Knoxfield', 'St Helena', 'Upwey', 'Bacchus Marsh', 'Coolaroo', 'Cranbourne North', 'Kilsyth', 'Montrose', 'Aspendale Gardens', 'Bullengarook', 'Clarinda', 'Deepdene', 'Delahey', 'Hurstbridge', 'Kurunjang', 'Wonga Park', 'Endeavour Hills', 'Officer', 'Waterways', 'Ardeer', 'Beaconsfield', 'Springvale South', 'Yarra Glen', 'Brookfield', 'Emerald', 'Whittlesea', 'Burnside', 'Attwood', 'Wallan', 'New Gisborne', 'Plumpton', 'Monbulk'] 
        suburb = st.selectbox("🏘️ Suburb", suburbs, help="Select the property suburb")
        
    with loc_col2:
        longitude = st.number_input("🌐 Longitude", min_value=-180.0, max_value=180.0, value=144.9, format="%.6f", help="Property longitude coordinate")
        council_areas = ['Yarra', 'Moonee Valley', 'Port Phillip', 'Darebin', 'Hobsons Bay', 'Stonnington', 'Boroondara', 'Monash', 'Glen Eira', 'Whitehorse', 'Maribyrnong', 'Bayside', 'Moreland', 'Manningham', 'Banyule', 'Melbourne', 'Kingston', 'Brimbank', 'Hume', 'Unknown', 'Knox', 'Maroondah', 'Casey', 'Melton', 'Greater Dandenong', 'Nillumbik', 'Whittlesea', 'Frankston', 'Macedon Ranges', 'Yarra Ranges', 'Wyndham', 'Cardinia', 'Unavailable', 'Moorabool']
        council_area = st.selectbox("🏛️ Council Area", council_areas, help="Local government council area")
        
    st.markdown("</div>", unsafe_allow_html=True)
    
    # Property & Sale Details Section
    st.markdown("""
    <div class="section-container">
        <h3 class="section-title">🏠 Property & Sale Details</h3>
    """, unsafe_allow_html=True)
    
    detail_col1, detail_col2 = st.columns(2)
    
    with detail_col1:
        type_options = {'h': 'House', 'u': 'Unit', 't': 'Townhouse'}
        type_label = st.selectbox("🏠 Property Type", list(type_options.values()), help="Type of property")
        type_ = [k for k, v in type_options.items() if v == type_label][0]
        
        top_sellers = ['Nelson', 'Jellis', 'hockingstuart', 'Barry', 'Ray', 'Marshall', 'Buxton', 'Biggin', 'Brad', 'Fletchers', 'Other']
        seller = st.selectbox("🏢 Estate Agent", top_sellers, help="Real estate agency")
        
    with detail_col2:
        method_options = {
            'S': 'Private Sale',
            'SP': 'Sold Prior',
            'PI': 'Price Inquiry',
            'VB': 'Vendor Bid',
            'SA': 'Sold After'
        }
        method_label = st.selectbox("💰 Sale Method", list(method_options.values()), help="Method of sale")
        method = [k for k, v in method_options.items() if v == method_label][0]
        
        regionnames = ['Northern Metropolitan', 'Western Metropolitan', 'Southern Metropolitan', 'Eastern Metropolitan', 'South-Eastern Metropolitan', 'Eastern Victoria', 'Northern Victoria', 'Western Victoria']
        regionname = st.selectbox("🗺️ Region", regionnames, help="Melbourne region")
        
    st.markdown("</div>", unsafe_allow_html=True)

with col2:
    # Prediction Panel
    st.markdown("""
    <div class="section-container">
        <h3 class="section-title">💰 Price Prediction</h3>
    """, unsafe_allow_html=True)
    
    # Custom prediction button
    predict_clicked = st.button("🚀 Predict Property Value", key="predict", help="Generate property price prediction")
    
    # Add some info about the prediction
    st.markdown("""
    <div style="background: #f8fafc; padding: 1rem; border-radius: 8px; margin: 1rem 0; border-left: 4px solid #f59e0b;">
        <h4 style="color: #1e3a8a; margin: 0 0 0.5rem 0;">📊 What we analyze:</h4>
        <ul style="margin: 0; padding-left: 1rem; color: #4b5563;">
            <li>Property characteristics</li>
            <li>Location factors</li>
            <li>Market trends</li>
            <li>Comparable sales</li>
        </ul>
    </div>
    """, unsafe_allow_html=True)
    
    st.markdown("</div>", unsafe_allow_html=True)

# Prediction Logic
if predict_clicked:
    # Calculate derived features
    bedroom2_x_bathroom = bedroom2 * bathroom
    
    # Validation
    errors = []
    if bedroom2 > rooms:
        errors.append("Bedrooms cannot exceed total rooms.")
    if landsize <= 0:
        errors.append("Land size must be greater than 0 sqm.")
    if yearbuilt > 2025:
        errors.append("Year built cannot be in the future.")
    if not (-38.5 < latitude < -37.5):
        errors.append("Latitude outside typical Melbourne range.")
    if not (144.5 < longitude < 145.5):
        errors.append("Longitude outside typical Melbourne range.")
    
    if errors:
        for err in errors:
            st.error(f"❌ {err}")
    else:
        with st.spinner("🔮 Analyzing property data..."):
            # Create dummy variables function
            def create_dummies(selected, categories, prefix):
                return {f"{prefix}_{cat}": 1 if selected == cat else 0 for cat in categories}
            
            # Create all dummy variables
            seller_dummies = create_dummies(seller, top_sellers, "SellerG")
            suburb_dummies = create_dummies(suburb, suburbs, "Suburb")
            type_dummies = create_dummies(type_, list(type_options.keys()), "Type")
            method_dummies = create_dummies(method, list(method_options.keys()), "Method")
            council_dummies = create_dummies(council_area, council_areas, "CouncilArea")
            region_dummies = create_dummies(regionname, regionnames, "Regionname")
            
            # Combine all input data
            input_data = {
                'Rooms': rooms,
                'Distance': distance,
                'Bedroom2': bedroom2,
                'Bathroom': bathroom,
                'Car': car,
                'Landsize': landsize,
                'YearBuilt': yearbuilt,
                'Lattitude': latitude,
                'Longtitude': longitude,
                'YearBuilt_missing': 0,
                'Car_missing': 0,
                'Bedroom2_x_Bathroom': bedroom2_x_bathroom,
                **seller_dummies,
                **suburb_dummies,
                **type_dummies,
                **method_dummies,
                **council_dummies,
                **region_dummies,
            }
            
            # Create DataFrame and align with model features
            input_df = pd.DataFrame([input_data])
            
            # Model features list (your existing list)
            model_features = [
    'Rooms', 'Distance', 'Bedroom2', 'Bathroom', 'Car', 'Landsize', 'YearBuilt',
    'Lattitude', 'Longtitude', 'YearBuilt_missing', 'Car_missing',
    'SellerG_Barry', 'SellerG_Biggin', 'SellerG_Brad', 'SellerG_Buxton',
    'SellerG_Fletchers', 'SellerG_Jellis', 'SellerG_Marshall', 'SellerG_Nelson',
    'SellerG_Other', 'SellerG_Ray', 'SellerG_hockingstuart',
    'Suburb_Abbotsford', 'Suburb_Aberfeldie', 'Suburb_Airport West', 'Suburb_Albanvale',
    'Suburb_Albert Park', 'Suburb_Albion', 'Suburb_Alphington', 'Suburb_Altona',
    'Suburb_Altona Meadows', 'Suburb_Altona North', 'Suburb_Ardeer', 'Suburb_Armadale',
    'Suburb_Ascot Vale', 'Suburb_Ashburton', 'Suburb_Ashwood', 'Suburb_Aspendale',
    'Suburb_Aspendale Gardens', 'Suburb_Attwood', 'Suburb_Avondale Heights',
    'Suburb_Bacchus Marsh', 'Suburb_Balaclava', 'Suburb_Balwyn', 'Suburb_Balwyn North',
    'Suburb_Bayswater', 'Suburb_Bayswater North', 'Suburb_Beaconsfield',
    'Suburb_Beaconsfield Upper', 'Suburb_Beaumaris', 'Suburb_Bellfield',
    'Suburb_Bentleigh', 'Suburb_Bentleigh East', 'Suburb_Berwick', 'Suburb_Black Rock',
    'Suburb_Blackburn', 'Suburb_Blackburn North', 'Suburb_Blackburn South',
    'Suburb_Bonbeach', 'Suburb_Boronia', 'Suburb_Box Hill', 'Suburb_Braybrook',
    'Suburb_Briar Hill', 'Suburb_Brighton', 'Suburb_Brighton East',
    'Suburb_Broadmeadows', 'Suburb_Brookfield', 'Suburb_Brooklyn', 'Suburb_Brunswick',
    'Suburb_Brunswick East', 'Suburb_Brunswick West', 'Suburb_Bulleen',
    'Suburb_Bullengarook', 'Suburb_Bundoora', 'Suburb_Burnley', 'Suburb_Burnside',
    'Suburb_Burnside Heights', 'Suburb_Burwood', 'Suburb_Burwood East',
    'Suburb_Cairnlea', 'Suburb_Camberwell', 'Suburb_Campbellfield', 'Suburb_Canterbury',
    'Suburb_Carlton', 'Suburb_Carlton North', 'Suburb_Carnegie', 'Suburb_Caroline Springs',
    'Suburb_Carrum', 'Suburb_Carrum Downs', 'Suburb_Caulfield', 'Suburb_Caulfield East',
    'Suburb_Caulfield North', 'Suburb_Caulfield South', 'Suburb_Chadstone',
    'Suburb_Chelsea', 'Suburb_Chelsea Heights', 'Suburb_Cheltenham',
    'Suburb_Chirnside Park', 'Suburb_Clarinda', 'Suburb_Clayton', 'Suburb_Clayton South',
    'Suburb_Clifton Hill', 'Suburb_Coburg', 'Suburb_Coburg North', 'Suburb_Collingwood',
    'Suburb_Coolaroo', 'Suburb_Craigieburn', 'Suburb_Cranbourne',
    'Suburb_Cranbourne North', 'Suburb_Cremorne', 'Suburb_Croydon',
    'Suburb_Croydon Hills', 'Suburb_Croydon North', 'Suburb_Croydon South',
    'Suburb_Dallas', 'Suburb_Dandenong', 'Suburb_Dandenong North', 'Suburb_Deepdene',
    'Suburb_Deer Park', 'Suburb_Delahey', 'Suburb_Derrimut', 'Suburb_Diamond Creek',
    'Suburb_Diggers Rest', 'Suburb_Dingley Village', 'Suburb_Docklands',
    'Suburb_Doncaster', 'Suburb_Doncaster East', 'Suburb_Donvale', 'Suburb_Doreen',
    'Suburb_Doveton', 'Suburb_Eaglemont', 'Suburb_East Melbourne',
    'Suburb_Edithvale', 'Suburb_Elsternwick', 'Suburb_Eltham', 'Suburb_Eltham North',
    'Suburb_Elwood', 'Suburb_Emerald', 'Suburb_Endeavour Hills',
    'Suburb_Epping', 'Suburb_Essendon', 'Suburb_Essendon North', 'Suburb_Essendon West',
    'Suburb_Fairfield', 'Suburb_Fawkner', 'Suburb_Ferntree Gully', 'Suburb_Fitzroy',
    'Suburb_Fitzroy North', 'Suburb_Flemington', 'Suburb_Footscray',
    'Suburb_Forest Hill', 'Suburb_Frankston', 'Suburb_Frankston North',
    'Suburb_Frankston South', 'Suburb_Gardenvale', 'Suburb_Gisborne',
    'Suburb_Gladstone Park', 'Suburb_Glen Huntly', 'Suburb_Glen Iris',
    'Suburb_Glen Waverley', 'Suburb_Glenroy', 'Suburb_Gowanbrae',
    'Suburb_Greensborough', 'Suburb_Greenvale', 'Suburb_Hadfield', 'Suburb_Hallam',
    'Suburb_Hampton', 'Suburb_Hampton East', 'Suburb_Hampton Park', 'Suburb_Hawthorn',
    'Suburb_Hawthorn East', 'Suburb_Healesville', 'Suburb_Heathmont',
    'Suburb_Heidelberg', 'Suburb_Heidelberg Heights', 'Suburb_Heidelberg West',
    'Suburb_Highett', 'Suburb_Hillside', 'Suburb_Hoppers Crossing', 'Suburb_Hughesdale',
    'Suburb_Huntingdale', 'Suburb_Hurstbridge', 'Suburb_Ivanhoe', 'Suburb_Ivanhoe East',
    'Suburb_Jacana', 'Suburb_Kealba', 'Suburb_Keilor', 'Suburb_Keilor Downs',
    'Suburb_Keilor East', 'Suburb_Keilor Lodge', 'Suburb_Keilor Park',
    'Suburb_Kensington', 'Suburb_Kew', 'Suburb_Kew East', 'Suburb_Keysborough',
    'Suburb_Kilsyth', 'Suburb_Kings Park', 'Suburb_Kingsbury', 'Suburb_Kingsville',
    'Suburb_Knoxfield', 'Suburb_Kooyong', 'Suburb_Kurunjang', 'Suburb_Lalor',
    'Suburb_Langwarrin', 'Suburb_Lower Plenty', 'Suburb_Maidstone', 'Suburb_Malvern',
    'Suburb_Malvern East', 'Suburb_Maribyrnong', 'Suburb_McKinnon',
    'Suburb_Meadow Heights', 'Suburb_Melbourne', 'Suburb_Melton', 'Suburb_Melton South',
    'Suburb_Melton West', 'Suburb_Mentone', 'Suburb_Mernda', 'Suburb_Middle Park',
    'Suburb_Mill Park', 'Suburb_Mitcham', 'Suburb_Monbulk', 'Suburb_Mont Albert',
    'Suburb_Montmorency', 'Suburb_Montrose', 'Suburb_Moonee Ponds', 'Suburb_Moorabbin',
    'Suburb_Mooroolbark', 'Suburb_Mordialloc', 'Suburb_Mount Evelyn',
    'Suburb_Mount Waverley', 'Suburb_Mulgrave', 'Suburb_Murrumbeena', 'Suburb_Narre Warren',
    'Suburb_New Gisborne', 'Suburb_Newport', 'Suburb_Niddrie', 'Suburb_Noble Park',
    'Suburb_North Melbourne', 'Suburb_North Warrandyte', 'Suburb_Northcote',
    'Suburb_Notting Hill', 'Suburb_Nunawading', 'Suburb_Oak Park', 'Suburb_Oakleigh',
    'Suburb_Oakleigh East', 'Suburb_Oakleigh South', 'Suburb_Officer',
    'Suburb_Ormond', 'Suburb_Pakenham', 'Suburb_Parkdale', 'Suburb_Parkville',
    'Suburb_Pascoe Vale', 'Suburb_Plumpton', 'Suburb_Point Cook', 'Suburb_Port Melbourne',
    'Suburb_Prahran', 'Suburb_Preston', 'Suburb_Princes Hill', 'Suburb_Reservoir',
    'Suburb_Richmond', 'Suburb_Riddells Creek', 'Suburb_Ringwood', 'Suburb_Ringwood East',
    'Suburb_Ringwood North', 'Suburb_Ripponlea', 'Suburb_Rockbank', 'Suburb_Rosanna',
    'Suburb_Rowville', 'Suburb_Roxburgh Park', 'Suburb_Sandhurst', 'Suburb_Sandringham',
    'Suburb_Scoresby', 'Suburb_Seabrook', 'Suburb_Seaford', 'Suburb_Seaholme',
    'Suburb_Seddon', 'Suburb_Silvan', 'Suburb_Skye', 'Suburb_South Kingsville',
    'Suburb_South Melbourne', 'Suburb_South Morang', 'Suburb_South Yarra',
    'Suburb_Southbank', 'Suburb_Spotswood', 'Suburb_Springvale', 'Suburb_Springvale South',
    'Suburb_St Albans', 'Suburb_St Helena', 'Suburb_St Kilda', 'Suburb_Strathmore',
    'Suburb_Strathmore Heights', 'Suburb_Sunbury', 'Suburb_Sunshine', 'Suburb_Sunshine North',
    'Suburb_Sunshine West', 'Suburb_Surrey Hills', 'Suburb_Sydenham', 'Suburb_Tarneit',
    'Suburb_Taylors Hill', 'Suburb_Taylors Lakes', 'Suburb_Templestowe',
    'Suburb_Templestowe Lower', 'Suburb_The Basin', 'Suburb_Thomastown', 'Suburb_Thornbury',
    'Suburb_Toorak', 'Suburb_Travancore', 'Suburb_Truganina', 'Suburb_Tullamarine',
    'Suburb_Upwey', 'Suburb_Vermont', 'Suburb_Vermont South', 'Suburb_Viewbank',
    'Suburb_Wallan', 'Suburb_Wantirna', 'Suburb_Wantirna South', 'Suburb_Warrandyte',
    'Suburb_Waterways', 'Suburb_Watsonia', 'Suburb_Watsonia North', 'Suburb_Werribee',
    'Suburb_West Footscray', 'Suburb_West Melbourne', 'Suburb_Westmeadows',
    'Suburb_Wheelers Hill', 'Suburb_Whittlesea', 'Suburb_Williams Landing',
    'Suburb_Williamstown', 'Suburb_Williamstown North', 'Suburb_Windsor',
    'Suburb_Wollert', 'Suburb_Wonga Park', 'Suburb_Wyndham Vale', 'Suburb_Yallambie',
    'Suburb_Yarra Glen', 'Suburb_Yarraville', 'Type_h', 'Type_t', 'Type_u',
    'Method_PI', 'Method_S', 'Method_SA', 'Method_SP', 'Method_VB',
    'CouncilArea_Banyule', 'CouncilArea_Bayside', 'CouncilArea_Boroondara',
    'CouncilArea_Brimbank', 'CouncilArea_Cardinia', 'CouncilArea_Casey',
    'CouncilArea_Darebin', 'CouncilArea_Frankston', 'CouncilArea_Glen Eira',
    'CouncilArea_Greater Dandenong', 'CouncilArea_Hobsons Bay', 'CouncilArea_Hume',
    'CouncilArea_Kingston', 'CouncilArea_Knox', 'CouncilArea_Macedon Ranges',
    'CouncilArea_Manningham', 'CouncilArea_Maribyrnong', 'CouncilArea_Maroondah',
    'CouncilArea_Melbourne', 'CouncilArea_Melton', 'CouncilArea_Monash',
    'CouncilArea_Moonee Valley', 'CouncilArea_Moorabool', 'CouncilArea_Moreland',
    'CouncilArea_Nillumbik', 'CouncilArea_Port Phillip', 'CouncilArea_Stonnington',
    'CouncilArea_Unavailable', 'CouncilArea_Unknown', 'CouncilArea_Whitehorse',
    'CouncilArea_Whittlesea', 'CouncilArea_Wyndham', 'CouncilArea_Yarra',
    'CouncilArea_Yarra Ranges', 'Regionname_Eastern Metropolitan',
    'Regionname_Eastern Victoria', 'Regionname_Northern Metropolitan',
    'Regionname_Northern Victoria', 'Regionname_South-Eastern Metropolitan',
    'Regionname_Southern Metropolitan', 'Regionname_Western Metropolitan',
    'Regionname_Western Victoria', 'Bedroom2_x_Bathroom'
]

            
            # Fill missing columns with zeros
            for col in model_features:
                if col not in input_df.columns:
                    input_df[col] = 0
            
            input_df = input_df[model_features]
            
            # Make prediction
            prediction = model.predict(input_df)[0]
            
            # Display beautiful result
            st.markdown(f"""
            <div class="result-container">
                <div class="result-label">Estimated Property Value</div>
                <div class="result-price">${prediction:,.0f}</div>
                <div style="margin-top: 1rem; opacity: 0.9;">
                    📊 Based on {len(model_features)} analyzed features
                </div>
            </div>
            """, unsafe_allow_html=True)
            
            # Additional insights
            st.success("✅ Prediction completed successfully!")
            
            # Display key property summary
            with st.expander("📋 Property Summary", expanded=True):
                col_a, col_b = st.columns(2)
                with col_a:
                    st.write(f"**🏠 Type:** {type_options[type_]}")
                    st.write(f"**🛏️ Bedrooms:** {bedroom2}")
                    st.write(f"**🛁 Bathrooms:** {bathroom}")
                    st.write(f"**🚗 Car Spaces:** {car}")
                with col_b:
                    st.write(f"**📍 Suburb:** {suburb}")
                    st.write(f"**🏙️ Distance to CBD:** {distance} km")
                    st.write(f"**📏 Land Size:** {landsize:,.0f} sqm")
                    st.write(f"**📅 Year Built:** {yearbuilt}")

# Footer
st.markdown("""
<div style="text-align: center; padding: 2rem; color: #6b7280; border-top: 1px solid #e5e7eb; margin-top: 3rem;">
    <p>🏠 Melbourne Property Predictor | Powered by Advanced Machine Learning</p>
</div>
""", unsafe_allow_html=True)
