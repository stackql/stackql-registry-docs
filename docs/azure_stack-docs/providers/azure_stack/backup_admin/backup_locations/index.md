---
title: backup_locations
hide_title: false
hide_table_of_contents: false
keywords:
  - backup_locations
  - backup_admin
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

Creates, updates, deletes, gets or lists a <code>backup_locations</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>backup_locations</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure_stack.backup_admin.backup_locations" /></td></tr>
</tbody></table>

## Fields
<Tabs
    defaultValue="view"
    values={[
        { label: 'vw_backup_locations', value: 'view', },
        { label: 'backup_locations', value: 'resource', },
    ]
}>
<TabItem value="view">

| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="id" /> | `text` | URI of the resource. |
| <CopyableCode code="name" /> | `text` | Name of the resource. |
| <CopyableCode code="external_store_default" /> | `text` | field from the `properties` object |
| <CopyableCode code="location" /> | `text` | Location of the resource. |
| <CopyableCode code="resourceGroupName" /> | `text` | field from the `properties` object |
| <CopyableCode code="subscriptionId" /> | `text` | field from the `properties` object |
| <CopyableCode code="tags" /> | `text` | List of key value pairs. |
| <CopyableCode code="type" /> | `text` | Type of resource. |
</TabItem>
<TabItem value="resource">

| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="id" /> | `string` | URI of the resource. |
| <CopyableCode code="name" /> | `string` | Name of the resource. |
| <CopyableCode code="location" /> | `string` | Location of the resource. |
| <CopyableCode code="properties" /> | `object` | Properties of a backup location. |
| <CopyableCode code="tags" /> | `object` | List of key value pairs. |
| <CopyableCode code="type" /> | `string` | Type of resource. |
</TabItem></Tabs>

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="location, resourceGroupName, subscriptionId" /> | Returns a specific backup location based on name. |
| <CopyableCode code="list" /> | `SELECT` | <CopyableCode code="resourceGroupName, subscriptionId" /> | Returns the list of backup locations. |
| <CopyableCode code="update" /> | `REPLACE` | <CopyableCode code="location, resourceGroupName, subscriptionId" /> | Update a backup location. |
| <CopyableCode code="prune_external_store" /> | `EXEC` | <CopyableCode code="location, resourceGroupName, subscriptionId" /> | Prune the external backup store. |

## `SELECT` examples

Returns the list of backup locations.

<Tabs
    defaultValue="view"
    values={[
        { label: 'vw_backup_locations', value: 'view', },
        { label: 'backup_locations', value: 'resource', },
    ]
}>
<TabItem value="view">

```sql
SELECT
id,
name,
external_store_default,
location,
resourceGroupName,
subscriptionId,
tags,
type
FROM azure_stack.backup_admin.vw_backup_locations
WHERE resourceGroupName = '{{ resourceGroupName }}'
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
tags,
type
FROM azure_stack.backup_admin.backup_locations
WHERE resourceGroupName = '{{ resourceGroupName }}'
AND subscriptionId = '{{ subscriptionId }}';
```
</TabItem></Tabs>


## `REPLACE` example

Replaces all fields in the specified <code>backup_locations</code> resource.

```sql
/*+ update */
REPLACE azure_stack.backup_admin.backup_locations
SET 
properties = '{{ properties }}',
location = '{{ location }}',
tags = '{{ tags }}'
WHERE 
location = '{{ location }}'
AND resourceGroupName = '{{ resourceGroupName }}'
AND subscriptionId = '{{ subscriptionId }}';
```
