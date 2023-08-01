---
title: endpoint_policies
hide_title: false
hide_table_of_contents: false
keywords:
  - endpoint_policies
  - networkservices
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
<tr><td><b>Name</b></td><td><code>endpoint_policies</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>google.networkservices.endpoint_policies</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `endpointPolicies` | `array` | List of EndpointPolicy resources. |
| `nextPageToken` | `string` | If there might be more results than those appearing in this response, then `next_page_token` is included. To get the next set of results, call this method again using the value of `next_page_token` as `page_token`. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `get` | `SELECT` | `endpointPoliciesId, locationsId, projectsId` | Gets details of a single EndpointPolicy. |
| `list` | `SELECT` | `locationsId, projectsId` | Lists EndpointPolicies in a given project and location. |
| `create` | `INSERT` | `locationsId, projectsId` | Creates a new EndpointPolicy in a given project and location. |
| `delete` | `DELETE` | `endpointPoliciesId, locationsId, projectsId` | Deletes a single EndpointPolicy. |
| `patch` | `EXEC` | `endpointPoliciesId, locationsId, projectsId` | Updates the parameters of a single EndpointPolicy. |
