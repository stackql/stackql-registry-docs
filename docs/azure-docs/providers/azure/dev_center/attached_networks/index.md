---
title: attached_networks
hide_title: false
hide_table_of_contents: false
keywords:
  - attached_networks
  - dev_center
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

Creates, updates, deletes, gets or lists a <code>attached_networks</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>attached_networks</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.dev_center.attached_networks" /></td></tr>
</tbody></table>

## Fields
<Tabs
    defaultValue="view"
    values={[
        { label: 'vw_attached_networks', value: 'view', },
        { label: 'attached_networks', value: 'resource', },
    ]
}>
<TabItem value="view">

| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="id" /> | `text` | Fully qualified resource ID for the resource. E.g. "/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/{resourceProviderNamespace}/{resourceType}/{resourceName}" |
| <CopyableCode code="name" /> | `text` | The name of the resource |
| <CopyableCode code="attachedNetworkConnectionName" /> | `text` | field from the `properties` object |
| <CopyableCode code="devCenterName" /> | `text` | field from the `properties` object |
| <CopyableCode code="domain_join_type" /> | `text` | field from the `properties` object |
| <CopyableCode code="health_check_status" /> | `text` | field from the `properties` object |
| <CopyableCode code="network_connection_id" /> | `text` | field from the `properties` object |
| <CopyableCode code="network_connection_location" /> | `text` | field from the `properties` object |
| <CopyableCode code="projectName" /> | `text` | field from the `properties` object |
| <CopyableCode code="provisioning_state" /> | `text` | field from the `properties` object |
| <CopyableCode code="resourceGroupName" /> | `text` | field from the `properties` object |
| <CopyableCode code="subscriptionId" /> | `text` | field from the `properties` object |
| <CopyableCode code="system_data" /> | `text` | field from the `properties` object |
| <CopyableCode code="type" /> | `text` | The type of the resource. E.g. "Microsoft.Compute/virtualMachines" or "Microsoft.Storage/storageAccounts" |
</TabItem>
<TabItem value="resource">

| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="id" /> | `string` | Fully qualified resource ID for the resource. E.g. "/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/{resourceProviderNamespace}/{resourceType}/{resourceName}" |
| <CopyableCode code="name" /> | `string` | The name of the resource |
| <CopyableCode code="properties" /> | `object` | Properties of an attached NetworkConnection. |
| <CopyableCode code="systemData" /> | `object` | Metadata pertaining to creation and last modification of the resource. |
| <CopyableCode code="type" /> | `string` | The type of the resource. E.g. "Microsoft.Compute/virtualMachines" or "Microsoft.Storage/storageAccounts" |
</TabItem></Tabs>

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get_by_dev_center" /> | `SELECT` | <CopyableCode code="attachedNetworkConnectionName, devCenterName, resourceGroupName, subscriptionId" /> | Gets an attached NetworkConnection. |
| <CopyableCode code="get_by_project" /> | `SELECT` | <CopyableCode code="attachedNetworkConnectionName, projectName, resourceGroupName, subscriptionId" /> | Gets an attached NetworkConnection. |
| <CopyableCode code="list_by_dev_center" /> | `SELECT` | <CopyableCode code="devCenterName, resourceGroupName, subscriptionId" /> | Lists the attached NetworkConnections for a DevCenter. |
| <CopyableCode code="list_by_project" /> | `SELECT` | <CopyableCode code="projectName, resourceGroupName, subscriptionId" /> | Lists the attached NetworkConnections for a Project. |
| <CopyableCode code="create_or_update" /> | `INSERT` | <CopyableCode code="attachedNetworkConnectionName, devCenterName, resourceGroupName, subscriptionId" /> | Creates or updates an attached NetworkConnection. |
| <CopyableCode code="delete" /> | `DELETE` | <CopyableCode code="attachedNetworkConnectionName, devCenterName, resourceGroupName, subscriptionId" /> | Un-attach a NetworkConnection. |

## `SELECT` examples

Lists the attached NetworkConnections for a Project.

<Tabs
    defaultValue="view"
    values={[
        { label: 'vw_attached_networks', value: 'view', },
        { label: 'attached_networks', value: 'resource', },
    ]
}>
<TabItem value="view">

```sql
SELECT
id,
name,
attachedNetworkConnectionName,
devCenterName,
domain_join_type,
health_check_status,
network_connection_id,
network_connection_location,
projectName,
provisioning_state,
resourceGroupName,
subscriptionId,
system_data,
type
FROM azure.dev_center.vw_attached_networks
WHERE projectName = '{{ projectName }}'
AND resourceGroupName = '{{ resourceGroupName }}'
AND subscriptionId = '{{ subscriptionId }}';
```
</TabItem>
<TabItem value="resource">


```sql
SELECT
id,
name,
properties,
systemData,
type
FROM azure.dev_center.attached_networks
WHERE projectName = '{{ projectName }}'
AND resourceGroupName = '{{ resourceGroupName }}'
AND subscriptionId = '{{ subscriptionId }}';
```
</TabItem></Tabs>


## `INSERT` example

Use the following StackQL query and manifest file to create a new <code>attached_networks</code> resource.

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
INSERT INTO azure.dev_center.attached_networks (
attachedNetworkConnectionName,
devCenterName,
resourceGroupName,
subscriptionId,
properties
)
SELECT 
'{{ attachedNetworkConnectionName }}',
'{{ devCenterName }}',
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
    - name: id
      value: string
    - name: name
      value: string
    - name: type
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
    - name: properties
      value:
        - name: provisioningState
          value: []
        - name: networkConnectionId
          value: string
        - name: networkConnectionLocation
          value: string
        - name: healthCheckStatus
          value: []
        - name: domainJoinType
          value: []

```
</TabItem>
</Tabs>

## `DELETE` example

Deletes the specified <code>attached_networks</code> resource.

```sql
/*+ delete */
DELETE FROM azure.dev_center.attached_networks
WHERE attachedNetworkConnectionName = '{{ attachedNetworkConnectionName }}'
AND devCenterName = '{{ devCenterName }}'
AND resourceGroupName = '{{ resourceGroupName }}'
AND subscriptionId = '{{ subscriptionId }}';
```
