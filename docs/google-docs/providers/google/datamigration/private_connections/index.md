
---
title: private_connections
hide_title: false
hide_table_of_contents: false
keywords:
  - private_connections
  - datamigration
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

Creates, updates, deletes or gets an <code>private_connection</code> resource or lists <code>private_connections</code> in a region

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>private_connections</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="google.datamigration.private_connections" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="name" /> | `string` | The name of the resource. |
| <CopyableCode code="createTime" /> | `string` | Output only. The create time of the resource. |
| <CopyableCode code="displayName" /> | `string` | The private connection display name. |
| <CopyableCode code="error" /> | `object` | The `Status` type defines a logical error model that is suitable for different programming environments, including REST APIs and RPC APIs. It is used by [gRPC](https://github.com/grpc). Each `Status` message contains three pieces of data: error code, error message, and error details. You can find out more about this error model and how to work with it in the [API Design Guide](https://cloud.google.com/apis/design/errors). |
| <CopyableCode code="labels" /> | `object` | The resource labels for private connections to use to annotate any related underlying resources such as Compute Engine VMs. An object containing a list of "key": "value" pairs. Example: `{ "name": "wrench", "mass": "1.3kg", "count": "3" }`. |
| <CopyableCode code="state" /> | `string` | Output only. The state of the private connection. |
| <CopyableCode code="updateTime" /> | `string` | Output only. The last update time of the resource. |
| <CopyableCode code="vpcPeeringConfig" /> | `object` | The VPC peering configuration is used to create VPC peering with the consumer's VPC. |

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="locationsId, privateConnectionsId, projectsId" /> | Gets details of a single private connection. |
| <CopyableCode code="list" /> | `SELECT` | <CopyableCode code="locationsId, projectsId" /> | Retrieves a list of private connections in a given project and location. |
| <CopyableCode code="create" /> | `INSERT` | <CopyableCode code="locationsId, projectsId" /> | Creates a new private connection in a given project and location. |
| <CopyableCode code="delete" /> | `DELETE` | <CopyableCode code="locationsId, privateConnectionsId, projectsId" /> | Deletes a single Database Migration Service private connection. |

## `SELECT` examples

Retrieves a list of private connections in a given project and location.

```sql
SELECT
name,
createTime,
displayName,
error,
labels,
state,
updateTime,
vpcPeeringConfig
FROM google.datamigration.private_connections
WHERE locationsId = '{{ locationsId }}'
AND projectsId = '{{ projectsId }}'; 
```

## `INSERT` example

Use the following StackQL query and manifest file to create a new <code>private_connections</code> resource.

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
INSERT INTO google.datamigration.private_connections (
locationsId,
projectsId,
name,
createTime,
updateTime,
labels,
displayName,
state,
error,
vpcPeeringConfig
)
SELECT 
'{{ locationsId }}',
'{{ projectsId }}',
'{{ name }}',
'{{ createTime }}',
'{{ updateTime }}',
'{{ labels }}',
'{{ displayName }}',
'{{ state }}',
'{{ error }}',
'{{ vpcPeeringConfig }}'
;
```
</TabItem>
<TabItem value="manifest">

```yaml
resources:
  - name: instance
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
      - name: state
        value: '{{ state }}'
      - name: error
        value: '{{ error }}'
      - name: vpcPeeringConfig
        value: '{{ vpcPeeringConfig }}'

```
</TabItem>
</Tabs>

## `DELETE` example

Deletes the specified private_connection resource.

```sql
DELETE FROM google.datamigration.private_connections
WHERE locationsId = '{{ locationsId }}'
AND privateConnectionsId = '{{ privateConnectionsId }}'
AND projectsId = '{{ projectsId }}';
```
