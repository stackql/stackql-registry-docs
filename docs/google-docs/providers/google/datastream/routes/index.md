---
title: routes
hide_title: false
hide_table_of_contents: false
keywords:
  - routes
  - datastream
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

Creates, updates, deletes, gets or lists a <code>routes</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>routes</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="google.datastream.routes" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="name" /> | `string` | Output only. The resource's name. |
| <CopyableCode code="createTime" /> | `string` | Output only. The create time of the resource. |
| <CopyableCode code="destinationAddress" /> | `string` | Required. Destination address for connection |
| <CopyableCode code="destinationPort" /> | `integer` | Destination port for connection |
| <CopyableCode code="displayName" /> | `string` | Required. Display name. |
| <CopyableCode code="labels" /> | `object` | Labels. |
| <CopyableCode code="updateTime" /> | `string` | Output only. The update time of the resource. |

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="locationsId, privateConnectionsId, projectsId, routesId" /> | Use this method to get details about a route. |
| <CopyableCode code="list" /> | `SELECT` | <CopyableCode code="locationsId, privateConnectionsId, projectsId" /> | Use this method to list routes created for a private connectivity configuration in a project and location. |
| <CopyableCode code="create" /> | `INSERT` | <CopyableCode code="locationsId, privateConnectionsId, projectsId" /> | Use this method to create a route for a private connectivity configuration in a project and location. |
| <CopyableCode code="delete" /> | `DELETE` | <CopyableCode code="locationsId, privateConnectionsId, projectsId, routesId" /> | Use this method to delete a route. |

## `SELECT` examples

Use this method to list routes created for a private connectivity configuration in a project and location.

```sql
SELECT
name,
createTime,
destinationAddress,
destinationPort,
displayName,
labels,
updateTime
FROM google.datastream.routes
WHERE locationsId = '{{ locationsId }}'
AND privateConnectionsId = '{{ privateConnectionsId }}'
AND projectsId = '{{ projectsId }}'; 
```

## `INSERT` example

Use the following StackQL query and manifest file to create a new <code>routes</code> resource.

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
INSERT INTO google.datastream.routes (
locationsId,
privateConnectionsId,
projectsId,
name,
createTime,
updateTime,
labels,
displayName,
destinationAddress,
destinationPort
)
SELECT 
'{{ locationsId }}',
'{{ privateConnectionsId }}',
'{{ projectsId }}',
'{{ name }}',
'{{ createTime }}',
'{{ updateTime }}',
'{{ labels }}',
'{{ displayName }}',
'{{ destinationAddress }}',
'{{ destinationPort }}'
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
    - name: displayName
      value: '{{ displayName }}'
    - name: destinationAddress
      value: '{{ destinationAddress }}'
    - name: destinationPort
      value: '{{ destinationPort }}'

```
</TabItem>
</Tabs>

## `DELETE` example

Deletes the specified <code>routes</code> resource.

```sql
/*+ delete */
DELETE FROM google.datastream.routes
WHERE locationsId = '{{ locationsId }}'
AND privateConnectionsId = '{{ privateConnectionsId }}'
AND projectsId = '{{ projectsId }}'
AND routesId = '{{ routesId }}';
```
