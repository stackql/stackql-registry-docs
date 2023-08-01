---
title: services
hide_title: false
hide_table_of_contents: false
keywords:
  - services
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
<tr><td><b>Name</b></td><td><code>services</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>google.servicedirectory.services</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `services` | `array` | The list of services. |
| `nextPageToken` | `string` | Token to retrieve the next page of results, or empty if there are no more results in the list. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `get` | `SELECT` | `locationsId, namespacesId, projectsId, servicesId` | Gets a service. |
| `list` | `SELECT` | `locationsId, namespacesId, projectsId` | Lists all services belonging to a namespace. |
| `create` | `INSERT` | `locationsId, namespacesId, projectsId` | Creates a service, and returns the new service. |
| `delete` | `DELETE` | `locationsId, namespacesId, projectsId, servicesId` | Deletes a service. This also deletes all endpoints associated with the service. |
| `patch` | `EXEC` | `locationsId, namespacesId, projectsId, servicesId` | Updates a service. |
| `resolve` | `EXEC` | `locationsId, namespacesId, projectsId, servicesId` | Returns a service and its associated endpoints. Resolving a service is not considered an active developer method. |
