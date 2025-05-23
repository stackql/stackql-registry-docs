googleadmin_auth_markdown = """
The following authentication methods are supported:
- <CopyableCode code="service_account" /> (using a Google Cloud service account)

> for more information on creating service accounts and key files, see .

### Setup instructions

To authorize a Google Cloud service account for use in the Admin SDK, follow the instructions provided here:  

<details>

<summary>1. Create a Service Account (from the Google Cloud Console)</summary>

- Create a Google Cloud service account (see [Service accounts overview](https://cloud.google.com/iam/docs/service-account-overview)).
- Download the JSON key file for the service account (see [Service account keys](https://cloud.google.com/iam/docs/service-account-creds#key-types)).
- From the Google Cloud Console, locate and select the service account created, go to __"Details" > "Advanced settings" > "Domain-wide delegation"__. 
- Copy the __"Client ID"__ of the service account to the clipboard.
- Click the __"VIEW GOOGLE WORKSPACE ADMIN CONSOLE"__ link. This will open the Google Workspace Admin Console in a new tab.

</details>

<details>

<summary>2. Enable the Admin SDK API for your project (from the Google Cloud Console)</summary>

- From the Google Cloud Console, in the same project that you created the Service Account in step 1, go to __"APIs & Services" > "Library"__.
- Search for __"Admin SDK API"__ and click on it.
- Click __"Enable"__.

</details>

<details>

<summary>3. Delegate Domain-Wide Authority to your Service Account (from the Google Workspace Admin Console)</summary>

- From the Google Workspace Admin Console, go to __"Security" > "Access and data control" > "API Controls" > "Domain-wide delegation" > "MANAGE DOMAIN-WIDE DELEGATION"__.
- Click __"Add new"__ and paste the __"Client ID"__ of the service account copied to the clipboard in step 1.
- In the __"OAuth scopes"__ field, enter the following scopes: __`https://www.googleapis.com/auth/cloud-platform`__ and __`https://www.googleapis.com/auth/admin.directory.user.readonly`__.
- Click __"Authorise"__.

</details>

<details>

<summary>4. Assign the Admin role to your Service Account (from the Google Workspace Admin Console)</summary>

- From the Google Workspace Admin Console, go to __"Account" > "Admin roles" > "User Management" > "Admins" > "Assign service accounts"__.
- Add the email to the service account created in step 1 and click __"Assign Role"__.  For more information, see [Assigning a role to a service account](https://developers.google.com/workspace/guides/create-credentials#assign_a_role_to_a_service_account).

</details>

### Service Account Environment Variable (default)

The following system environment variable is used by default:  

- <CopyableCode code="GOOGLE_CREDENTIALS" /> - contents of the <code>google</code> service account key json file

This variable is sourced at runtime (from the local machine using `export GOOGLE_CREDENTIALS=cat creds/my-sa-key.json` for example or as a CI variable/secret).

<details>

<summary>Specifying the service account key file location directly</summary>

You can specify the path to the service account key file without using the default environment variable by using the `--auth` flag of the `stackql` program.  For example:  

```bash
AUTH='{ "google": { "type": "service_account",  "credentialsfilepath": "creds/sa-key.json" }}'
stackql shell --auth="${AUTH}"
```

or using PowerShell:  

```powershell
$Auth = "{ 'google': { 'type': 'service_account',  'credentialsfilepath': 'creds/sa-key.json' }}"
stackql.exe shell --auth=$Auth
```

</details>
"""

