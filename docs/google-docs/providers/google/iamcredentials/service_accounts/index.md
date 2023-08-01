---
title: service_accounts
hide_title: false
hide_table_of_contents: false
keywords:
  - service_accounts
  - iamcredentials
  - google    
  - stackql
  - infrastructure-as-code
  - configuration-as-data
  - cloud inventory
description: Query, deploy and manage Google Cloud Platform (GCP) infrastructure and resources using SQL
custom_edit_url: null
image: /img/providers/google/stackql-google-provider-featured-image.png
---
  
    

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>service_accounts</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>google.iamcredentials.service_accounts</code></td></tr>
</tbody></table>

## Fields
`SELECT` not supported for this resource, use `SHOW METHODS` to view available operations for the resource and then invoke a supported method using the `EXEC` command  
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `generate_access_token` | `EXEC` | `projectsId, serviceAccountsId` | Generates an OAuth 2.0 access token for a service account. |
| `generate_id_token` | `EXEC` | `projectsId, serviceAccountsId` | Generates an OpenID Connect ID token for a service account. |
| `sign_blob` | `EXEC` | `projectsId, serviceAccountsId` | Signs a blob using a service account's system-managed private key. |
| `sign_jwt` | `EXEC` | `projectsId, serviceAccountsId` | Signs a JWT using a service account's system-managed private key. |
