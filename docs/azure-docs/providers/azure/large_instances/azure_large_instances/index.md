---
title: azure_large_instances
hide_title: false
hide_table_of_contents: false
keywords:
  - azure_large_instances
  - large_instances
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

Creates, updates, deletes, gets or lists a <code>azure_large_instances</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>azure_large_instances</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.large_instances.azure_large_instances" /></td></tr>
</tbody></table>

## Fields
<Tabs
    defaultValue="view"
    values={[
        { label: 'vw_azure_large_instances', value: 'view', },
        { label: 'azure_large_instances', value: 'resource', },
    ]
}>
<TabItem value="view">

| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="azureLargeInstanceName" /> | `text` | field from the `properties` object |
| <CopyableCode code="azure_large_instance_id" /> | `text` | field from the `properties` object |
| <CopyableCode code="hardware_profile" /> | `text` | field from the `properties` object |
| <CopyableCode code="hw_revision" /> | `text` | field from the `properties` object |
| <CopyableCode code="location" /> | `text` | The geo-location where the resource lives |
| <CopyableCode code="network_profile" /> | `text` | field from the `properties` object |
| <CopyableCode code="os_profile" /> | `text` | field from the `properties` object |
| <CopyableCode code="partner_node_id" /> | `text` | field from the `properties` object |
| <CopyableCode code="power_state" /> | `text` | field from the `properties` object |
| <CopyableCode code="provisioning_state" /> | `text` | field from the `properties` object |
| <CopyableCode code="proximity_placement_group" /> | `text` | field from the `properties` object |
| <CopyableCode code="resourceGroupName" /> | `text` | field from the `properties` object |
| <CopyableCode code="storage_profile" /> | `text` | field from the `properties` object |
| <CopyableCode code="subscriptionId" /> | `text` | field from the `properties` object |
| <CopyableCode code="tags" /> | `text` | Resource tags. |
</TabItem>
<TabItem value="resource">

| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="location" /> | `string` | The geo-location where the resource lives |
| <CopyableCode code="properties" /> | `object` | Describes the properties of an Azure Large Instance. |
| <CopyableCode code="tags" /> | `object` | Resource tags. |
</TabItem></Tabs>

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="azureLargeInstanceName, resourceGroupName, subscriptionId" /> | Gets an Azure Large Instance for the specified subscription, resource group,
and instance name. |
| <CopyableCode code="list_by_resource_group" /> | `SELECT` | <CopyableCode code="resourceGroupName, subscriptionId" /> | Gets a list of Azure Large Instances in the specified subscription and resource
group. The operations returns various properties of each Azure Large Instance. |
| <CopyableCode code="list_by_subscription" /> | `SELECT` | <CopyableCode code="subscriptionId" /> | Gets a list of Azure Large Instances in the specified subscription. The
operations returns various properties of each Azure Large Instance. |
| <CopyableCode code="update" /> | `UPDATE` | <CopyableCode code="azureLargeInstanceName, resourceGroupName, subscriptionId" /> | Patches the Tags field of an Azure Large Instance for the specified
subscription, resource group, and instance name. |
| <CopyableCode code="restart" /> | `EXEC` | <CopyableCode code="azureLargeInstanceName, resourceGroupName, subscriptionId" /> | The operation to restart an Azure Large Instance (only for compute instances) |
| <CopyableCode code="shutdown" /> | `EXEC` | <CopyableCode code="azureLargeInstanceName, resourceGroupName, subscriptionId" /> | The operation to shutdown an Azure Large Instance (only for compute instances) |
| <CopyableCode code="start" /> | `EXEC` | <CopyableCode code="azureLargeInstanceName, resourceGroupName, subscriptionId" /> | The operation to start an Azure Large Instance (only for compute instances) |

## `SELECT` examples

Gets a list of Azure Large Instances in the specified subscription. The
operations returns various properties of each Azure Large Instance.

<Tabs
    defaultValue="view"
    values={[
        { label: 'vw_azure_large_instances', value: 'view', },
        { label: 'azure_large_instances', value: 'resource', },
    ]
}>
<TabItem value="view">

```sql
SELECT
azureLargeInstanceName,
azure_large_instance_id,
hardware_profile,
hw_revision,
location,
network_profile,
os_profile,
partner_node_id,
power_state,
provisioning_state,
proximity_placement_group,
resourceGroupName,
storage_profile,
subscriptionId,
tags
FROM azure.large_instances.vw_azure_large_instances
WHERE subscriptionId = '{{ subscriptionId }}';
```
</TabItem>
<TabItem value="resource">


```sql
SELECT
location,
properties,
tags
FROM azure.large_instances.azure_large_instances
WHERE subscriptionId = '{{ subscriptionId }}';
```
</TabItem></Tabs>


## `UPDATE` example

Updates a <code>azure_large_instances</code> resource.

```sql
/*+ update */
UPDATE azure.large_instances.azure_large_instances
SET 
tags = '{{ tags }}'
WHERE 
azureLargeInstanceName = '{{ azureLargeInstanceName }}'
AND resourceGroupName = '{{ resourceGroupName }}'
AND subscriptionId = '{{ subscriptionId }}';
```
