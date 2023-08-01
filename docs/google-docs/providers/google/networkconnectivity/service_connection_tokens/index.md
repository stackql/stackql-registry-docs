---
title: service_connection_tokens
hide_title: false
hide_table_of_contents: false
keywords:
  - service_connection_tokens
  - networkconnectivity
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
<tr><td><b>Name</b></td><td><code>service_connection_tokens</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>google.networkconnectivity.service_connection_tokens</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `serviceConnectionTokens` | `array` | ServiceConnectionTokens to be returned. |
| `unreachable` | `array` | Locations that could not be reached. |
| `nextPageToken` | `string` | The next pagination token in the List response. It should be used as page_token for the following request. An empty value means no more result. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `get` | `SELECT` | `locationsId, projectsId, serviceConnectionTokensId` | Gets details of a single ServiceConnectionToken. |
| `list` | `SELECT` | `locationsId, projectsId` | Lists ServiceConnectionTokens in a given project and location. |
| `create` | `INSERT` | `locationsId, projectsId` | Creates a new ServiceConnectionToken in a given project and location. |
| `delete` | `DELETE` | `locationsId, projectsId, serviceConnectionTokensId` | Deletes a single ServiceConnectionToken. |
