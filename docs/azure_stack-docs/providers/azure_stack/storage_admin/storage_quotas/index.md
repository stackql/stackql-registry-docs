---
title: storage_quotas
hide_title: false
hide_table_of_contents: false
keywords:
  - storage_quotas
  - storage_admin
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

Creates, updates, deletes, gets or lists a <code>storage_quotas</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>storage_quotas</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure_stack.storage_admin.storage_quotas" /></td></tr>
</tbody></table>

## Fields
<Tabs
    defaultValue="view"
    values={[
        { label: 'vw_storage_quotas', value: 'view', },
        { label: 'storage_quotas', value: 'resource', },
    ]
}>
<TabItem value="view">

| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="id" /> | `text` | Resource ID. |
| <CopyableCode code="name" /> | `text` | Resource Name. |
| <CopyableCode code="capacity_in_gb" /> | `text` | field from the `properties` object |
| <CopyableCode code="location" /> | `text` | Resource Location. |
| <CopyableCode code="number_of_storage_accounts" /> | `text` | field from the `properties` object |
| <CopyableCode code="quotaName" /> | `text` | field from the `properties` object |
| <CopyableCode code="subscriptionId" /> | `text` | field from the `properties` object |
| <CopyableCode code="type" /> | `text` | Resource Type. |
</TabItem>
<TabItem value="resource">

| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="id" /> | `string` | Resource ID. |
| <CopyableCode code="name" /> | `string` | Resource Name. |
| <CopyableCode code="location" /> | `string` | Resource Location. |
| <CopyableCode code="properties" /> | `object` | Storage quota properties. |
| <CopyableCode code="type" /> | `string` | Resource Type. |
</TabItem></Tabs>

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="location, quotaName, subscriptionId" /> | Returns the specified storage quota. |
| <CopyableCode code="list" /> | `SELECT` | <CopyableCode code="location, subscriptionId" /> | Returns a list of storage quotas at the given location. |
| <CopyableCode code="create_or_update" /> | `INSERT` | <CopyableCode code="location, quotaName, subscriptionId" /> | Create or update an existing storage quota. |
| <CopyableCode code="delete" /> | `DELETE` | <CopyableCode code="location, quotaName, subscriptionId" /> | Delete an existing quota |

## `SELECT` examples

Returns a list of storage quotas at the given location.

<Tabs
    defaultValue="view"
    values={[
        { label: 'vw_storage_quotas', value: 'view', },
        { label: 'storage_quotas', value: 'resource', },
    ]
}>
<TabItem value="view">

```sql
SELECT
id,
name,
capacity_in_gb,
location,
number_of_storage_accounts,
quotaName,
subscriptionId,
type
FROM azure_stack.storage_admin.vw_storage_quotas
WHERE location = '{{ location }}'
AND subscriptionId = '{{ subscriptionId }}';
```
</TabItem>
<TabItem value="resource">


```sql
SELECT
id,
name,
location,
properties,
type
FROM azure_stack.storage_admin.storage_quotas
WHERE location = '{{ location }}'
AND subscriptionId = '{{ subscriptionId }}';
```
</TabItem></Tabs>


## `INSERT` example

Use the following StackQL query and manifest file to create a new <code>storage_quotas</code> resource.

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
INSERT INTO azure_stack.storage_admin.storage_quotas (
location,
quotaName,
subscriptionId,
properties
)
SELECT 
'{{ location }}',
'{{ quotaName }}',
'{{ subscriptionId }}',
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
        - name: numberOfStorageAccounts
          value: integer
        - name: capacityInGb
          value: integer
    - name: id
      value: string
    - name: name
      value: string
    - name: type
      value: string
    - name: location
      value: string

```
</TabItem>
</Tabs>

## `DELETE` example

Deletes the specified <code>storage_quotas</code> resource.

```sql
/*+ delete */
DELETE FROM azure_stack.storage_admin.storage_quotas
WHERE location = '{{ location }}'
AND quotaName = '{{ quotaName }}'
AND subscriptionId = '{{ subscriptionId }}';
```
