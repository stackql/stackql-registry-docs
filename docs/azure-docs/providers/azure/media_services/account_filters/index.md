---
title: account_filters
hide_title: false
hide_table_of_contents: false
keywords:
  - account_filters
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

Creates, updates, deletes, gets or lists a <code>account_filters</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>account_filters</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.media_services.account_filters" /></td></tr>
</tbody></table>

## Fields
<Tabs
    defaultValue="view"
    values={[
        { label: 'vw_account_filters', value: 'view', },
        { label: 'account_filters', value: 'resource', },
    ]
}>
<TabItem value="view">

| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="accountName" /> | `text` | field from the `properties` object |
| <CopyableCode code="filterName" /> | `text` | field from the `properties` object |
| <CopyableCode code="first_quality" /> | `text` | field from the `properties` object |
| <CopyableCode code="presentation_time_range" /> | `text` | field from the `properties` object |
| <CopyableCode code="resourceGroupName" /> | `text` | field from the `properties` object |
| <CopyableCode code="subscriptionId" /> | `text` | field from the `properties` object |
| <CopyableCode code="system_data" /> | `text` | field from the `properties` object |
| <CopyableCode code="tracks" /> | `text` | field from the `properties` object |
</TabItem>
<TabItem value="resource">

| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="properties" /> | `object` | The Media Filter properties. |
| <CopyableCode code="systemData" /> | `object` | Metadata pertaining to creation and last modification of the resource. |
</TabItem></Tabs>

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="accountName, filterName, resourceGroupName, subscriptionId" /> | Get the details of an Account Filter in the Media Services account. |
| <CopyableCode code="list" /> | `SELECT` | <CopyableCode code="accountName, resourceGroupName, subscriptionId" /> | List Account Filters in the Media Services account. |
| <CopyableCode code="create_or_update" /> | `INSERT` | <CopyableCode code="accountName, filterName, resourceGroupName, subscriptionId" /> | Creates or updates an Account Filter in the Media Services account. |
| <CopyableCode code="delete" /> | `DELETE` | <CopyableCode code="accountName, filterName, resourceGroupName, subscriptionId" /> | Deletes an Account Filter in the Media Services account. |
| <CopyableCode code="update" /> | `UPDATE` | <CopyableCode code="accountName, filterName, resourceGroupName, subscriptionId" /> | Updates an existing Account Filter in the Media Services account. |

## `SELECT` examples

List Account Filters in the Media Services account.

<Tabs
    defaultValue="view"
    values={[
        { label: 'vw_account_filters', value: 'view', },
        { label: 'account_filters', value: 'resource', },
    ]
}>
<TabItem value="view">

```sql
SELECT
accountName,
filterName,
first_quality,
presentation_time_range,
resourceGroupName,
subscriptionId,
system_data,
tracks
FROM azure.media_services.vw_account_filters
WHERE accountName = '{{ accountName }}'
AND resourceGroupName = '{{ resourceGroupName }}'
AND subscriptionId = '{{ subscriptionId }}';
```
</TabItem>
<TabItem value="resource">


```sql
SELECT
properties,
systemData
FROM azure.media_services.account_filters
WHERE accountName = '{{ accountName }}'
AND resourceGroupName = '{{ resourceGroupName }}'
AND subscriptionId = '{{ subscriptionId }}';
```
</TabItem></Tabs>


## `INSERT` example

Use the following StackQL query and manifest file to create a new <code>account_filters</code> resource.

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
INSERT INTO azure.media_services.account_filters (
accountName,
filterName,
resourceGroupName,
subscriptionId,
properties
)
SELECT 
'{{ accountName }}',
'{{ filterName }}',
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
        - name: presentationTimeRange
          value:
            - name: startTimestamp
              value: integer
            - name: endTimestamp
              value: integer
            - name: presentationWindowDuration
              value: integer
            - name: liveBackoffDuration
              value: integer
            - name: timescale
              value: integer
            - name: forceEndTimestamp
              value: boolean
        - name: firstQuality
          value:
            - name: bitrate
              value: integer
        - name: tracks
          value:
            - - name: trackSelections
                value:
                  - - name: property
                      value: string
                    - name: value
                      value: string
                    - name: operation
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

## `UPDATE` example

Updates a <code>account_filters</code> resource.

```sql
/*+ update */
UPDATE azure.media_services.account_filters
SET 
properties = '{{ properties }}'
WHERE 
accountName = '{{ accountName }}'
AND filterName = '{{ filterName }}'
AND resourceGroupName = '{{ resourceGroupName }}'
AND subscriptionId = '{{ subscriptionId }}';
```

## `DELETE` example

Deletes the specified <code>account_filters</code> resource.

```sql
/*+ delete */
DELETE FROM azure.media_services.account_filters
WHERE accountName = '{{ accountName }}'
AND filterName = '{{ filterName }}'
AND resourceGroupName = '{{ resourceGroupName }}'
AND subscriptionId = '{{ subscriptionId }}';
```
