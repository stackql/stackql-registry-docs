---
title: keys
hide_title: false
hide_table_of_contents: false
keywords:
  - keys
  - iam
  - google    
  - stackql
  - infrastructure-as-code
  - configuration-as-data
  - cloud inventory
description: Query, deploy and manage Google Cloud Platform (GCP) infrastructure and resources using SQL
custom_edit_url: null
image: https://storage.googleapis.com/stackql-web-assets/blog/stackql-blog-post-featured-image.png
---
  
    

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>keys</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>google.iam.keys</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `name` | `string` | The resource name of the service account key in the following format `projects/{PROJECT_ID}/serviceAccounts/{ACCOUNT}/keys/{key}`. |
| `keyType` | `string` | The key type. |
| `validAfterTime` | `string` | The key can be used after this timestamp. |
| `privateKeyData` | `string` | The private key data. Only provided in `CreateServiceAccountKey` responses. Make sure to keep the private key data secure because it allows for the assertion of the service account identity. When base64 decoded, the private key data can be used to authenticate with Google API client libraries and with gcloud auth activate-service-account. |
| `keyAlgorithm` | `string` | Specifies the algorithm (and possibly key size) for the key. |
| `keyOrigin` | `string` | The key origin. |
| `disabled` | `boolean` | The key status. |
| `validBeforeTime` | `string` | The key can be used before this timestamp. For system-managed key pairs, this timestamp is the end time for the private key signing operation. The public key could still be used for verification for a few hours after this time. |
| `privateKeyType` | `string` | The output format for the private key. Only provided in `CreateServiceAccountKey` responses, not in `GetServiceAccountKey` or `ListServiceAccountKey` responses. Google never exposes system-managed private keys, and never retains user-managed private keys. |
| `publicKeyData` | `string` | The public key data. Only provided in `GetServiceAccountKey` responses. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `projects_serviceAccounts_keys_get` | `SELECT` | `keysId, projectsId, serviceAccountsId` | Gets a ServiceAccountKey. |
| `projects_serviceAccounts_keys_list` | `SELECT` | `projectsId, serviceAccountsId` | Lists every ServiceAccountKey for a service account. |
| `projects_serviceAccounts_keys_create` | `INSERT` | `projectsId, serviceAccountsId` | Creates a ServiceAccountKey. |
| `projects_serviceAccounts_keys_delete` | `DELETE` | `keysId, projectsId, serviceAccountsId` | Deletes a ServiceAccountKey. Deleting a service account key does not revoke short-lived credentials that have been issued based on the service account key. |
| `projects_serviceAccounts_keys_disable` | `EXEC` | `keysId, projectsId, serviceAccountsId` | Disable a ServiceAccountKey. A disabled service account key can be re-enabled with EnableServiceAccountKey. |
| `projects_serviceAccounts_keys_enable` | `EXEC` | `keysId, projectsId, serviceAccountsId` | Enable a ServiceAccountKey. |
| `projects_serviceAccounts_keys_upload` | `EXEC` | `projectsId, serviceAccountsId` | Uploads the public key portion of a key pair that you manage, and associates the public key with a ServiceAccount. After you upload the public key, you can use the private key from the key pair as a service account key. |
