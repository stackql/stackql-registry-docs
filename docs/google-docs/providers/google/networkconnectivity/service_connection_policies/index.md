---
title: service_connection_policies
hide_title: false
hide_table_of_contents: false
keywords:
  - service_connection_policies
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
<tr><td><b>Name</b></td><td><code>service_connection_policies</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>google.networkconnectivity.service_connection_policies</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `unreachable` | `array` | Locations that could not be reached. |
| `nextPageToken` | `string` | The next pagination token in the List response. It should be used as page_token for the following request. An empty value means no more result. |
| `serviceConnectionPolicies` | `array` | ServiceConnectionPolicies to be returned. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `get` | `SELECT` | `locationsId, projectsId, serviceConnectionPoliciesId` | Gets details of a single ServiceConnectionPolicy. |
| `list` | `SELECT` | `locationsId, projectsId` | Lists ServiceConnectionPolicies in a given project and location. |
| `create` | `INSERT` | `locationsId, projectsId` | Creates a new ServiceConnectionPolicy in a given project and location. |
| `delete` | `DELETE` | `locationsId, projectsId, serviceConnectionPoliciesId` | Deletes a single ServiceConnectionPolicy. |
| `patch` | `EXEC` | `locationsId, projectsId, serviceConnectionPoliciesId` | Updates the parameters of a single ServiceConnectionPolicy. |
