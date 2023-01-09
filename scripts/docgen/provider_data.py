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
}
}

auth_blocks = {
'googleworkspace': {
    'auth': """
{
  "googleworkspace": {
    /**
      * Type of authentication to use, suported values include: service_account, interactive
      * @type String
      */
    "type": string, 
    /**
      * path to service account key file.
      * @type String
      */
    "credentialsfilepath": string, 
  }
}
""",
    'example': {
        'linux':
"""
AUTH='{ "googleworkspace": { "type": "service_account",  "credentialsfilepath": "creds/sa-key.json" }}'
stackql shell --auth="${AUTH}"
""",
        'windows':
"""
$Auth = "{ 'googleworkspace': { 'type': 'service_account',  'credentialsfilepath': 'creds/sa-key.json' }}"
stackql.exe shell --auth=$Auth
"""
    }
},
'googlemybusiness': {
    'auth': """
{
  "googlemybusiness": {
    /**
      * Type of authentication to use, suported values include: service_account, interactive
      * @type String
      */
    "type": string, 
    /**
      * path to service account key file.
      * @type String
      */
    "credentialsfilepath": string, 
  }
}
""",
    'example': {
        'linux':
"""
AUTH='{ "googlemybusiness": { "type": "service_account",  "credentialsfilepath": "creds/sa-key.json" }}'
stackql shell --auth="${AUTH}"
""",
        'windows':
"""
$Auth = "{ 'googlemybusiness': { 'type': 'service_account',  'credentialsfilepath': 'creds/sa-key.json' }}"
stackql.exe shell --auth=$Auth
"""
    }
},
'googledevelopers': {
    'auth': """
{
  "googledevelopers": {
    /**
      * Type of authentication to use, suported values include: service_account, interactive
      * @type String
      */
    "type": string, 
    /**
      * path to service account key file.
      * @type String
      */
    "credentialsfilepath": string, 
  }
}
""",
    'example': {
        'linux':
"""
AUTH='{ "googledevelopers": { "type": "service_account",  "credentialsfilepath": "creds/sa-key.json" }}'
stackql shell --auth="${AUTH}"
""",
        'windows':
"""
$Auth = "{ 'googledevelopers': { 'type': 'service_account',  'credentialsfilepath': 'creds/sa-key.json' }}"
stackql.exe shell --auth=$Auth
"""
    }
},
'googleanalytics': {
    'auth': """
{
  "googleanalytics": {
    /**
      * Type of authentication to use, suported values include: service_account, interactive
      * @type String
      */
    "type": string, 
    /**
      * path to service account key file.
      * @type String
      */
    "credentialsfilepath": string, 
  }
}
""",
    'example': {
        'linux':
"""
AUTH='{ "googleanalytics": { "type": "service_account",  "credentialsfilepath": "creds/sa-key.json" }}'
stackql shell --auth="${AUTH}"
""",
        'windows':
"""
$Auth = "{ 'googleanalytics': { 'type': 'service_account',  'credentialsfilepath': 'creds/sa-key.json' }}"
stackql.exe shell --auth=$Auth
"""
    }
},
'googleads': {
    'auth': """
{
  "googleads": {
    /**
      * Type of authentication to use, suported values include: service_account, interactive
      * @type String
      */
    "type": string, 
    /**
      * path to service account key file.
      * @type String
      */
    "credentialsfilepath": string, 
  }
}
""",
    'example': {
        'linux':
"""
AUTH='{ "googleads": { "type": "service_account",  "credentialsfilepath": "creds/sa-key.json" }}'
stackql shell --auth="${AUTH}"
""",
        'windows':
"""
$Auth = "{ 'googleads': { 'type': 'service_account',  'credentialsfilepath': 'creds/sa-key.json' }}"
stackql.exe shell --auth=$Auth
"""
    }
},
'youtube': {
    'auth': """
{
  "youtube": {
    /**
      * Type of authentication to use, suported values include: service_account, interactive
      * @type String
      */
    "type": string, 
    /**
      * path to service account key file.
      * @type String
      */
    "credentialsfilepath": string, 
  }
}
""",
    'example': {
        'linux':
"""
AUTH='{ "youtube": { "type": "service_account",  "credentialsfilepath": "creds/sa-key.json" }}'
stackql shell --auth="${AUTH}"
""",
        'windows':
"""
$Auth = "{ 'youtube': { 'type': 'service_account',  'credentialsfilepath': 'creds/sa-key.json' }}"
stackql.exe shell --auth=$Auth
"""
    }
},  
'firebase': {
    'auth': """
{
  "firebase": {
    /**
      * Type of authentication to use, suported values include: service_account, interactive
      * @type String
      */
    "type": string, 
    /**
      * path to service account key file.
      * @type String
      */
    "credentialsfilepath": string, 
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
    /**
      * Type of authentication to use, suported values include: basic
      * @type String
      */
    "type": string, 
    /**
      * Environment variable name containing the api key or credentials.
      * Variable value must be a base64 encoded string of the form: username:password
      * @type String
      */
    "credentialsenvvar": string, 
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
    /**
      * Type of authentication to use, suported values include: service_account, interactive
      * @type String
      */
    "type": string, 
    /**
      * path to service account key file.
      * @type String
      */
    "credentialsfilepath": string, 
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
    /**
      * Type of authentication to use, suported values include: api_key, null_auth
      * @type String
      */
    "type": string, 
    /**
      * Environment variable name containing the api key or credentials.
      * @type String
      */
    "credentialsenvvar": string, 
    /**
      * Value prepended to the request header, e.g. "Bearer "
      * Must be set to "Bearer "
      * @type String
      */
    "valuePrefix": string, 
  }
}
""",
    'example': {}
},
'netlify': {
    'auth': """
{
  "netlify": {
    /**
      * Type of authentication to use, suported values include: api_key
      * @type String
      */
    "type": string, 
    /**
      * Environment variable name containing the api key or credentials.
      * @type String
      */
    "credentialsenvvar": string, 
    /**
      * Value prepended to the request header, e.g. "Bearer "
      * Must be set to "Bearer "
      * @type String
      */
    "valuePrefix": string, 
  }
}
""",
    'example': {
        'linux':
"""
NETLIFY_TOKEN=yourtoken
AUTH='{ "netlify": { "type": "api_key",  "credentialsenvvar": "NETLIFY_TOKEN", "valuePrefix": "Bearer " }}'
stackql shell --auth="${AUTH}"
""",
        'windows':
"""
$env:NETLIFY_TOKEN = "yourtoken"
$Auth = "{ 'netlify': { 'type': 'api_key',  'credentialsenvvar': 'NETLIFY_TOKEN', 'valuePrefix': 'Bearer ' }}"
stackql.exe shell --auth=$Auth
"""
    }
},
'okta': {
    'auth': """
{
    "okta": {
     /**
      * Type of authentication to use, suported values include:  api_key
      * @type String
      */
     "type": string, 
     /**
      * Environment variable name containing the api key or credentials.
      * @type String
      */
     "credentialsenvvar": string, 
    }
}
""",
    'example': {
        'linux':
"""
OKTA_SECRET_KEY=yourapikey
AUTH='{ "okta": { "type": "api_key",  "credentialsenvvar": "OKTA_SECRET_KEY" }}'
stackql shell --auth="${AUTH}"
""",
        'windows':
"""
$env:OKTA_SECRET_KEY = "yourapikey"
$Auth = "{ 'okta': { 'type': 'api_key',  'credentialsenvvar': 'OKTA_SECRET_KEY' }}"
stackql.exe shell --auth=$Auth
"""
    }
},
'aws': {
    'auth': """
{
    "aws": {
     /**
      * Type of authentication to use, suported values include:  aws_signing_v4
      * @type String
      */
     "type": string, 
     /**
      * Environment variable name containing the api key or credentials.
      * @type String
      */
     "credentialsenvvar": string,
     /**
      * Value of AWS_ACCESS_KEY_ID.
      * @type String
      */
     "keyID": string,      
    }
}
""",
    'example': {
        'linux':
"""
AUTH="{ \"aws\": { \"type\": \"aws_signing_v4\", \"credentialsenvvar\": \"AWS_SECRET_ACCESS_KEY\", \"keyID\": \"${AWS_ACCESS_KEY_ID}\" }}"
stackql shell --auth="${AUTH}"
""",
        'windows':  
"""
$Auth = "{ 'aws': { 'type': 'aws_signing_v4',  'credentialsenvvar': 'AWS_SECRET_ACCESS_KEY', 'keyID': '$Env.AWS_ACCESS_KEY_ID' }}"
stackql.exe shell --auth=$Auth
"""
    }
},
'azure': {
    'auth': """
{
  "azure": {
    /**
      * Type of authentication to use, suported values include: api_key
      * @type String
      */
    "type": string, 
    /**
      * Environment variable name containing the api token obtained using the azure cli or SDK.
      * @type String
      */
    "credentialsenvvar": string, 
    /**
      * Value prepended to the request header, e.g. "Bearer "
      * Must be set to "Bearer "
      * @type String
      */
    "valuePrefix": string, 
  }
}
""",
    'example': {
        'linux': """
AZ_ACCESS_TOKEN_RAW=$(az account get-access-token --query accessToken --output tsv)
export AZ_ACCESS_TOKEN=`echo $AZ_ACCESS_TOKEN_RAW | tr -d '\\r'`
AUTH='{ "azure": { "type": "api_key", "valuePrefix": "Bearer ", "credentialsenvvar": "AZ_ACCESS_TOKEN" } }'
stackql shell --auth="${AUTH}"
""",
        'windows': """
$Env:AZ_ACCESS_TOKEN = "$(az account get-access-token --query accessToken --output tsv)".Trim("`r")
$Auth = "{ 'azure': { 'type': 'api_key', 'valuePrefix': 'Bearer ', 'credentialsenvvar': 'AZ_ACCESS_TOKEN' } }"
stackql.exe shell --auth=$Auth
"""
    }
}
}