---
title: groups
hide_title: false
hide_table_of_contents: false
keywords:
  - groups
  - managed_network
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

Creates, updates, deletes, gets or lists a <code>groups</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>groups</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.managed_network.groups" /></td></tr>
</tbody></table>

## Fields
<Tabs
    defaultValue="view"
    values={[
        { label: 'vw_groups', value: 'view', },
        { label: 'groups', value: 'resource', },
    ]
}>
<TabItem value="view">

| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="etag" /> | `text` | field from the `properties` object |
| <CopyableCode code="kind" /> | `text` | Responsibility role under which this Managed Network Group will be created |
| <CopyableCode code="managedNetworkGroupName" /> | `text` | field from the `properties` object |
| <CopyableCode code="managedNetworkName" /> | `text` | field from the `properties` object |
| <CopyableCode code="management_groups" /> | `text` | field from the `properties` object |
| <CopyableCode code="provisioning_state" /> | `text` | field from the `properties` object |
| <CopyableCode code="resourceGroupName" /> | `text` | field from the `properties` object |
| <CopyableCode code="subnets" /> | `text` | field from the `properties` object |
| <CopyableCode code="subscriptionId" /> | `text` | field from the `properties` object |
| <CopyableCode code="subscriptions" /> | `text` | field from the `properties` object |
| <CopyableCode code="virtual_networks" /> | `text` | field from the `properties` object |
</TabItem>
<TabItem value="resource">

| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="kind" /> | `string` | Responsibility role under which this Managed Network Group will be created |
| <CopyableCode code="properties" /> | `object` | Properties of a Managed Network Group |
</TabItem></Tabs>

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="managedNetworkGroupName, managedNetworkName, resourceGroupName, subscriptionId" /> | The Get ManagedNetworkGroups operation gets a Managed Network Group specified by the resource group, Managed Network name, and group name |
| <CopyableCode code="list_by_managed_network" /> | `SELECT` | <CopyableCode code="managedNetworkName, resourceGroupName, subscriptionId" /> | The ListByManagedNetwork ManagedNetworkGroup operation retrieves all the Managed Network Groups in a specified Managed Networks in a paginated format. |
| <CopyableCode code="create_or_update" /> | `INSERT` | <CopyableCode code="managedNetworkGroupName, managedNetworkName, resourceGroupName, subscriptionId" /> | The Put ManagedNetworkGroups operation creates or updates a Managed Network Group resource |
| <CopyableCode code="delete" /> | `DELETE` | <CopyableCode code="managedNetworkGroupName, managedNetworkName, resourceGroupName, subscriptionId" /> | The Delete ManagedNetworkGroups operation deletes a Managed Network Group specified by the resource group, Managed Network name, and group name |

## `SELECT` examples

The ListByManagedNetwork ManagedNetworkGroup operation retrieves all the Managed Network Groups in a specified Managed Networks in a paginated format.

<Tabs
    defaultValue="view"
    values={[
        { label: 'vw_groups', value: 'view', },
        { label: 'groups', value: 'resource', },
    ]
}>
<TabItem value="view">

```sql
SELECT
etag,
kind,
managedNetworkGroupName,
managedNetworkName,
management_groups,
provisioning_state,
resourceGroupName,
subnets,
subscriptionId,
subscriptions,
virtual_networks
FROM azure.managed_network.vw_groups
WHERE managedNetworkName = '{{ managedNetworkName }}'
AND resourceGroupName = '{{ resourceGroupName }}'
AND subscriptionId = '{{ subscriptionId }}';
```
</TabItem>
<TabItem value="resource">


```sql
SELECT
kind,
properties
FROM azure.managed_network.groups
WHERE managedNetworkName = '{{ managedNetworkName }}'
AND resourceGroupName = '{{ resourceGroupName }}'
AND subscriptionId = '{{ subscriptionId }}';
```
</TabItem></Tabs>


## `INSERT` example

Use the following StackQL query and manifest file to create a new <code>groups</code> resource.

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
INSERT INTO azure.managed_network.groups (
managedNetworkGroupName,
managedNetworkName,
resourceGroupName,
subscriptionId,
properties,
kind
)
SELECT 
'{{ managedNetworkGroupName }}',
'{{ managedNetworkName }}',
'{{ resourceGroupName }}',
'{{ subscriptionId }}',
'{{ properties }}',
'{{ kind }}'
;
```
</TabItem>
<TabItem value="manifest">

```yaml
- name: your_resource_model_name
  props:
    - name: properties
      value:
        - name: managementGroups
          value:
            - - name: id
                value: string
        - name: subscriptions
          value:
            - - name: id
                value: string
        - name: virtualNetworks
          value:
            - - name: id
                value: string
        - name: subnets
          value:
            - - name: id
                value: string
        - name: provisioningState
          value: string
        - name: etag
          value: string
    - name: kind
      value: string

```
</TabItem>
</Tabs>

## `DELETE` example

Deletes the specified <code>groups</code> resource.

```sql
/*+ delete */
DELETE FROM azure.managed_network.groups
WHERE managedNetworkGroupName = '{{ managedNetworkGroupName }}'
AND managedNetworkName = '{{ managedNetworkName }}'
AND resourceGroupName = '{{ resourceGroupName }}'
AND subscriptionId = '{{ subscriptionId }}';
```
