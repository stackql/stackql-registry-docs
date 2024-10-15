---
title: bandwidth_settings
hide_title: false
hide_table_of_contents: false
keywords:
  - bandwidth_settings
  - storsimple_8000_series
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

Creates, updates, deletes, gets or lists a <code>bandwidth_settings</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>bandwidth_settings</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure_extras.storsimple_8000_series.bandwidth_settings" /></td></tr>
</tbody></table>

## Fields
<Tabs
    defaultValue="view"
    values={[
        { label: 'vw_bandwidth_settings', value: 'view', },
        { label: 'bandwidth_settings', value: 'resource', },
    ]
}>
<TabItem value="view">

| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="id" /> | `text` | The path ID that uniquely identifies the object. |
| <CopyableCode code="name" /> | `text` | The name of the object. |
| <CopyableCode code="bandwidthSettingName" /> | `text` | field from the `properties` object |
| <CopyableCode code="kind" /> | `text` | The Kind of the object. Currently only Series8000 is supported |
| <CopyableCode code="managerName" /> | `text` | field from the `properties` object |
| <CopyableCode code="resourceGroupName" /> | `text` | field from the `properties` object |
| <CopyableCode code="schedules" /> | `text` | field from the `properties` object |
| <CopyableCode code="subscriptionId" /> | `text` | field from the `properties` object |
| <CopyableCode code="type" /> | `text` | The hierarchical type of the object. |
| <CopyableCode code="volume_count" /> | `text` | field from the `properties` object |
</TabItem>
<TabItem value="resource">

| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="id" /> | `string` | The path ID that uniquely identifies the object. |
| <CopyableCode code="name" /> | `string` | The name of the object. |
| <CopyableCode code="kind" /> | `string` | The Kind of the object. Currently only Series8000 is supported |
| <CopyableCode code="properties" /> | `object` | The properties of the bandwidth setting. |
| <CopyableCode code="type" /> | `string` | The hierarchical type of the object. |
</TabItem></Tabs>

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="bandwidthSettingName, managerName, resourceGroupName, subscriptionId" /> | Returns the properties of the specified bandwidth setting name. |
| <CopyableCode code="list_by_manager" /> | `SELECT` | <CopyableCode code="managerName, resourceGroupName, subscriptionId" /> | Retrieves all the bandwidth setting in a manager. |
| <CopyableCode code="create_or_update" /> | `INSERT` | <CopyableCode code="bandwidthSettingName, managerName, resourceGroupName, subscriptionId, data__properties" /> | Creates or updates the bandwidth setting |
| <CopyableCode code="delete" /> | `DELETE` | <CopyableCode code="bandwidthSettingName, managerName, resourceGroupName, subscriptionId" /> | Deletes the bandwidth setting |

## `SELECT` examples

Retrieves all the bandwidth setting in a manager.

<Tabs
    defaultValue="view"
    values={[
        { label: 'vw_bandwidth_settings', value: 'view', },
        { label: 'bandwidth_settings', value: 'resource', },
    ]
}>
<TabItem value="view">

```sql
SELECT
id,
name,
bandwidthSettingName,
kind,
managerName,
resourceGroupName,
schedules,
subscriptionId,
type,
volume_count
FROM azure_extras.storsimple_8000_series.vw_bandwidth_settings
WHERE managerName = '{{ managerName }}'
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
FROM azure_extras.storsimple_8000_series.bandwidth_settings
WHERE managerName = '{{ managerName }}'
AND resourceGroupName = '{{ resourceGroupName }}'
AND subscriptionId = '{{ subscriptionId }}';
```
</TabItem></Tabs>


## `INSERT` example

Use the following StackQL query and manifest file to create a new <code>bandwidth_settings</code> resource.

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
INSERT INTO azure_extras.storsimple_8000_series.bandwidth_settings (
bandwidthSettingName,
managerName,
resourceGroupName,
subscriptionId,
data__properties,
kind,
properties
)
SELECT 
'{{ bandwidthSettingName }}',
'{{ managerName }}',
'{{ resourceGroupName }}',
'{{ subscriptionId }}',
'{{ data__properties }}',
'{{ kind }}',
'{{ properties }}'
;
```
</TabItem>
<TabItem value="manifest">

```yaml
- name: your_resource_model_name
  props:
    - name: id
      value: string
    - name: name
      value: string
    - name: type
      value: string
    - name: kind
      value: string
    - name: properties
      value:
        - name: schedules
          value:
            - - name: start
                value:
                  - name: hours
                    value: integer
                  - name: minutes
                    value: integer
                  - name: seconds
                    value: integer
              - name: rateInMbps
                value: integer
              - name: days
                value:
                  - string
        - name: volumeCount
          value: integer

```
</TabItem>
</Tabs>

## `DELETE` example

Deletes the specified <code>bandwidth_settings</code> resource.

```sql
/*+ delete */
DELETE FROM azure_extras.storsimple_8000_series.bandwidth_settings
WHERE bandwidthSettingName = '{{ bandwidthSettingName }}'
AND managerName = '{{ managerName }}'
AND resourceGroupName = '{{ resourceGroupName }}'
AND subscriptionId = '{{ subscriptionId }}';
```
