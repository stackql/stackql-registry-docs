---
title: desktops
hide_title: false
hide_table_of_contents: false
keywords:
  - desktops
  - desktop_virtualization
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

Creates, updates, deletes, gets or lists a <code>desktops</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>desktops</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.desktop_virtualization.desktops" /></td></tr>
</tbody></table>

## Fields
<Tabs
    defaultValue="view"
    values={[
        { label: 'vw_desktops', value: 'view', },
        { label: 'desktops', value: 'resource', },
    ]
}>
<TabItem value="view">

| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="id" /> | `text` | Fully qualified resource ID for the resource. E.g. "/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/{resourceProviderNamespace}/{resourceType}/{resourceName}" |
| <CopyableCode code="name" /> | `text` | The name of the resource |
| <CopyableCode code="description" /> | `text` | field from the `properties` object |
| <CopyableCode code="applicationGroupName" /> | `text` | field from the `properties` object |
| <CopyableCode code="desktopName" /> | `text` | field from the `properties` object |
| <CopyableCode code="friendly_name" /> | `text` | field from the `properties` object |
| <CopyableCode code="icon_content" /> | `text` | field from the `properties` object |
| <CopyableCode code="icon_hash" /> | `text` | field from the `properties` object |
| <CopyableCode code="object_id" /> | `text` | field from the `properties` object |
| <CopyableCode code="resourceGroupName" /> | `text` | field from the `properties` object |
| <CopyableCode code="subscriptionId" /> | `text` | field from the `properties` object |
| <CopyableCode code="system_data" /> | `text` | field from the `properties` object |
| <CopyableCode code="type" /> | `text` | The type of the resource. E.g. "Microsoft.Compute/virtualMachines" or "Microsoft.Storage/storageAccounts" |
</TabItem>
<TabItem value="resource">

| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="id" /> | `string` | Fully qualified resource ID for the resource. E.g. "/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/{resourceProviderNamespace}/{resourceType}/{resourceName}" |
| <CopyableCode code="name" /> | `string` | The name of the resource |
| <CopyableCode code="properties" /> | `object` | Schema for Desktop properties. |
| <CopyableCode code="systemData" /> | `object` | Metadata pertaining to creation and last modification of the resource. |
| <CopyableCode code="type" /> | `string` | The type of the resource. E.g. "Microsoft.Compute/virtualMachines" or "Microsoft.Storage/storageAccounts" |
</TabItem></Tabs>

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="applicationGroupName, desktopName, resourceGroupName, subscriptionId" /> | Get a desktop. |
| <CopyableCode code="list" /> | `SELECT` | <CopyableCode code="applicationGroupName, resourceGroupName, subscriptionId" /> | List desktops. |
| <CopyableCode code="update" /> | `UPDATE` | <CopyableCode code="applicationGroupName, desktopName, resourceGroupName, subscriptionId" /> | Update a desktop. |

## `SELECT` examples

List desktops.

<Tabs
    defaultValue="view"
    values={[
        { label: 'vw_desktops', value: 'view', },
        { label: 'desktops', value: 'resource', },
    ]
}>
<TabItem value="view">

```sql
SELECT
id,
name,
description,
applicationGroupName,
desktopName,
friendly_name,
icon_content,
icon_hash,
object_id,
resourceGroupName,
subscriptionId,
system_data,
type
FROM azure.desktop_virtualization.vw_desktops
WHERE applicationGroupName = '{{ applicationGroupName }}'
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
FROM azure.desktop_virtualization.desktops
WHERE applicationGroupName = '{{ applicationGroupName }}'
AND resourceGroupName = '{{ resourceGroupName }}'
AND subscriptionId = '{{ subscriptionId }}';
```
</TabItem></Tabs>


## `UPDATE` example

Updates a <code>desktops</code> resource.

```sql
/*+ update */
UPDATE azure.desktop_virtualization.desktops
SET 
tags = '{{ tags }}',
properties = '{{ properties }}'
WHERE 
applicationGroupName = '{{ applicationGroupName }}'
AND desktopName = '{{ desktopName }}'
AND resourceGroupName = '{{ resourceGroupName }}'
AND subscriptionId = '{{ subscriptionId }}';
```
