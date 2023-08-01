---
title: namespaces
hide_title: false
hide_table_of_contents: false
keywords:
  - namespaces
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
<tr><td><b>Name</b></td><td><code>namespaces</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>google.servicedirectory.namespaces</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `namespaces` | `array` | The list of namespaces. |
| `nextPageToken` | `string` | Token to retrieve the next page of results, or empty if there are no more results in the list. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `get` | `SELECT` | `locationsId, namespacesId, projectsId` | Gets a namespace. |
| `list` | `SELECT` | `locationsId, projectsId` | Lists all namespaces. |
| `create` | `INSERT` | `locationsId, projectsId` | Creates a namespace, and returns the new namespace. |
| `delete` | `DELETE` | `locationsId, namespacesId, projectsId` | Deletes a namespace. This also deletes all services and endpoints in the namespace. |
| `patch` | `EXEC` | `locationsId, namespacesId, projectsId` | Updates a namespace. |