google_auth_markdown = """
The following authentication methods are supported:
- <CopyableCode code="service_account" />
- <CopyableCode code="interactive" /> for running interactive queries from Cloud Shell or other machines where the user is authenticated using <CopyableCode code="gcloud auth login" />

> for more information on creating service accounts and key files, see [Service accounts overview](https://cloud.google.com/iam/docs/service-account-overview).

### Service Account Environment Variable (default)

The following system environment variable is used by default:  

- <CopyableCode code="GOOGLE_CREDENTIALS" /> - contents of the <code>google</code> service account key json file.  This variable is sourced at runtime (from the local machine using <code>export GOOGLE_CREDENTIALS=cat creds/my-sa-key.json</code> for example or as a CI variable/secret).

This variable is sourced at runtime (from the local machine using `export GOOGLE_CREDENTIALS=$(cat creds/my-sa-key.json)` for example or as a CI variable/secret).

<details>

<summary>Specifying the service account key file location directly</summary>

You can specify the path to the service account key file without using the default environment variable by using the <CopyableCode code="--auth" /> flag of the <code>stackql</code> program.  For example:  

```bash
AUTH='{ "google": { "type": "service_account",  "credentialsfilepath": "creds/sa-key.json" }}'
stackql shell --auth="${AUTH}"
```

or using PowerShell:  

```powershell
$Auth = "{ 'google': { 'type': 'service_account',  'credentialsfilepath': 'creds/sa-key.json' }}"
stackql.exe shell --auth=$Auth
```

</details>

### Interactive Authentication
When you are using Google Cloud Shell or on a machine where you have authenticated using <CopyableCode code="gcloud auth login" />, you can then use the following authentication method:   

```bash
AUTH='{ "google": { "type": "interactive" }}'
stackql shell --auth="${AUTH}"
```

or using PowerShell:  

```powershell
$Auth = "{ 'google': { 'type': 'interactive' }}"
stackql.exe shell --auth=$Auth
```
"""

provider_data = {
  'confluent': {
      'meta_description': 'Query, deploy, and manage Confluent Cloud resources using SQL.',
      'description': 'Confluent Cloud for managing Kafka clusters, topics, and streaming services in a scalable cloud environment.',
      'image': '/img/providers/confluent/stackql-confluent-provider-featured-image.png'
  },
  'anthropic': {
      'meta_description': 'Query, deploy, and manage Anthropic resources using SQL.',
      'description': 'AI models including Claude for advanced language understanding and generation.',
      'image': '/img/providers/anthropic/stackql-anthropic-provider-featured-image.png'
  },    
  'openai': {
      'meta_description': 'Query, deploy, and manage OpenAI and ChatGPT resources using SQL.',
      'description': 'AI models for natural language processing and content generation.',
      'image': '/img/providers/openai/stackql-openai-provider-featured-image.png'
  },
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
  'googleadmin': {
      'meta_description': 'Query and manage Google Workspace users and groups using SQL.',
      'description': 'Google Workspace identity services.',
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
      'description': 'Cloud services by AWS.',
      'image': '/img/providers/aws/stackql-aws-provider-featured-image.png' 
  },
  'azure': {
      'meta_description': 'Query, deploy and manage Azure resources using SQL',
      'description': 'Cloud computing services operated by Microsoft.',
      'image': '/img/providers/azure/stackql-azure-provider-featured-image.png' 
  },
  'azure_extras': {
      'meta_description': 'Query, deploy and manage Azure resources using SQL',
      'description': 'Additional Azure cloud computing services by Microsoft.',
      'image': '/img/providers/azure/stackql-azure-provider-featured-image.png' 
  },
  'azure_isv': {
      'meta_description': 'Query, deploy and manage Azure resources using SQL',
      'description': 'Provision, manage, and integrate independent software vendor services on Azure.',
      'image': '/img/providers/azure/stackql-azure-provider-featured-image.png' 
  },
  'azure_stack': {
      'meta_description': 'Query, deploy and manage Azure resources using SQL',
      'description': 'Build and run hybrid apps across datacenters, edge locations, remote offices, and the cloud.',
      'image': '/img/providers/azure/stackql-azure-provider-featured-image.png' 
  },    
  'linode': {
      'meta_description': 'Query, deploy and manage Linode resources using SQL',
      'description': 'Cloud Computing Services by Akamai.',
      'image': '/img/providers/linode/stackql-linode-provider-featured-image.png' 
  },
  'vercel': {
      'meta_description': 'Query, deploy, and manage Vercel resources using SQL',
      'description': 'Cloud platform for serverless deployment and hosting of web applications.',
      'image': '/img/providers/vercel/stackql-vercel-provider-featured-image.png'
  },
  'godaddy': {
      'meta_description': 'Query, deploy and manage GoDaddy resources using SQL',
      'description': 'Domain registration and web hosting services.',
      'image': '/img/providers/godaddy/stackql-godaddy-provider-featured-image.png'
  },
  'pagerduty': {
      'meta_description': 'Query, manage, and integrate PagerDuty resources using SQL',
      'description': 'Incident management platform for real-time operations and response workflows.',
      'image': '/img/providers/pagerduty/stackql-pagerduty-provider-featured-image.png'
  },
  'datadog': {
      'meta_description': 'Query, monitor, and manage Datadog resources using SQL',
      'description': 'Monitoring, alerting and reporting platform for cloud platforms and applications.',
      'image': '/img/providers/datadog/stackql-datadog-provider-featured-image.png'
  },
  'homebrew': {
      'meta_description': 'Query and report on Homebrew packages using SQL',
      'description': 'Open-source package manager for macOS and Linux.',
      'image': '/img/providers/homebrew/stackql-homebrew-provider-featured-image.png'
  },
}

