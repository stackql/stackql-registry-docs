---
title: storage_settings
hide_title: false
hide_table_of_contents: false
keywords:
  - storage_settings
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

Creates, updates, deletes, gets or lists a <code>storage_settings</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>storage_settings</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure_stack.storage_admin.storage_settings" /></td></tr>
</tbody></table>

## Fields
<Tabs
    defaultValue="view"
    values={[
        { label: 'vw_storage_settings', value: 'view', },
        { label: 'storage_settings', value: 'resource', },
    ]
}>
<TabItem value="view">

| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="id" /> | `text` | Resource ID. |
| <CopyableCode code="name" /> | `text` | Resource Name. |
| <CopyableCode code="location" /> | `text` | Resource Location. |
| <CopyableCode code="retention_period_for_deleted_storage_accounts_in_days" /> | `text` | field from the `properties` object |
| <CopyableCode code="subscriptionId" /> | `text` | field from the `properties` object |
| <CopyableCode code="type" /> | `text` | Resource Type. |
</TabItem>
<TabItem value="resource">

| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="id" /> | `string` | Resource ID. |
| <CopyableCode code="name" /> | `string` | Resource Name. |
| <CopyableCode code="location" /> | `string` | Resource Location. |
| <CopyableCode code="properties" /> | `object` | Properties of storage setting. |
| <CopyableCode code="type" /> | `string` | Resource Type. |
</TabItem></Tabs>

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="location, subscriptionId" /> | Returns the storage resource provider settings. |
| <CopyableCode code="update" /> | `REPLACE` | <CopyableCode code="location, subscriptionId" /> | Update storage resource provider settings. |

## `SELECT` examples

Returns the storage resource provider settings.

<Tabs
    defaultValue="view"
    values={[
        { label: 'vw_storage_settings', value: 'view', },
        { label: 'storage_settings', value: 'resource', },
    ]
}>
<TabItem value="view">

```sql
SELECT
id,
name,
location,
retention_period_for_deleted_storage_accounts_in_days,
subscriptionId,
type
FROM azure_stack.storage_admin.vw_storage_settings
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
FROM azure_stack.storage_admin.storage_settings
WHERE location = '{{ location }}'
AND subscriptionId = '{{ subscriptionId }}';
```
</TabItem></Tabs>


## `REPLACE` example

Replaces all fields in the specified <code>storage_settings</code> resource.

```sql
/*+ update */
REPLACE azure_stack.storage_admin.storage_settings
SET 
properties = '{{ properties }}'
WHERE 
location = '{{ location }}'
AND subscriptionId = '{{ subscriptionId }}';
```
