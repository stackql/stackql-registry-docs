---
title: endpoints
hide_title: false
hide_table_of_contents: false
keywords:
  - endpoints
  - storage_mover
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

Creates, updates, deletes, gets or lists a <code>endpoints</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>endpoints</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.storage_mover.endpoints" /></td></tr>
</tbody></table>

## Fields
<Tabs
    defaultValue="view"
    values={[
        { label: 'vw_endpoints', value: 'view', },
        { label: 'endpoints', value: 'resource', },
    ]
}>
<TabItem value="view">

| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="description" /> | `text` | field from the `properties` object |
| <CopyableCode code="endpointName" /> | `text` | field from the `properties` object |
| <CopyableCode code="endpoint_type" /> | `text` | field from the `properties` object |
| <CopyableCode code="provisioning_state" /> | `text` | field from the `properties` object |
| <CopyableCode code="resourceGroupName" /> | `text` | field from the `properties` object |
| <CopyableCode code="storageMoverName" /> | `text` | field from the `properties` object |
| <CopyableCode code="subscriptionId" /> | `text` | field from the `properties` object |
| <CopyableCode code="system_data" /> | `text` | field from the `properties` object |
</TabItem>
<TabItem value="resource">

| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="properties" /> | `object` | The resource specific properties for the Storage Mover resource. |
| <CopyableCode code="systemData" /> | `object` | Metadata pertaining to creation and last modification of the resource. |
</TabItem></Tabs>

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="endpointName, resourceGroupName, storageMoverName, subscriptionId" /> | Gets an Endpoint resource. |
| <CopyableCode code="list" /> | `SELECT` | <CopyableCode code="resourceGroupName, storageMoverName, subscriptionId" /> | Lists all Endpoints in a Storage Mover. |
| <CopyableCode code="create_or_update" /> | `INSERT` | <CopyableCode code="endpointName, resourceGroupName, storageMoverName, subscriptionId, data__properties" /> | Creates or updates an Endpoint resource, which represents a data transfer source or destination. |
| <CopyableCode code="delete" /> | `DELETE` | <CopyableCode code="endpointName, resourceGroupName, storageMoverName, subscriptionId" /> | Deletes an Endpoint resource. |
| <CopyableCode code="update" /> | `UPDATE` | <CopyableCode code="endpointName, resourceGroupName, storageMoverName, subscriptionId" /> | Updates properties for an Endpoint resource. Properties not specified in the request body will be unchanged. |

## `SELECT` examples

Lists all Endpoints in a Storage Mover.

<Tabs
    defaultValue="view"
    values={[
        { label: 'vw_endpoints', value: 'view', },
        { label: 'endpoints', value: 'resource', },
    ]
}>
<TabItem value="view">

```sql
SELECT
description,
endpointName,
endpoint_type,
provisioning_state,
resourceGroupName,
storageMoverName,
subscriptionId,
system_data
FROM azure.storage_mover.vw_endpoints
WHERE resourceGroupName = '{{ resourceGroupName }}'
AND storageMoverName = '{{ storageMoverName }}'
AND subscriptionId = '{{ subscriptionId }}';
```
</TabItem>
<TabItem value="resource">


```sql
SELECT
properties,
systemData
FROM azure.storage_mover.endpoints
WHERE resourceGroupName = '{{ resourceGroupName }}'
AND storageMoverName = '{{ storageMoverName }}'
AND subscriptionId = '{{ subscriptionId }}';
```
</TabItem></Tabs>


## `INSERT` example

Use the following StackQL query and manifest file to create a new <code>endpoints</code> resource.

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
INSERT INTO azure.storage_mover.endpoints (
endpointName,
resourceGroupName,
storageMoverName,
subscriptionId,
data__properties,
properties,
systemData
)
SELECT 
'{{ endpointName }}',
'{{ resourceGroupName }}',
'{{ storageMoverName }}',
'{{ subscriptionId }}',
'{{ data__properties }}',
'{{ properties }}',
'{{ systemData }}'
;
```
</TabItem>
<TabItem value="manifest">

```yaml
- name: your_resource_model_name
  props:
    - name: properties
      value:
        - name: endpointType
          value: []
        - name: description
          value: string
        - name: provisioningState
          value: []
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

Updates a <code>endpoints</code> resource.

```sql
/*+ update */
UPDATE azure.storage_mover.endpoints
SET 
properties = '{{ properties }}'
WHERE 
endpointName = '{{ endpointName }}'
AND resourceGroupName = '{{ resourceGroupName }}'
AND storageMoverName = '{{ storageMoverName }}'
AND subscriptionId = '{{ subscriptionId }}';
```

## `DELETE` example

Deletes the specified <code>endpoints</code> resource.

```sql
/*+ delete */
DELETE FROM azure.storage_mover.endpoints
WHERE endpointName = '{{ endpointName }}'
AND resourceGroupName = '{{ resourceGroupName }}'
AND storageMoverName = '{{ storageMoverName }}'
AND subscriptionId = '{{ subscriptionId }}';
```
