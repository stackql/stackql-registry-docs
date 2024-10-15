---
title: keys
hide_title: false
hide_table_of_contents: false
keywords:
  - keys
  - synapse
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

Creates, updates, deletes, gets or lists a <code>keys</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>keys</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.synapse.keys" /></td></tr>
</tbody></table>

## Fields
<Tabs
    defaultValue="view"
    values={[
        { label: 'vw_keys', value: 'view', },
        { label: 'keys', value: 'resource', },
    ]
}>
<TabItem value="view">

| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="is_active_cmk" /> | `text` | field from the `properties` object |
| <CopyableCode code="keyName" /> | `text` | field from the `properties` object |
| <CopyableCode code="key_vault_url" /> | `text` | field from the `properties` object |
| <CopyableCode code="resourceGroupName" /> | `text` | field from the `properties` object |
| <CopyableCode code="subscriptionId" /> | `text` | field from the `properties` object |
| <CopyableCode code="workspaceName" /> | `text` | field from the `properties` object |
</TabItem>
<TabItem value="resource">

| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="properties" /> | `object` | Key properties |
</TabItem></Tabs>

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="keyName, resourceGroupName, subscriptionId, workspaceName" /> | Gets a workspace key |
| <CopyableCode code="list_by_workspace" /> | `SELECT` | <CopyableCode code="resourceGroupName, subscriptionId, workspaceName" /> | Returns a list of keys in a workspace |
| <CopyableCode code="create_or_update" /> | `INSERT` | <CopyableCode code="keyName, resourceGroupName, subscriptionId, workspaceName" /> | Creates or updates a workspace key |
| <CopyableCode code="delete" /> | `DELETE` | <CopyableCode code="keyName, resourceGroupName, subscriptionId, workspaceName" /> | Deletes a workspace key |

## `SELECT` examples

Returns a list of keys in a workspace

<Tabs
    defaultValue="view"
    values={[
        { label: 'vw_keys', value: 'view', },
        { label: 'keys', value: 'resource', },
    ]
}>
<TabItem value="view">

```sql
SELECT
is_active_cmk,
keyName,
key_vault_url,
resourceGroupName,
subscriptionId,
workspaceName
FROM azure.synapse.vw_keys
WHERE resourceGroupName = '{{ resourceGroupName }}'
AND subscriptionId = '{{ subscriptionId }}'
AND workspaceName = '{{ workspaceName }}';
```
</TabItem>
<TabItem value="resource">


```sql
SELECT
properties
FROM azure.synapse.keys
WHERE resourceGroupName = '{{ resourceGroupName }}'
AND subscriptionId = '{{ subscriptionId }}'
AND workspaceName = '{{ workspaceName }}';
```
</TabItem></Tabs>


## `INSERT` example

Use the following StackQL query and manifest file to create a new <code>keys</code> resource.

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
INSERT INTO azure.synapse.keys (
keyName,
resourceGroupName,
subscriptionId,
workspaceName,
properties
)
SELECT 
'{{ keyName }}',
'{{ resourceGroupName }}',
'{{ subscriptionId }}',
'{{ workspaceName }}',
'{{ properties }}'
;
```
</TabItem>
<TabItem value="manifest">

```yaml
- name: your_resource_model_name
  props:
    - name: properties
      value:
        - name: isActiveCMK
          value: boolean
        - name: keyVaultUrl
          value: string

```
</TabItem>
</Tabs>

## `DELETE` example

Deletes the specified <code>keys</code> resource.

```sql
/*+ delete */
DELETE FROM azure.synapse.keys
WHERE keyName = '{{ keyName }}'
AND resourceGroupName = '{{ resourceGroupName }}'
AND subscriptionId = '{{ subscriptionId }}'
AND workspaceName = '{{ workspaceName }}';
```
