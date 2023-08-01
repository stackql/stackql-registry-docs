---
title: trust_configs
hide_title: false
hide_table_of_contents: false
keywords:
  - trust_configs
  - certificatemanager
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
<tr><td><b>Name</b></td><td><code>trust_configs</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>google.certificatemanager.trust_configs</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `trustConfigs` | `array` | A list of TrustConfigs for the parent resource. |
| `unreachable` | `array` | Locations that could not be reached. |
| `nextPageToken` | `string` | If there might be more results than those appearing in this response, then `next_page_token` is included. To get the next set of results, call this method again using the value of `next_page_token` as `page_token`. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `get` | `SELECT` | `locationsId, projectsId, trustConfigsId` | Gets details of a single TrustConfig. |
| `list` | `SELECT` | `locationsId, projectsId` | Lists TrustConfigs in a given project and location. |
| `create` | `INSERT` | `locationsId, projectsId` | Creates a new TrustConfig in a given project and location. |
| `delete` | `DELETE` | `locationsId, projectsId, trustConfigsId` | Deletes a single TrustConfig. |
| `patch` | `EXEC` | `locationsId, projectsId, trustConfigsId` | Updates a TrustConfig. |
