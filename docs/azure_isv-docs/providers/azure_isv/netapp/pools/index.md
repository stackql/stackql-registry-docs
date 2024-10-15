---
title: pools
hide_title: false
hide_table_of_contents: false
keywords:
  - pools
  - netapp
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

Creates, updates, deletes, gets or lists a <code>pools</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>pools</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure_isv.netapp.pools" /></td></tr>
</tbody></table>

## Fields
<Tabs
    defaultValue="view"
    values={[
        { label: 'vw_pools', value: 'view', },
        { label: 'pools', value: 'resource', },
    ]
}>
<TabItem value="view">

| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="accountName" /> | `text` | field from the `properties` object |
| <CopyableCode code="cool_access" /> | `text` | field from the `properties` object |
| <CopyableCode code="encryption_type" /> | `text` | field from the `properties` object |
| <CopyableCode code="etag" /> | `text` | A unique read-only string that changes whenever the resource is updated. |
| <CopyableCode code="location" /> | `text` | The geo-location where the resource lives |
| <CopyableCode code="poolName" /> | `text` | field from the `properties` object |
| <CopyableCode code="pool_id" /> | `text` | field from the `properties` object |
| <CopyableCode code="provisioning_state" /> | `text` | field from the `properties` object |
| <CopyableCode code="qos_type" /> | `text` | field from the `properties` object |
| <CopyableCode code="resourceGroupName" /> | `text` | field from the `properties` object |
| <CopyableCode code="service_level" /> | `text` | field from the `properties` object |
| <CopyableCode code="size" /> | `text` | field from the `properties` object |
| <CopyableCode code="subscriptionId" /> | `text` | field from the `properties` object |
| <CopyableCode code="tags" /> | `text` | Resource tags. |
| <CopyableCode code="total_throughput_mibps" /> | `text` | field from the `properties` object |
| <CopyableCode code="utilized_throughput_mibps" /> | `text` | field from the `properties` object |
</TabItem>
<TabItem value="resource">

| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="etag" /> | `string` | A unique read-only string that changes whenever the resource is updated. |
| <CopyableCode code="location" /> | `string` | The geo-location where the resource lives |
| <CopyableCode code="properties" /> | `object` | Pool properties |
| <CopyableCode code="tags" /> | `object` | Resource tags. |
</TabItem></Tabs>

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="accountName, poolName, resourceGroupName, subscriptionId" /> | Get details of the specified capacity pool |
| <CopyableCode code="list" /> | `SELECT` | <CopyableCode code="accountName, resourceGroupName, subscriptionId" /> | List all capacity pools in the NetApp Account |
| <CopyableCode code="create_or_update" /> | `INSERT` | <CopyableCode code="accountName, poolName, resourceGroupName, subscriptionId, data__location, data__properties" /> | Create or Update a capacity pool |
| <CopyableCode code="delete" /> | `DELETE` | <CopyableCode code="accountName, poolName, resourceGroupName, subscriptionId" /> | Delete the specified capacity pool |
| <CopyableCode code="update" /> | `UPDATE` | <CopyableCode code="accountName, poolName, resourceGroupName, subscriptionId" /> | Patch the specified capacity pool |

## `SELECT` examples

List all capacity pools in the NetApp Account

<Tabs
    defaultValue="view"
    values={[
        { label: 'vw_pools', value: 'view', },
        { label: 'pools', value: 'resource', },
    ]
}>
<TabItem value="view">

```sql
SELECT
accountName,
cool_access,
encryption_type,
etag,
location,
poolName,
pool_id,
provisioning_state,
qos_type,
resourceGroupName,
service_level,
size,
subscriptionId,
tags,
total_throughput_mibps,
utilized_throughput_mibps
FROM azure_isv.netapp.vw_pools
WHERE accountName = '{{ accountName }}'
AND resourceGroupName = '{{ resourceGroupName }}'
AND subscriptionId = '{{ subscriptionId }}';
```
</TabItem>
<TabItem value="resource">


```sql
SELECT
etag,
location,
properties,
tags
FROM azure_isv.netapp.pools
WHERE accountName = '{{ accountName }}'
AND resourceGroupName = '{{ resourceGroupName }}'
AND subscriptionId = '{{ subscriptionId }}';
```
</TabItem></Tabs>


## `INSERT` example

Use the following StackQL query and manifest file to create a new <code>pools</code> resource.

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
INSERT INTO azure_isv.netapp.pools (
accountName,
poolName,
resourceGroupName,
subscriptionId,
data__location,
data__properties,
tags,
location,
properties
)
SELECT 
'{{ accountName }}',
'{{ poolName }}',
'{{ resourceGroupName }}',
'{{ subscriptionId }}',
'{{ data__location }}',
'{{ data__properties }}',
'{{ tags }}',
'{{ location }}',
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
    - name: etag
      value: string
    - name: properties
      value:
        - name: poolId
          value: string
        - name: size
          value: integer
        - name: serviceLevel
          value: []
        - name: provisioningState
          value: string
        - name: totalThroughputMibps
          value: number
        - name: utilizedThroughputMibps
          value: number
        - name: qosType
          value: string
        - name: coolAccess
          value: boolean
        - name: encryptionType
          value: string

```
</TabItem>
</Tabs>

## `UPDATE` example

Updates a <code>pools</code> resource.

```sql
/*+ update */
UPDATE azure_isv.netapp.pools
SET 
location = '{{ location }}',
tags = '{{ tags }}',
properties = '{{ properties }}'
WHERE 
accountName = '{{ accountName }}'
AND poolName = '{{ poolName }}'
AND resourceGroupName = '{{ resourceGroupName }}'
AND subscriptionId = '{{ subscriptionId }}';
```

## `DELETE` example

Deletes the specified <code>pools</code> resource.

```sql
/*+ delete */
DELETE FROM azure_isv.netapp.pools
WHERE accountName = '{{ accountName }}'
AND poolName = '{{ poolName }}'
AND resourceGroupName = '{{ resourceGroupName }}'
AND subscriptionId = '{{ subscriptionId }}';
```
