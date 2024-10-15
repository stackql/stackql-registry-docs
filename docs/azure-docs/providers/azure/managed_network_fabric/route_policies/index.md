---
title: route_policies
hide_title: false
hide_table_of_contents: false
keywords:
  - route_policies
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

Creates, updates, deletes, gets or lists a <code>route_policies</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>route_policies</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.managed_network_fabric.route_policies" /></td></tr>
</tbody></table>

## Fields
<Tabs
    defaultValue="view"
    values={[
        { label: 'vw_route_policies', value: 'view', },
        { label: 'route_policies', value: 'resource', },
    ]
}>
<TabItem value="view">

| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="address_family_type" /> | `text` | field from the `properties` object |
| <CopyableCode code="administrative_state" /> | `text` | field from the `properties` object |
| <CopyableCode code="annotation" /> | `text` | field from the `properties` object |
| <CopyableCode code="configuration_state" /> | `text` | field from the `properties` object |
| <CopyableCode code="default_action" /> | `text` | field from the `properties` object |
| <CopyableCode code="location" /> | `text` | The geo-location where the resource lives |
| <CopyableCode code="network_fabric_id" /> | `text` | field from the `properties` object |
| <CopyableCode code="provisioning_state" /> | `text` | field from the `properties` object |
| <CopyableCode code="resourceGroupName" /> | `text` | field from the `properties` object |
| <CopyableCode code="routePolicyName" /> | `text` | field from the `properties` object |
| <CopyableCode code="statements" /> | `text` | field from the `properties` object |
| <CopyableCode code="subscriptionId" /> | `text` | field from the `properties` object |
| <CopyableCode code="tags" /> | `text` | Resource tags. |
</TabItem>
<TabItem value="resource">

| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="location" /> | `string` | The geo-location where the resource lives |
| <CopyableCode code="properties" /> | `object` | RoutePolicyProperties defines the resource properties. |
| <CopyableCode code="tags" /> | `object` | Resource tags. |
</TabItem></Tabs>

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="resourceGroupName, routePolicyName, subscriptionId" /> | Implements Route Policy GET method. |
| <CopyableCode code="list_by_resource_group" /> | `SELECT` | <CopyableCode code="resourceGroupName, subscriptionId" /> | Implements RoutePolicies list by resource group GET method. |
| <CopyableCode code="list_by_subscription" /> | `SELECT` | <CopyableCode code="subscriptionId" /> | Implements RoutePolicies list by subscription GET method. |
| <CopyableCode code="create" /> | `INSERT` | <CopyableCode code="resourceGroupName, routePolicyName, subscriptionId, data__location, data__properties" /> | Implements Route Policy PUT method. |
| <CopyableCode code="delete" /> | `DELETE` | <CopyableCode code="resourceGroupName, routePolicyName, subscriptionId" /> | Implements Route Policy DELETE method. |
| <CopyableCode code="update" /> | `UPDATE` | <CopyableCode code="resourceGroupName, routePolicyName, subscriptionId" /> | API to update certain properties of the Route Policy resource. |
| <CopyableCode code="commit_configuration" /> | `EXEC` | <CopyableCode code="resourceGroupName, routePolicyName, subscriptionId" /> | Commits the configuration of the given resources. |
| <CopyableCode code="validate_configuration" /> | `EXEC` | <CopyableCode code="resourceGroupName, routePolicyName, subscriptionId" /> | Validates the configuration of the resources. |

## `SELECT` examples

Implements RoutePolicies list by subscription GET method.

<Tabs
    defaultValue="view"
    values={[
        { label: 'vw_route_policies', value: 'view', },
        { label: 'route_policies', value: 'resource', },
    ]
}>
<TabItem value="view">

```sql
SELECT
address_family_type,
administrative_state,
annotation,
configuration_state,
default_action,
location,
network_fabric_id,
provisioning_state,
resourceGroupName,
routePolicyName,
statements,
subscriptionId,
tags
FROM azure.managed_network_fabric.vw_route_policies
WHERE subscriptionId = '{{ subscriptionId }}';
```
</TabItem>
<TabItem value="resource">


```sql
SELECT
location,
properties,
tags
FROM azure.managed_network_fabric.route_policies
WHERE subscriptionId = '{{ subscriptionId }}';
```
</TabItem></Tabs>


## `INSERT` example

Use the following StackQL query and manifest file to create a new <code>route_policies</code> resource.

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
INSERT INTO azure.managed_network_fabric.route_policies (
resourceGroupName,
routePolicyName,
subscriptionId,
data__location,
data__properties,
tags,
location,
properties
)
SELECT 
'{{ resourceGroupName }}',
'{{ routePolicyName }}',
'{{ subscriptionId }}',
'{{ data__location }}',
'{{ data__properties }}',
'{{ tags }}',
'{{ location }}',
'{{ properties }}'
;
```
</TabItem>
<TabItem value="manifest">

```yaml
- name: your_resource_model_name
  props:
    - name: tags
      value: object
    - name: location
      value: string
    - name: properties
      value:
        - name: annotation
          value: string
        - name: defaultAction
          value: []
        - name: statements
          value:
            - - name: annotation
                value: string
              - name: sequenceNumber
                value: integer
              - name: condition
                value:
                  - name: type
                    value: string
                  - name: ipPrefixId
                    value: string
                  - name: ipCommunityIds
                    value:
                      - string
                  - name: ipExtendedCommunityIds
                    value:
                      - string
              - name: action
                value:
                  - name: localPreference
                    value: integer
                  - name: actionType
                    value: string
                  - name: ipCommunityProperties
                    value:
                      - name: add
                        value:
                          - name: ipCommunityIds
                            value:
                              - string
                  - name: ipExtendedCommunityProperties
                    value:
                      - name: add
                        value:
                          - name: ipExtendedCommunityIds
                            value:
                              - string
        - name: networkFabricId
          value: []
        - name: addressFamilyType
          value: string
        - name: configurationState
          value: []
        - name: provisioningState
          value: []
        - name: administrativeState
          value: []

```
</TabItem>
</Tabs>

## `UPDATE` example

Updates a <code>route_policies</code> resource.

```sql
/*+ update */
UPDATE azure.managed_network_fabric.route_policies
SET 
properties = '{{ properties }}',
tags = '{{ tags }}'
WHERE 
resourceGroupName = '{{ resourceGroupName }}'
AND routePolicyName = '{{ routePolicyName }}'
AND subscriptionId = '{{ subscriptionId }}';
```

## `DELETE` example

Deletes the specified <code>route_policies</code> resource.

```sql
/*+ delete */
DELETE FROM azure.managed_network_fabric.route_policies
WHERE resourceGroupName = '{{ resourceGroupName }}'
AND routePolicyName = '{{ routePolicyName }}'
AND subscriptionId = '{{ subscriptionId }}';
```
