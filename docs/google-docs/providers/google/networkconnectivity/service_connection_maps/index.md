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
import Tabs from '@theme/Tabs';
import TabItem from '@theme/TabItem';

Creates, updates, deletes, gets or lists a <code>service_connection_maps</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>service_connection_maps</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="google.networkconnectivity.service_connection_maps" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="name" /> | `string` | Immutable. The name of a ServiceConnectionMap. Format: projects/{project}/locations/{location}/serviceConnectionMaps/{service_connection_map} See: https://google.aip.dev/122#fields-representing-resource-names |
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
| <CopyableCode code="patch" /> | `UPDATE` | <CopyableCode code="locationsId, projectsId, serviceConnectionMapsId" /> | Updates the parameters of a single ServiceConnectionMap. |

## `SELECT` examples

Lists ServiceConnectionMaps in a given project and location.

```sql
SELECT
name,
description,
consumerPscConfigs,
consumerPscConnections,
createTime,
etag,
infrastructure,
labels,
producerPscConfigs,
serviceClass,
serviceClassUri,
token,
updateTime
FROM google.networkconnectivity.service_connection_maps
WHERE locationsId = '{{ locationsId }}'
AND projectsId = '{{ projectsId }}'; 
```

## `INSERT` example

Use the following StackQL query and manifest file to create a new <code>service_connection_maps</code> resource.

<Tabs
    defaultValue="all"
    values={[
        { label: 'All Properties', value: 'all', },
        { label: 'Manifest', value: 'manifest', },
    ]
}>
<TabItem value="all">

```sql
/*+ create */
INSERT INTO google.networkconnectivity.service_connection_maps (
locationsId,
projectsId,
name,
createTime,
updateTime,
labels,
description,
serviceClass,
serviceClassUri,
infrastructure,
producerPscConfigs,
consumerPscConfigs,
consumerPscConnections,
token,
etag
)
SELECT 
'{{ locationsId }}',
'{{ projectsId }}',
'{{ name }}',
'{{ createTime }}',
'{{ updateTime }}',
'{{ labels }}',
'{{ description }}',
'{{ serviceClass }}',
'{{ serviceClassUri }}',
'{{ infrastructure }}',
'{{ producerPscConfigs }}',
'{{ consumerPscConfigs }}',
'{{ consumerPscConnections }}',
'{{ token }}',
'{{ etag }}'
;
```
</TabItem>
<TabItem value="manifest">

```yaml
- name: your_resource_model_name
  props:
    - name: name
      value: '{{ name }}'
    - name: createTime
      value: '{{ createTime }}'
    - name: updateTime
      value: '{{ updateTime }}'
    - name: labels
      value: '{{ labels }}'
    - name: description
      value: '{{ description }}'
    - name: serviceClass
      value: '{{ serviceClass }}'
    - name: serviceClassUri
      value: '{{ serviceClassUri }}'
    - name: infrastructure
      value: '{{ infrastructure }}'
    - name: producerPscConfigs
      value: '{{ producerPscConfigs }}'
    - name: consumerPscConfigs
      value: '{{ consumerPscConfigs }}'
    - name: consumerPscConnections
      value: '{{ consumerPscConnections }}'
    - name: token
      value: '{{ token }}'
    - name: etag
      value: '{{ etag }}'

```
</TabItem>
</Tabs>

## `UPDATE` example

Updates a <code>service_connection_maps</code> resource.

```sql
/*+ update */
UPDATE google.networkconnectivity.service_connection_maps
SET 
name = '{{ name }}',
createTime = '{{ createTime }}',
updateTime = '{{ updateTime }}',
labels = '{{ labels }}',
description = '{{ description }}',
serviceClass = '{{ serviceClass }}',
serviceClassUri = '{{ serviceClassUri }}',
infrastructure = '{{ infrastructure }}',
producerPscConfigs = '{{ producerPscConfigs }}',
consumerPscConfigs = '{{ consumerPscConfigs }}',
consumerPscConnections = '{{ consumerPscConnections }}',
token = '{{ token }}',
etag = '{{ etag }}'
WHERE 
locationsId = '{{ locationsId }}'
AND projectsId = '{{ projectsId }}'
AND serviceConnectionMapsId = '{{ serviceConnectionMapsId }}';
```

## `DELETE` example

Deletes the specified <code>service_connection_maps</code> resource.

```sql
/*+ delete */
DELETE FROM google.networkconnectivity.service_connection_maps
WHERE locationsId = '{{ locationsId }}'
AND projectsId = '{{ projectsId }}'
AND serviceConnectionMapsId = '{{ serviceConnectionMapsId }}';
```
