---
title: debug_tokens
hide_title: false
hide_table_of_contents: false
keywords:
  - debug_tokens
  - firebaseappcheck
  - firebase    
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
<tr><td><b>Name</b></td><td><code>debug_tokens</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>firebase.firebaseappcheck.debug_tokens</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `name` | `string` | Required. The relative resource name of the debug token, in the format: ``` projects/{project_number}/apps/{app_id}/debugTokens/{debug_token_id} ``` |
| `token` | `string` | Required. Input only. Immutable. The secret token itself. Must be provided during creation, and must be a UUID4, case insensitive. This field is immutable once set, and cannot be provided during an UpdateDebugToken request. You can, however, delete this debug token using DeleteDebugToken to revoke it. For security reasons, this field will never be populated in any response. |
| `displayName` | `string` | Required. A human readable display name used to identify this debug token. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `projects_apps_debugTokens_get` | `SELECT` | `appsId, debugTokensId, projectsId` | Gets the specified DebugToken. For security reasons, the `token` field is never populated in the response. |
| `projects_apps_debugTokens_list` | `SELECT` | `appsId, projectsId` | Lists all DebugTokens for the specified app. For security reasons, the `token` field is never populated in the response. |
| `projects_apps_debugTokens_create` | `INSERT` | `appsId, projectsId` | Creates a new DebugToken for the specified app. For security reasons, after the creation operation completes, the `token` field cannot be updated or retrieved, but you can revoke the debug token using DeleteDebugToken. Each app can have a maximum of 20 debug tokens. |
| `projects_apps_debugTokens_delete` | `DELETE` | `appsId, debugTokensId, projectsId` | Deletes the specified DebugToken. A deleted debug token cannot be used to exchange for an App Check token. Use this method when you suspect the secret `token` has been compromised or when you no longer need the debug token. |
| `projects_apps_debugTokens_patch` | `EXEC` | `appsId, debugTokensId, projectsId` | Updates the specified DebugToken. For security reasons, the `token` field cannot be updated, nor will it be populated in the response, but you can revoke the debug token using DeleteDebugToken. |
