provider_data = {
'digitalocean': {
    'meta_description': 'Query, deploy and manage Sumologic resources using SQL',
    'description': 'Cloud computing services and Infrastructure as a Service (IaaS).',
    'image': '/img/providers/digitalocean/stackql-digitalocean-provider-featured-image.png' 
},
'sumologic': {
    'meta_description': 'Query, deploy and manage Sumologic resources using SQL',
    'description': 'Cloud-native, real-time, unified logs and metrics analytics platform.',
    'image': '/img/providers/sumologic/stackql-sumologic-provider-featured-image.png' 
},
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
'firebase': {
    'meta_description': 'Query, deploy and manage Google Cloud Platform (GCP) infrastructure and resources using SQL',
    'description': 'Application development platform for creating mobile and web applications.',
    'image': '/img/providers/firebase/stackql-firebase-provider-featured-image.png' 
},
'github': {
    'meta_description': 'Query, deploy and manage GitHub resources using SQL',
    'description': 'Web-based version-control and collaboration.',
    'image': '/img/providers/github/stackql-github-provider-featured-image.png' 
},
'google': {
    'meta_description': 'Query, deploy and manage Google Cloud Platform (GCP) infrastructure and resources using SQL',
    'description': 'Cloud computing services offered by Google.',
    'image': '/img/providers/google/stackql-google-provider-featured-image.png' 
},
'k8s': {
    'meta_description': 'Query, deploy and manage Kubernetes resources using SQL',
    'description': 'Open source container management platform.',
    'image': '/img/providers/k8s/stackql-k8s-provider-featured-image.png' 
},
'netlify': {
    'meta_description': 'Query, deploy and manage Netlify resources using SQL',
    'description': 'Web development and content distribution platform.',
    'image': '/img/providers/netlify/stackql-netlify-provider-featured-image.png' 
},
'okta': {
    'meta_description': 'Query, deploy and manage Okta resources using SQL',
    'description': 'Authentication and authorization services.',
    'image': '/img/providers/okta/stackql-okta-provider-featured-image.png' 
},
'aws': {
    'meta_description': 'Query, deploy and manage AWS resources using SQL',
    'description': 'Cloud services from AWS.',
    'image': '/img/providers/aws/stackql-aws-provider-featured-image.png' 
},
'azure': {
    'meta_description': 'Query, deploy and manage Azure resources using SQL',
    'description': ' Cloud computing services operated by Microsoft.',
    'image': '/img/providers/azure/stackql-azure-provider-featured-image.png' 
},
'azure_extras': {
    'meta_description': 'Query, deploy and manage Azure resources using SQL',
    'description': ' Additional Azure cloud computing services by Microsoft.',
    'image': '/img/providers/azure/stackql-azure-provider-featured-image.png' 
}
}

