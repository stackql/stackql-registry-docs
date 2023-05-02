google_auth_markdown = """
The following authentication methods are supported:
- `service_account`
- `interactive` for running interactive queries from Cloud Shell or other machines where the user is authenticated using `gcloud auth login`

> for more information on creating service accounts and key files, see [Service accounts overview](https://cloud.google.com/iam/docs/service-account-overview).

### Service Account Environment Variable (default)

The following system environment variable is used by default:  

- `GOOGLE_CREDENTIALS` - contents of the `google` service account key json file

This variable is sourced at runtime (from the local machine or as a CI variable/secret).

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

### Interactive Authentication
When you are using Google Cloud Shell or on a machine where you have authenticated using `gcloud auth login`, you can then use the following authentication method:   

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
# 
# Digital Ocean
#  
  'digitalocean': {
    'custom': False,
    'variables': """
- `DIGITALOCEAN_ACCESS_TOKEN` - DigitalOcean API token (see [How to Create a Personal Access Token](https://docs.digitalocean.com/reference/api/create-personal-access-token/))
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
- `SUMOLOGIC_ACCESSID` - SumoLogic Access ID (see [Generating an Access Key](https://help.sumologic.com/docs/manage/security/access-keys/))
- `SUMOLOGIC_ACCESSKEY` - SumoLogic Access Key (see [Generating an Access Key](https://help.sumologic.com/docs/manage/security/access-keys/))
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
- `STACKQL_GITHUB_USERNAME` - GitHub username (login)
- `STACKQL_GITHUB_PASSWORD` - GitHub Personal Access Token (see [Creating a personal access token](https://docs.github.com/en/enterprise-server@3.4/authentication/keeping-your-account-and-data-secure/creating-a-personal-access-token))
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
- `NETLIFY_AUTH_TOKEN` - Netlify API token (see [How to Create a Netlify API Token](https://docs.netlify.com/api/get-started/#authentication))
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
- `OKTA_API_TOKEN` - Okta API Token (see [Creating an Okta API Token](https://developer.okta.com/docs/guides/create-an-api-token/))
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
# Google
# 
  'google': {
    'custom': True,
    'custom_markdown': google_auth_markdown,
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
StackQL uses Azure application credentials obtained using the `az login` command from the Azure SDK.  For more information, see [here](https://learn.microsoft.com/en-us/cli/azure/authenticate-azure-cli).
""",
  },
# 
# Azure Extras
# 
  'azure_extras': {
    'custom': True,
    'custom_markdown': """
StackQL uses Azure application credentials obtained using the `az login` command from the Azure SDK.  For more information, see [here](https://learn.microsoft.com/en-us/cli/azure/authenticate-azure-cli).
""",
  },
# 
# k8s
# 
  'k8s': {
    'custom': True,
    'custom_markdown': """
:::note

__`cluster_addr`__ is a required paramter for all operations using the `k8s` provider, for example:  

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

The __`protocol`__ parameter is required when accessing a Kubernetes cluster via `kubectl proxy`, see the example below:  

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

Alternatively, you could add the `--tls.allowInsecure=true` argument to the `stackql` command, it is not recommended however. 

:::
"""
  }
}