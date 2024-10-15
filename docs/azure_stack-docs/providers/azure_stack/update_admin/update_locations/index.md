---
title: update_locations
hide_title: false
hide_table_of_contents: false
keywords:
  - update_locations
  - update_admin
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

Creates, updates, deletes, gets or lists a <code>update_locations</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>update_locations</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure_stack.update_admin.update_locations" /></td></tr>
</tbody></table>

## Fields
<Tabs
    defaultValue="view"
    values={[
        { label: 'vw_update_locations', value: 'view', },
        { label: 'update_locations', value: 'resource', },
    ]
}>
<TabItem value="view">

| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="id" /> | `text` | URI of the resource. |
| <CopyableCode code="name" /> | `text` | Name of the resource. |
| <CopyableCode code="current_oem_version" /> | `text` | field from the `properties` object |
| <CopyableCode code="current_version" /> | `text` | field from the `properties` object |
| <CopyableCode code="hardware_model" /> | `text` | field from the `properties` object |
| <CopyableCode code="last_checked" /> | `text` | field from the `properties` object |
| <CopyableCode code="last_updated" /> | `text` | field from the `properties` object |
| <CopyableCode code="location" /> | `text` | Region location of resource. |
| <CopyableCode code="oem_family" /> | `text` | field from the `properties` object |
| <CopyableCode code="package_versions" /> | `text` | field from the `properties` object |
| <CopyableCode code="resourceGroupName" /> | `text` | field from the `properties` object |
| <CopyableCode code="state" /> | `text` | field from the `properties` object |
| <CopyableCode code="subscriptionId" /> | `text` | field from the `properties` object |
| <CopyableCode code="tags" /> | `text` | List of key-value pairs. |
| <CopyableCode code="type" /> | `text` | Type of resource. |
| <CopyableCode code="updateLocation" /> | `text` | field from the `properties` object |
</TabItem>
<TabItem value="resource">

| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="id" /> | `string` | URI of the resource. |
| <CopyableCode code="name" /> | `string` | Name of the resource. |
| <CopyableCode code="location" /> | `string` | Region location of resource. |
| <CopyableCode code="properties" /> | `object` | Model which holds information related to update location. |
| <CopyableCode code="tags" /> | `object` | List of key-value pairs. |
| <CopyableCode code="type" /> | `string` | Type of resource. |
</TabItem></Tabs>

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="resourceGroupName, subscriptionId, updateLocation" /> | Get an update location based on name. |
| <CopyableCode code="list" /> | `SELECT` | <CopyableCode code="resourceGroupName, subscriptionId" /> | Get the list of update locations. |

## `SELECT` examples

Get the list of update locations.

<Tabs
    defaultValue="view"
    values={[
        { label: 'vw_update_locations', value: 'view', },
        { label: 'update_locations', value: 'resource', },
    ]
}>
<TabItem value="view">

```sql
SELECT
id,
name,
current_oem_version,
current_version,
hardware_model,
last_checked,
last_updated,
location,
oem_family,
package_versions,
resourceGroupName,
state,
subscriptionId,
tags,
type,
updateLocation
FROM azure_stack.update_admin.vw_update_locations
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
FROM azure_stack.update_admin.update_locations
WHERE resourceGroupName = '{{ resourceGroupName }}'
AND subscriptionId = '{{ subscriptionId }}';
```
</TabItem></Tabs>

