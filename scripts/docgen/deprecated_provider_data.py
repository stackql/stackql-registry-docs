provider_data = {
    'googleworkspace': {
        'meta_description': 'Query, deploy and manage Google Cloud Platform (GCP) infrastructure and resources using SQL',
        'description': 'Productivity and collaboration tools for businesses.',
        'image': '/img/providers/googleworkspace/stackql-googleworkspace-provider-featured-image.png' 
    },
    'googlemybusiness': {
        'meta_description': 'Query, deploy and manage Google Cloud Platform (GCP) infrastructure and resources using SQL',
        'description': 'Tools for businesses to manage their online presence.',
        'image': '/img/providers/googlemybusiness/stackql-googlemybusiness-provider-featured-image.png' 
    },
    'googledevelopers': {
        'meta_description': 'Query, deploy and manage Google Cloud Platform (GCP) infrastructure and resources using SQL',
        'description': 'Developer APIs by Google.',
        'image': '/img/providers/googledevelopers/stackql-googledevelopers-provider-featured-image.png' 
    },
    'googleanalytics': {
        'meta_description': 'Query, deploy and manage Google Cloud Platform (GCP) infrastructure and resources using SQL',
        'description': 'Web tracking and analytics service.',
        'image': '/img/providers/googleanalytics/stackql-googleanalytics-provider-featured-image.png' 
    },
    'googleads': {
        'meta_description': 'Query, deploy and manage Google Cloud Platform (GCP) infrastructure and resources using SQL',
        'description': 'Online advertising platform by Google.',
        'image': '/img/providers/googleads/stackql-googleads-provider-featured-image.png' 
    },
    'youtube': {
        'meta_description': 'Query, deploy and manage Google Cloud Platform (GCP) infrastructure and resources using SQL',
        'description': 'Online video sharing and social media platform.',
        'image': '/img/providers/youtube/stackql-youtube-provider-featured-image.png' 
    },
}

auth_blocks = {
  'googleworkspace': {
      'auth': """
  {
    "googleworkspace": {
      "type": string, // authentication type to use, suported values:  service_account
      "credentialsfilepath": string, // path to service account key file
      "scopes": string[], // array of scopes required for API authorization, see [scopes](https://developers.google.com/identity/protocols/oauth2/scopes)
    }
  }
  """,
      'example': {
          'linux':
  """
  AUTH='{ "googleworkspace": { "type": "service_account",  "credentialsfilepath": "creds/sa-key.json", "scopes": ["https://www.googleapis.com/auth/drive", "..."]  }}'
  stackql shell --auth="${AUTH}"
  """,
          'windows':
  """
  $Auth = "{ 'googleworkspace': { 'type': 'service_account',  'credentialsfilepath': 'creds/sa-key.json', 'scopes': ['https://www.googleapis.com/auth/drive', '...'] }}"
  stackql.exe shell --auth=$Auth
  """
      }
  },
  'googlemybusiness': {
      'auth': """
  {
    "googlemybusiness": {
      "type": string, // authentication type to use, suported values:  service_account
      "credentialsfilepath": string, // path to service account key file
      "scopes": string[], // array of scopes required for API authorization, see [scopes](https://developers.google.com/identity/protocols/oauth2/scopes)
    }
  }
  """,
      'example': {
          'linux':
  """
  AUTH='{ "googlemybusiness": { "type": "service_account",  "credentialsfilepath": "creds/sa-key.json", "scopes": ["https://www.googleapis.com/auth/...", "..."]  }}'
  stackql shell --auth="${AUTH}"
  """,
          'windows':
  """
  $Auth = "{ 'googlemybusiness': { 'type': 'service_account',  'credentialsfilepath': 'creds/sa-key.json', 'scopes': ['https://www.googleapis.com/auth/...', '...'] }}"
  stackql.exe shell --auth=$Auth
  """
      }
  },
  'googledevelopers': {
      'auth': """
  {
    "googledevelopers": {
      "type": string, // authentication type to use, suported values:  service_account
      "credentialsfilepath": string, // path to service account key file
      "scopes": string[], // array of scopes required for API authorization, see [scopes](https://developers.google.com/identity/protocols/oauth2/scopes)
    }
  }
  """,
      'example': {
          'linux':
  """
  AUTH='{ "googledevelopers": { "type": "service_account",  "credentialsfilepath": "creds/sa-key.json", "scopes": ["https://www.googleapis.com/auth/...", "..."]  }}'
  stackql shell --auth="${AUTH}"
  """,
          'windows':
  """
  $Auth = "{ 'googledevelopers': { 'type': 'service_account',  'credentialsfilepath': 'creds/sa-key.json', 'scopes': ['https://www.googleapis.com/auth/...', '...'] }}"
  stackql.exe shell --auth=$Auth
  """
      }
  },
  'googleanalytics': {
      'auth': """
  {
    "googleanalytics": {
      "type": string, // authentication type to use, suported values:  service_account
      "credentialsfilepath": string, // path to service account key file
      "scopes": string[], // array of scopes required for API authorization, see [scopes](https://developers.google.com/identity/protocols/oauth2/scopes)
    }
  }
  """,
      'example': {
          'linux':
  """
  AUTH='{ "googleanalytics": { "type": "service_account",  "credentialsfilepath": "creds/sa-key.json", "scopes": ["https://www.googleapis.com/auth/...", "..."]  }}'
  stackql shell --auth="${AUTH}"
  """,
          'windows':
  """
  $Auth = "{ 'googleanalytics': { 'type': 'service_account',  'credentialsfilepath': 'creds/sa-key.json', 'scopes': ['https://www.googleapis.com/auth/...', '...'] }}"
  stackql.exe shell --auth=$Auth
  """
      }
  },
  'googleads': {
      'auth': """
  {
    "googleads": {
      "type": string, // authentication type to use, suported values:  service_account
      "credentialsfilepath": string, // path to service account key file
      "scopes": string[], // array of scopes required for API authorization, see [scopes](https://developers.google.com/identity/protocols/oauth2/scopes)
    }
  }
  """,
      'example': {
          'linux':
  """
  AUTH='{ "googleads": { "type": "service_account",  "credentialsfilepath": "creds/sa-key.json", "scopes": ["https://www.googleapis.com/auth/...", "..."]  }}'
  stackql shell --auth="${AUTH}"
  """,
          'windows':
  """
  $Auth = "{ 'googleads': { 'type': 'service_account',  'credentialsfilepath': 'creds/sa-key.json', 'scopes': ['https://www.googleapis.com/auth/...', '...'] }}"
  stackql.exe shell --auth=$Auth
  """
      }
  },
  'youtube': {
      'auth': """
  {
    "youtube": {
      "type": string, // authentication type to use, suported values:  service_account
      "credentialsfilepath": string, // path to service account key file
      "scopes": string[], // array of scopes required for API authorization, see [scopes](https://developers.google.com/identity/protocols/oauth2/scopes)
    }
  }
  """,
      'example': {
          'linux':
  """
  AUTH='{ "youtube": { "type": "service_account",  "credentialsfilepath": "creds/sa-key.json", "scopes": ["https://www.googleapis.com/auth/...", "..."]  }}'
  stackql shell --auth="${AUTH}"
  """,
          'windows':
  """
  $Auth = "{ 'youtube': { 'type': 'service_account',  'credentialsfilepath': 'creds/sa-key.json', 'scopes': ['https://www.googleapis.com/auth/...', '...'] }}"
  stackql.exe shell --auth=$Auth
  """
      }
  },
}