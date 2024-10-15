---
title: managed_instance_keys
hide_title: false
hide_table_of_contents: false
keywords:
  - managed_instance_keys
  - sql
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

Creates, updates, deletes, gets or lists a <code>managed_instance_keys</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>managed_instance_keys</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.sql.managed_instance_keys" /></td></tr>
</tbody></table>

## Fields
<Tabs
    defaultValue="view"
    values={[
        { label: 'vw_managed_instance_keys', value: 'view', },
        { label: 'managed_instance_keys', value: 'resource', },
    ]
}>
<TabItem value="view">

| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="auto_rotation_enabled" /> | `text` | field from the `properties` object |
| <CopyableCode code="creation_date" /> | `text` | field from the `properties` object |
| <CopyableCode code="keyName" /> | `text` | field from the `properties` object |
| <CopyableCode code="kind" /> | `text` | Kind of encryption protector. This is metadata used for the Azure portal experience. |
| <CopyableCode code="managedInstanceName" /> | `text` | field from the `properties` object |
| <CopyableCode code="resourceGroupName" /> | `text` | field from the `properties` object |
| <CopyableCode code="server_key_type" /> | `text` | field from the `properties` object |
| <CopyableCode code="subscriptionId" /> | `text` | field from the `properties` object |
| <CopyableCode code="thumbprint" /> | `text` | field from the `properties` object |
| <CopyableCode code="uri" /> | `text` | field from the `properties` object |
</TabItem>
<TabItem value="resource">

| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="kind" /> | `string` | Kind of encryption protector. This is metadata used for the Azure portal experience. |
| <CopyableCode code="properties" /> | `object` | Properties for a key execution. |
</TabItem></Tabs>

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="keyName, managedInstanceName, resourceGroupName, subscriptionId" /> | Gets a managed instance key. |
| <CopyableCode code="create_or_update" /> | `INSERT` | <CopyableCode code="keyName, managedInstanceName, resourceGroupName, subscriptionId" /> | Creates or updates a managed instance key. |
| <CopyableCode code="delete" /> | `DELETE` | <CopyableCode code="keyName, managedInstanceName, resourceGroupName, subscriptionId" /> | Deletes the managed instance key with the given name. |

## `SELECT` examples

Gets a managed instance key.

<Tabs
    defaultValue="view"
    values={[
        { label: 'vw_managed_instance_keys', value: 'view', },
        { label: 'managed_instance_keys', value: 'resource', },
    ]
}>
<TabItem value="view">

```sql
SELECT
auto_rotation_enabled,
creation_date,
keyName,
kind,
managedInstanceName,
resourceGroupName,
server_key_type,
subscriptionId,
thumbprint,
uri
FROM azure.sql.vw_managed_instance_keys
WHERE keyName = '{{ keyName }}'
AND managedInstanceName = '{{ managedInstanceName }}'
AND resourceGroupName = '{{ resourceGroupName }}'
AND subscriptionId = '{{ subscriptionId }}';
```
</TabItem>
<TabItem value="resource">


```sql
SELECT
kind,
properties
FROM azure.sql.managed_instance_keys
WHERE keyName = '{{ keyName }}'
AND managedInstanceName = '{{ managedInstanceName }}'
AND resourceGroupName = '{{ resourceGroupName }}'
AND subscriptionId = '{{ subscriptionId }}';
```
</TabItem></Tabs>


## `INSERT` example

Use the following StackQL query and manifest file to create a new <code>managed_instance_keys</code> resource.

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
INSERT INTO azure.sql.managed_instance_keys (
keyName,
managedInstanceName,
resourceGroupName,
subscriptionId,
properties
)
SELECT 
'{{ keyName }}',
'{{ managedInstanceName }}',
'{{ resourceGroupName }}',
'{{ subscriptionId }}',
'{{ properties }}'
;
```
</TabItem>
<TabItem value="manifest">

```yaml
- name: your_resource_model_name
  props:
    - name: kind
      value: string
    - name: properties
      value:
        - name: serverKeyType
          value: string
        - name: uri
          value: string
        - name: thumbprint
          value: string
        - name: creationDate
          value: string
        - name: autoRotationEnabled
          value: boolean

```
</TabItem>
</Tabs>

## `DELETE` example

Deletes the specified <code>managed_instance_keys</code> resource.

```sql
/*+ delete */
DELETE FROM azure.sql.managed_instance_keys
WHERE keyName = '{{ keyName }}'
AND managedInstanceName = '{{ managedInstanceName }}'
AND resourceGroupName = '{{ resourceGroupName }}'
AND subscriptionId = '{{ subscriptionId }}';
```
