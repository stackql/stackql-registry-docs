---
title: azure_bare_metal_storage_instances
hide_title: false
hide_table_of_contents: false
keywords:
  - azure_bare_metal_storage_instances
  - bare_metal_infrastructure
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

Creates, updates, deletes, gets or lists a <code>azure_bare_metal_storage_instances</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>azure_bare_metal_storage_instances</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.bare_metal_infrastructure.azure_bare_metal_storage_instances" /></td></tr>
</tbody></table>

## Fields
<Tabs
    defaultValue="view"
    values={[
        { label: 'vw_azure_bare_metal_storage_instances', value: 'view', },
        { label: 'azure_bare_metal_storage_instances', value: 'resource', },
    ]
}>
<TabItem value="view">

| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="azureBareMetalStorageInstanceName" /> | `text` | field from the `properties` object |
| <CopyableCode code="azure_bare_metal_storage_instance_unique_identifier" /> | `text` | field from the `properties` object |
| <CopyableCode code="identity" /> | `text` | Identity for Azure Bare Metal Storage Instance. |
| <CopyableCode code="location" /> | `text` | The geo-location where the resource lives |
| <CopyableCode code="resourceGroupName" /> | `text` | field from the `properties` object |
| <CopyableCode code="storage_properties" /> | `text` | field from the `properties` object |
| <CopyableCode code="subscriptionId" /> | `text` | field from the `properties` object |
| <CopyableCode code="tags" /> | `text` | Resource tags. |
</TabItem>
<TabItem value="resource">

| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="identity" /> | `object` | Identity for Azure Bare Metal Storage Instance. |
| <CopyableCode code="location" /> | `string` | The geo-location where the resource lives |
| <CopyableCode code="properties" /> | `object` | Describes the properties of an AzureBareMetalStorageInstance. |
| <CopyableCode code="tags" /> | `object` | Resource tags. |
</TabItem></Tabs>

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="azureBareMetalStorageInstanceName, resourceGroupName, subscriptionId" /> | Gets an Azure Bare Metal Storage instance for the specified subscription, resource group, and instance name. |
| <CopyableCode code="list_by_resource_group" /> | `SELECT` | <CopyableCode code="resourceGroupName, subscriptionId" /> | Gets a list of AzureBareMetalStorage instances in the specified subscription and resource group. The operations returns various properties of each Azure Bare Metal Instance. |
| <CopyableCode code="list_by_subscription" /> | `SELECT` | <CopyableCode code="subscriptionId" /> | Gets a list of AzureBareMetalStorage instances in the specified subscription. The operations returns various properties of each Azure Bare Metal Instance. |
| <CopyableCode code="create" /> | `INSERT` | <CopyableCode code="azureBareMetalStorageInstanceName, resourceGroupName, subscriptionId" /> | Creates an Azure Bare Metal Storage Instance for the specified subscription, resource group, and instance name. |
| <CopyableCode code="delete" /> | `DELETE` | <CopyableCode code="azureBareMetalStorageInstanceName, resourceGroupName, subscriptionId" /> | Deletes an Azure Bare Metal Storage Instance for the specified subscription, resource group, and instance name. |
| <CopyableCode code="update" /> | `UPDATE` | <CopyableCode code="azureBareMetalStorageInstanceName, resourceGroupName, subscriptionId" /> | Patches the Tags field of a Azure BareMetalStorage instance for the specified subscription, resource group, and instance name. |

## `SELECT` examples

Gets a list of AzureBareMetalStorage instances in the specified subscription. The operations returns various properties of each Azure Bare Metal Instance.

<Tabs
    defaultValue="view"
    values={[
        { label: 'vw_azure_bare_metal_storage_instances', value: 'view', },
        { label: 'azure_bare_metal_storage_instances', value: 'resource', },
    ]
}>
<TabItem value="view">

```sql
SELECT
azureBareMetalStorageInstanceName,
azure_bare_metal_storage_instance_unique_identifier,
identity,
location,
resourceGroupName,
storage_properties,
subscriptionId,
tags
FROM azure.bare_metal_infrastructure.vw_azure_bare_metal_storage_instances
WHERE subscriptionId = '{{ subscriptionId }}';
```
</TabItem>
<TabItem value="resource">


```sql
SELECT
identity,
location,
properties,
tags
FROM azure.bare_metal_infrastructure.azure_bare_metal_storage_instances
WHERE subscriptionId = '{{ subscriptionId }}';
```
</TabItem></Tabs>


## `INSERT` example

Use the following StackQL query and manifest file to create a new <code>azure_bare_metal_storage_instances</code> resource.

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
INSERT INTO azure.bare_metal_infrastructure.azure_bare_metal_storage_instances (
azureBareMetalStorageInstanceName,
resourceGroupName,
subscriptionId,
properties,
identity,
tags,
location
)
SELECT 
'{{ azureBareMetalStorageInstanceName }}',
'{{ resourceGroupName }}',
'{{ subscriptionId }}',
'{{ properties }}',
'{{ identity }}',
'{{ tags }}',
'{{ location }}'
;
```
</TabItem>
<TabItem value="manifest">

```yaml
- name: your_resource_model_name
  props:
    - name: properties
      value:
        - name: azureBareMetalStorageInstanceUniqueIdentifier
          value: string
        - name: storageProperties
          value:
            - name: provisioningState
              value: string
            - name: offeringType
              value: string
            - name: storageType
              value: string
            - name: generation
              value: string
            - name: hardwareType
              value: string
            - name: workloadType
              value: string
            - name: storageBillingProperties
              value:
                - name: billingMode
                  value: string
                - name: azureBareMetalStorageInstanceSize
                  value: string
    - name: identity
      value:
        - name: principalId
          value: string
        - name: tenantId
          value: string
        - name: type
          value: string
    - name: tags
      value: object
    - name: location
      value: string

```
</TabItem>
</Tabs>

## `UPDATE` example

Updates a <code>azure_bare_metal_storage_instances</code> resource.

```sql
/*+ update */
UPDATE azure.bare_metal_infrastructure.azure_bare_metal_storage_instances
SET 
identity = '{{ identity }}',
tags = '{{ tags }}'
WHERE 
azureBareMetalStorageInstanceName = '{{ azureBareMetalStorageInstanceName }}'
AND resourceGroupName = '{{ resourceGroupName }}'
AND subscriptionId = '{{ subscriptionId }}';
```

## `DELETE` example

Deletes the specified <code>azure_bare_metal_storage_instances</code> resource.

```sql
/*+ delete */
DELETE FROM azure.bare_metal_infrastructure.azure_bare_metal_storage_instances
WHERE azureBareMetalStorageInstanceName = '{{ azureBareMetalStorageInstanceName }}'
AND resourceGroupName = '{{ resourceGroupName }}'
AND subscriptionId = '{{ subscriptionId }}';
```
