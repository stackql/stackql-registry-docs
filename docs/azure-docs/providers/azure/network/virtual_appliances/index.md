---
title: virtual_appliances
hide_title: false
hide_table_of_contents: false
keywords:
  - virtual_appliances
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

Creates, updates, deletes, gets or lists a <code>virtual_appliances</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>virtual_appliances</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.network.virtual_appliances" /></td></tr>
</tbody></table>

## Fields
<Tabs
    defaultValue="view"
    values={[
        { label: 'vw_virtual_appliances', value: 'view', },
        { label: 'virtual_appliances', value: 'resource', },
    ]
}>
<TabItem value="view">

| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="id" /> | `text` | Resource ID. |
| <CopyableCode code="name" /> | `text` | Resource name. |
| <CopyableCode code="additional_nics" /> | `text` | field from the `properties` object |
| <CopyableCode code="address_prefix" /> | `text` | field from the `properties` object |
| <CopyableCode code="boot_strap_configuration_blobs" /> | `text` | field from the `properties` object |
| <CopyableCode code="cloud_init_configuration" /> | `text` | field from the `properties` object |
| <CopyableCode code="cloud_init_configuration_blobs" /> | `text` | field from the `properties` object |
| <CopyableCode code="delegation" /> | `text` | field from the `properties` object |
| <CopyableCode code="deployment_type" /> | `text` | field from the `properties` object |
| <CopyableCode code="etag" /> | `text` | A unique read-only string that changes whenever the resource is updated. |
| <CopyableCode code="identity" /> | `text` | Identity for the resource. |
| <CopyableCode code="inbound_security_rules" /> | `text` | field from the `properties` object |
| <CopyableCode code="internet_ingress_public_ips" /> | `text` | field from the `properties` object |
| <CopyableCode code="location" /> | `text` | Resource location. |
| <CopyableCode code="networkVirtualApplianceName" /> | `text` | field from the `properties` object |
| <CopyableCode code="network_profile" /> | `text` | field from the `properties` object |
| <CopyableCode code="nva_sku" /> | `text` | field from the `properties` object |
| <CopyableCode code="partner_managed_resource" /> | `text` | field from the `properties` object |
| <CopyableCode code="provisioning_state" /> | `text` | field from the `properties` object |
| <CopyableCode code="resourceGroupName" /> | `text` | field from the `properties` object |
| <CopyableCode code="ssh_public_key" /> | `text` | field from the `properties` object |
| <CopyableCode code="subscriptionId" /> | `text` | field from the `properties` object |
| <CopyableCode code="tags" /> | `text` | Resource tags. |
| <CopyableCode code="type" /> | `text` | Resource type. |
| <CopyableCode code="virtual_appliance_asn" /> | `text` | field from the `properties` object |
| <CopyableCode code="virtual_appliance_connections" /> | `text` | field from the `properties` object |
| <CopyableCode code="virtual_appliance_nics" /> | `text` | field from the `properties` object |
| <CopyableCode code="virtual_appliance_sites" /> | `text` | field from the `properties` object |
| <CopyableCode code="virtual_hub" /> | `text` | field from the `properties` object |
</TabItem>
<TabItem value="resource">

| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="id" /> | `string` | Resource ID. |
| <CopyableCode code="name" /> | `string` | Resource name. |
| <CopyableCode code="etag" /> | `string` | A unique read-only string that changes whenever the resource is updated. |
| <CopyableCode code="identity" /> | `object` | Identity for the resource. |
| <CopyableCode code="location" /> | `string` | Resource location. |
| <CopyableCode code="properties" /> | `object` | Network Virtual Appliance definition. |
| <CopyableCode code="tags" /> | `object` | Resource tags. |
| <CopyableCode code="type" /> | `string` | Resource type. |
</TabItem></Tabs>

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="networkVirtualApplianceName, resourceGroupName, subscriptionId" /> | Gets the specified Network Virtual Appliance. |
| <CopyableCode code="list" /> | `SELECT` | <CopyableCode code="subscriptionId" /> | Gets all Network Virtual Appliances in a subscription. |
| <CopyableCode code="list_by_resource_group" /> | `SELECT` | <CopyableCode code="resourceGroupName, subscriptionId" /> | Lists all Network Virtual Appliances in a resource group. |
| <CopyableCode code="create_or_update" /> | `INSERT` | <CopyableCode code="networkVirtualApplianceName, resourceGroupName, subscriptionId" /> | Creates or updates the specified Network Virtual Appliance. |
| <CopyableCode code="delete" /> | `DELETE` | <CopyableCode code="networkVirtualApplianceName, resourceGroupName, subscriptionId" /> | Deletes the specified Network Virtual Appliance. |
| <CopyableCode code="restart" /> | `EXEC` | <CopyableCode code="networkVirtualApplianceName, resourceGroupName, subscriptionId" /> | Restarts one or more VMs belonging to the specified Network Virtual Appliance. |
| <CopyableCode code="update_tags" /> | `EXEC` | <CopyableCode code="networkVirtualApplianceName, resourceGroupName, subscriptionId" /> | Updates a Network Virtual Appliance. |

