---
title: client_tls_policies
hide_title: false
hide_table_of_contents: false
keywords:
  - client_tls_policies
  - networksecurity
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
<tr><td><b>Name</b></td><td><code>client_tls_policies</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>google.networksecurity.client_tls_policies</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `nextPageToken` | `string` | If there might be more results than those appearing in this response, then `next_page_token` is included. To get the next set of results, call this method again using the value of `next_page_token` as `page_token`. |
| `clientTlsPolicies` | `array` | List of ClientTlsPolicy resources. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `projects_locations_client_tls_policies_list` | `SELECT` | `locationsId, projectsId` | Lists ClientTlsPolicies in a given project and location. |
| `projects_locations_client_tls_policies_create` | `INSERT` | `locationsId, projectsId` | Creates a new ClientTlsPolicy in a given project and location. |
| `projects_locations_client_tls_policies_delete` | `DELETE` | `clientTlsPoliciesId, locationsId, projectsId` | Deletes a single ClientTlsPolicy. |
| `projects_locations_client_tls_policies_get` | `EXEC` | `clientTlsPoliciesId, locationsId, projectsId` | Gets details of a single ClientTlsPolicy. |
| `projects_locations_client_tls_policies_patch` | `EXEC` | `clientTlsPoliciesId, locationsId, projectsId` | Updates the parameters of a single ClientTlsPolicy. |
