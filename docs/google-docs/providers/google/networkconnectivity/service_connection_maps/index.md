---
title: service_connection_maps
hide_title: false
hide_table_of_contents: false
keywords:
  - service_connection_maps
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
<tr><td><b>Name</b></td><td><code>service_connection_maps</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>google.networkconnectivity.service_connection_maps</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `name` | `string` | Immutable. The name of a ServiceConnectionMap. Format: projects/&#123;project&#125;/locations/&#123;location&#125;/serviceConnectionMaps/&#123;service_connection_map&#125; See: https://google.aip.dev/122#fields-representing-resource-names |
| `description` | `string` | A description of this resource. |
| `createTime` | `string` | Output only. Time when the ServiceConnectionMap was created. |
| `updateTime` | `string` | Output only. Time when the ServiceConnectionMap was updated. |
| `infrastructure` | `string` | Output only. The infrastructure used for connections between consumers/producers. |
| `labels` | `object` | User-defined labels. |
| `etag` | `string` | Optional. The etag is computed by the server, and may be sent on update and delete requests to ensure the client has an up-to-date value before proceeding. |
| `producerPscConfigs` | `array` | The PSC configurations on producer side. |
| `consumerPscConnections` | `array` | Output only. PSC connection details on consumer side. |
| `serviceClassUri` | `string` | Output only. The service class uri this ServiceConnectionMap is for. |
| `token` | `string` | The token provided by the consumer. This token authenticates that the consumer can create a connecton within the specified project and network. |
| `consumerPscConfigs` | `array` | The PSC configurations on consumer side. |
| `serviceClass` | `string` | The service class identifier this ServiceConnectionMap is for. The user of ServiceConnectionMap create API needs to have networkconnecitivty.serviceclasses.use iam permission for the service class. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `get` | `SELECT` | `locationsId, projectsId, serviceConnectionMapsId` | Gets details of a single ServiceConnectionMap. |
| `list` | `SELECT` | `locationsId, projectsId` | Lists ServiceConnectionMaps in a given project and location. |
| `create` | `INSERT` | `locationsId, projectsId` | Creates a new ServiceConnectionMap in a given project and location. |
| `delete` | `DELETE` | `locationsId, projectsId, serviceConnectionMapsId` | Deletes a single ServiceConnectionMap. |
| `_list` | `EXEC` | `locationsId, projectsId` | Lists ServiceConnectionMaps in a given project and location. |
| `patch` | `EXEC` | `locationsId, projectsId, serviceConnectionMapsId` | Updates the parameters of a single ServiceConnectionMap. |
