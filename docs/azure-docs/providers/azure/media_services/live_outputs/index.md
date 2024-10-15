---
title: live_outputs
hide_title: false
hide_table_of_contents: false
keywords:
  - live_outputs
  - media_services
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

Creates, updates, deletes, gets or lists a <code>live_outputs</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>live_outputs</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.media_services.live_outputs" /></td></tr>
</tbody></table>

## Fields
<Tabs
    defaultValue="view"
    values={[
        { label: 'vw_live_outputs', value: 'view', },
        { label: 'live_outputs', value: 'resource', },
    ]
}>
<TabItem value="view">

| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="description" /> | `text` | field from the `properties` object |
| <CopyableCode code="accountName" /> | `text` | field from the `properties` object |
| <CopyableCode code="archive_window_length" /> | `text` | field from the `properties` object |
| <CopyableCode code="asset_name" /> | `text` | field from the `properties` object |
| <CopyableCode code="created" /> | `text` | field from the `properties` object |
| <CopyableCode code="hls" /> | `text` | field from the `properties` object |
| <CopyableCode code="last_modified" /> | `text` | field from the `properties` object |
| <CopyableCode code="liveEventName" /> | `text` | field from the `properties` object |
| <CopyableCode code="liveOutputName" /> | `text` | field from the `properties` object |
| <CopyableCode code="manifest_name" /> | `text` | field from the `properties` object |
| <CopyableCode code="output_snap_time" /> | `text` | field from the `properties` object |
| <CopyableCode code="provisioning_state" /> | `text` | field from the `properties` object |
| <CopyableCode code="resourceGroupName" /> | `text` | field from the `properties` object |
| <CopyableCode code="resource_state" /> | `text` | field from the `properties` object |
| <CopyableCode code="rewind_window_length" /> | `text` | field from the `properties` object |
| <CopyableCode code="subscriptionId" /> | `text` | field from the `properties` object |
| <CopyableCode code="system_data" /> | `text` | field from the `properties` object |
</TabItem>
<TabItem value="resource">

| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="properties" /> | `object` | The JSON object that contains the properties required to create a live output. |
| <CopyableCode code="systemData" /> | `object` | Metadata pertaining to creation and last modification of the resource. |
</TabItem></Tabs>

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="accountName, liveEventName, liveOutputName, resourceGroupName, subscriptionId" /> | Gets a live output. |
| <CopyableCode code="list" /> | `SELECT` | <CopyableCode code="accountName, liveEventName, resourceGroupName, subscriptionId" /> | Lists the live outputs of a live event. |
| <CopyableCode code="create" /> | `INSERT` | <CopyableCode code="accountName, liveEventName, liveOutputName, resourceGroupName, subscriptionId" /> | Creates a new live output. |
| <CopyableCode code="delete" /> | `DELETE` | <CopyableCode code="accountName, liveEventName, liveOutputName, resourceGroupName, subscriptionId" /> | Deletes a live output. Deleting a live output does not delete the asset the live output is writing to. |
| <CopyableCode code="async_operation" /> | `EXEC` | <CopyableCode code="accountName, operationId, resourceGroupName, subscriptionId" /> | Get a Live Output operation status. |
| <CopyableCode code="operation_location" /> | `EXEC` | <CopyableCode code="accountName, liveEventName, liveOutputName, operationId, resourceGroupName, subscriptionId" /> | Get a Live Output operation status. |

## `SELECT` examples

Lists the live outputs of a live event.

<Tabs
    defaultValue="view"
    values={[
        { label: 'vw_live_outputs', value: 'view', },
        { label: 'live_outputs', value: 'resource', },
    ]
}>
<TabItem value="view">

```sql
SELECT
description,
accountName,
archive_window_length,
asset_name,
created,
hls,
last_modified,
liveEventName,
liveOutputName,
manifest_name,
output_snap_time,
provisioning_state,
resourceGroupName,
resource_state,
rewind_window_length,
subscriptionId,
system_data
FROM azure.media_services.vw_live_outputs
WHERE accountName = '{{ accountName }}'
AND liveEventName = '{{ liveEventName }}'
AND resourceGroupName = '{{ resourceGroupName }}'
AND subscriptionId = '{{ subscriptionId }}';
```
</TabItem>
<TabItem value="resource">


```sql
SELECT
properties,
systemData
FROM azure.media_services.live_outputs
WHERE accountName = '{{ accountName }}'
AND liveEventName = '{{ liveEventName }}'
AND resourceGroupName = '{{ resourceGroupName }}'
AND subscriptionId = '{{ subscriptionId }}';
```
</TabItem></Tabs>


## `INSERT` example

Use the following StackQL query and manifest file to create a new <code>live_outputs</code> resource.

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
INSERT INTO azure.media_services.live_outputs (
accountName,
liveEventName,
liveOutputName,
resourceGroupName,
subscriptionId,
properties
)
SELECT 
'{{ accountName }}',
'{{ liveEventName }}',
'{{ liveOutputName }}',
'{{ resourceGroupName }}',
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
        - name: description
          value: string
        - name: assetName
          value: string
        - name: archiveWindowLength
          value: string
        - name: rewindWindowLength
          value: string
        - name: manifestName
          value: string
        - name: hls
          value:
            - name: fragmentsPerTsSegment
              value: integer
        - name: outputSnapTime
          value: integer
        - name: created
          value: string
        - name: lastModified
          value: string
        - name: provisioningState
          value: string
        - name: resourceState
          value: string
    - name: systemData
      value:
        - name: createdBy
          value: string
        - name: createdByType
          value: string
        - name: createdAt
          value: string
        - name: lastModifiedBy
          value: string
        - name: lastModifiedByType
          value: string
        - name: lastModifiedAt
          value: string

```
</TabItem>
</Tabs>

## `DELETE` example

Deletes the specified <code>live_outputs</code> resource.

```sql
/*+ delete */
DELETE FROM azure.media_services.live_outputs
WHERE accountName = '{{ accountName }}'
AND liveEventName = '{{ liveEventName }}'
AND liveOutputName = '{{ liveOutputName }}'
AND resourceGroupName = '{{ resourceGroupName }}'
AND subscriptionId = '{{ subscriptionId }}';
```
