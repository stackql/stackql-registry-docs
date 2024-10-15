---
title: azure_bare_metal_instances
hide_title: false
hide_table_of_contents: false
keywords:
  - azure_bare_metal_instances
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

Creates, updates, deletes, gets or lists a <code>azure_bare_metal_instances</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>azure_bare_metal_instances</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.bare_metal_infrastructure.azure_bare_metal_instances" /></td></tr>
</tbody></table>

## Fields
<Tabs
    defaultValue="view"
    values={[
        { label: 'vw_azure_bare_metal_instances', value: 'view', },
        { label: 'azure_bare_metal_instances', value: 'resource', },
    ]
}>
<TabItem value="view">

| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="azureBareMetalInstanceName" /> | `text` | field from the `properties` object |
| <CopyableCode code="azure_bare_metal_instance_id" /> | `text` | field from the `properties` object |
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
| <CopyableCode code="properties" /> | `object` | Describes the properties of an Azure Bare Metal Instance. |
| <CopyableCode code="tags" /> | `object` | Resource tags. |
</TabItem></Tabs>

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="azureBareMetalInstanceName, resourceGroupName, subscriptionId" /> | Gets an Azure Bare Metal Instance for the specified subscription, resource group, and instance name. |
| <CopyableCode code="list_by_resource_group" /> | `SELECT` | <CopyableCode code="resourceGroupName, subscriptionId" /> | Gets a list of Azure Bare Metal Instances in the specified subscription and resource group. The operations returns various properties of each Azure Bare Metal Instance. |
| <CopyableCode code="list_by_subscription" /> | `SELECT` | <CopyableCode code="subscriptionId" /> | Returns a list of Azure Bare Metal Instances in the specified subscription. The operations returns various properties of each Azure Bare Metal Instance. |
| <CopyableCode code="create" /> | `INSERT` | <CopyableCode code="azureBareMetalInstanceName, resourceGroupName, subscriptionId" /> | Creates an Azure Bare Metal Instance for the specified subscription, resource group, and instance name. |
| <CopyableCode code="delete" /> | `DELETE` | <CopyableCode code="azureBareMetalInstanceName, resourceGroupName, subscriptionId" /> | Deletes an Azure Bare Metal Instance for the specified subscription, resource group, and instance name. |
| <CopyableCode code="update" /> | `UPDATE` | <CopyableCode code="azureBareMetalInstanceName, resourceGroupName, subscriptionId" /> | Patches the Tags field of a Azure Bare Metal Instance for the specified subscription, resource group, and instance name. |
| <CopyableCode code="restart" /> | `EXEC` | <CopyableCode code="azureBareMetalInstanceName, resourceGroupName, subscriptionId" /> | The operation to restart an Azure Bare Metal Instance |
| <CopyableCode code="shutdown" /> | `EXEC` | <CopyableCode code="azureBareMetalInstanceName, resourceGroupName, subscriptionId" /> | The operation to shutdown an Azure Bare Metal Instance |
| <CopyableCode code="start" /> | `EXEC` | <CopyableCode code="azureBareMetalInstanceName, resourceGroupName, subscriptionId" /> | The operation to start an Azure Bare Metal instance |

## `SELECT` examples

Returns a list of Azure Bare Metal Instances in the specified subscription. The operations returns various properties of each Azure Bare Metal Instance.

<Tabs
    defaultValue="view"
    values={[
        { label: 'vw_azure_bare_metal_instances', value: 'view', },
        { label: 'azure_bare_metal_instances', value: 'resource', },
    ]
}>
<TabItem value="view">

```sql
SELECT
azureBareMetalInstanceName,
azure_bare_metal_instance_id,
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
FROM azure.bare_metal_infrastructure.vw_azure_bare_metal_instances
WHERE subscriptionId = '{{ subscriptionId }}';
```
</TabItem>
<TabItem value="resource">


```sql
SELECT
location,
properties,
tags
FROM azure.bare_metal_infrastructure.azure_bare_metal_instances
WHERE subscriptionId = '{{ subscriptionId }}';
```
</TabItem></Tabs>


## `INSERT` example

Use the following StackQL query and manifest file to create a new <code>azure_bare_metal_instances</code> resource.

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
INSERT INTO azure.bare_metal_infrastructure.azure_bare_metal_instances (
azureBareMetalInstanceName,
resourceGroupName,
subscriptionId,
properties,
tags,
location
)
SELECT 
'{{ azureBareMetalInstanceName }}',
'{{ resourceGroupName }}',
'{{ subscriptionId }}',
'{{ properties }}',
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
        - name: hardwareProfile
          value:
            - name: hardwareType
              value: string
            - name: azureBareMetalInstanceSize
              value: string
        - name: storageProfile
          value:
            - name: nfsIpAddress
              value: string
            - name: osDisks
              value:
                - - name: name
                    value: string
                  - name: diskSizeGB
                    value: integer
                  - name: lun
                    value: integer
        - name: osProfile
          value:
            - name: computerName
              value: string
            - name: osType
              value: string
            - name: version
              value: string
            - name: sshPublicKey
              value: string
        - name: networkProfile
          value:
            - name: networkInterfaces
              value:
                - - name: ipAddress
                    value: string
            - name: circuitId
              value: string
        - name: azureBareMetalInstanceId
          value: string
        - name: powerState
          value: string
        - name: proximityPlacementGroup
          value: string
        - name: hwRevision
          value: string
        - name: partnerNodeId
          value: string
        - name: provisioningState
          value: string
    - name: tags
      value: object
    - name: location
      value: string

```
</TabItem>
</Tabs>

## `UPDATE` example

Updates a <code>azure_bare_metal_instances</code> resource.

```sql
/*+ update */
UPDATE azure.bare_metal_infrastructure.azure_bare_metal_instances
SET 
tags = '{{ tags }}'
WHERE 
azureBareMetalInstanceName = '{{ azureBareMetalInstanceName }}'
AND resourceGroupName = '{{ resourceGroupName }}'
AND subscriptionId = '{{ subscriptionId }}';
```

## `DELETE` example

Deletes the specified <code>azure_bare_metal_instances</code> resource.

```sql
/*+ delete */
DELETE FROM azure.bare_metal_infrastructure.azure_bare_metal_instances
WHERE azureBareMetalInstanceName = '{{ azureBareMetalInstanceName }}'
AND resourceGroupName = '{{ resourceGroupName }}'
AND subscriptionId = '{{ subscriptionId }}';
```