auth_blocks = {
# 
# Confluent
#  
'confluent': {
    'custom': False,
    'variables': """
- <CopyableCode code="CONFLUENT_CLOUD_API_KEY" /> - Confluent Cloud API key (see <a href="https://confluent.cloud/settings/api-keys">Confluent Cloud API keys</a>)
- <CopyableCode code="CONFLUENT_CLOUD_API_SECRET" /> - Confluent Cloud API secret (see <a href="https://confluent.cloud/settings/api-keys">Confluent Cloud API keys</a>)
    """,
    'linux': """
AUTH='{ "confluent": { "type": "basic", "username_var": "MY_CONFLUENT_CLOUD_API_KEY_VAR", "password_var": "MY_CONFLUENT_CLOUD_API_SECRET_VAR" }}'
stackql shell --auth="${AUTH}"
    """,
    'windows': """
$Auth = "{ 'confluent': { 'type': 'basic', 'username_var': 'MY_CONFLUENT_CLOUD_API_KEY_VAR', 'password_var': 'MY_CONFLUENT_CLOUD_API_SECRET_VAR' }}"
stackql.exe shell --auth=$Auth
    """,
},
# 
# Anthropic
#  
'anthropic': {
    'custom': False,
    'variables': """
- <CopyableCode code="ANTHROPIC_API_KEY" /> - Anthropic API key (see <a href="https://docs.anthropic.com/claude/reference/getting-started-with-the-api">How to Create an Anthropic API Key</a>)
    """,
    'linux': """
AUTH='{ "anthropic": { "type": "bearer", "credentialsenvvar": "MY_ANTHROPIC_API_KEY_VAR" }}'
stackql shell --auth="${AUTH}"
    """,
    'windows': """
$Auth = "{ 'anthropic': { 'type': 'bearer', 'credentialsenvvar': 'MY_ANTHROPIC_API_KEY_VAR' }}"
stackql.exe shell --auth=$Auth
    """,
},
# 
# OpenAI
#  
  'openai': {
        'custom': False,
        'variables': """
- <CopyableCode code="OPENAI_API_KEY" /> - OpenAI API key (see <a href="https://platform.openai.com/account/api-keys">How to Create an OpenAI API Key</a>)
        """,
        'linux': """
AUTH='{ "openai": { "type": "bearer", "credentialsenvvar": "MY_OPENAI_API_KEY_VAR" }}'
stackql shell --auth="${AUTH}"
        """,
        'windows': """
$Auth = "{ 'openai': { 'type': 'bearer', 'credentialsenvvar': 'MY_OPENAI_API_KEY_VAR' }}"
stackql.exe shell --auth=$Auth
        """,
},
# 
# Linode
#  
  'linode': {
    'custom': False,
    'variables': """
- <CopyableCode code="LINODE_TOKEN" /> - Linode API token (see <a href="https://www.linode.com/docs/products/tools/api/guides/manage-api-tokens/#create-an-api-token">How to Create a Linode API Token</a>)
  """,
    'linux': """
AUTH='{ "linode": { "type": "bearer",  "credentialsenvvar": "YOUR_LINODE_TOKEN_VAR" }}'
stackql shell --auth="${AUTH}"
""",
    'windows': """
$Auth = "{ 'linode': { 'type': 'bearer',  'credentialsenvvar': 'YOUR_LINODE_TOKEN_VAR' }}"
stackql.exe shell --auth=$Auth
""",
  },
# 
# Digital Ocean
#  
  'digitalocean': {
    'custom': False,
    'variables': """
- <CopyableCode code="DIGITALOCEAN_ACCESS_TOKEN" /> - DigitalOcean API token (see <a href="https://docs.digitalocean.com/reference/api/create-personal-access-token/">How to Create a Personal Access Token</a>)
  """,
    'linux': """
AUTH='{ "digitalocean": { "type": "bearer",  "credentialsenvvar": "YOUR_DIGITALOCEAN_TOKEN_VAR" }}'
stackql shell --auth="${AUTH}"
""",
    'windows': """
$Auth = "{ 'digitalocean': { 'type': 'bearer',  'credentialsenvvar': 'YOUR_DIGITALOCEAN_TOKEN_VAR' }}"
stackql.exe shell --auth=$Auth
""",
  },
# 
# Sumo Logic
#  
  'sumologic': {
    'custom': False,
    'variables': """
- <CopyableCode code="SUMOLOGIC_ACCESSID" /> - SumoLogic Access ID (see <a href="https://help.sumologic.com/docs/manage/security/access-keys/">Generating an Access Key</a>)
- <CopyableCode code="SUMOLOGIC_ACCESSKEY" /> - SumoLogic Access Key (see <a href="https://help.sumologic.com/docs/manage/security/access-keys/">Generating an Access Key</a>)
  """,
    'linux': """
AUTH='{ "sumologic": { "type": "basic",  "username_var": "YOUR_SUMOLOGIC_ACCESS_ID_VAR", "password_var": "YOUR_SUMOLOGIC_ACCESS_KEY_VAR" }}'
stackql shell --auth="${AUTH}"
""",
    'windows': """
$Auth = "{ 'sumologic': { 'type': 'basic',  'username_var': 'YOUR_SUMOLOGIC_ACCESS_ID_VAR', 'password_var': 'YOUR_SUMOLOGIC_ACCESS_KEY_VAR' }}"
stackql.exe shell --auth=$Auth
""",
  },  
# 
# GitHub
#  
  'github': {
    'custom': False,
    'variables': """
- <CopyableCode code="STACKQL_GITHUB_USERNAME" /> - GitHub username (login)
- <CopyableCode code="STACKQL_GITHUB_PASSWORD" /> - GitHub Personal Access Token (see <a href="https://docs.github.com/en/enterprise-server@3.4/authentication/keeping-your-account-and-data-secure/creating-a-personal-access-token">Creating a personal access token</a>)
  """,
    'linux': """
AUTH='{ "github": { "type": "basic",  "username_var": "YOUR_GITHUB_USERNAME_VAR", "password_var": "YOUR_GITHUB_PASSWORD_VAR" }}'
stackql shell --auth="${AUTH}"
""",
    'windows': """
$Auth = "{ 'github': { 'type': 'basic',  'username_var': 'YOUR_GITHUB_USERNAME_VAR', 'password_var': 'YOUR_GITHUB_PASSWORD_VAR' }}"
stackql.exe shell --auth=$Auth
""",
  },
# 
# Netlify
#  
 'netlify': {
    'custom': False,
    'variables': """
- <CopyableCode code="NETLIFY_AUTH_TOKEN" /> - Netlify API token (see <a href="https://docs.netlify.com/api/get-started/#authentication">How to Create a Netlify API Token</a>)
  """,
    'linux': """
AUTH='{ "netlify": { "type": "bearer",  "credentialsenvvar": "YOUR_NETLIFY_AUTH_TOKEN_VAR" }}'
stackql shell --auth="${AUTH}"
""",
    'windows': """
$Auth = "{ 'netlify': { 'type': 'bearer',  'credentialsenvvar': 'YOUR_NETLIFY_AUTH_TOKEN_VAR' }}"
stackql.exe shell --auth=$Auth
""",
 },
# 
# AWS
# 
  'aws': {
    'custom': False,
    'variables': """
- `AWS_ACCESS_KEY_ID` - AWS Access Key ID (see [How to Create AWS Credentials](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_credentials_access-keys.html))
- `AWS_SECRET_ACCESS_KEY` - AWS Secret Access Key (see [How to Create AWS Credentials](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_credentials_access-keys.html))
- `AWS_SESSION_TOKEN` - [__OPTIONAL:__ only required if using `aws sts assume-role`] AWS Session Token (see [Temporary security credentials in IAM](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_credentials_temp.html))
  """,
    'linux': """
AUTH='{ "aws": { "type": "aws_signing_v4", "keyIDenvvar": "YOUR_ACCESS_KEY_ID_VAR", "credentialsenvvar": "YOUR_SECRET_KEY_VAR" }}'
stackql shell --auth="${AUTH}"
""",
    'windows': """
$Auth = "{ 'aws': { 'type': 'aws_signing_v4',  'keyIDenvvar': 'YOUR_ACCESS_KEY_ID_VAR', 'credentialsenvvar': 'YOUR_SECRET_KEY_VAR' }}"
stackql.exe shell --auth=$Auth
""",
  },
# 
# Okta
#
  'okta': {
    'custom': False,
    'variables': """
- <CopyableCode code="OKTA_API_TOKEN" /> - Okta API Token (see <a href="https://developer.okta.com/docs/guides/create-an-api-token/">Creating an Okta API Token</a>)
  """,
    'linux': """
AUTH='{ "okta": { "type": "api_key", "valuePrefix": "SSWS ", "credentialsenvvar": "YOUR_OKTA_API_TOKEN_VAR" }}'
stackql shell --auth="${AUTH}"
""",
    'windows': """
$Auth = "{ 'okta': { 'type': 'api_key',  'valuePrefix': 'SSWS ', 'credentialsenvvar': 'YOUR_OKTA_API_TOKEN_VAR' }}"
stackql.exe shell --auth=$Auth
""",
  },
# 
# Vercel
#
  'vercel': {
    'custom': False,
    'variables': """
- <CopyableCode code="VERCEL_API_TOKEN" /> - Vercel API Token (see <a href="https://vercel.com/account/tokens">Creating a Vercel API Token</a>)
  """,
    'linux': """
AUTH='{ "okta": { "type": "bearer", "credentialsenvvar": "YOUR_VERCEL_API_TOKEN_VAR" }}'
stackql shell --auth="${AUTH}"
""",
    'windows': """
$Auth = "{ 'okta': { 'type': 'bearer', 'credentialsenvvar': 'YOUR_VERCEL_API_TOKEN_VAR' }}"
stackql.exe shell --auth=$Auth
""",
  },
# 
# Godaddy
#
  'godaddy': {
    'custom': False,
    'variables': """
- <CopyableCode code="GODADDY_API_KEY" /> - Godaddy API key (see <a href="https://developer.godaddy.com/keys">Creating a Godaddy API Key</a>)
  """,
    'linux': """
AUTH='{ "okta": { "type": "bearer", "credentialsenvvar": "YOUR_GODADDY_API_KEY_VAR" }}'
stackql shell --auth="${AUTH}"
""",
    'windows': """
$Auth = "{ 'okta': { 'type': 'bearer', 'credentialsenvvar': 'YOUR_GODADDY_API_KEY_VAR' }}"
stackql.exe shell --auth=$Auth
""",
  },
# 
# PagerDuty
#
'pagerduty': {
  'custom': False,
  'variables': """
- <CopyableCode code="PAGERDUTY_API_TOKEN" /> - PagerDuty API token (see <a href="https://support.pagerduty.com/docs/api-access-keys#section-generating-a-general-access-rest-api-key">Creating a PagerDuty API Token</a>)
  """,
  'linux': """
AUTH='{ "pagerduty": { "type": "bearer", "credentialsenvvar": "YOUR_PAGERDUTY_API_TOKEN_VAR" }}'
stackql shell --auth="${AUTH}"
""",
  'windows': """
$Auth = "{ 'pagerduty': { 'type': 'bearer', 'credentialsenvvar': 'YOUR_PAGERDUTY_API_TOKEN_VAR' }}"
stackql.exe shell --auth=$Auth
""",
},
# 
# Datadog
#
'datadog': {
  'custom': False,
  'variables': """
- <CopyableCode code="DD_API_KEY" /> - Datadog API key (see <a href="https://docs.datadoghq.com/account_management/api-app-keys/#api-keys">Datadog API Key Documentation</a>)
- <CopyableCode code="DD_APP_KEY" /> - Datadog Application Key (see <a href="https://docs.datadoghq.com/account_management/api-app-keys/#application-keys">Datadog Application Key Documentation</a>)
  """,
  'linux': """
AUTH='{ "datadog": { "type": "custom", "location": "header", "name": "DD-API-KEY", "credentialsenvvar": "YOUR_DD_API_KEY_VAR", "successor": { "type": "custom", "location": "header", "name": "DD-APPLICATION-KEY", "credentialsenvvar": "YOUR_DD_APP_KEY_VAR" }}}'
stackql shell --auth="${AUTH}"
""",
  'windows': """
$Auth = "{ 'datadog': { 'type': 'custom', 'location': 'header', 'name': 'DD-API-KEY', 'credentialsenvvar': 'YOUR_DD_API_KEY_VAR', 'successor': { 'type': 'custom', 'location': 'header', 'name': 'DD-APPLICATION-KEY', 'credentialsenvvar': 'YOUR_DD_APP_KEY_VAR' }}}"
stackql.exe shell --auth=$Auth
""",
},
# 
# Homebrew
#
'homebrew': {
  'custom': True,
  'custom_markdown': """
> The `homebrew` provider for StackQL supports `SELECT` methods only and does not require any environment variables to be set for authentication.  
"""
},
# 
# Google
# 
  'google': {
    'custom': True,
    'custom_markdown': google_auth_markdown,
  },
# 
# Google Admin
# 
  'googleadmin': {
    'custom': True,
    'custom_markdown': googleadmin_auth_markdown,
  },  
# 
# Firebase
# 
  'firebase': {
    'custom': True,
    'custom_markdown': google_auth_markdown,
  },
# 
# Azure
# 
  'azure': {
    'custom': True,
    'custom_markdown': """
StackQL uses Azure application credentials obtained using the <CopyableCode code="az login" /> command from the Azure SDK.  For more information, see <a href="https://learn.microsoft.com/en-us/cli/azure/authenticate-azure-cli">here</a>.

### Authenticating using an Azure Service Principal

To authenticate using an Azure Service Principal, set the following environment variables: <CopyableCode code="AZURE_TENANT_ID" />, <CopyableCode code="AZURE_CLIENT_ID" /> and <CopyableCode code="AZURE_CLIENT_SECRET" />, see [__creating-an-azure-service-principal__](https://learn.microsoft.com/en-us/azure/developer/go/azure-sdk-authentication-service-principal?tabs=azure-cli#2-create-an-azure-service-principal).
""",
  },

# 
# Azure Extras
# 
  'azure_extras': {
    'custom': True,
    'custom_markdown': """
StackQL uses Azure application credentials obtained using the <CopyableCode code="az login" /> command from the Azure SDK.  For more information, see <a href="https://learn.microsoft.com/en-us/cli/azure/authenticate-azure-cli">here</a>.

### Authenticating using an Azure Service Principal

To authenticate using an Azure Service Principal, set the following environment variables: <CopyableCode code="AZURE_TENANT_ID" />, <CopyableCode code="AZURE_CLIENT_ID" /> and <CopyableCode code="AZURE_CLIENT_SECRET" />, see [__creating-an-azure-service-principal__](https://learn.microsoft.com/en-us/azure/developer/go/azure-sdk-authentication-service-principal?tabs=azure-cli#2-create-an-azure-service-principal).
""",
  },
# 
# Azure ISV
# 
  'azure_isv': {
    'custom': True,
    'custom_markdown': """
StackQL uses Azure application credentials obtained using the <CopyableCode code="az login" /> command from the Azure SDK.  For more information, see <a href="https://learn.microsoft.com/en-us/cli/azure/authenticate-azure-cli">here</a>.

### Authenticating using an Azure Service Principal

To authenticate using an Azure Service Principal, set the following environment variables: <CopyableCode code="AZURE_TENANT_ID" />, <CopyableCode code="AZURE_CLIENT_ID" /> and <CopyableCode code="AZURE_CLIENT_SECRET" />, see [__creating-an-azure-service-principal__](https://learn.microsoft.com/en-us/azure/developer/go/azure-sdk-authentication-service-principal?tabs=azure-cli#2-create-an-azure-service-principal).
""",
  },
# 
# Azure Stack
# 
  'azure_stack': {
    'custom': True,
    'custom_markdown': """
StackQL uses Azure application credentials obtained using the <CopyableCode code="az login" /> command from the Azure SDK.  For more information, see <a href="https://learn.microsoft.com/en-us/cli/azure/authenticate-azure-cli">here</a>.

### Authenticating using an Azure Service Principal

To authenticate using an Azure Service Principal, set the following environment variables: <CopyableCode code="AZURE_TENANT_ID" />, <CopyableCode code="AZURE_CLIENT_ID" /> and <CopyableCode code="AZURE_CLIENT_SECRET" />, see [__creating-an-azure-service-principal__](https://learn.microsoft.com/en-us/azure/developer/go/azure-sdk-authentication-service-principal?tabs=azure-cli#2-create-an-azure-service-principal).
""",
  },    
# 
# k8s
# 
  'k8s': {
    'custom': True,
    'custom_markdown': """
:::note

<b><CopyableCode code="cluster_addr" /></b> is a required parameter for all operations using the <code>k8s</code> provider, for example:  

```sql
SELECT name, namespace, uid, creationTimestamp 
FROM k8s.core_v1.service_account 
WHERE cluster_addr = '35.244.65.136' AND namespace = 'kube-system' 
ORDER BY name ASC;
```
:::

### Example using `kubectl proxy`
`kubectl proxy` is the default authentication method for the `k8s` provider, no other variables or configuration is necessary to query the `k8s` provider if you are using this method.  

:::note

The <CopyableCode code="protocol" /> parameter is required when accessing a Kubernetes cluster via `kubectl proxy`, see the example below:  

```sql
select name, namespace, uid, creationTimestamp 
from k8s.core_v1.pod 
where protocol = 'http' 
and cluster_addr = 'localhost:8080'  
order by name asc limit 3;
```
:::

### Example using direct cluster access
If you are using an access token to access the `k8s` API, follow the instructions below (use `exec` instead of `shell` for non interactive operations):

```bash
export K8S_TOKEN='eyJhbGciOiJ...'
AUTH='{ "k8s": { "type": "bearer", "credentialsenvvar": "K8S_TOKEN" } }'
stackql shell --auth="${AUTH}" --tls.CABundle k8s_cert_bundle.pem
```
:::note

You will need to generate a certificate bundle for your cluster (`k8s_cert_bundle.pem` in the preceeding example), you can use the following code to generate this (for MacOS or Linux):  

```bash
kubectl get secret -o jsonpath="{.items[?(@.type==\"kubernetes.io/service-account-token\")].data['ca\.crt']}" | base64 -i --decode > k8s_cert_bundle.pem
```

Alternatively, you could add the <CopyableCode code="--tls.allowInsecure=true" /> argument to the `stackql` command, it is not recommended however. 

:::
"""
  }
}

