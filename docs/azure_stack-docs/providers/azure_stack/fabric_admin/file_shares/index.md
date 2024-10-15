---
title: file_shares
hide_title: false
hide_table_of_contents: false
keywords:
  - file_shares
  - fabric_admin
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

Creates, updates, deletes, gets or lists a <code>file_shares</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>file_shares</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure_stack.fabric_admin.file_shares" /></td></tr>
</tbody></table>

## Fields
<Tabs
    defaultValue="view"
    values={[
        { label: 'vw_file_shares', value: 'view', },
        { label: 'file_shares', value: 'resource', },
    ]
}>
<TabItem value="view">

| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="id" /> | `text` | URI of the resource. |
| <CopyableCode code="name" /> | `text` | Name of the resource. |
| <CopyableCode code="associated_volume" /> | `text` | field from the `properties` object |
| <CopyableCode code="fileShare" /> | `text` | field from the `properties` object |
| <CopyableCode code="location" /> | `text` | The region where the resource is located. |
| <CopyableCode code="resourceGroupName" /> | `text` | field from the `properties` object |
| <CopyableCode code="subscriptionId" /> | `text` | field from the `properties` object |
| <CopyableCode code="tags" /> | `text` | List of key-value pairs. |
| <CopyableCode code="type" /> | `text` | Type of resource. |
| <CopyableCode code="unc_path" /> | `text` | field from the `properties` object |
</TabItem>
<TabItem value="resource">

| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="id" /> | `string` | URI of the resource. |
| <CopyableCode code="name" /> | `string` | Name of the resource. |
| <CopyableCode code="location" /> | `string` | The region where the resource is located. |
| <CopyableCode code="properties" /> | `object` | Properties of a file share resource. |
| <CopyableCode code="tags" /> | `object` | List of key-value pairs. |
| <CopyableCode code="type" /> | `string` | Type of resource. |
</TabItem></Tabs>

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="fileShare, location, resourceGroupName, subscriptionId" /> | Returns the requested fabric file share. |
| <CopyableCode code="list" /> | `SELECT` | <CopyableCode code="location, resourceGroupName, subscriptionId" /> | Returns a list of all fabric file shares at a certain location. |

## `SELECT` examples

Returns a list of all fabric file shares at a certain location.

<Tabs
    defaultValue="view"
    values={[
        { label: 'vw_file_shares', value: 'view', },
        { label: 'file_shares', value: 'resource', },
    ]
}>
<TabItem value="view">

```sql
SELECT
id,
name,
associated_volume,
fileShare,
location,
resourceGroupName,
subscriptionId,
tags,
type,
unc_path
FROM azure_stack.fabric_admin.vw_file_shares
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
FROM azure_stack.fabric_admin.file_shares
WHERE location = '{{ location }}'
AND resourceGroupName = '{{ resourceGroupName }}'
AND subscriptionId = '{{ subscriptionId }}';
```
</TabItem></Tabs>

