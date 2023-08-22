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
| `name` | `string` | Required. Name of the ServiceBinding resource. It matches pattern `projects/*/locations/global/serviceBindings/service_binding_name`. |
| `description` | `string` | Optional. A free-text description of the resource. Max length 1024 characters. |
| `labels` | `object` | Optional. Set of label tags associated with the ServiceBinding resource. |
| `service` | `string` | Required. The full Service Directory Service name of the format projects/*/locations/*/namespaces/*/services/* |
| `serviceId` | `string` | Output only. The unique identifier of the Service Directory Service against which the Service Binding resource is validated. This is populated when the Service Binding resource is used in another resource (like Backend Service). This is of the UUID4 format. |
| `updateTime` | `string` | Output only. The timestamp when the resource was updated. |
| `createTime` | `string` | Output only. The timestamp when the resource was created. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `get` | `SELECT` | `locationsId, projectsId, serviceBindingsId` | Gets details of a single ServiceBinding. |
| `list` | `SELECT` | `locationsId, projectsId` | Lists ServiceBinding in a given project and location. |
| `create` | `INSERT` | `locationsId, projectsId` | Creates a new ServiceBinding in a given project and location. |
| `delete` | `DELETE` | `locationsId, projectsId, serviceBindingsId` | Deletes a single ServiceBinding. |
| `_list` | `EXEC` | `locationsId, projectsId` | Lists ServiceBinding in a given project and location. |
