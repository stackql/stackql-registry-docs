---
title: dedicated_cloud_nodes
hide_title: false
hide_table_of_contents: false
keywords:
  - dedicated_cloud_nodes
  - vmware_cloud_simple
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

Creates, updates, deletes, gets or lists a <code>dedicated_cloud_nodes</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>dedicated_cloud_nodes</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure_isv.vmware_cloud_simple.dedicated_cloud_nodes" /></td></tr>
</tbody></table>

## Fields
<Tabs
    defaultValue="view"
    values={[
        { label: 'vw_dedicated_cloud_nodes', value: 'view', },
        { label: 'dedicated_cloud_nodes', value: 'resource', },
    ]
}>
<TabItem value="view">

| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="id" /> | `text` | /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/{resourceProviderNamespace}/dedicatedCloudNodes/{dedicatedCloudNodeName} |
| <CopyableCode code="name" /> | `text` | {dedicatedCloudNodeName} |
| <CopyableCode code="availability_zone_id" /> | `text` | field from the `properties` object |
| <CopyableCode code="availability_zone_name" /> | `text` | field from the `properties` object |
| <CopyableCode code="cloud_rack_name" /> | `text` | field from the `properties` object |
| <CopyableCode code="created" /> | `text` | field from the `properties` object |
| <CopyableCode code="dedicatedCloudNodeName" /> | `text` | field from the `properties` object |
| <CopyableCode code="location" /> | `text` | Azure region |
| <CopyableCode code="nodes_count" /> | `text` | field from the `properties` object |
| <CopyableCode code="placement_group_id" /> | `text` | field from the `properties` object |
| <CopyableCode code="placement_group_name" /> | `text` | field from the `properties` object |
| <CopyableCode code="private_cloud_id" /> | `text` | field from the `properties` object |
| <CopyableCode code="private_cloud_name" /> | `text` | field from the `properties` object |
| <CopyableCode code="provisioning_state" /> | `text` | field from the `properties` object |
| <CopyableCode code="purchase_id" /> | `text` | field from the `properties` object |
| <CopyableCode code="resourceGroupName" /> | `text` | field from the `properties` object |
| <CopyableCode code="sku" /> | `text` | The purchase SKU for CloudSimple paid resources |
| <CopyableCode code="sku_description" /> | `text` | field from the `properties` object |
| <CopyableCode code="status" /> | `text` | field from the `properties` object |
| <CopyableCode code="subscriptionId" /> | `text` | field from the `properties` object |
| <CopyableCode code="tags" /> | `text` | Tags model |
| <CopyableCode code="type" /> | `text` | {resourceProviderNamespace}/{resourceType} |
| <CopyableCode code="vmware_cluster_name" /> | `text` | field from the `properties` object |
</TabItem>
<TabItem value="resource">

| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="id" /> | `string` | /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/{resourceProviderNamespace}/dedicatedCloudNodes/{dedicatedCloudNodeName} |
| <CopyableCode code="name" /> | `string` | {dedicatedCloudNodeName} |
| <CopyableCode code="location" /> | `string` | Azure region |
| <CopyableCode code="properties" /> | `object` | Properties of dedicated cloud node |
| <CopyableCode code="sku" /> | `object` | The purchase SKU for CloudSimple paid resources |
| <CopyableCode code="tags" /> | `object` | Tags model |
| <CopyableCode code="type" /> | `string` | {resourceProviderNamespace}/{resourceType} |
</TabItem></Tabs>

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="dedicatedCloudNodeName, resourceGroupName, subscriptionId" /> | Returns dedicated cloud node |
| <CopyableCode code="list_by_resource_group" /> | `SELECT` | <CopyableCode code="resourceGroupName, subscriptionId" /> | Returns list of dedicate cloud nodes within resource group |
| <CopyableCode code="list_by_subscription" /> | `SELECT` | <CopyableCode code="subscriptionId" /> | Returns list of dedicate cloud nodes within subscription |
| <CopyableCode code="create_or_update" /> | `INSERT` | <CopyableCode code="Referer, dedicatedCloudNodeName, resourceGroupName, subscriptionId, data__location" /> | Returns dedicated cloud node by its name |
| <CopyableCode code="delete" /> | `DELETE` | <CopyableCode code="dedicatedCloudNodeName, resourceGroupName, subscriptionId" /> | Delete dedicated cloud node |
| <CopyableCode code="update" /> | `UPDATE` | <CopyableCode code="dedicatedCloudNodeName, resourceGroupName, subscriptionId" /> | Patches dedicated node properties |

