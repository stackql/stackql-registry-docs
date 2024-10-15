---
title: profiles
hide_title: false
hide_table_of_contents: false
keywords:
  - profiles
  - network
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

Creates, updates, deletes, gets or lists a <code>profiles</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>profiles</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.network.profiles" /></td></tr>
</tbody></table>

## Fields
<Tabs
    defaultValue="view"
    values={[
        { label: 'vw_profiles', value: 'view', },
        { label: 'profiles', value: 'resource', },
    ]
}>
<TabItem value="view">

| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="id" /> | `text` | Resource ID. |
| <CopyableCode code="name" /> | `text` | Resource name. |
| <CopyableCode code="container_network_interface_configurations" /> | `text` | field from the `properties` object |
| <CopyableCode code="container_network_interfaces" /> | `text` | field from the `properties` object |
| <CopyableCode code="etag" /> | `text` | A unique read-only string that changes whenever the resource is updated. |
| <CopyableCode code="location" /> | `text` | Resource location. |
| <CopyableCode code="networkProfileName" /> | `text` | field from the `properties` object |
| <CopyableCode code="provisioning_state" /> | `text` | field from the `properties` object |
| <CopyableCode code="resourceGroupName" /> | `text` | field from the `properties` object |
| <CopyableCode code="resource_guid" /> | `text` | field from the `properties` object |
| <CopyableCode code="subscriptionId" /> | `text` | field from the `properties` object |
| <CopyableCode code="tags" /> | `text` | Resource tags. |
| <CopyableCode code="type" /> | `text` | Resource type. |
</TabItem>
<TabItem value="resource">

| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="id" /> | `string` | Resource ID. |
| <CopyableCode code="name" /> | `string` | Resource name. |
| <CopyableCode code="etag" /> | `string` | A unique read-only string that changes whenever the resource is updated. |
| <CopyableCode code="location" /> | `string` | Resource location. |
| <CopyableCode code="properties" /> | `object` | Network profile properties. |
| <CopyableCode code="tags" /> | `object` | Resource tags. |
| <CopyableCode code="type" /> | `string` | Resource type. |
</TabItem></Tabs>

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="networkProfileName, resourceGroupName, subscriptionId" /> | Gets the specified network profile in a specified resource group. |
| <CopyableCode code="list" /> | `SELECT` | <CopyableCode code="resourceGroupName, subscriptionId" /> | Gets all network profiles in a resource group. |
| <CopyableCode code="list_all" /> | `SELECT` | <CopyableCode code="subscriptionId" /> | Gets all the network profiles in a subscription. |
| <CopyableCode code="create_or_update" /> | `INSERT` | <CopyableCode code="networkProfileName, resourceGroupName, subscriptionId" /> | Creates or updates a network profile. |
| <CopyableCode code="delete" /> | `DELETE` | <CopyableCode code="networkProfileName, resourceGroupName, subscriptionId" /> | Deletes the specified network profile. |
| <CopyableCode code="update_tags" /> | `EXEC` | <CopyableCode code="networkProfileName, resourceGroupName, subscriptionId" /> | Updates network profile tags. |

## `SELECT` examples

Gets all the network profiles in a subscription.

<Tabs
    defaultValue="view"
    values={[
        { label: 'vw_profiles', value: 'view', },
        { label: 'profiles', value: 'resource', },
    ]
}>
<TabItem value="view">

```sql
SELECT
id,
name,
container_network_interface_configurations,
container_network_interfaces,
etag,
location,
networkProfileName,
provisioning_state,
resourceGroupName,
resource_guid,
subscriptionId,
tags,
type
FROM azure.network.vw_profiles
WHERE subscriptionId = '{{ subscriptionId }}';
```
</TabItem>
<TabItem value="resource">


```sql
SELECT
id,
name,
etag,
location,
properties,
tags,
type
FROM azure.network.profiles
WHERE subscriptionId = '{{ subscriptionId }}';
```
</TabItem></Tabs>


## `INSERT` example

