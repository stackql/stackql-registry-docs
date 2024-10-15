---
title: l3_isolation_domains
hide_title: false
hide_table_of_contents: false
keywords:
  - l3_isolation_domains
  - managed_network_fabric
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

Creates, updates, deletes, gets or lists a <code>l3_isolation_domains</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>l3_isolation_domains</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.managed_network_fabric.l3_isolation_domains" /></td></tr>
</tbody></table>

## Fields
<Tabs
    defaultValue="view"
    values={[
        { label: 'vw_l3_isolation_domains', value: 'view', },
        { label: 'l3_isolation_domains', value: 'resource', },
    ]
}>
<TabItem value="view">

| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="administrative_state" /> | `text` | field from the `properties` object |
| <CopyableCode code="aggregate_route_configuration" /> | `text` | field from the `properties` object |
| <CopyableCode code="annotation" /> | `text` | field from the `properties` object |
| <CopyableCode code="configuration_state" /> | `text` | field from the `properties` object |
| <CopyableCode code="connected_subnet_route_policy" /> | `text` | field from the `properties` object |
| <CopyableCode code="l3IsolationDomainName" /> | `text` | field from the `properties` object |
| <CopyableCode code="location" /> | `text` | The geo-location where the resource lives |
| <CopyableCode code="network_fabric_id" /> | `text` | field from the `properties` object |
| <CopyableCode code="provisioning_state" /> | `text` | field from the `properties` object |
| <CopyableCode code="redistribute_connected_subnets" /> | `text` | field from the `properties` object |
| <CopyableCode code="redistribute_static_routes" /> | `text` | field from the `properties` object |
| <CopyableCode code="resourceGroupName" /> | `text` | field from the `properties` object |
| <CopyableCode code="subscriptionId" /> | `text` | field from the `properties` object |
| <CopyableCode code="tags" /> | `text` | Resource tags. |
</TabItem>
<TabItem value="resource">

| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="location" /> | `string` | The geo-location where the resource lives |
| <CopyableCode code="properties" /> | `object` | L3 Isolation Domain Properties defines the properties of the resource. |
| <CopyableCode code="tags" /> | `object` | Resource tags. |
</TabItem></Tabs>

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="l3IsolationDomainName, resourceGroupName, subscriptionId" /> | Retrieves details of this L3 Isolation Domain. |
| <CopyableCode code="list_by_resource_group" /> | `SELECT` | <CopyableCode code="resourceGroupName, subscriptionId" /> | Displays L3IsolationDomains list by resource group GET method. |
| <CopyableCode code="list_by_subscription" /> | `SELECT` | <CopyableCode code="subscriptionId" /> | Displays L3IsolationDomains list by subscription GET method. |
| <CopyableCode code="create" /> | `INSERT` | <CopyableCode code="l3IsolationDomainName, resourceGroupName, subscriptionId, data__properties" /> | Create isolation domain resources for layer 3 connectivity between compute nodes and for communication with external services .This configuration is applied on the devices only after the creation of networks is completed and isolation domain is enabled.  |
| <CopyableCode code="delete" /> | `DELETE` | <CopyableCode code="l3IsolationDomainName, resourceGroupName, subscriptionId" /> | Deletes layer 3 connectivity between compute nodes by managed by named L3 Isolation name. |
| <CopyableCode code="update" /> | `UPDATE` | <CopyableCode code="l3IsolationDomainName, resourceGroupName, subscriptionId" /> | API to update certain properties of the L3 Isolation Domain resource. |
| <CopyableCode code="commit_configuration" /> | `EXEC` | <CopyableCode code="l3IsolationDomainName, resourceGroupName, subscriptionId" /> | Commits the configuration of the given resources. |
| <CopyableCode code="update_administrative_state" /> | `EXEC` | <CopyableCode code="l3IsolationDomainName, resourceGroupName, subscriptionId" /> | Enables racks for this Isolation Domain. |
| <CopyableCode code="validate_configuration" /> | `EXEC` | <CopyableCode code="l3IsolationDomainName, resourceGroupName, subscriptionId" /> | Validates the configuration of the resources. |

## `SELECT` examples

Displays L3IsolationDomains list by subscription GET method.

<Tabs
    defaultValue="view"
    values={[
        { label: 'vw_l3_isolation_domains', value: 'view', },
        { label: 'l3_isolation_domains', value: 'resource', },
    ]
}>
<TabItem value="view">

```sql
SELECT
administrative_state,
aggregate_route_configuration,
annotation,
configuration_state,
connected_subnet_route_policy,
l3IsolationDomainName,
location,
network_fabric_id,
provisioning_state,
redistribute_connected_subnets,
redistribute_static_routes,
resourceGroupName,
subscriptionId,
tags
FROM azure.managed_network_fabric.vw_l3_isolation_domains
WHERE subscriptionId = '{{ subscriptionId }}';
```
</TabItem>
<TabItem value="resource">


```sql
SELECT
location,
properties,
tags
FROM azure.managed_network_fabric.l3_isolation_domains
WHERE subscriptionId = '{{ subscriptionId }}';
```
</TabItem></Tabs>


## `INSERT` example

Use the following StackQL query and manifest file to create a new <code>l3_isolation_domains</code> resource.

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
INSERT INTO azure.managed_network_fabric.l3_isolation_domains (
l3IsolationDomainName,
resourceGroupName,
subscriptionId,
data__properties,
properties,
tags,
location
)
SELECT 
'{{ l3IsolationDomainName }}',
'{{ resourceGroupName }}',
'{{ subscriptionId }}',
'{{ data__properties }}',
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
        - name: annotation
          value: string
        - name: redistributeConnectedSubnets
          value: string
        - name: redistributeStaticRoutes
          value: string
        - name: aggregateRouteConfiguration
          value:
            - name: ipv4Routes
              value:
                - - name: prefix
                    value: string
            - name: ipv6Routes
              value:
                - - name: prefix
                    value: string
        - name: connectedSubnetRoutePolicy
          value:
            - name: exportRoutePolicyId
              value: []
            - name: exportRoutePolicy
              value: []
        - name: networkFabricId
          value: []
        - name: configurationState
          value: []
        - name: provisioningState
          value: []
        - name: administrativeState
          value: []
    - name: tags
      value: object
    - name: location
      value: string

```
</TabItem>
</Tabs>

## `UPDATE` example

Updates a <code>l3_isolation_domains</code> resource.

```sql
/*+ update */
UPDATE azure.managed_network_fabric.l3_isolation_domains
SET 
properties = '{{ properties }}',
tags = '{{ tags }}'
WHERE 
l3IsolationDomainName = '{{ l3IsolationDomainName }}'
AND resourceGroupName = '{{ resourceGroupName }}'
AND subscriptionId = '{{ subscriptionId }}';
```

## `DELETE` example

Deletes the specified <code>l3_isolation_domains</code> resource.

```sql
/*+ delete */
DELETE FROM azure.managed_network_fabric.l3_isolation_domains
WHERE l3IsolationDomainName = '{{ l3IsolationDomainName }}'
AND resourceGroupName = '{{ resourceGroupName }}'
AND subscriptionId = '{{ subscriptionId }}';
```
