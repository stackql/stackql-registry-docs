---
title: trunked_networks
hide_title: false
hide_table_of_contents: false
keywords:
  - trunked_networks
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

Creates, updates, deletes, gets or lists a <code>trunked_networks</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>trunked_networks</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.nexus.trunked_networks" /></td></tr>
</tbody></table>

## Fields
<Tabs
    defaultValue="view"
    values={[
        { label: 'vw_trunked_networks', value: 'view', },
        { label: 'trunked_networks', value: 'resource', },
    ]
}>
<TabItem value="view">

| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="associated_resource_ids" /> | `text` | field from the `properties` object |
| <CopyableCode code="cluster_id" /> | `text` | field from the `properties` object |
| <CopyableCode code="detailed_status" /> | `text` | field from the `properties` object |
| <CopyableCode code="detailed_status_message" /> | `text` | field from the `properties` object |
| <CopyableCode code="extended_location" /> | `text` | field from the `properties` object |
| <CopyableCode code="hybrid_aks_clusters_associated_ids" /> | `text` | field from the `properties` object |
| <CopyableCode code="hybrid_aks_plugin_type" /> | `text` | field from the `properties` object |
| <CopyableCode code="interface_name" /> | `text` | field from the `properties` object |
| <CopyableCode code="isolation_domain_ids" /> | `text` | field from the `properties` object |
| <CopyableCode code="location" /> | `text` | The geo-location where the resource lives |
| <CopyableCode code="provisioning_state" /> | `text` | field from the `properties` object |
| <CopyableCode code="resourceGroupName" /> | `text` | field from the `properties` object |
| <CopyableCode code="subscriptionId" /> | `text` | field from the `properties` object |
| <CopyableCode code="tags" /> | `text` | Resource tags. |
| <CopyableCode code="trunkedNetworkName" /> | `text` | field from the `properties` object |
| <CopyableCode code="virtual_machines_associated_ids" /> | `text` | field from the `properties` object |
| <CopyableCode code="vlans" /> | `text` | field from the `properties` object |
</TabItem>
<TabItem value="resource">

| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="extendedLocation" /> | `object` |  |
| <CopyableCode code="location" /> | `string` | The geo-location where the resource lives |
| <CopyableCode code="properties" /> | `object` |  |
| <CopyableCode code="tags" /> | `object` | Resource tags. |
</TabItem></Tabs>

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="resourceGroupName, subscriptionId, trunkedNetworkName" /> | Get properties of the provided trunked network. |
| <CopyableCode code="list_by_resource_group" /> | `SELECT` | <CopyableCode code="resourceGroupName, subscriptionId" /> | Get a list of trunked networks in the provided resource group. |
| <CopyableCode code="list_by_subscription" /> | `SELECT` | <CopyableCode code="subscriptionId" /> | Get a list of trunked networks in the provided subscription. |
| <CopyableCode code="create_or_update" /> | `INSERT` | <CopyableCode code="resourceGroupName, subscriptionId, trunkedNetworkName, data__extendedLocation, data__properties" /> | Create a new trunked network or update the properties of the existing trunked network. |
| <CopyableCode code="delete" /> | `DELETE` | <CopyableCode code="resourceGroupName, subscriptionId, trunkedNetworkName" /> | Delete the provided trunked network. |
| <CopyableCode code="update" /> | `UPDATE` | <CopyableCode code="resourceGroupName, subscriptionId, trunkedNetworkName" /> | Update tags associated with the provided trunked network. |

## `SELECT` examples

Get a list of trunked networks in the provided subscription.

<Tabs
    defaultValue="view"
    values={[
        { label: 'vw_trunked_networks', value: 'view', },
        { label: 'trunked_networks', value: 'resource', },
    ]
}>
<TabItem value="view">

```sql
SELECT
associated_resource_ids,
cluster_id,
detailed_status,
detailed_status_message,
extended_location,
hybrid_aks_clusters_associated_ids,
hybrid_aks_plugin_type,
interface_name,
isolation_domain_ids,
location,
provisioning_state,
resourceGroupName,
subscriptionId,
tags,
trunkedNetworkName,
virtual_machines_associated_ids,
vlans
FROM azure.nexus.vw_trunked_networks
WHERE subscriptionId = '{{ subscriptionId }}';
```
</TabItem>
<TabItem value="resource">


```sql
SELECT
extendedLocation,
location,
properties,
tags
FROM azure.nexus.trunked_networks
WHERE subscriptionId = '{{ subscriptionId }}';
```
</TabItem></Tabs>


## `INSERT` example

Use the following StackQL query and manifest file to create a new <code>trunked_networks</code> resource.

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
INSERT INTO azure.nexus.trunked_networks (
resourceGroupName,
subscriptionId,
trunkedNetworkName,
data__extendedLocation,
data__properties,
extendedLocation,
properties,
tags,
location
)
SELECT 
'{{ resourceGroupName }}',
'{{ subscriptionId }}',
'{{ trunkedNetworkName }}',
'{{ data__extendedLocation }}',
'{{ data__properties }}',
'{{ extendedLocation }}',
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
    - name: extendedLocation
      value:
        - name: name
          value: string
        - name: type
          value: string
    - name: properties
      value:
        - name: associatedResourceIds
          value:
            - string
        - name: clusterId
          value: string
        - name: detailedStatus
          value: string
        - name: detailedStatusMessage
          value: string
        - name: hybridAksClustersAssociatedIds
          value:
            - string
        - name: hybridAksPluginType
          value: string
        - name: interfaceName
          value: string
        - name: isolationDomainIds
          value:
            - string
        - name: provisioningState
          value: string
        - name: virtualMachinesAssociatedIds
          value:
            - string
        - name: vlans
          value:
            - integer
    - name: tags
      value: object
    - name: location
      value: string

```
</TabItem>
</Tabs>

## `UPDATE` example

Updates a <code>trunked_networks</code> resource.

```sql
/*+ update */
UPDATE azure.nexus.trunked_networks
SET 
tags = '{{ tags }}'
WHERE 
resourceGroupName = '{{ resourceGroupName }}'
AND subscriptionId = '{{ subscriptionId }}'
AND trunkedNetworkName = '{{ trunkedNetworkName }}';
```

## `DELETE` example

Deletes the specified <code>trunked_networks</code> resource.

```sql
/*+ delete */
DELETE FROM azure.nexus.trunked_networks
WHERE resourceGroupName = '{{ resourceGroupName }}'
AND subscriptionId = '{{ subscriptionId }}'
AND trunkedNetworkName = '{{ trunkedNetworkName }}';
```