Use the following StackQL query and manifest file to create a new <code>profiles</code> resource.

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
INSERT INTO azure.network.profiles (
networkProfileName,
resourceGroupName,
subscriptionId,
properties,
id,
location,
tags
)
SELECT 
'{{ networkProfileName }}',
'{{ resourceGroupName }}',
'{{ subscriptionId }}',
'{{ properties }}',
'{{ id }}',
'{{ location }}',
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
        - name: containerNetworkInterfaces
          value:
            - - name: properties
                value:
                  - name: containerNetworkInterfaceConfiguration
                    value:
                      - name: properties
                        value:
                          - name: ipConfigurations
                            value:
                              - - name: properties
                                  value:
                                    - name: subnet
                                      value:
                                        - name: properties
                                          value:
                                            - name: addressPrefix
                                              value: string
                                            - name: addressPrefixes
                                              value:
                                                - string
                                            - name: networkSecurityGroup
                                              value:
                                                - name: properties
                                                  value: []
                                                - name: etag
                                                  value: string
                                                - name: id
                                                  value: string
                                                - name: name
                                                  value: string
                                                - name: type
                                                  value: string
                                                - name: location
                                                  value: string
                                                - name: tags
                                                  value: object
                                            - name: routeTable
                                              value:
                                                - name: properties
                                                  value: []
                                                - name: etag
                                                  value: string
                                                - name: id
                                                  value: string
                                                - name: name
                                                  value: string
                                                - name: type
                                                  value: string
                                                - name: location
                                                  value: string
                                                - name: tags
                                                  value: object
                                            - name: natGateway
                                              value:
                                                - name: id
                                                  value: string
                                            - name: serviceEndpoints
                                              value:
                                                - - name: service
                                                    value: string
                                                  - name: locations
                                                    value:
                                                      - string
                                                  - name: provisioningState
                                                    value: []
                                            - name: serviceEndpointPolicies
                                              value:
                                                - - name: properties
                                                    value: []
                                                  - name: etag
                                                    value: string
                                                  - name: kind
                                                    value: string
                                                  - name: id
                                                    value: string
                                                  - name: name
                                                    value: string
                                                  - name: type
                                                    value: string
                                                  - name: location
                                                    value: string
                                                  - name: tags
                                                    value: object
                                            - name: privateEndpoints
                                              value:
                                                - - name: extendedLocation
                                                    value: []
                                                  - name: properties
                                                    value: []
                                                  - name: etag
                                                    value: string
                                                  - name: id
                                                    value: string
                                                  - name: name
                                                    value: string
                                                  - name: type
                                                    value: string
                                                  - name: location
                                                    value: string
                                                  - name: tags
                                                    value: object
                                            - name: ipConfigurations
                                              value:
                                                - - name: properties
                                                    value: []
                                                  - name: name
                                                    value: string
                                                  - name: etag
                                                    value: string
                                                  - name: id
                                                    value: string
                                            - name: ipConfigurationProfiles
                                              value:
                                                - - name: name
                                                    value: string
                                                  - name: type
                                                    value: string
                                                  - name: etag
                                                    value: string
                                                  - name: id
                                                    value: string
                                            - name: ipAllocations
                                              value:
                                                - - name: id
                                                    value: string
                                            - name: resourceNavigationLinks
                                              value:
                                                - - name: properties
                                                    value: []
                                                  - name: name
                                                    value: string
                                                  - name: id
                                                    value: string
                                                  - name: etag
                                                    value: string
                                                  - name: type
                                                    value: string
                                            - name: serviceAssociationLinks
                                              value:
                                                - - name: properties
                                                    value: []
                                                  - name: name
                                                    value: string
                                                  - name: etag
                                                    value: string
                                                  - name: type
                                                    value: string
                                                  - name: id
                                                    value: string
                                            - name: delegations
                                              value:
                                                - - name: properties
                                                    value: []
                                                  - name: name
                                                    value: string
                                                  - name: etag
                                                    value: string
                                                  - name: type
                                                    value: string
                                                  - name: id
                                                    value: string
                                            - name: purpose
                                              value: string
                                            - name: privateEndpointNetworkPolicies
                                              value: string
                                            - name: privateLinkServiceNetworkPolicies
                                              value: string
                                            - name: applicationGatewayIPConfigurations
                                              value:
                                                - - name: properties
                                                    value: []
                                                  - name: name
                                                    value: string
                                                  - name: etag
                                                    value: string
                                                  - name: type
                                                    value: string
                                                  - name: id
                                                    value: string
                                            - name: sharingScope
                                              value: string
                                            - name: defaultOutboundAccess
                                              value: boolean
                                        - name: name
                                          value: string
                                        - name: etag
                                          value: string
                                        - name: type
                                          value: string
                                        - name: id
                                          value: string
                                - name: name
                                  value: string
                                - name: type
                                  value: string
                                - name: etag
                                  value: string
                                - name: id
                                  value: string
                          - name: containerNetworkInterfaces
                            value:
                              - - name: id
                                  value: string
                      - name: name
                        value: string
                      - name: type
                        value: string
                      - name: etag
                        value: string
                      - name: id
                        value: string
                  - name: container
                    value:
                      - name: id
                        value: string
                  - name: ipConfigurations
                    value:
                      - - name: properties
                          value: []
                        - name: name
                          value: string
                        - name: type
                          value: string
                        - name: etag
                          value: string
              - name: name
                value: string
              - name: type
                value: string
              - name: etag
                value: string
              - name: id
                value: string
        - name: containerNetworkInterfaceConfigurations
          value:
            - - name: name
                value: string
              - name: type
                value: string
              - name: etag
                value: string
              - name: id
                value: string
        - name: resourceGuid
          value: string
    - name: etag
      value: string
    - name: id
      value: string
    - name: name
      value: string
    - name: type
      value: string
    - name: location
      value: string
    - name: tags
      value: object

```
</TabItem>
</Tabs>

## `DELETE` example

Deletes the specified <code>profiles</code> resource.

```sql
/*+ delete */
DELETE FROM azure.network.profiles
WHERE networkProfileName = '{{ networkProfileName }}'
AND resourceGroupName = '{{ resourceGroupName }}'
AND subscriptionId = '{{ subscriptionId }}';
```
