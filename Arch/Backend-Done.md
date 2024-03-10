## Models

#### Patient Model
- Patient

    - phone number
        - UUID for our purpose
    - Patient Id
        - using mongoose _id
    - Patient Name
    - Date of birth
        - age gets calc by virtual function 
    - Health Report 
        - (owm model later/chart )
        - Url for now

    - Existing disease
        - No use as of now
        - (later make this its own model)
    - timestamps: true
        - Created At
        - Updated At

    - previous test/reports
        - stores either cloudinary url or data 
        - can use something that make the pdf from data (latex)
    
    - reference to symptoms
        doing (done but to figure out how does it work)?


#### Symptoms
- Symptoms
    - array of Symptom
    - do we need to store the users too ?

#### Symptom

- Symptom 
    - name
    - description
    - severity
    - duration
    - createdAt

    all these feilds are required