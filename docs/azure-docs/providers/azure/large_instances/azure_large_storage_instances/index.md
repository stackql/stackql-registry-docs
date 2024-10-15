---
title: azure_large_storage_instances
hide_title: false
hide_table_of_contents: false
keywords:
  - azure_large_storage_instances
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

Creates, updates, deletes, gets or lists a <code>azure_large_storage_instances</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>azure_large_storage_instances</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.large_instances.azure_large_storage_instances" /></td></tr>
</tbody></table>

## Fields
<Tabs
    defaultValue="view"
    values={[
        { label: 'vw_azure_large_storage_instances', value: 'view', },
        { label: 'azure_large_storage_instances', value: 'resource', },
    ]
}>
<TabItem value="view">

| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="azureLargeStorageInstanceName" /> | `text` | field from the `properties` object |
| <CopyableCode code="azure_large_storage_instance_unique_identifier" /> | `text` | field from the `properties` object |
| <CopyableCode code="location" /> | `text` | The geo-location where the resource lives |
| <CopyableCode code="resourceGroupName" /> | `text` | field from the `properties` object |
| <CopyableCode code="storage_properties" /> | `text` | field from the `properties` object |
| <CopyableCode code="subscriptionId" /> | `text` | field from the `properties` object |
| <CopyableCode code="tags" /> | `text` | Resource tags. |
</TabItem>
<TabItem value="resource">

| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="location" /> | `string` | The geo-location where the resource lives |
| <CopyableCode code="properties" /> | `object` | Describes the properties of an AzureLargeStorageInstance. |
| <CopyableCode code="tags" /> | `object` | Resource tags. |
</TabItem></Tabs>

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="azureLargeStorageInstanceName, resourceGroupName, subscriptionId" /> | Gets an Azure Large Storage instance for the specified subscription, resource
group, and instance name. |
| <CopyableCode code="list_by_resource_group" /> | `SELECT` | <CopyableCode code="resourceGroupName, subscriptionId" /> | Gets a list of AzureLargeStorageInstances in the specified subscription and
resource group. The operations returns various properties of each Azure
LargeStorage instance. |
| <CopyableCode code="list_by_subscription" /> | `SELECT` | <CopyableCode code="subscriptionId" /> | Gets a list of AzureLargeStorageInstances in the specified subscription. The
operations returns various properties of each Azure LargeStorage instance. |
| <CopyableCode code="update" /> | `UPDATE` | <CopyableCode code="azureLargeStorageInstanceName, resourceGroupName, subscriptionId" /> | Patches the Tags field of a Azure Large Storage Instance for the specified
subscription, resource group, and instance name. |

## `SELECT` examples

Gets a list of AzureLargeStorageInstances in the specified subscription. The
operations returns various properties of each Azure LargeStorage instance.

<Tabs
    defaultValue="view"
    values={[
        { label: 'vw_azure_large_storage_instances', value: 'view', },
        { label: 'azure_large_storage_instances', value: 'resource', },
    ]
}>
<TabItem value="view">

```sql
SELECT
azureLargeStorageInstanceName,
azure_large_storage_instance_unique_identifier,
location,
resourceGroupName,
storage_properties,
subscriptionId,
tags
FROM azure.large_instances.vw_azure_large_storage_instances
WHERE subscriptionId = '{{ subscriptionId }}';
```
</TabItem>
<TabItem value="resource">


```sql
SELECT
location,
properties,
tags
FROM azure.large_instances.azure_large_storage_instances
WHERE subscriptionId = '{{ subscriptionId }}';
```
</TabItem></Tabs>


## `UPDATE` example

Updates a <code>azure_large_storage_instances</code> resource.

```sql
/*+ update */
UPDATE azure.large_instances.azure_large_storage_instances
SET 
tags = '{{ tags }}'
WHERE 
azureLargeStorageInstanceName = '{{ azureLargeStorageInstanceName }}'
AND resourceGroupName = '{{ resourceGroupName }}'
AND subscriptionId = '{{ subscriptionId }}';
```
