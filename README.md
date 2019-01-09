# Fides

## Prerequisites

## Installation

### Install the agent
To install Fides AI agent for Python:

1. Install the client library 
    ```bash
    pip install fides
    ```  
    
1. Setting up authentication
    ```bash
    fides-admin generate_config_file LICENSE_KEY=...
    ```

### Explain a model

   ```python
    # Import client library
    import fides
    
    # Instantiate a client
    credentials = {
       'key': ...
    }
    client = fides.Client(credentials) 
     
    # The model to analyze 
    model_id = ... # Replace with the unique model identifier
    client.bind(prediction_fc=model.fit,
                training_data=X_train.values,
                mode='classification',
                class_names=['Positive', 'Negative'], 
                feature_names=X_train.columns.values,
                categorical_features=[1, 3, 7, 8],
                categorical_names={'Gender': {0: 'Male', 1: 'Female'}})
    
    # Track and explain inference
    client.explain(model_id, x, y) 
   ```



## Troubleshoot your installation
