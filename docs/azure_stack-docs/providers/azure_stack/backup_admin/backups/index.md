---
title: backups
hide_title: false
hide_table_of_contents: false
keywords:
  - backups
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

Creates, updates, deletes, gets or lists a <code>backups</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>backups</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure_stack.backup_admin.backups" /></td></tr>
</tbody></table>

## Fields
<Tabs
    defaultValue="view"
    values={[
        { label: 'vw_backups', value: 'view', },
        { label: 'backups', value: 'resource', },
    ]
}>
<TabItem value="view">

| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="id" /> | `text` | URI of the resource. |
| <CopyableCode code="name" /> | `text` | Name of the resource. |
| <CopyableCode code="backup" /> | `text` | field from the `properties` object |
| <CopyableCode code="backup_info" /> | `text` | field from the `properties` object |
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
| <CopyableCode code="properties" /> | `object` | Properties for a backup. |
| <CopyableCode code="tags" /> | `object` | List of key value pairs. |
| <CopyableCode code="type" /> | `string` | Type of resource. |
</TabItem></Tabs>

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="backup, location, resourceGroupName, subscriptionId" /> | Returns a backup from a location based on name. |
| <CopyableCode code="list" /> | `SELECT` | <CopyableCode code="location, resourceGroupName, subscriptionId" /> | Returns a list of backups from a location. |
| <CopyableCode code="restore" /> | `EXEC` | <CopyableCode code="backup, location, resourceGroupName, subscriptionId" /> | Restore a backup. |

## `SELECT` examples

Returns a list of backups from a location.

<Tabs
    defaultValue="view"
    values={[
        { label: 'vw_backups', value: 'view', },
        { label: 'backups', value: 'resource', },
    ]
}>
<TabItem value="view">

```sql
SELECT
id,
name,
backup,
backup_info,
location,
resourceGroupName,
subscriptionId,
tags,
type
FROM azure_stack.backup_admin.vw_backups
WHERE location = '{{ location }}'
AND resourceGroupName = '{{ resourceGroupName }}'
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
FROM azure_stack.backup_admin.backups
WHERE location = '{{ location }}'
AND resourceGroupName = '{{ resourceGroupName }}'
AND subscriptionId = '{{ subscriptionId }}';
```
</TabItem></Tabs>

