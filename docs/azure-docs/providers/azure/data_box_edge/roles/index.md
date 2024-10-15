---
title: roles
hide_title: false
hide_table_of_contents: false
keywords:
  - roles
  - data_box_edge
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

Creates, updates, deletes, gets or lists a <code>roles</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>roles</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.data_box_edge.roles" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="id" /> | `string` | The path ID that uniquely identifies the object. |
| <CopyableCode code="name" /> | `string` | The object name. |
| <CopyableCode code="kind" /> | `string` | Role type. |
| <CopyableCode code="systemData" /> | `object` | Metadata pertaining to creation and last modification of the resource. |
| <CopyableCode code="type" /> | `string` | The hierarchical type of the object. |

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="deviceName, name, resourceGroupName, subscriptionId" /> | Gets a specific role by name. |
| <CopyableCode code="list_by_data_box_edge_device" /> | `SELECT` | <CopyableCode code="deviceName, resourceGroupName, subscriptionId" /> | Lists all the roles configured in a Data Box Edge/Data Box Gateway device. |
| <CopyableCode code="create_or_update" /> | `INSERT` | <CopyableCode code="deviceName, name, resourceGroupName, subscriptionId, data__kind" /> | Create or update a role. |
| <CopyableCode code="delete" /> | `DELETE` | <CopyableCode code="deviceName, name, resourceGroupName, subscriptionId" /> | Deletes the role on the device. |

## `SELECT` examples

Lists all the roles configured in a Data Box Edge/Data Box Gateway device.


```sql
SELECT
id,
name,
kind,
systemData,
type
FROM azure.data_box_edge.roles
WHERE deviceName = '{{ deviceName }}'
AND resourceGroupName = '{{ resourceGroupName }}'
AND subscriptionId = '{{ subscriptionId }}';
```
## `INSERT` example

Use the following StackQL query and manifest file to create a new <code>roles</code> resource.

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
INSERT INTO azure.data_box_edge.roles (
deviceName,
name,
resourceGroupName,
subscriptionId,
data__kind,
kind
)
SELECT 
'{{ deviceName }}',
'{{ name }}',
'{{ resourceGroupName }}',
'{{ subscriptionId }}',
'{{ data__kind }}',
'{{ kind }}'
;
```
</TabItem>
<TabItem value="manifest">

```yaml
- name: your_resource_model_name
  props:
    - name: id
      value: string
    - name: name
      value: string
    - name: type
      value: string
    - name: kind
      value: string
    - name: systemData
      value:
        - name: createdBy
          value: string
        - name: createdByType
          value: string
        - name: createdAt
          value: string
        - name: lastModifiedBy
          value: string
        - name: lastModifiedByType
          value: string
        - name: lastModifiedAt
          value: string

```
</TabItem>
</Tabs>

## `DELETE` example

Deletes the specified <code>roles</code> resource.

```sql
/*+ delete */
DELETE FROM azure.data_box_edge.roles
WHERE deviceName = '{{ deviceName }}'
AND name = '{{ name }}'
AND resourceGroupName = '{{ resourceGroupName }}'
AND subscriptionId = '{{ subscriptionId }}';
```
