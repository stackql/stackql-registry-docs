---
title: diagnostic_settings_diagnostic_proactive_log_collection_settings
hide_title: false
hide_table_of_contents: false
keywords:
  - diagnostic_settings_diagnostic_proactive_log_collection_settings
  - data_box_edge
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

Creates, updates, deletes, gets or lists a <code>diagnostic_settings_diagnostic_proactive_log_collection_settings</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>diagnostic_settings_diagnostic_proactive_log_collection_settings</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.data_box_edge.diagnostic_settings_diagnostic_proactive_log_collection_settings" /></td></tr>
</tbody></table>

## Fields
<Tabs
    defaultValue="view"
    values={[
        { label: 'vw_diagnostic_settings_diagnostic_proactive_log_collection_settings', value: 'view', },
        { label: 'diagnostic_settings_diagnostic_proactive_log_collection_settings', value: 'resource', },
    ]
}>
<TabItem value="view">

| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="id" /> | `text` | The path ID that uniquely identifies the object. |
| <CopyableCode code="name" /> | `text` | The object name. |
| <CopyableCode code="deviceName" /> | `text` | field from the `properties` object |
| <CopyableCode code="resourceGroupName" /> | `text` | field from the `properties` object |
| <CopyableCode code="subscriptionId" /> | `text` | field from the `properties` object |
| <CopyableCode code="system_data" /> | `text` | field from the `properties` object |
| <CopyableCode code="type" /> | `text` | The hierarchical type of the object. |
| <CopyableCode code="user_consent" /> | `text` | field from the `properties` object |
</TabItem>
<TabItem value="resource">

| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="id" /> | `string` | The path ID that uniquely identifies the object. |
| <CopyableCode code="name" /> | `string` | The object name. |
| <CopyableCode code="properties" /> | `object` | The properties of proactive log collection settings. |
| <CopyableCode code="systemData" /> | `object` | Metadata pertaining to creation and last modification of the resource. |
| <CopyableCode code="type" /> | `string` | The hierarchical type of the object. |
</TabItem></Tabs>

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="deviceName, resourceGroupName, subscriptionId" /> | Gets the proactive log collection settings of the specified Data Box Edge/Data Box Gateway device. |
| <CopyableCode code="update" /> | `REPLACE` | <CopyableCode code="deviceName, resourceGroupName, subscriptionId, data__properties" /> | Updates the proactive log collection settings on a Data Box Edge/Data Box Gateway device. |

## `SELECT` examples

Gets the proactive log collection settings of the specified Data Box Edge/Data Box Gateway device.

<Tabs
    defaultValue="view"
    values={[
        { label: 'vw_diagnostic_settings_diagnostic_proactive_log_collection_settings', value: 'view', },
        { label: 'diagnostic_settings_diagnostic_proactive_log_collection_settings', value: 'resource', },
    ]
}>
<TabItem value="view">

```sql
SELECT
id,
name,
deviceName,
resourceGroupName,
subscriptionId,
system_data,
type,
user_consent
FROM azure.data_box_edge.vw_diagnostic_settings_diagnostic_proactive_log_collection_settings
WHERE deviceName = '{{ deviceName }}'
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
FROM azure.data_box_edge.diagnostic_settings_diagnostic_proactive_log_collection_settings
WHERE deviceName = '{{ deviceName }}'
AND resourceGroupName = '{{ resourceGroupName }}'
AND subscriptionId = '{{ subscriptionId }}';
```
</TabItem></Tabs>


## `REPLACE` example

Replaces all fields in the specified <code>diagnostic_settings_diagnostic_proactive_log_collection_settings</code> resource.

```sql
/*+ update */
REPLACE azure.data_box_edge.diagnostic_settings_diagnostic_proactive_log_collection_settings
SET 
properties = '{{ properties }}'
WHERE 
deviceName = '{{ deviceName }}'
AND resourceGroupName = '{{ resourceGroupName }}'
AND subscriptionId = '{{ subscriptionId }}'
AND data__properties = '{{ data__properties }}';
```
