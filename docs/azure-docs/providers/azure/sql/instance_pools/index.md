---
title: instance_pools
hide_title: false
hide_table_of_contents: false
keywords:
  - instance_pools
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

Creates, updates, deletes, gets or lists a <code>instance_pools</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>instance_pools</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.sql.instance_pools" /></td></tr>
</tbody></table>

## Fields
<Tabs
    defaultValue="view"
    values={[
        { label: 'vw_instance_pools', value: 'view', },
        { label: 'instance_pools', value: 'resource', },
    ]
}>
<TabItem value="view">

| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="dns_zone" /> | `text` | field from the `properties` object |
| <CopyableCode code="instancePoolName" /> | `text` | field from the `properties` object |
| <CopyableCode code="license_type" /> | `text` | field from the `properties` object |
| <CopyableCode code="location" /> | `text` | Resource location. |
| <CopyableCode code="maintenance_configuration_id" /> | `text` | field from the `properties` object |
| <CopyableCode code="resourceGroupName" /> | `text` | field from the `properties` object |
| <CopyableCode code="sku" /> | `text` | An ARM Resource SKU. |
| <CopyableCode code="subnet_id" /> | `text` | field from the `properties` object |
| <CopyableCode code="subscriptionId" /> | `text` | field from the `properties` object |
| <CopyableCode code="tags" /> | `text` | Resource tags. |
| <CopyableCode code="v_cores" /> | `text` | field from the `properties` object |
</TabItem>
<TabItem value="resource">

| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="location" /> | `string` | Resource location. |
| <CopyableCode code="properties" /> | `object` | Properties of an instance pool. |
| <CopyableCode code="sku" /> | `object` | An ARM Resource SKU. |
| <CopyableCode code="tags" /> | `object` | Resource tags. |
</TabItem></Tabs>

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="instancePoolName, resourceGroupName, subscriptionId" /> | Gets an instance pool. |
| <CopyableCode code="list" /> | `SELECT` | <CopyableCode code="subscriptionId" /> | Gets a list of all instance pools in the subscription. |
| <CopyableCode code="list_by_resource_group" /> | `SELECT` | <CopyableCode code="resourceGroupName, subscriptionId" /> | Gets a list of instance pools in the resource group |
| <CopyableCode code="create_or_update" /> | `INSERT` | <CopyableCode code="instancePoolName, resourceGroupName, subscriptionId, data__location" /> | Creates or updates an instance pool. |
| <CopyableCode code="delete" /> | `DELETE` | <CopyableCode code="instancePoolName, resourceGroupName, subscriptionId" /> | Deletes an instance pool |
| <CopyableCode code="update" /> | `UPDATE` | <CopyableCode code="instancePoolName, resourceGroupName, subscriptionId" /> | Updates an instance pool. |

## `SELECT` examples

Gets a list of all instance pools in the subscription.

<Tabs
    defaultValue="view"
    values={[
        { label: 'vw_instance_pools', value: 'view', },
        { label: 'instance_pools', value: 'resource', },
    ]
}>
<TabItem value="view">

```sql
SELECT
dns_zone,
instancePoolName,
license_type,
location,
maintenance_configuration_id,
resourceGroupName,
sku,
subnet_id,
subscriptionId,
tags,
v_cores
FROM azure.sql.vw_instance_pools
WHERE subscriptionId = '{{ subscriptionId }}';
```
</TabItem>
<TabItem value="resource">


```sql
SELECT
location,
properties,
sku,
tags
FROM azure.sql.instance_pools
WHERE subscriptionId = '{{ subscriptionId }}';
```
</TabItem></Tabs>


## `INSERT` example

Use the following StackQL query and manifest file to create a new <code>instance_pools</code> resource.

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
INSERT INTO azure.sql.instance_pools (
instancePoolName,
resourceGroupName,
subscriptionId,
data__location,
location,
tags,
sku,
properties
)
SELECT 
'{{ instancePoolName }}',
'{{ resourceGroupName }}',
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
    - name: properties
      value:
        - name: subnetId
          value: string
        - name: vCores
          value: integer
        - name: licenseType
          value: string
        - name: dnsZone
          value: string
        - name: maintenanceConfigurationId
          value: string

```
</TabItem>
</Tabs>

## `UPDATE` example

Updates a <code>instance_pools</code> resource.

```sql
/*+ update */
UPDATE azure.sql.instance_pools
SET 
sku = '{{ sku }}',
properties = '{{ properties }}',
tags = '{{ tags }}'
WHERE 
instancePoolName = '{{ instancePoolName }}'
AND resourceGroupName = '{{ resourceGroupName }}'
AND subscriptionId = '{{ subscriptionId }}';
```

## `DELETE` example

Deletes the specified <code>instance_pools</code> resource.

```sql
/*+ delete */
DELETE FROM azure.sql.instance_pools
WHERE instancePoolName = '{{ instancePoolName }}'
AND resourceGroupName = '{{ resourceGroupName }}'
AND subscriptionId = '{{ subscriptionId }}';
```
