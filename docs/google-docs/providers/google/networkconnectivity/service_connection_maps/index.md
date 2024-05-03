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

import CopyableCode from '@site/src/components/CopyableCode/CopyableCode';




## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>service_connection_maps</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="google.networkconnectivity.service_connection_maps" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="name" /> | `string` | Immutable. The name of a ServiceConnectionMap. Format: projects/&#123;project&#125;/locations/&#123;location&#125;/serviceConnectionMaps/&#123;service_connection_map&#125; See: https://google.aip.dev/122#fields-representing-resource-names |
| <CopyableCode code="description" /> | `string` | A description of this resource. |
| <CopyableCode code="consumerPscConfigs" /> | `array` | The PSC configurations on consumer side. |
| <CopyableCode code="consumerPscConnections" /> | `array` | Output only. PSC connection details on consumer side. |
| <CopyableCode code="createTime" /> | `string` | Output only. Time when the ServiceConnectionMap was created. |
| <CopyableCode code="etag" /> | `string` | Optional. The etag is computed by the server, and may be sent on update and delete requests to ensure the client has an up-to-date value before proceeding. |
| <CopyableCode code="infrastructure" /> | `string` | Output only. The infrastructure used for connections between consumers/producers. |
| <CopyableCode code="labels" /> | `object` | User-defined labels. |
| <CopyableCode code="producerPscConfigs" /> | `array` | The PSC configurations on producer side. |
| <CopyableCode code="serviceClass" /> | `string` | The service class identifier this ServiceConnectionMap is for. The user of ServiceConnectionMap create API needs to have networkconnecitivty.serviceclasses.use iam permission for the service class. |
| <CopyableCode code="serviceClassUri" /> | `string` | Output only. The service class uri this ServiceConnectionMap is for. |
| <CopyableCode code="token" /> | `string` | The token provided by the consumer. This token authenticates that the consumer can create a connecton within the specified project and network. |
| <CopyableCode code="updateTime" /> | `string` | Output only. Time when the ServiceConnectionMap was updated. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="locationsId, projectsId, serviceConnectionMapsId" /> | Gets details of a single ServiceConnectionMap. |
| <CopyableCode code="list" /> | `SELECT` | <CopyableCode code="locationsId, projectsId" /> | Lists ServiceConnectionMaps in a given project and location. |
| <CopyableCode code="create" /> | `INSERT` | <CopyableCode code="locationsId, projectsId" /> | Creates a new ServiceConnectionMap in a given project and location. |
| <CopyableCode code="delete" /> | `DELETE` | <CopyableCode code="locationsId, projectsId, serviceConnectionMapsId" /> | Deletes a single ServiceConnectionMap. |
| <CopyableCode code="_list" /> | `EXEC` | <CopyableCode code="locationsId, projectsId" /> | Lists ServiceConnectionMaps in a given project and location. |
| <CopyableCode code="patch" /> | `EXEC` | <CopyableCode code="locationsId, projectsId, serviceConnectionMapsId" /> | Updates the parameters of a single ServiceConnectionMap. |
