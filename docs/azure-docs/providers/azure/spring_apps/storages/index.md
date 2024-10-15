---
title: storages
hide_title: false
hide_table_of_contents: false
keywords:
  - storages
  - spring_apps
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

Creates, updates, deletes, gets or lists a <code>storages</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>storages</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.spring_apps.storages" /></td></tr>
</tbody></table>

## Fields
<Tabs
    defaultValue="view"
    values={[
        { label: 'vw_storages', value: 'view', },
        { label: 'storages', value: 'resource', },
    ]
}>
<TabItem value="view">

| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="resourceGroupName" /> | `text` | field from the `properties` object |
| <CopyableCode code="serviceName" /> | `text` | field from the `properties` object |
| <CopyableCode code="storageName" /> | `text` | field from the `properties` object |
| <CopyableCode code="storage_type" /> | `text` | field from the `properties` object |
| <CopyableCode code="subscriptionId" /> | `text` | field from the `properties` object |
</TabItem>
<TabItem value="resource">

| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="properties" /> | `object` | Storage resource payload. |
</TabItem></Tabs>

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="resourceGroupName, serviceName, storageName, subscriptionId" /> | Get the storage resource. |
| <CopyableCode code="list" /> | `SELECT` | <CopyableCode code="resourceGroupName, serviceName, subscriptionId" /> | List all the storages of one Azure Spring Apps resource. |
| <CopyableCode code="create_or_update" /> | `INSERT` | <CopyableCode code="resourceGroupName, serviceName, storageName, subscriptionId" /> | Create or update storage resource. |
| <CopyableCode code="delete" /> | `DELETE` | <CopyableCode code="resourceGroupName, serviceName, storageName, subscriptionId" /> | Delete the storage resource. |

## `SELECT` examples

List all the storages of one Azure Spring Apps resource.

<Tabs
    defaultValue="view"
    values={[
        { label: 'vw_storages', value: 'view', },
        { label: 'storages', value: 'resource', },
    ]
}>
<TabItem value="view">

```sql
SELECT
resourceGroupName,
serviceName,
storageName,
storage_type,
subscriptionId
FROM azure.spring_apps.vw_storages
WHERE resourceGroupName = '{{ resourceGroupName }}'
AND serviceName = '{{ serviceName }}'
AND subscriptionId = '{{ subscriptionId }}';
```
</TabItem>
<TabItem value="resource">


```sql
SELECT
properties
FROM azure.spring_apps.storages
WHERE resourceGroupName = '{{ resourceGroupName }}'
AND serviceName = '{{ serviceName }}'
AND subscriptionId = '{{ subscriptionId }}';
```
</TabItem></Tabs>


## `INSERT` example

Use the following StackQL query and manifest file to create a new <code>storages</code> resource.

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
INSERT INTO azure.spring_apps.storages (
resourceGroupName,
serviceName,
storageName,
subscriptionId,
properties
)
SELECT 
'{{ resourceGroupName }}',
'{{ serviceName }}',
'{{ storageName }}',
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
        - name: storageType
          value: string

```
</TabItem>
</Tabs>

## `DELETE` example

Deletes the specified <code>storages</code> resource.

```sql
/*+ delete */
DELETE FROM azure.spring_apps.storages
WHERE resourceGroupName = '{{ resourceGroupName }}'
AND serviceName = '{{ serviceName }}'
AND storageName = '{{ storageName }}'
AND subscriptionId = '{{ subscriptionId }}';
```
