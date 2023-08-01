---
title: secrets
hide_title: false
hide_table_of_contents: false
keywords:
  - secrets
  - secretmanager
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
<tr><td><b>Name</b></td><td><code>secrets</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>google.secretmanager.secrets</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `totalSize` | `integer` | The total number of Secrets but 0 when the ListSecretsRequest.filter field is set. |
| `nextPageToken` | `string` | A token to retrieve the next page of results. Pass this value in ListSecretsRequest.page_token to retrieve the next page. |
| `secrets` | `array` | The list of Secrets sorted in reverse by create_time (newest first). |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `get` | `SELECT` | `projectsId, secretsId` | Gets metadata for a given Secret. |
| `list` | `SELECT` | `projectsId` | Lists Secrets. |
| `create` | `INSERT` | `projectsId` | Creates a new Secret containing no SecretVersions. |
| `delete` | `DELETE` | `projectsId, secretsId` | Deletes a Secret. |
| `patch` | `EXEC` | `projectsId, secretsId` | Updates metadata of an existing Secret. |
