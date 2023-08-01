---
title: service_bindings
hide_title: false
hide_table_of_contents: false
keywords:
  - service_bindings
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
<tr><td><b>Name</b></td><td><code>service_bindings</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>google.networkservices.service_bindings</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `nextPageToken` | `string` | If there might be more results than those appearing in this response, then `next_page_token` is included. To get the next set of results, call this method again using the value of `next_page_token` as `page_token`. |
| `serviceBindings` | `array` | List of ServiceBinding resources. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `get` | `SELECT` | `locationsId, projectsId, serviceBindingsId` | Gets details of a single ServiceBinding. |
| `list` | `SELECT` | `locationsId, projectsId` | Lists ServiceBinding in a given project and location. |
| `create` | `INSERT` | `locationsId, projectsId` | Creates a new ServiceBinding in a given project and location. |
| `delete` | `DELETE` | `locationsId, projectsId, serviceBindingsId` | Deletes a single ServiceBinding. |
