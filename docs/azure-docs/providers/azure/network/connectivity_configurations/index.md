---
title: connectivity_configurations
hide_title: false
hide_table_of_contents: false
keywords:
  - connectivity_configurations
  - network
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

Creates, updates, deletes, gets or lists a <code>connectivity_configurations</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>connectivity_configurations</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.network.connectivity_configurations" /></td></tr>
</tbody></table>

## Fields
<Tabs
    defaultValue="view"
    values={[
        { label: 'vw_connectivity_configurations', value: 'view', },
        { label: 'connectivity_configurations', value: 'resource', },
    ]
}>
<TabItem value="view">

| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="id" /> | `text` | Resource ID. |
| <CopyableCode code="name" /> | `text` | Resource name. |
| <CopyableCode code="description" /> | `text` | field from the `properties` object |
| <CopyableCode code="applies_to_groups" /> | `text` | field from the `properties` object |
| <CopyableCode code="configurationName" /> | `text` | field from the `properties` object |
| <CopyableCode code="connectivity_topology" /> | `text` | field from the `properties` object |
| <CopyableCode code="delete_existing_peering" /> | `text` | field from the `properties` object |
| <CopyableCode code="etag" /> | `text` | A unique read-only string that changes whenever the resource is updated. |
| <CopyableCode code="hubs" /> | `text` | field from the `properties` object |
| <CopyableCode code="is_global" /> | `text` | field from the `properties` object |
| <CopyableCode code="networkManagerName" /> | `text` | field from the `properties` object |
| <CopyableCode code="provisioning_state" /> | `text` | field from the `properties` object |
| <CopyableCode code="resourceGroupName" /> | `text` | field from the `properties` object |
| <CopyableCode code="resource_guid" /> | `text` | field from the `properties` object |
| <CopyableCode code="subscriptionId" /> | `text` | field from the `properties` object |
| <CopyableCode code="system_data" /> | `text` | field from the `properties` object |
| <CopyableCode code="type" /> | `text` | Resource type. |
</TabItem>
<TabItem value="resource">

| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="id" /> | `string` | Resource ID. |
| <CopyableCode code="name" /> | `string` | Resource name. |
| <CopyableCode code="etag" /> | `string` | A unique read-only string that changes whenever the resource is updated. |
| <CopyableCode code="properties" /> | `object` | Properties of network manager connectivity configuration |
| <CopyableCode code="systemData" /> | `object` | Metadata pertaining to creation and last modification of the resource. |
| <CopyableCode code="type" /> | `string` | Resource type. |
</TabItem></Tabs>

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="configurationName, networkManagerName, resourceGroupName, subscriptionId" /> | Gets a Network Connectivity Configuration, specified by the resource group, network manager name, and connectivity Configuration name |
| <CopyableCode code="list" /> | `SELECT` | <CopyableCode code="networkManagerName, resourceGroupName, subscriptionId" /> | Lists all the network manager connectivity configuration in a specified network manager. |
| <CopyableCode code="create_or_update" /> | `INSERT` | <CopyableCode code="configurationName, networkManagerName, resourceGroupName, subscriptionId" /> | Creates/Updates a new network manager connectivity configuration |
| <CopyableCode code="delete" /> | `DELETE` | <CopyableCode code="configurationName, networkManagerName, resourceGroupName, subscriptionId" /> | Deletes a network manager connectivity configuration, specified by the resource group, network manager name, and connectivity configuration name |

## `SELECT` examples

Lists all the network manager connectivity configuration in a specified network manager.

<Tabs
    defaultValue="view"
    values={[
        { label: 'vw_connectivity_configurations', value: 'view', },
        { label: 'connectivity_configurations', value: 'resource', },
    ]
}>
<TabItem value="view">

```sql
SELECT
id,
name,
description,
applies_to_groups,
configurationName,
connectivity_topology,
delete_existing_peering,
etag,
hubs,
is_global,
networkManagerName,
provisioning_state,
resourceGroupName,
resource_guid,
subscriptionId,
system_data,
type
FROM azure.network.vw_connectivity_configurations
WHERE networkManagerName = '{{ networkManagerName }}'
AND resourceGroupName = '{{ resourceGroupName }}'
AND subscriptionId = '{{ subscriptionId }}';
```
</TabItem>
<TabItem value="resource">


```sql
SELECT
id,
name,
etag,
properties,
systemData,
type
FROM azure.network.connectivity_configurations
WHERE networkManagerName = '{{ networkManagerName }}'
AND resourceGroupName = '{{ resourceGroupName }}'
AND subscriptionId = '{{ subscriptionId }}';
```
</TabItem></Tabs>


## `INSERT` example

Use the following StackQL query and manifest file to create a new <code>connectivity_configurations</code> resource.

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
INSERT INTO azure.network.connectivity_configurations (
configurationName,
networkManagerName,
resourceGroupName,
subscriptionId,
properties
)
SELECT 
'{{ configurationName }}',
'{{ networkManagerName }}',
'{{ resourceGroupName }}',
'{{ subscriptionId }}',
'{{ properties }}'
;
```
</TabItem>
<TabItem value="manifest">

```yaml
- name: your_resource_model_name
  props:
    - name: properties
      value:
        - name: description
          value: string
        - name: connectivityTopology
          value: string
        - name: hubs
          value:
            - - name: resourceId
                value: string
              - name: resourceType
                value: string
        - name: isGlobal
          value: string
        - name: appliesToGroups
          value:
            - - name: networkGroupId
                value: string
              - name: useHubGateway
                value: string
              - name: isGlobal
                value: string
              - name: groupConnectivity
                value: string
        - name: provisioningState
          value: []
        - name: deleteExistingPeering
          value: string
        - name: resourceGuid
          value: string
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
    - name: id
      value: string
    - name: name
      value: string
    - name: type
      value: string
    - name: etag
      value: string

```
</TabItem>
</Tabs>

## `DELETE` example

Deletes the specified <code>connectivity_configurations</code> resource.

```sql
/*+ delete */
DELETE FROM azure.network.connectivity_configurations
WHERE configurationName = '{{ configurationName }}'
AND networkManagerName = '{{ networkManagerName }}'
AND resourceGroupName = '{{ resourceGroupName }}'
AND subscriptionId = '{{ subscriptionId }}';
```
