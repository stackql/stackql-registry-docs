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
| `createTime` | `string` | Output only. The timestamp when the resource was created. |
| `labels` | `object` | Optional. Set of label tags associated with the ServiceBinding resource. |
| `service` | `string` | Required. The full Service Directory Service name of the format projects/*/locations/*/namespaces/*/services/* |
| `updateTime` | `string` | Output only. The timestamp when the resource was updated. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `projects_locations_serviceBindings_get` | `SELECT` | `locationsId, projectsId, serviceBindingsId` | Gets details of a single ServiceBinding. |
| `projects_locations_serviceBindings_list` | `SELECT` | `locationsId, projectsId` | Lists ServiceBinding in a given project and location. |
| `projects_locations_serviceBindings_create` | `INSERT` | `locationsId, projectsId` | Creates a new ServiceBinding in a given project and location. |
| `projects_locations_serviceBindings_delete` | `DELETE` | `locationsId, projectsId, serviceBindingsId` | Deletes a single ServiceBinding. |
