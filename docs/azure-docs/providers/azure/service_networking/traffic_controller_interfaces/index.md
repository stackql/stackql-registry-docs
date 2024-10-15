---
title: traffic_controller_interfaces
hide_title: false
hide_table_of_contents: false
keywords:
  - traffic_controller_interfaces
  - service_networking
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

Creates, updates, deletes, gets or lists a <code>traffic_controller_interfaces</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>traffic_controller_interfaces</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.service_networking.traffic_controller_interfaces" /></td></tr>
</tbody></table>

## Fields
<Tabs
    defaultValue="view"
    values={[
        { label: 'vw_traffic_controller_interfaces', value: 'view', },
        { label: 'traffic_controller_interfaces', value: 'resource', },
    ]
}>
<TabItem value="view">

| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="associations" /> | `text` | field from the `properties` object |
| <CopyableCode code="configuration_endpoints" /> | `text` | field from the `properties` object |
| <CopyableCode code="frontends" /> | `text` | field from the `properties` object |
| <CopyableCode code="location" /> | `text` | The geo-location where the resource lives |
| <CopyableCode code="provisioning_state" /> | `text` | field from the `properties` object |
| <CopyableCode code="resourceGroupName" /> | `text` | field from the `properties` object |
| <CopyableCode code="security_policies" /> | `text` | field from the `properties` object |
| <CopyableCode code="security_policy_configurations" /> | `text` | field from the `properties` object |
| <CopyableCode code="subscriptionId" /> | `text` | field from the `properties` object |
| <CopyableCode code="tags" /> | `text` | Resource tags. |
| <CopyableCode code="trafficControllerName" /> | `text` | field from the `properties` object |
</TabItem>
<TabItem value="resource">

| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="location" /> | `string` | The geo-location where the resource lives |
| <CopyableCode code="properties" /> | `object` | Traffic Controller Properties. |
| <CopyableCode code="tags" /> | `object` | Resource tags. |
</TabItem></Tabs>

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="resourceGroupName, subscriptionId, trafficControllerName" /> | Get a TrafficController |
| <CopyableCode code="list_by_resource_group" /> | `SELECT` | <CopyableCode code="resourceGroupName, subscriptionId" /> | List TrafficController resources by resource group |
| <CopyableCode code="list_by_subscription" /> | `SELECT` | <CopyableCode code="subscriptionId" /> | List TrafficController resources by subscription ID |
| <CopyableCode code="create_or_update" /> | `INSERT` | <CopyableCode code="resourceGroupName, subscriptionId, trafficControllerName" /> | Create a TrafficController |
| <CopyableCode code="delete" /> | `DELETE` | <CopyableCode code="resourceGroupName, subscriptionId, trafficControllerName" /> | Delete a TrafficController |
| <CopyableCode code="update" /> | `UPDATE` | <CopyableCode code="resourceGroupName, subscriptionId, trafficControllerName" /> | Update a TrafficController |

## `SELECT` examples

List TrafficController resources by subscription ID

<Tabs
    defaultValue="view"
    values={[
        { label: 'vw_traffic_controller_interfaces', value: 'view', },
        { label: 'traffic_controller_interfaces', value: 'resource', },
    ]
}>
<TabItem value="view">

```sql
SELECT
associations,
configuration_endpoints,
frontends,
location,
provisioning_state,
resourceGroupName,
security_policies,
security_policy_configurations,
subscriptionId,
tags,
trafficControllerName
FROM azure.service_networking.vw_traffic_controller_interfaces
WHERE subscriptionId = '{{ subscriptionId }}';
```
</TabItem>
<TabItem value="resource">


```sql
SELECT
location,
properties,
tags
FROM azure.service_networking.traffic_controller_interfaces
WHERE subscriptionId = '{{ subscriptionId }}';
```
</TabItem></Tabs>


## `INSERT` example

Use the following StackQL query and manifest file to create a new <code>traffic_controller_interfaces</code> resource.

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
INSERT INTO azure.service_networking.traffic_controller_interfaces (
resourceGroupName,
subscriptionId,
trafficControllerName,
properties,
tags,
location
)
SELECT 
'{{ resourceGroupName }}',
'{{ subscriptionId }}',
'{{ trafficControllerName }}',
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
        - name: configurationEndpoints
          value:
            - string
        - name: frontends
          value:
            - - name: id
                value: string
        - name: associations
          value:
            - - name: id
                value: string
        - name: securityPolicies
          value:
            - - name: id
                value: string
        - name: securityPolicyConfigurations
          value:
            - name: wafSecurityPolicy
              value:
                - name: id
                  value: string
        - name: provisioningState
          value: []
    - name: tags
      value: object
    - name: location
      value: string

```
</TabItem>
</Tabs>

## `UPDATE` example

Updates a <code>traffic_controller_interfaces</code> resource.

```sql
/*+ update */
UPDATE azure.service_networking.traffic_controller_interfaces
SET 
tags = '{{ tags }}',
properties = '{{ properties }}'
WHERE 
resourceGroupName = '{{ resourceGroupName }}'
AND subscriptionId = '{{ subscriptionId }}'
AND trafficControllerName = '{{ trafficControllerName }}';
```

## `DELETE` example

Deletes the specified <code>traffic_controller_interfaces</code> resource.

```sql
/*+ delete */
DELETE FROM azure.service_networking.traffic_controller_interfaces
WHERE resourceGroupName = '{{ resourceGroupName }}'
AND subscriptionId = '{{ subscriptionId }}'
AND trafficControllerName = '{{ trafficControllerName }}';
```
