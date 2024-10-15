---
title: replicas
hide_title: false
hide_table_of_contents: false
keywords:
  - replicas
  - signalr
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

Creates, updates, deletes, gets or lists a <code>replicas</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>replicas</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.signalr.replicas" /></td></tr>
</tbody></table>

## Fields
<Tabs
    defaultValue="view"
    values={[
        { label: 'vw_replicas', value: 'view', },
        { label: 'replicas', value: 'resource', },
    ]
}>
<TabItem value="view">

| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="location" /> | `text` | The geo-location where the resource lives |
| <CopyableCode code="provisioning_state" /> | `text` | field from the `properties` object |
| <CopyableCode code="region_endpoint_enabled" /> | `text` | field from the `properties` object |
| <CopyableCode code="replicaName" /> | `text` | field from the `properties` object |
| <CopyableCode code="resourceGroupName" /> | `text` | field from the `properties` object |
| <CopyableCode code="resourceName" /> | `text` | field from the `properties` object |
| <CopyableCode code="resource_stopped" /> | `text` | field from the `properties` object |
| <CopyableCode code="sku" /> | `text` | The billing information of the resource. |
| <CopyableCode code="subscriptionId" /> | `text` | field from the `properties` object |
| <CopyableCode code="tags" /> | `text` | Resource tags. |
</TabItem>
<TabItem value="resource">

| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="location" /> | `string` | The geo-location where the resource lives |
| <CopyableCode code="properties" /> | `object` |  |
| <CopyableCode code="sku" /> | `object` | The billing information of the resource. |
| <CopyableCode code="tags" /> | `object` | Resource tags. |
</TabItem></Tabs>

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="replicaName, resourceGroupName, resourceName, subscriptionId" /> | Get the replica and its properties. |
| <CopyableCode code="list" /> | `SELECT` | <CopyableCode code="resourceGroupName, resourceName, subscriptionId" /> | List all replicas belong to this resource |
| <CopyableCode code="create_or_update" /> | `INSERT` | <CopyableCode code="replicaName, resourceGroupName, resourceName, subscriptionId" /> | Create or update a replica. |
| <CopyableCode code="delete" /> | `DELETE` | <CopyableCode code="replicaName, resourceGroupName, resourceName, subscriptionId" /> | Operation to delete a replica. |
| <CopyableCode code="update" /> | `UPDATE` | <CopyableCode code="replicaName, resourceGroupName, resourceName, subscriptionId" /> | Operation to update an exiting replica. |
| <CopyableCode code="restart" /> | `EXEC` | <CopyableCode code="replicaName, resourceGroupName, resourceName, subscriptionId" /> | Operation to restart a replica. |

## `SELECT` examples

List all replicas belong to this resource

<Tabs
    defaultValue="view"
    values={[
        { label: 'vw_replicas', value: 'view', },
        { label: 'replicas', value: 'resource', },
    ]
}>
<TabItem value="view">

```sql
SELECT
location,
provisioning_state,
region_endpoint_enabled,
replicaName,
resourceGroupName,
resourceName,
resource_stopped,
sku,
subscriptionId,
tags
FROM azure.signalr.vw_replicas
WHERE resourceGroupName = '{{ resourceGroupName }}'
AND resourceName = '{{ resourceName }}'
AND subscriptionId = '{{ subscriptionId }}';
```
</TabItem>
<TabItem value="resource">


```sql
SELECT
location,
properties,
sku,
tags
FROM azure.signalr.replicas
WHERE resourceGroupName = '{{ resourceGroupName }}'
AND resourceName = '{{ resourceName }}'
AND subscriptionId = '{{ subscriptionId }}';
```
</TabItem></Tabs>


## `INSERT` example

Use the following StackQL query and manifest file to create a new <code>replicas</code> resource.

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
INSERT INTO azure.signalr.replicas (
replicaName,
resourceGroupName,
resourceName,
subscriptionId,
tags,
location,
sku,
properties
)
SELECT 
'{{ replicaName }}',
'{{ resourceGroupName }}',
'{{ resourceName }}',
'{{ subscriptionId }}',
'{{ tags }}',
'{{ location }}',
'{{ sku }}',
'{{ properties }}'
;
```
</TabItem>
<TabItem value="manifest">

```yaml
- name: your_resource_model_name
  props:
    - name: tags
      value: object
    - name: location
      value: string
    - name: sku
      value:
        - name: name
          value: string
        - name: tier
          value: []
        - name: size
          value: string
        - name: family
          value: string
        - name: capacity
          value: integer
    - name: properties
      value:
        - name: provisioningState
          value: []
        - name: regionEndpointEnabled
          value: string
        - name: resourceStopped
          value: string

```
</TabItem>
</Tabs>

## `UPDATE` example

Updates a <code>replicas</code> resource.

```sql
/*+ update */
UPDATE azure.signalr.replicas
SET 
tags = '{{ tags }}',
location = '{{ location }}',
sku = '{{ sku }}',
properties = '{{ properties }}'
WHERE 
replicaName = '{{ replicaName }}'
AND resourceGroupName = '{{ resourceGroupName }}'
AND resourceName = '{{ resourceName }}'
AND subscriptionId = '{{ subscriptionId }}';
```

## `DELETE` example

Deletes the specified <code>replicas</code> resource.

```sql
/*+ delete */
DELETE FROM azure.signalr.replicas
WHERE replicaName = '{{ replicaName }}'
AND resourceGroupName = '{{ resourceGroupName }}'
AND resourceName = '{{ resourceName }}'
AND subscriptionId = '{{ subscriptionId }}';
```
