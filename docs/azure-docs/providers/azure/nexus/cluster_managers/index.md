---
title: cluster_managers
hide_title: false
hide_table_of_contents: false
keywords:
  - cluster_managers
  - nexus
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

Creates, updates, deletes, gets or lists a <code>cluster_managers</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>cluster_managers</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.nexus.cluster_managers" /></td></tr>
</tbody></table>

## Fields
<Tabs
    defaultValue="view"
    values={[
        { label: 'vw_cluster_managers', value: 'view', },
        { label: 'cluster_managers', value: 'resource', },
    ]
}>
<TabItem value="view">

| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="analytics_workspace_id" /> | `text` | field from the `properties` object |
| <CopyableCode code="availability_zones" /> | `text` | field from the `properties` object |
| <CopyableCode code="clusterManagerName" /> | `text` | field from the `properties` object |
| <CopyableCode code="cluster_versions" /> | `text` | field from the `properties` object |
| <CopyableCode code="detailed_status" /> | `text` | field from the `properties` object |
| <CopyableCode code="detailed_status_message" /> | `text` | field from the `properties` object |
| <CopyableCode code="fabric_controller_id" /> | `text` | field from the `properties` object |
| <CopyableCode code="identity" /> | `text` | Managed service identity (system assigned and/or user assigned identities) |
| <CopyableCode code="location" /> | `text` | The geo-location where the resource lives |
| <CopyableCode code="managed_resource_group_configuration" /> | `text` | field from the `properties` object |
| <CopyableCode code="manager_extended_location" /> | `text` | field from the `properties` object |
| <CopyableCode code="provisioning_state" /> | `text` | field from the `properties` object |
| <CopyableCode code="resourceGroupName" /> | `text` | field from the `properties` object |
| <CopyableCode code="subscriptionId" /> | `text` | field from the `properties` object |
| <CopyableCode code="tags" /> | `text` | Resource tags. |
| <CopyableCode code="vm_size" /> | `text` | field from the `properties` object |
</TabItem>
<TabItem value="resource">

| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="identity" /> | `object` | Managed service identity (system assigned and/or user assigned identities) |
| <CopyableCode code="location" /> | `string` | The geo-location where the resource lives |
| <CopyableCode code="properties" /> | `object` |  |
| <CopyableCode code="tags" /> | `object` | Resource tags. |
</TabItem></Tabs>

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="clusterManagerName, resourceGroupName, subscriptionId" /> | Get the properties of the provided cluster manager. |
| <CopyableCode code="list_by_resource_group" /> | `SELECT` | <CopyableCode code="resourceGroupName, subscriptionId" /> | Get a list of cluster managers in the provided resource group. |
| <CopyableCode code="list_by_subscription" /> | `SELECT` | <CopyableCode code="subscriptionId" /> | Get a list of cluster managers in the provided subscription. |
| <CopyableCode code="create_or_update" /> | `INSERT` | <CopyableCode code="clusterManagerName, resourceGroupName, subscriptionId, data__properties" /> | Create a new cluster manager or update properties of the cluster manager if it exists. |
| <CopyableCode code="delete" /> | `DELETE` | <CopyableCode code="clusterManagerName, resourceGroupName, subscriptionId" /> | Delete the provided cluster manager. |
| <CopyableCode code="update" /> | `UPDATE` | <CopyableCode code="clusterManagerName, resourceGroupName, subscriptionId" /> | Patch properties of the provided cluster manager, or update the tags assigned to the cluster manager. Properties and tag updates can be done independently. |

## `SELECT` examples

Get a list of cluster managers in the provided subscription.

<Tabs
    defaultValue="view"
    values={[
        { label: 'vw_cluster_managers', value: 'view', },
        { label: 'cluster_managers', value: 'resource', },
    ]
}>
<TabItem value="view">

```sql
SELECT
analytics_workspace_id,
availability_zones,
clusterManagerName,
cluster_versions,
detailed_status,
detailed_status_message,
fabric_controller_id,
identity,
location,
managed_resource_group_configuration,
manager_extended_location,
provisioning_state,
resourceGroupName,
subscriptionId,
tags,
vm_size
FROM azure.nexus.vw_cluster_managers
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
FROM azure.nexus.cluster_managers
WHERE subscriptionId = '{{ subscriptionId }}';
```
</TabItem></Tabs>


## `INSERT` example

Use the following StackQL query and manifest file to create a new <code>cluster_managers</code> resource.

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
INSERT INTO azure.nexus.cluster_managers (
clusterManagerName,
resourceGroupName,
subscriptionId,
data__properties,
identity,
properties,
tags,
location
)
SELECT 
'{{ clusterManagerName }}',
'{{ resourceGroupName }}',
'{{ subscriptionId }}',
'{{ data__properties }}',
'{{ identity }}',
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
    - name: identity
      value:
        - name: principalId
          value: string
        - name: tenantId
          value: string
        - name: type
          value: []
        - name: userAssignedIdentities
          value: []
    - name: properties
      value:
        - name: analyticsWorkspaceId
          value: string
        - name: availabilityZones
          value:
            - string
        - name: clusterVersions
          value:
            - - name: supportExpiryDate
                value: string
              - name: targetClusterVersion
                value: string
        - name: detailedStatus
          value: string
        - name: detailedStatusMessage
          value: string
        - name: fabricControllerId
          value: string
        - name: managedResourceGroupConfiguration
          value:
            - name: location
              value: string
            - name: name
              value: string
        - name: managerExtendedLocation
          value:
            - name: name
              value: string
            - name: type
              value: string
        - name: provisioningState
          value: string
        - name: vmSize
          value: string
    - name: tags
      value: object
    - name: location
      value: string

```
</TabItem>
</Tabs>

## `UPDATE` example

Updates a <code>cluster_managers</code> resource.

```sql
/*+ update */
UPDATE azure.nexus.cluster_managers
SET 
identity = '{{ identity }}',
tags = '{{ tags }}'
WHERE 
clusterManagerName = '{{ clusterManagerName }}'
AND resourceGroupName = '{{ resourceGroupName }}'
AND subscriptionId = '{{ subscriptionId }}';
```

## `DELETE` example

Deletes the specified <code>cluster_managers</code> resource.

```sql
/*+ delete */
DELETE FROM azure.nexus.cluster_managers
WHERE clusterManagerName = '{{ clusterManagerName }}'
AND resourceGroupName = '{{ resourceGroupName }}'
AND subscriptionId = '{{ subscriptionId }}';
```
