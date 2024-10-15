---
title: peering_policies
hide_title: false
hide_table_of_contents: false
keywords:
  - peering_policies
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

Creates, updates, deletes, gets or lists a <code>peering_policies</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>peering_policies</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.managed_network.peering_policies" /></td></tr>
</tbody></table>

## Fields
<Tabs
    defaultValue="view"
    values={[
        { label: 'vw_peering_policies', value: 'view', },
        { label: 'peering_policies', value: 'resource', },
    ]
}>
<TabItem value="view">

| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="etag" /> | `text` | field from the `properties` object |
| <CopyableCode code="hub" /> | `text` | field from the `properties` object |
| <CopyableCode code="managedNetworkName" /> | `text` | field from the `properties` object |
| <CopyableCode code="managedNetworkPeeringPolicyName" /> | `text` | field from the `properties` object |
| <CopyableCode code="mesh" /> | `text` | field from the `properties` object |
| <CopyableCode code="provisioning_state" /> | `text` | field from the `properties` object |
| <CopyableCode code="resourceGroupName" /> | `text` | field from the `properties` object |
| <CopyableCode code="spokes" /> | `text` | field from the `properties` object |
| <CopyableCode code="subscriptionId" /> | `text` | field from the `properties` object |
| <CopyableCode code="type" /> | `text` | field from the `properties` object |
</TabItem>
<TabItem value="resource">

| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="properties" /> | `object` | Properties of a Managed Network Peering Policy |
</TabItem></Tabs>

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="managedNetworkName, managedNetworkPeeringPolicyName, resourceGroupName, subscriptionId" /> | The Get ManagedNetworkPeeringPolicies operation gets a Managed Network Peering Policy resource, specified by the  resource group, Managed Network name, and peering policy name |
| <CopyableCode code="list_by_managed_network" /> | `SELECT` | <CopyableCode code="managedNetworkName, resourceGroupName, subscriptionId" /> | The ListByManagedNetwork PeeringPolicies operation retrieves all the Managed Network Peering Policies in a specified Managed Network, in a paginated format. |
| <CopyableCode code="create_or_update" /> | `INSERT` | <CopyableCode code="managedNetworkName, managedNetworkPeeringPolicyName, resourceGroupName, subscriptionId" /> | The Put ManagedNetworkPeeringPolicies operation creates/updates a new Managed Network Peering Policy |
| <CopyableCode code="delete" /> | `DELETE` | <CopyableCode code="managedNetworkName, managedNetworkPeeringPolicyName, resourceGroupName, subscriptionId" /> | The Delete ManagedNetworkPeeringPolicies operation deletes a Managed Network Peering Policy, specified by the  resource group, Managed Network name, and peering policy name |

## `SELECT` examples

The ListByManagedNetwork PeeringPolicies operation retrieves all the Managed Network Peering Policies in a specified Managed Network, in a paginated format.

<Tabs
    defaultValue="view"
    values={[
        { label: 'vw_peering_policies', value: 'view', },
        { label: 'peering_policies', value: 'resource', },
    ]
}>
<TabItem value="view">

```sql
SELECT
etag,
hub,
managedNetworkName,
managedNetworkPeeringPolicyName,
mesh,
provisioning_state,
resourceGroupName,
spokes,
subscriptionId,
type
FROM azure.managed_network.vw_peering_policies
WHERE managedNetworkName = '{{ managedNetworkName }}'
AND resourceGroupName = '{{ resourceGroupName }}'
AND subscriptionId = '{{ subscriptionId }}';
```
</TabItem>
<TabItem value="resource">


```sql
SELECT
properties
FROM azure.managed_network.peering_policies
WHERE managedNetworkName = '{{ managedNetworkName }}'
AND resourceGroupName = '{{ resourceGroupName }}'
AND subscriptionId = '{{ subscriptionId }}';
```
</TabItem></Tabs>


## `INSERT` example

Use the following StackQL query and manifest file to create a new <code>peering_policies</code> resource.

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
INSERT INTO azure.managed_network.peering_policies (
managedNetworkName,
managedNetworkPeeringPolicyName,
resourceGroupName,
subscriptionId,
properties
)
SELECT 
'{{ managedNetworkName }}',
'{{ managedNetworkPeeringPolicyName }}',
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
        - name: type
          value: string
        - name: hub
          value:
            - name: id
              value: string
        - name: spokes
          value:
            - - name: id
                value: string
        - name: mesh
          value:
            - - name: id
                value: string
        - name: provisioningState
          value: string
        - name: etag
          value: string

```
</TabItem>
</Tabs>

## `DELETE` example

Deletes the specified <code>peering_policies</code> resource.

```sql
/*+ delete */
DELETE FROM azure.managed_network.peering_policies
WHERE managedNetworkName = '{{ managedNetworkName }}'
AND managedNetworkPeeringPolicyName = '{{ managedNetworkPeeringPolicyName }}'
AND resourceGroupName = '{{ resourceGroupName }}'
AND subscriptionId = '{{ subscriptionId }}';
```