auth_blocks = {
'digitalocean': {
  'variables': """
- `DIGITALOCEAN_TOKEN` - DigitalOcean API token
  """,
 'linux': """
AUTH='{ "netlify": { "type": "bearer",  "credentialsenvvar": "YOUR_DIGITALOCEAN_TOKEN_VAR" }}'
stackql shell --auth="${AUTH}"
 """,
 'windows': """
$Auth = "{ 'netlify': { 'type': 'bearer',  'credentialsenvvar': 'YOUR_DIGITALOCEAN_TOKEN_VAR' }}"
stackql.exe shell --auth=$Auth
 """,
},
'sumologic': {
    'auth': """
{
  "sumologic": {
    "type": string, // authentication type to use, suported values:  basic
    "credentialsenvvar": string, // env var name containing the base64 encoded string in the form: username:password
  }
}
""",
    'example': {
        'linux':
"""
export SUMO_CREDS=$(echo -n 'youraccessid:YOURACCESSTOKEN' | base64 --wrap 0)
AUTH='{ "sumologic": { "type": "basic", "credentialsenvvar": "SUMO_CREDS" } }'
stackql shell --auth="${AUTH}"
""",
        'windows':
"""
$env:SUMO_CREDS = [System.Convert]::ToBase64String([System.Text.Encoding]::UTF8.GetBytes("youraccessid:YOURACCESSTOKEN"))
$Auth = "{ 'sumologic': { 'type': 'basic', 'credentialsenvvar': 'SUMO_CREDS' } }"
stackql.exe shell --auth=$Auth
"""
    }
},  
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
'firebase': {
    'auth': """
{
  "firebase": {
    "type": string, // authentication type to use, suported values:  service_account
    "credentialsfilepath": string, // path to service account key file
  }
}
""",
    'example': {
        'linux':
"""
AUTH='{ "firebase": { "type": "service_account",  "credentialsfilepath": "creds/sa-key.json" }}'
stackql shell --auth="${AUTH}"
""",
        'windows':
"""
$Auth = "{ 'firebase': { 'type': 'service_account',  'credentialsfilepath': 'creds/sa-key.json' }}'
stackql.exe shell --auth=$Auth
"""
    }
},
'github': {
    'auth': """
{
  "github": {
    "type": string, // authentication type to use, suported values:  basic
    "credentialsenvvar": string, // env var name containing the base64 encoded string in the form: username:password
  }
}
""",
    'example': {
        'linux': 
"""
export GITHUB_CREDS=$(echo -n 'yourusername:ghp_YOURPERSONALACCESSTOKEN' | base64)
AUTH='{ "github": { "type": "basic", "credentialsenvvar": "GITHUB_CREDS" } }'
stackql shell --auth="${AUTH}"
""",
        'windows':
"""
$env:GITHUB_CREDS = [System.Convert]::ToBase64String([System.Text.Encoding]::UTF8.GetBytes("yourusername:ghp_YOURPERSONALACCESSTOKEN"))
$Auth = "{ 'github': { 'type': 'basic', 'credentialsenvvar': 'GITHUB_CREDS' } }"
stackql shell --auth=$Auth
"""
    }
},
'google': {
    'auth': """
{
  "google": {
    "type": string, // authentication type to use, suported values include: service_account, interactive
    "credentialsfilepath": string, // path to service account key file
  }
}
""",
    'example': {
        'linux':
"""
AUTH='{ "google": { "type": "service_account",  "credentialsfilepath": "creds/sa-key.json" }}'
stackql shell --auth="${AUTH}"
""",
        'windows':
"""
$Auth = "{ 'google': { 'type': 'service_account',  'credentialsfilepath': 'creds/sa-key.json' }}"
stackql.exe shell --auth=$Auth
"""
    }
},
'k8s': {
    'auth': """
{
  "k8s": {
    "type": string, // authentication type to use, suported values include: bearer, null_auth
    "credentialsenvvar": string, // env var name containing the api key or credentials
  }
}
""",
    'example': {}
},
'netlify': {
    'auth': """
{
  "netlify": {
    "type": string, // authentication type to use, suported values include: bearer
    "credentialsenvvar": string, // env var name containing the acces token
  }
}
""",
    'example': {
        'linux':
"""
NETLIFY_TOKEN=yourtoken
AUTH='{ "netlify": { "type": "bearer",  "credentialsenvvar": "NETLIFY_TOKEN" }}'
stackql shell --auth="${AUTH}"
""",
        'windows':
"""
$env:NETLIFY_TOKEN = "yourtoken"
$Auth = "{ 'netlify': { 'type': 'bearer',  'credentialsenvvar': 'NETLIFY_TOKEN' }}"
stackql.exe shell --auth=$Auth
"""
    }
},
'okta': {
    'auth': """
{
  "okta": {
    "type": string, // authentication type to use, suported values: api_key
    "credentialsenvvar": string, // env var name containing the api key
    "valuePrefix": string, // authorization prefix, suported values: "SSWS "
  }
}
""",
    'example': {
        'linux':
"""
OKTA_SECRET_KEY=yourapikey
AUTH='{ "okta": { "type": "api_key",  "credentialsenvvar": "OKTA_SECRET_KEY", "valuePrefix": "SSWS " }}'
stackql shell --auth="${AUTH}"
""",
        'windows':
"""
$env:OKTA_SECRET_KEY = "yourapikey"
$Auth = "{ 'okta': { 'type': 'api_key',  'credentialsenvvar': 'OKTA_SECRET_KEY', 'valuePrefix': 'SSWS ' }}"
stackql.exe shell --auth=$Auth
"""
    }
},
'aws': {
    'auth': """
{
  "aws": {
    "type": string, // authentication type to use, suported values:  aws_signing_v4
    "keyIDenvvar": string, // env var containing AWS_ACCESS_KEY_ID
    "credentialsenvvar": string, // env var containing AWS_SECRET_ACCESS_KEY
  }
}
""",
    'example': {
        'linux':
"""
AUTH="{ \"aws\": { \"type\": \"aws_signing_v4\", \"credentialsenvvar\": \"AWS_SECRET_ACCESS_KEY\", \"keyIDenvvar\": \"AWS_ACCESS_KEY_ID\" }}"
stackql shell --auth="${AUTH}"
""",
        'windows':  
"""
$Auth = "{ 'aws': { 'type': 'aws_signing_v4',  'credentialsenvvar': 'AWS_SECRET_ACCESS_KEY', 'keyIDenvvar': 'AWS_ACCESS_KEY_ID' }}"
stackql.exe shell --auth=$Auth
"""
    }
},
'azure': {
    'auth': """
{
  "azure": {
    "type": string, // authentication type to use, suported values include: bearer
    "credentialsenvvar": string, // env var name containing the access token
  }
}
""",
    'example': {
        'linux': """
AZ_ACCESS_TOKEN_RAW=$(az account get-access-token --query accessToken --output tsv)
export AZ_ACCESS_TOKEN=`echo $AZ_ACCESS_TOKEN_RAW | tr -d '\\r'`
AUTH='{ "azure": { "type": "bearer", "credentialsenvvar": "AZ_ACCESS_TOKEN" } }'
stackql shell --auth="${AUTH}"
""",
        'windows': """
$Env:AZ_ACCESS_TOKEN = "$(az account get-access-token --query accessToken --output tsv)".Trim("`r")
$Auth = "{ 'azure': { 'type': 'bearer', 'credentialsenvvar': 'AZ_ACCESS_TOKEN' } }"
stackql.exe shell --auth=$Auth
"""
    }
},
'azure_extras': {
    'auth': """
{
  "azure_extras": {
    "type": string, // authentication type to use, suported values include: bearer
    "credentialsenvvar": string, // env var name containing the access token
  }
}
""",
    'example': {
        'linux': """
AZ_ACCESS_TOKEN_RAW=$(az account get-access-token --query accessToken --output tsv)
export AZ_ACCESS_TOKEN=`echo $AZ_ACCESS_TOKEN_RAW | tr -d '\\r'`
AUTH='{ "azure_extras": { "type": "bearer", "credentialsenvvar": "AZ_ACCESS_TOKEN" } }'
stackql shell --auth="${AUTH}"
""",
        'windows': """
$Env:AZ_ACCESS_TOKEN = "$(az account get-access-token --query accessToken --output tsv)".Trim("`r")
$Auth = "{ 'azure_extras': { 'type': 'bearer', 'credentialsenvvar': 'AZ_ACCESS_TOKEN' } }"
stackql.exe shell --auth=$Auth
"""
    }
}
}