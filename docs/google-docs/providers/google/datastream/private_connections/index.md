---
title: private_connections
hide_title: false
hide_table_of_contents: false
keywords:
  - private_connections
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

Creates, updates, deletes, gets or lists a <code>private_connections</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>private_connections</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="google.datastream.private_connections" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="name" /> | `string` | Output only. The resource's name. |
| <CopyableCode code="createTime" /> | `string` | Output only. The create time of the resource. |
| <CopyableCode code="displayName" /> | `string` | Required. Display name. |
| <CopyableCode code="error" /> | `object` | Represent a user-facing Error. |
| <CopyableCode code="labels" /> | `object` | Labels. |
| <CopyableCode code="state" /> | `string` | Output only. The state of the Private Connection. |
| <CopyableCode code="updateTime" /> | `string` | Output only. The update time of the resource. |
| <CopyableCode code="vpcPeeringConfig" /> | `object` | The VPC Peering configuration is used to create VPC peering between Datastream and the consumer's VPC. |

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="locationsId, privateConnectionsId, projectsId" /> | Use this method to get details about a private connectivity configuration. |
| <CopyableCode code="list" /> | `SELECT` | <CopyableCode code="locationsId, projectsId" /> | Use this method to list private connectivity configurations in a project and location. |
| <CopyableCode code="create" /> | `INSERT` | <CopyableCode code="locationsId, projectsId" /> | Use this method to create a private connectivity configuration. |
| <CopyableCode code="delete" /> | `DELETE` | <CopyableCode code="locationsId, privateConnectionsId, projectsId" /> | Use this method to delete a private connectivity configuration. |

## `SELECT` examples

Use this method to list private connectivity configurations in a project and location.

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
FROM google.datastream.private_connections
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
INSERT INTO google.datastream.private_connections (
locationsId,
projectsId,
labels,
displayName,
vpcPeeringConfig
)
SELECT 
'{{ locationsId }}',
'{{ projectsId }}',
'{{ labels }}',
'{{ displayName }}',
'{{ vpcPeeringConfig }}'
;
```
</TabItem>
<TabItem value="manifest">

```yaml
- name: your_resource_model_name
  props:
    - name: name
      value: string
    - name: createTime
      value: string
    - name: updateTime
      value: string
    - name: labels
      value: object
    - name: displayName
      value: string
    - name: state
      value: string
    - name: error
      value:
        - name: reason
          value: string
        - name: errorUuid
          value: string
        - name: message
          value: string
        - name: errorTime
          value: string
        - name: details
          value: object
    - name: vpcPeeringConfig
      value:
        - name: vpc
          value: string
        - name: subnet
          value: string

```
</TabItem>
</Tabs>

## `DELETE` example

Deletes the specified <code>private_connections</code> resource.

```sql
/*+ delete */
DELETE FROM google.datastream.private_connections
WHERE locationsId = '{{ locationsId }}'
AND privateConnectionsId = '{{ privateConnectionsId }}'
AND projectsId = '{{ projectsId }}';
```
