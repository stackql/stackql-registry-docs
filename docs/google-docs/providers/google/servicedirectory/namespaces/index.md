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
| `name` | `string` | Immutable. The resource name for the namespace in the format `projects/*/locations/*/namespaces/*`. |
| `uid` | `string` | Output only. The globally unique identifier of the namespace in the UUID4 format. |
| `labels` | `object` | Optional. Resource labels associated with this namespace. No more than 64 user labels can be associated with a given resource. Label keys and values can be no longer than 63 characters. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `get` | `SELECT` | `locationsId, namespacesId, projectsId` | Gets a namespace. |
| `list` | `SELECT` | `locationsId, projectsId` | Lists all namespaces. |
| `create` | `INSERT` | `locationsId, projectsId` | Creates a namespace, and returns the new namespace. |
| `delete` | `DELETE` | `locationsId, namespacesId, projectsId` | Deletes a namespace. This also deletes all services and endpoints in the namespace. |
| `_list` | `EXEC` | `locationsId, projectsId` | Lists all namespaces. |
| `patch` | `EXEC` | `locationsId, namespacesId, projectsId` | Updates a namespace. |
