---
title: slot_configuration_names
hide_title: false
hide_table_of_contents: false
keywords:
  - slot_configuration_names
  - app_service
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

Creates, updates, deletes, gets or lists a <code>slot_configuration_names</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>slot_configuration_names</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.app_service.slot_configuration_names" /></td></tr>
</tbody></table>

## Fields
<Tabs
    defaultValue="view"
    values={[
        { label: 'vw_slot_configuration_names', value: 'view', },
        { label: 'slot_configuration_names', value: 'resource', },
    ]
}>
<TabItem value="view">

| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="id" /> | `text` | Resource Id. |
| <CopyableCode code="name" /> | `text` | Resource Name. |
| <CopyableCode code="app_setting_names" /> | `text` | field from the `properties` object |
| <CopyableCode code="azure_storage_config_names" /> | `text` | field from the `properties` object |
| <CopyableCode code="connection_string_names" /> | `text` | field from the `properties` object |
| <CopyableCode code="kind" /> | `text` | Kind of resource. |
| <CopyableCode code="resourceGroupName" /> | `text` | field from the `properties` object |
| <CopyableCode code="subscriptionId" /> | `text` | field from the `properties` object |
| <CopyableCode code="type" /> | `text` | Resource type. |
</TabItem>
<TabItem value="resource">

| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="id" /> | `string` | Resource Id. |
| <CopyableCode code="name" /> | `string` | Resource Name. |
| <CopyableCode code="kind" /> | `string` | Kind of resource. |
| <CopyableCode code="properties" /> | `object` | Names for connection strings, application settings, and external Azure storage account configuration
identifiers to be marked as sticky to the deployment slot and not moved during a swap operation.
This is valid for all deployment slots in an app. |
| <CopyableCode code="type" /> | `string` | Resource type. |
</TabItem></Tabs>

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="list" /> | `SELECT` | <CopyableCode code="name, resourceGroupName, subscriptionId" /> | Description for Gets the names of app settings and connection strings that stick to the slot (not swapped). |
| <CopyableCode code="update" /> | `REPLACE` | <CopyableCode code="name, resourceGroupName, subscriptionId" /> | Description for Updates the names of application settings and connection string that remain with the slot during swap operation. |

## `SELECT` examples

Description for Gets the names of app settings and connection strings that stick to the slot (not swapped).

<Tabs
    defaultValue="view"
    values={[
        { label: 'vw_slot_configuration_names', value: 'view', },
        { label: 'slot_configuration_names', value: 'resource', },
    ]
}>
<TabItem value="view">

```sql
SELECT
id,
name,
app_setting_names,
azure_storage_config_names,
connection_string_names,
kind,
resourceGroupName,
subscriptionId,
type
FROM azure.app_service.vw_slot_configuration_names
WHERE name = '{{ name }}'
AND resourceGroupName = '{{ resourceGroupName }}'
AND subscriptionId = '{{ subscriptionId }}';
```
</TabItem>
<TabItem value="resource">


```sql
SELECT
id,
name,
kind,
properties,
type
FROM azure.app_service.slot_configuration_names
WHERE name = '{{ name }}'
AND resourceGroupName = '{{ resourceGroupName }}'
AND subscriptionId = '{{ subscriptionId }}';
```
</TabItem></Tabs>


## `REPLACE` example

Replaces all fields in the specified <code>slot_configuration_names</code> resource.

```sql
/*+ update */
REPLACE azure.app_service.slot_configuration_names
SET 
kind = '{{ kind }}',
properties = '{{ properties }}'
WHERE 
name = '{{ name }}'
AND resourceGroupName = '{{ resourceGroupName }}'
AND subscriptionId = '{{ subscriptionId }}';
```
