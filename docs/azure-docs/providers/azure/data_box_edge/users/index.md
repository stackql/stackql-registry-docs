---
title: users
hide_title: false
hide_table_of_contents: false
keywords:
  - users
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

Creates, updates, deletes, gets or lists a <code>users</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>users</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.data_box_edge.users" /></td></tr>
</tbody></table>

## Fields
<Tabs
    defaultValue="view"
    values={[
        { label: 'vw_users', value: 'view', },
        { label: 'users', value: 'resource', },
    ]
}>
<TabItem value="view">

| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="id" /> | `text` | The path ID that uniquely identifies the object. |
| <CopyableCode code="name" /> | `text` | The object name. |
| <CopyableCode code="deviceName" /> | `text` | field from the `properties` object |
| <CopyableCode code="encrypted_password" /> | `text` | field from the `properties` object |
| <CopyableCode code="resourceGroupName" /> | `text` | field from the `properties` object |
| <CopyableCode code="share_access_rights" /> | `text` | field from the `properties` object |
| <CopyableCode code="subscriptionId" /> | `text` | field from the `properties` object |
| <CopyableCode code="system_data" /> | `text` | field from the `properties` object |
| <CopyableCode code="type" /> | `text` | The hierarchical type of the object. |
| <CopyableCode code="user_type" /> | `text` | field from the `properties` object |
</TabItem>
<TabItem value="resource">

| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="id" /> | `string` | The path ID that uniquely identifies the object. |
| <CopyableCode code="name" /> | `string` | The object name. |
| <CopyableCode code="properties" /> | `object` | The user properties. |
| <CopyableCode code="systemData" /> | `object` | Metadata pertaining to creation and last modification of the resource. |
| <CopyableCode code="type" /> | `string` | The hierarchical type of the object. |
</TabItem></Tabs>

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="deviceName, name, resourceGroupName, subscriptionId" /> | Gets the properties of the specified user. |
| <CopyableCode code="list_by_data_box_edge_device" /> | `SELECT` | <CopyableCode code="deviceName, resourceGroupName, subscriptionId" /> | Gets all the users registered on a Data Box Edge/Data Box Gateway device. |
| <CopyableCode code="create_or_update" /> | `INSERT` | <CopyableCode code="deviceName, name, resourceGroupName, subscriptionId, data__properties" /> | Creates a new user or updates an existing user's information on a Data Box Edge/Data Box Gateway device. |
| <CopyableCode code="delete" /> | `DELETE` | <CopyableCode code="deviceName, name, resourceGroupName, subscriptionId" /> | Deletes the user on a databox edge/gateway device. |

## `SELECT` examples

Gets all the users registered on a Data Box Edge/Data Box Gateway device.

<Tabs
    defaultValue="view"
    values={[
        { label: 'vw_users', value: 'view', },
        { label: 'users', value: 'resource', },
    ]
}>
<TabItem value="view">

```sql
SELECT
id,
name,
deviceName,
encrypted_password,
resourceGroupName,
share_access_rights,
subscriptionId,
system_data,
type,
user_type
FROM azure.data_box_edge.vw_users
WHERE deviceName = '{{ deviceName }}'
AND resourceGroupName = '{{ resourceGroupName }}'
AND subscriptionId = '{{ subscriptionId }}';
```
</TabItem>
<TabItem value="resource">


```sql
SELECT
id,
name,
properties,
systemData,
type
FROM azure.data_box_edge.users
WHERE deviceName = '{{ deviceName }}'
AND resourceGroupName = '{{ resourceGroupName }}'
AND subscriptionId = '{{ subscriptionId }}';
```
</TabItem></Tabs>


## `INSERT` example

Use the following StackQL query and manifest file to create a new <code>users</code> resource.

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
INSERT INTO azure.data_box_edge.users (
deviceName,
name,
resourceGroupName,
subscriptionId,
data__properties,
properties
)
SELECT 
'{{ deviceName }}',
'{{ name }}',
'{{ resourceGroupName }}',
'{{ subscriptionId }}',
'{{ data__properties }}',
'{{ properties }}'
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
    - name: properties
      value:
        - name: encryptedPassword
          value:
            - name: value
              value: string
            - name: encryptionCertThumbprint
              value: string
            - name: encryptionAlgorithm
              value: string
        - name: shareAccessRights
          value:
            - - name: shareId
                value: string
              - name: accessType
                value: string
        - name: userType
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

Deletes the specified <code>users</code> resource.

```sql
/*+ delete */
DELETE FROM azure.data_box_edge.users
WHERE deviceName = '{{ deviceName }}'
AND name = '{{ name }}'
AND resourceGroupName = '{{ resourceGroupName }}'
AND subscriptionId = '{{ subscriptionId }}';
```
