---
title: endpoints
hide_title: false
hide_table_of_contents: false
keywords:
  - endpoints
  - servicedirectory
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
<tr><td><b>Name</b></td><td><code>endpoints</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>google.servicedirectory.endpoints</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `nextPageToken` | `string` | Token to retrieve the next page of results, or empty if there are no more results in the list. |
| `endpoints` | `array` | The list of endpoints. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `get` | `SELECT` | `endpointsId, locationsId, namespacesId, projectsId, servicesId` | Gets an endpoint. |
| `list` | `SELECT` | `locationsId, namespacesId, projectsId, servicesId` | Lists all endpoints. |
| `create` | `INSERT` | `locationsId, namespacesId, projectsId, servicesId` | Creates an endpoint, and returns the new endpoint. |
| `delete` | `DELETE` | `endpointsId, locationsId, namespacesId, projectsId, servicesId` | Deletes an endpoint. |
| `patch` | `EXEC` | `endpointsId, locationsId, namespacesId, projectsId, servicesId` | Updates an endpoint. |
