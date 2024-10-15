---
title: snapshots
hide_title: false
hide_table_of_contents: false
keywords:
  - snapshots
  - app_configuration
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

Creates, updates, deletes, gets or lists a <code>snapshots</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>snapshots</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.app_configuration.snapshots" /></td></tr>
</tbody></table>

## Fields
<Tabs
    defaultValue="view"
    values={[
        { label: 'vw_snapshots', value: 'view', },
        { label: 'snapshots', value: 'resource', },
    ]
}>
<TabItem value="view">

| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="id" /> | `text` | The resource ID. |
| <CopyableCode code="name" /> | `text` | The name of the snapshot. |
| <CopyableCode code="composition_type" /> | `text` | field from the `properties` object |
| <CopyableCode code="configStoreName" /> | `text` | field from the `properties` object |
| <CopyableCode code="created" /> | `text` | field from the `properties` object |
| <CopyableCode code="etag" /> | `text` | field from the `properties` object |
| <CopyableCode code="expires" /> | `text` | field from the `properties` object |
| <CopyableCode code="filters" /> | `text` | field from the `properties` object |
| <CopyableCode code="items_count" /> | `text` | field from the `properties` object |
| <CopyableCode code="provisioning_state" /> | `text` | field from the `properties` object |
| <CopyableCode code="resourceGroupName" /> | `text` | field from the `properties` object |
| <CopyableCode code="retention_period" /> | `text` | field from the `properties` object |
| <CopyableCode code="size" /> | `text` | field from the `properties` object |
| <CopyableCode code="snapshotName" /> | `text` | field from the `properties` object |
| <CopyableCode code="status" /> | `text` | field from the `properties` object |
| <CopyableCode code="subscriptionId" /> | `text` | field from the `properties` object |
| <CopyableCode code="tags" /> | `text` | field from the `properties` object |
| <CopyableCode code="type" /> | `text` | The type of the resource. |
</TabItem>
<TabItem value="resource">

| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="id" /> | `string` | The resource ID. |
| <CopyableCode code="name" /> | `string` | The name of the snapshot. |
| <CopyableCode code="properties" /> | `object` | All snapshot properties. |
| <CopyableCode code="type" /> | `string` | The type of the resource. |
</TabItem></Tabs>

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="configStoreName, resourceGroupName, snapshotName, subscriptionId" /> | Gets the properties of the specified snapshot. NOTE: This operation is intended for use in Azure Resource Manager (ARM) Template deployments. For all other scenarios involving App Configuration snapshots the data plane API should be used instead. |
| <CopyableCode code="create" /> | `INSERT` | <CopyableCode code="configStoreName, resourceGroupName, snapshotName, subscriptionId" /> | Creates a snapshot. NOTE: This operation is intended for use in Azure Resource Manager (ARM) Template deployments. For all other scenarios involving App Configuration snapshots the data plane API should be used instead. |

## `SELECT` examples

Gets the properties of the specified snapshot. NOTE: This operation is intended for use in Azure Resource Manager (ARM) Template deployments. For all other scenarios involving App Configuration snapshots the data plane API should be used instead.

<Tabs
    defaultValue="view"
    values={[
        { label: 'vw_snapshots', value: 'view', },
        { label: 'snapshots', value: 'resource', },
    ]
}>
<TabItem value="view">

```sql
SELECT
id,
name,
composition_type,
configStoreName,
created,
etag,
expires,
filters,
items_count,
provisioning_state,
resourceGroupName,
retention_period,
size,
snapshotName,
status,
subscriptionId,
tags,
type
FROM azure.app_configuration.vw_snapshots
WHERE configStoreName = '{{ configStoreName }}'
AND resourceGroupName = '{{ resourceGroupName }}'
AND snapshotName = '{{ snapshotName }}'
AND subscriptionId = '{{ subscriptionId }}';
```
</TabItem>
<TabItem value="resource">


```sql
SELECT
id,
name,
properties,
type
FROM azure.app_configuration.snapshots
WHERE configStoreName = '{{ configStoreName }}'
AND resourceGroupName = '{{ resourceGroupName }}'
AND snapshotName = '{{ snapshotName }}'
AND subscriptionId = '{{ subscriptionId }}';
```
</TabItem></Tabs>


## `INSERT` example

Use the following StackQL query and manifest file to create a new <code>snapshots</code> resource.

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
INSERT INTO azure.app_configuration.snapshots (
configStoreName,
resourceGroupName,
snapshotName,
subscriptionId,
properties
)
SELECT 
'{{ configStoreName }}',
'{{ resourceGroupName }}',
'{{ snapshotName }}',
'{{ subscriptionId }}',
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
    - name: properties
      value:
        - name: provisioningState
          value: string
        - name: status
          value: string
        - name: filters
          value:
            - - name: key
                value: string
              - name: label
                value: string
        - name: compositionType
          value: string
        - name: created
          value: string
        - name: expires
          value: string
        - name: retentionPeriod
          value: integer
        - name: size
          value: integer
        - name: itemsCount
          value: integer
        - name: tags
          value: object
        - name: etag
          value: string

```
</TabItem>
</Tabs>
