---
title: elastic_pools
hide_title: false
hide_table_of_contents: false
keywords:
  - elastic_pools
  - sql
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

Creates, updates, deletes, gets or lists a <code>elastic_pools</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>elastic_pools</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.sql.elastic_pools" /></td></tr>
</tbody></table>

## Fields
<Tabs
    defaultValue="view"
    values={[
        { label: 'vw_elastic_pools', value: 'view', },
        { label: 'elastic_pools', value: 'resource', },
    ]
}>
<TabItem value="view">

| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="availability_zone" /> | `text` | field from the `properties` object |
| <CopyableCode code="creation_date" /> | `text` | field from the `properties` object |
| <CopyableCode code="elasticPoolName" /> | `text` | field from the `properties` object |
| <CopyableCode code="high_availability_replica_count" /> | `text` | field from the `properties` object |
| <CopyableCode code="kind" /> | `text` | Kind of elastic pool. This is metadata used for the Azure portal experience. |
| <CopyableCode code="license_type" /> | `text` | field from the `properties` object |
| <CopyableCode code="location" /> | `text` | Resource location. |
| <CopyableCode code="maintenance_configuration_id" /> | `text` | field from the `properties` object |
| <CopyableCode code="max_size_bytes" /> | `text` | field from the `properties` object |
| <CopyableCode code="min_capacity" /> | `text` | field from the `properties` object |
| <CopyableCode code="per_database_settings" /> | `text` | field from the `properties` object |
| <CopyableCode code="preferred_enclave_type" /> | `text` | field from the `properties` object |
| <CopyableCode code="resourceGroupName" /> | `text` | field from the `properties` object |
| <CopyableCode code="serverName" /> | `text` | field from the `properties` object |
| <CopyableCode code="sku" /> | `text` | An ARM Resource SKU. |
| <CopyableCode code="state" /> | `text` | field from the `properties` object |
| <CopyableCode code="subscriptionId" /> | `text` | field from the `properties` object |
| <CopyableCode code="tags" /> | `text` | Resource tags. |
| <CopyableCode code="zone_redundant" /> | `text` | field from the `properties` object |
</TabItem>
<TabItem value="resource">

| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="kind" /> | `string` | Kind of elastic pool. This is metadata used for the Azure portal experience. |
| <CopyableCode code="location" /> | `string` | Resource location. |
| <CopyableCode code="properties" /> | `object` | Properties of an elastic pool |
| <CopyableCode code="sku" /> | `object` | An ARM Resource SKU. |
| <CopyableCode code="tags" /> | `object` | Resource tags. |
</TabItem></Tabs>

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="elasticPoolName, resourceGroupName, serverName, subscriptionId" /> | Gets an elastic pool. |
| <CopyableCode code="list_by_server" /> | `SELECT` | <CopyableCode code="resourceGroupName, serverName, subscriptionId" /> | Gets all elastic pools in a server. |
| <CopyableCode code="create_or_update" /> | `INSERT` | <CopyableCode code="elasticPoolName, resourceGroupName, serverName, subscriptionId, data__location" /> | Creates or updates an elastic pool. |
| <CopyableCode code="delete" /> | `DELETE` | <CopyableCode code="elasticPoolName, resourceGroupName, serverName, subscriptionId" /> | Deletes an elastic pool. |
| <CopyableCode code="update" /> | `UPDATE` | <CopyableCode code="elasticPoolName, resourceGroupName, serverName, subscriptionId" /> | Updates an elastic pool. |
| <CopyableCode code="failover" /> | `EXEC` | <CopyableCode code="elasticPoolName, resourceGroupName, serverName, subscriptionId" /> | Failovers an elastic pool. |

## `SELECT` examples

Gets all elastic pools in a server.

<Tabs
    defaultValue="view"
    values={[
        { label: 'vw_elastic_pools', value: 'view', },
        { label: 'elastic_pools', value: 'resource', },
    ]
}>
<TabItem value="view">

```sql
SELECT
availability_zone,
creation_date,
elasticPoolName,
high_availability_replica_count,
kind,
license_type,
location,
maintenance_configuration_id,
max_size_bytes,
min_capacity,
per_database_settings,
preferred_enclave_type,
resourceGroupName,
serverName,
sku,
state,
subscriptionId,
tags,
zone_redundant
FROM azure.sql.vw_elastic_pools
WHERE resourceGroupName = '{{ resourceGroupName }}'
AND serverName = '{{ serverName }}'
AND subscriptionId = '{{ subscriptionId }}';
```
</TabItem>
<TabItem value="resource">


```sql
SELECT
kind,
location,
properties,
sku,
tags
FROM azure.sql.elastic_pools
WHERE resourceGroupName = '{{ resourceGroupName }}'
AND serverName = '{{ serverName }}'
AND subscriptionId = '{{ subscriptionId }}';
```
</TabItem></Tabs>


## `INSERT` example

Use the following StackQL query and manifest file to create a new <code>elastic_pools</code> resource.

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
INSERT INTO azure.sql.elastic_pools (
elasticPoolName,
resourceGroupName,
serverName,
subscriptionId,
data__location,
location,
tags,
sku,
properties
)
SELECT 
'{{ elasticPoolName }}',
'{{ resourceGroupName }}',
'{{ serverName }}',
'{{ subscriptionId }}',
'{{ data__location }}',
'{{ location }}',
'{{ tags }}',
'{{ sku }}',
'{{ properties }}'
;
```
</TabItem>
<TabItem value="manifest">

```yaml
- name: your_resource_model_name
  props:
    - name: location
      value: string
    - name: tags
      value: object
    - name: sku
      value:
        - name: name
          value: string
        - name: tier
          value: string
        - name: size
          value: string
        - name: family
          value: string
        - name: capacity
          value: integer
    - name: kind
      value: string
    - name: properties
      value:
        - name: state
          value: string
        - name: creationDate
          value: string
        - name: maxSizeBytes
          value: integer
        - name: minCapacity
          value: number
        - name: perDatabaseSettings
          value:
            - name: minCapacity
              value: number
            - name: maxCapacity
              value: number
        - name: zoneRedundant
          value: boolean
        - name: licenseType
          value: string
        - name: maintenanceConfigurationId
          value: string
        - name: highAvailabilityReplicaCount
          value: integer
        - name: preferredEnclaveType
          value: string
        - name: availabilityZone
          value: string

```
</TabItem>
</Tabs>

## `UPDATE` example

Updates a <code>elastic_pools</code> resource.

```sql
/*+ update */
UPDATE azure.sql.elastic_pools
SET 
sku = '{{ sku }}',
properties = '{{ properties }}',
tags = '{{ tags }}'
WHERE 
elasticPoolName = '{{ elasticPoolName }}'
AND resourceGroupName = '{{ resourceGroupName }}'
AND serverName = '{{ serverName }}'
AND subscriptionId = '{{ subscriptionId }}';
```

## `DELETE` example

Deletes the specified <code>elastic_pools</code> resource.

```sql
/*+ delete */
DELETE FROM azure.sql.elastic_pools
WHERE elasticPoolName = '{{ elasticPoolName }}'
AND resourceGroupName = '{{ resourceGroupName }}'
AND serverName = '{{ serverName }}'
AND subscriptionId = '{{ subscriptionId }}';
```