server_variables_blocks = {
    'aws': """
The following parameter is required for the `aws` provider:  

- `region` - AWS region (e.g. `us-east-1`)

This parameter must be supplied to the `WHERE` clause of each `SELECT` statement.
    """,
    'okta': """
The following parameter is required for the `okta` provider:  

- <CopyableCode code="subdomain" /> - The Okta tenant domain, for example <code>my-company</code> would be supplied if your Okta domain is <code>my-company.okta.com</code>

This parameter must be supplied to the `WHERE` clause of each `SELECT` statement.
    """,
    'sumologic': """
The following parameter is required for the `sumologic` provider if you are not using the `us2` region:  

- <CopyableCode code="region" /> - The SumoLogic regional endpoint (e.g. <code>au</code>, <code>ca</code>, <code>de</code>, <code>eu</code>, <code>fed</code>, <code>in</code>, <code>jp</code>)

This parameter would be supplied to the `WHERE` clause of each `SELECT` statement if you are not usign the `us2` region.
    """,
    'k8s': """
The following parameters may be required for the `k8s` provider:  

- <CopyableCode code="protocol" /> - <code>https</code> or <code>http</code> (default: <code>https</code>)
- <CopyableCode code="cluster_addr" /> - The hostname of the Kubernetes cluster (default: <code>localhost</code>)

This parameter would be supplied to the `WHERE` clause of each `SELECT` statement.
    """,
}