## `SELECT` examples

Returns list of dedicate cloud nodes within subscription

<Tabs
    defaultValue="view"
    values={[
        { label: 'vw_dedicated_cloud_nodes', value: 'view', },
        { label: 'dedicated_cloud_nodes', value: 'resource', },
    ]
}>
<TabItem value="view">

```sql
SELECT
id,
name,
availability_zone_id,
availability_zone_name,
cloud_rack_name,
created,
dedicatedCloudNodeName,
location,
nodes_count,
placement_group_id,
placement_group_name,
private_cloud_id,
private_cloud_name,
provisioning_state,
purchase_id,
resourceGroupName,
sku,
sku_description,
status,
subscriptionId,
tags,
type,
vmware_cluster_name
FROM azure_isv.vmware_cloud_simple.vw_dedicated_cloud_nodes
WHERE subscriptionId = '{{ subscriptionId }}';
```
</TabItem>
<TabItem value="resource">


```sql
SELECT
id,
name,
location,
properties,
sku,
tags,
type
FROM azure_isv.vmware_cloud_simple.dedicated_cloud_nodes
WHERE subscriptionId = '{{ subscriptionId }}';
```
</TabItem></Tabs>


## `INSERT` example

Use the following StackQL query and manifest file to create a new <code>dedicated_cloud_nodes</code> resource.

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
INSERT INTO azure_isv.vmware_cloud_simple.dedicated_cloud_nodes (
Referer,
dedicatedCloudNodeName,
resourceGroupName,
subscriptionId,
data__location,
location,
properties,
sku,
tags
)
SELECT 
'{{ Referer }}',
'{{ dedicatedCloudNodeName }}',
'{{ resourceGroupName }}',
'{{ subscriptionId }}',
'{{ data__location }}',
'{{ location }}',
'{{ properties }}',
'{{ sku }}',
'{{ tags }}'
;
```
</TabItem>
<TabItem value="manifest">

```yaml
- name: your_resource_model_name
  props:
    - name: id
      value: string
    - name: location
      value: string
    - name: name
      value: string
    - name: properties
      value:
        - name: availabilityZoneId
          value: string
        - name: availabilityZoneName
          value: string
        - name: cloudRackName
          value: string
        - name: created
          value: string
        - name: nodesCount
          value: integer
        - name: placementGroupId
          value: string
        - name: placementGroupName
          value: string
        - name: privateCloudId
          value: string
        - name: privateCloudName
          value: string
        - name: provisioningState
          value: string
        - name: purchaseId
          value: string
        - name: skuDescription
          value:
            - name: id
              value: string
            - name: name
              value: string
        - name: status
          value: string
        - name: vmwareClusterName
          value: string
    - name: sku
      value:
        - name: capacity
          value: string
        - name: description
          value: string
        - name: family
          value: string
        - name: name
          value: string
        - name: tier
          value: string
    - name: tags
      value: []
    - name: type
      value: string

```
</TabItem>
</Tabs>

## `UPDATE` example

Updates a <code>dedicated_cloud_nodes</code> resource.

```sql
/*+ update */
UPDATE azure_isv.vmware_cloud_simple.dedicated_cloud_nodes
SET 
tags = '{{ tags }}'
WHERE 
dedicatedCloudNodeName = '{{ dedicatedCloudNodeName }}'
AND resourceGroupName = '{{ resourceGroupName }}'
AND subscriptionId = '{{ subscriptionId }}';
```

## `DELETE` example

Deletes the specified <code>dedicated_cloud_nodes</code> resource.

```sql
/*+ delete */
DELETE FROM azure_isv.vmware_cloud_simple.dedicated_cloud_nodes
WHERE dedicatedCloudNodeName = '{{ dedicatedCloudNodeName }}'
AND resourceGroupName = '{{ resourceGroupName }}'
AND subscriptionId = '{{ subscriptionId }}';
```
