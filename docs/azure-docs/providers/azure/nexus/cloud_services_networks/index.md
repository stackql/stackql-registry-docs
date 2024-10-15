---
title: cloud_services_networks
hide_title: false
hide_table_of_contents: false
keywords:
  - cloud_services_networks
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

Creates, updates, deletes, gets or lists a <code>cloud_services_networks</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>cloud_services_networks</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.nexus.cloud_services_networks" /></td></tr>
</tbody></table>

## Fields
<Tabs
    defaultValue="view"
    values={[
        { label: 'vw_cloud_services_networks', value: 'view', },
        { label: 'cloud_services_networks', value: 'resource', },
    ]
}>
<TabItem value="view">

| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="additional_egress_endpoints" /> | `text` | field from the `properties` object |
| <CopyableCode code="associated_resource_ids" /> | `text` | field from the `properties` object |
| <CopyableCode code="cloudServicesNetworkName" /> | `text` | field from the `properties` object |
| <CopyableCode code="cluster_id" /> | `text` | field from the `properties` object |
| <CopyableCode code="detailed_status" /> | `text` | field from the `properties` object |
| <CopyableCode code="detailed_status_message" /> | `text` | field from the `properties` object |
| <CopyableCode code="enable_default_egress_endpoints" /> | `text` | field from the `properties` object |
| <CopyableCode code="enabled_egress_endpoints" /> | `text` | field from the `properties` object |
| <CopyableCode code="extended_location" /> | `text` | field from the `properties` object |
| <CopyableCode code="hybrid_aks_clusters_associated_ids" /> | `text` | field from the `properties` object |
| <CopyableCode code="interface_name" /> | `text` | field from the `properties` object |
| <CopyableCode code="location" /> | `text` | The geo-location where the resource lives |
| <CopyableCode code="provisioning_state" /> | `text` | field from the `properties` object |
| <CopyableCode code="resourceGroupName" /> | `text` | field from the `properties` object |
| <CopyableCode code="subscriptionId" /> | `text` | field from the `properties` object |
| <CopyableCode code="tags" /> | `text` | Resource tags. |
| <CopyableCode code="virtual_machines_associated_ids" /> | `text` | field from the `properties` object |
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
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="cloudServicesNetworkName, resourceGroupName, subscriptionId" /> | Get properties of the provided cloud services network. |
| <CopyableCode code="list_by_resource_group" /> | `SELECT` | <CopyableCode code="resourceGroupName, subscriptionId" /> | Get a list of cloud services networks in the provided resource group. |
| <CopyableCode code="list_by_subscription" /> | `SELECT` | <CopyableCode code="subscriptionId" /> | Get a list of cloud services networks in the provided subscription. |
| <CopyableCode code="create_or_update" /> | `INSERT` | <CopyableCode code="cloudServicesNetworkName, resourceGroupName, subscriptionId, data__extendedLocation" /> | Create a new cloud services network or update the properties of the existing cloud services network. |
| <CopyableCode code="delete" /> | `DELETE` | <CopyableCode code="cloudServicesNetworkName, resourceGroupName, subscriptionId" /> | Delete the provided cloud services network. |
| <CopyableCode code="update" /> | `UPDATE` | <CopyableCode code="cloudServicesNetworkName, resourceGroupName, subscriptionId" /> | Update properties of the provided cloud services network, or update the tags associated with it. Properties and tag updates can be done independently. |

## `SELECT` examples

Get a list of cloud services networks in the provided subscription.

<Tabs
    defaultValue="view"
    values={[
        { label: 'vw_cloud_services_networks', value: 'view', },
        { label: 'cloud_services_networks', value: 'resource', },
    ]
}>
<TabItem value="view">

```sql
SELECT
additional_egress_endpoints,
associated_resource_ids,
cloudServicesNetworkName,
cluster_id,
detailed_status,
detailed_status_message,
enable_default_egress_endpoints,
enabled_egress_endpoints,
extended_location,
hybrid_aks_clusters_associated_ids,
interface_name,
location,
provisioning_state,
resourceGroupName,
subscriptionId,
tags,
virtual_machines_associated_ids
FROM azure.nexus.vw_cloud_services_networks
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
FROM azure.nexus.cloud_services_networks
WHERE subscriptionId = '{{ subscriptionId }}';
```
</TabItem></Tabs>


## `INSERT` example

Use the following StackQL query and manifest file to create a new <code>cloud_services_networks</code> resource.

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
INSERT INTO azure.nexus.cloud_services_networks (
cloudServicesNetworkName,
resourceGroupName,
subscriptionId,
data__extendedLocation,
extendedLocation,
properties,
tags,
location
)
SELECT 
'{{ cloudServicesNetworkName }}',
'{{ resourceGroupName }}',
'{{ subscriptionId }}',
'{{ data__extendedLocation }}',
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
        - name: additionalEgressEndpoints
          value:
            - - name: category
                value: string
              - name: endpoints
                value:
                  - - name: domainName
                      value: string
                    - name: port
                      value: integer
        - name: associatedResourceIds
          value:
            - string
        - name: clusterId
          value: string
        - name: detailedStatus
          value: string
        - name: detailedStatusMessage
          value: string
        - name: enableDefaultEgressEndpoints
          value: string
        - name: enabledEgressEndpoints
          value:
            - - name: category
                value: string
              - name: endpoints
                value:
                  - - name: domainName
                      value: string
                    - name: port
                      value: integer
        - name: hybridAksClustersAssociatedIds
          value:
            - string
        - name: interfaceName
          value: string
        - name: provisioningState
          value: string
        - name: virtualMachinesAssociatedIds
          value:
            - string
    - name: tags
      value: object
    - name: location
      value: string

```
</TabItem>
</Tabs>

## `UPDATE` example

Updates a <code>cloud_services_networks</code> resource.

```sql
/*+ update */
UPDATE azure.nexus.cloud_services_networks
SET 
properties = '{{ properties }}',
tags = '{{ tags }}'
WHERE 
cloudServicesNetworkName = '{{ cloudServicesNetworkName }}'
AND resourceGroupName = '{{ resourceGroupName }}'
AND subscriptionId = '{{ subscriptionId }}';
```

## `DELETE` example

Deletes the specified <code>cloud_services_networks</code> resource.

```sql
/*+ delete */
DELETE FROM azure.nexus.cloud_services_networks
WHERE cloudServicesNetworkName = '{{ cloudServicesNetworkName }}'
AND resourceGroupName = '{{ resourceGroupName }}'
AND subscriptionId = '{{ subscriptionId }}';
```