## `SELECT` examples

Gets all Network Virtual Appliances in a subscription.

<Tabs
    defaultValue="view"
    values={[
        { label: 'vw_virtual_appliances', value: 'view', },
        { label: 'virtual_appliances', value: 'resource', },
    ]
}>
<TabItem value="view">

```sql
SELECT
id,
name,
additional_nics,
address_prefix,
boot_strap_configuration_blobs,
cloud_init_configuration,
cloud_init_configuration_blobs,
delegation,
deployment_type,
etag,
identity,
inbound_security_rules,
internet_ingress_public_ips,
location,
networkVirtualApplianceName,
network_profile,
nva_sku,
partner_managed_resource,
provisioning_state,
resourceGroupName,
ssh_public_key,
subscriptionId,
tags,
type,
virtual_appliance_asn,
virtual_appliance_connections,
virtual_appliance_nics,
virtual_appliance_sites,
virtual_hub
FROM azure.network.vw_virtual_appliances
WHERE subscriptionId = '{{ subscriptionId }}';
```
</TabItem>
<TabItem value="resource">


```sql
SELECT
id,
name,
etag,
identity,
location,
properties,
tags,
type
FROM azure.network.virtual_appliances
WHERE subscriptionId = '{{ subscriptionId }}';
```
</TabItem></Tabs>


## `INSERT` example

Use the following StackQL query and manifest file to create a new <code>virtual_appliances</code> resource.

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
INSERT INTO azure.network.virtual_appliances (
networkVirtualApplianceName,
resourceGroupName,
subscriptionId,
properties,
identity,
id,
location,
tags
)
SELECT 
'{{ networkVirtualApplianceName }}',
'{{ resourceGroupName }}',
'{{ subscriptionId }}',
'{{ properties }}',
'{{ identity }}',
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
        - name: nvaSku
          value:
            - name: vendor
              value: string
            - name: bundledScaleUnit
              value: string
            - name: marketPlaceVersion
              value: string
        - name: addressPrefix
          value: string
        - name: bootStrapConfigurationBlobs
          value:
            - string
        - name: virtualHub
          value:
            - name: id
              value: string
        - name: cloudInitConfigurationBlobs
          value:
            - string
        - name: cloudInitConfiguration
          value: string
        - name: virtualApplianceAsn
          value: integer
        - name: sshPublicKey
          value: string
        - name: virtualApplianceNics
          value:
            - - name: nicType
                value: string
              - name: name
                value: string
              - name: publicIpAddress
                value: string
              - name: privateIpAddress
                value: string
              - name: instanceName
                value: string
        - name: networkProfile
          value:
            - name: networkInterfaceConfigurations
              value:
                - - name: type
                    value: string
                  - name: properties
                    value:
                      - name: ipConfigurations
                        value:
                          - - name: name
                              value: string
                            - name: properties
                              value:
                                - name: primary
                                  value: boolean
        - name: additionalNics
          value:
            - - name: name
                value: string
              - name: hasPublicIp
                value: boolean
        - name: internetIngressPublicIps
          value:
            - - name: id
                value: string
        - name: virtualApplianceSites
          value:
            - - name: id
                value: string
        - name: virtualApplianceConnections
          value:
            - - name: id
                value: string
        - name: inboundSecurityRules
          value:
            - - name: id
                value: string
        - name: provisioningState
          value: []
        - name: deploymentType
          value: string
        - name: delegation
          value:
            - name: serviceName
              value: string
        - name: partnerManagedResource
          value:
            - name: id
              value: string
            - name: internalLoadBalancerId
              value: string
            - name: standardLoadBalancerId
              value: string
    - name: identity
      value:
        - name: principalId
          value: string
        - name: tenantId
          value: string
        - name: type
          value: string
        - name: userAssignedIdentities
          value: object
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

Deletes the specified <code>virtual_appliances</code> resource.

```sql
/*+ delete */
DELETE FROM azure.network.virtual_appliances
WHERE networkVirtualApplianceName = '{{ networkVirtualApplianceName }}'
AND resourceGroupName = '{{ resourceGroupName }}'
AND subscriptionId = '{{ subscriptionId }}';
```
