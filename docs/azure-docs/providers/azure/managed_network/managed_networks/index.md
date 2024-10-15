---
title: managed_networks
hide_title: false
hide_table_of_contents: false
keywords:
  - managed_networks
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

Creates, updates, deletes, gets or lists a <code>managed_networks</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>managed_networks</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.managed_network.managed_networks" /></td></tr>
</tbody></table>

## Fields
<Tabs
    defaultValue="view"
    values={[
        { label: 'vw_managed_networks', value: 'view', },
        { label: 'managed_networks', value: 'resource', },
    ]
}>
<TabItem value="view">

| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="connectivity" /> | `text` | field from the `properties` object |
| <CopyableCode code="etag" /> | `text` | field from the `properties` object |
| <CopyableCode code="managedNetworkName" /> | `text` | field from the `properties` object |
| <CopyableCode code="provisioning_state" /> | `text` | field from the `properties` object |
| <CopyableCode code="resourceGroupName" /> | `text` | field from the `properties` object |
| <CopyableCode code="scope" /> | `text` | field from the `properties` object |
| <CopyableCode code="subscriptionId" /> | `text` | field from the `properties` object |
| <CopyableCode code="tags" /> | `text` | Resource tags |
</TabItem>
<TabItem value="resource">

| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="properties" /> | `object` | Properties of Managed Network |
| <CopyableCode code="tags" /> | `object` | Resource tags |
</TabItem></Tabs>

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="managedNetworkName, resourceGroupName, subscriptionId" /> | The Get ManagedNetworks operation gets a Managed Network Resource, specified by the resource group and Managed Network name |
| <CopyableCode code="list_by_resource_group" /> | `SELECT` | <CopyableCode code="resourceGroupName, subscriptionId" /> | The ListByResourceGroup ManagedNetwork operation retrieves all the Managed Network resources in a resource group in a paginated format. |
| <CopyableCode code="list_by_subscription" /> | `SELECT` | <CopyableCode code="subscriptionId" /> | The ListBySubscription  ManagedNetwork operation retrieves all the Managed Network Resources in the current subscription in a paginated format. |
| <CopyableCode code="create_or_update" /> | `INSERT` | <CopyableCode code="managedNetworkName, resourceGroupName, subscriptionId" /> | The Put ManagedNetworks operation creates/updates a Managed Network Resource, specified by resource group and Managed Network name |
| <CopyableCode code="delete" /> | `DELETE` | <CopyableCode code="managedNetworkName, resourceGroupName, subscriptionId" /> | The Delete ManagedNetworks operation deletes a Managed Network Resource, specified by the  resource group and Managed Network name |
| <CopyableCode code="update" /> | `UPDATE` | <CopyableCode code="managedNetworkName, resourceGroupName, subscriptionId" /> | Updates the specified Managed Network resource tags. |

## `SELECT` examples

The ListBySubscription  ManagedNetwork operation retrieves all the Managed Network Resources in the current subscription in a paginated format.

<Tabs
    defaultValue="view"
    values={[
        { label: 'vw_managed_networks', value: 'view', },
        { label: 'managed_networks', value: 'resource', },
    ]
}>
<TabItem value="view">

```sql
SELECT
connectivity,
etag,
managedNetworkName,
provisioning_state,
resourceGroupName,
scope,
subscriptionId,
tags
FROM azure.managed_network.vw_managed_networks
WHERE subscriptionId = '{{ subscriptionId }}';
```
</TabItem>
<TabItem value="resource">


```sql
SELECT
properties,
tags
FROM azure.managed_network.managed_networks
WHERE subscriptionId = '{{ subscriptionId }}';
```
</TabItem></Tabs>


## `INSERT` example

Use the following StackQL query and manifest file to create a new <code>managed_networks</code> resource.

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
INSERT INTO azure.managed_network.managed_networks (
managedNetworkName,
resourceGroupName,
subscriptionId,
properties,
tags
)
SELECT 
'{{ managedNetworkName }}',
'{{ resourceGroupName }}',
'{{ subscriptionId }}',
'{{ properties }}',
'{{ tags }}'
;
```
</TabItem>
<TabItem value="manifest">

```yaml
- name: your_resource_model_name
  props:
    - name: properties
      value:
        - name: scope
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
        - name: connectivity
          value:
            - name: groups
              value:
                - - name: properties
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
            - name: peerings
              value:
                - - name: properties
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
        - name: provisioningState
          value: string
        - name: etag
          value: string
    - name: tags
      value: object

```
</TabItem>
</Tabs>

## `UPDATE` example

Updates a <code>managed_networks</code> resource.

```sql
/*+ update */
UPDATE azure.managed_network.managed_networks
SET 
tags = '{{ tags }}'
WHERE 
managedNetworkName = '{{ managedNetworkName }}'
AND resourceGroupName = '{{ resourceGroupName }}'
AND subscriptionId = '{{ subscriptionId }}';
```

## `DELETE` example

Deletes the specified <code>managed_networks</code> resource.

```sql
/*+ delete */
DELETE FROM azure.managed_network.managed_networks
WHERE managedNetworkName = '{{ managedNetworkName }}'
AND resourceGroupName = '{{ resourceGroupName }}'
AND subscriptionId = '{{ subscriptionId }}';
```
