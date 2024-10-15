---
title: azure_firewalls
hide_title: false
hide_table_of_contents: false
keywords:
  - azure_firewalls
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

Creates, updates, deletes, gets or lists a <code>azure_firewalls</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>azure_firewalls</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.network.azure_firewalls" /></td></tr>
</tbody></table>

## Fields
<Tabs
    defaultValue="view"
    values={[
        { label: 'vw_azure_firewalls', value: 'view', },
        { label: 'azure_firewalls', value: 'resource', },
    ]
}>
<TabItem value="view">

| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="id" /> | `text` | Resource ID. |
| <CopyableCode code="name" /> | `text` | Resource name. |
| <CopyableCode code="additional_properties" /> | `text` | field from the `properties` object |
| <CopyableCode code="application_rule_collections" /> | `text` | field from the `properties` object |
| <CopyableCode code="autoscale_configuration" /> | `text` | field from the `properties` object |
| <CopyableCode code="azureFirewallName" /> | `text` | field from the `properties` object |
| <CopyableCode code="etag" /> | `text` | A unique read-only string that changes whenever the resource is updated. |
| <CopyableCode code="firewall_policy" /> | `text` | field from the `properties` object |
| <CopyableCode code="hub_ip_addresses" /> | `text` | field from the `properties` object |
| <CopyableCode code="ip_configurations" /> | `text` | field from the `properties` object |
| <CopyableCode code="ip_groups" /> | `text` | field from the `properties` object |
| <CopyableCode code="location" /> | `text` | Resource location. |
| <CopyableCode code="management_ip_configuration" /> | `text` | field from the `properties` object |
| <CopyableCode code="nat_rule_collections" /> | `text` | field from the `properties` object |
| <CopyableCode code="network_rule_collections" /> | `text` | field from the `properties` object |
| <CopyableCode code="provisioning_state" /> | `text` | field from the `properties` object |
| <CopyableCode code="resourceGroupName" /> | `text` | field from the `properties` object |
| <CopyableCode code="sku" /> | `text` | field from the `properties` object |
| <CopyableCode code="subscriptionId" /> | `text` | field from the `properties` object |
| <CopyableCode code="tags" /> | `text` | Resource tags. |
| <CopyableCode code="threat_intel_mode" /> | `text` | field from the `properties` object |
| <CopyableCode code="type" /> | `text` | Resource type. |
| <CopyableCode code="virtual_hub" /> | `text` | field from the `properties` object |
| <CopyableCode code="zones" /> | `text` | A list of availability zones denoting where the resource needs to come from. |
</TabItem>
<TabItem value="resource">

| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="id" /> | `string` | Resource ID. |
| <CopyableCode code="name" /> | `string` | Resource name. |
| <CopyableCode code="etag" /> | `string` | A unique read-only string that changes whenever the resource is updated. |
| <CopyableCode code="location" /> | `string` | Resource location. |
| <CopyableCode code="properties" /> | `object` | Properties of the Azure Firewall. |
| <CopyableCode code="tags" /> | `object` | Resource tags. |
| <CopyableCode code="type" /> | `string` | Resource type. |
| <CopyableCode code="zones" /> | `array` | A list of availability zones denoting where the resource needs to come from. |
</TabItem></Tabs>

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="azureFirewallName, resourceGroupName, subscriptionId" /> | Gets the specified Azure Firewall. |
| <CopyableCode code="list" /> | `SELECT` | <CopyableCode code="resourceGroupName, subscriptionId" /> | Lists all Azure Firewalls in a resource group. |
| <CopyableCode code="list_all" /> | `SELECT` | <CopyableCode code="subscriptionId" /> | Gets all the Azure Firewalls in a subscription. |
| <CopyableCode code="create_or_update" /> | `INSERT` | <CopyableCode code="azureFirewallName, resourceGroupName, subscriptionId" /> | Creates or updates the specified Azure Firewall. |
| <CopyableCode code="delete" /> | `DELETE` | <CopyableCode code="azureFirewallName, resourceGroupName, subscriptionId" /> | Deletes the specified Azure Firewall. |
| <CopyableCode code="packet_capture" /> | `EXEC` | <CopyableCode code="azureFirewallName, resourceGroupName, subscriptionId" /> | Runs a packet capture on AzureFirewall. |
| <CopyableCode code="update_tags" /> | `EXEC` | <CopyableCode code="azureFirewallName, resourceGroupName, subscriptionId" /> | Updates tags of an Azure Firewall resource. |

## `SELECT` examples

Gets all the Azure Firewalls in a subscription.

<Tabs
    defaultValue="view"
    values={[
        { label: 'vw_azure_firewalls', value: 'view', },
        { label: 'azure_firewalls', value: 'resource', },
    ]
}>
<TabItem value="view">

```sql
SELECT
id,
name,
additional_properties,
application_rule_collections,
autoscale_configuration,
azureFirewallName,
etag,
firewall_policy,
hub_ip_addresses,
ip_configurations,
ip_groups,
location,
management_ip_configuration,
nat_rule_collections,
network_rule_collections,
provisioning_state,
resourceGroupName,
sku,
subscriptionId,
tags,
threat_intel_mode,
type,
virtual_hub,
zones
FROM azure.network.vw_azure_firewalls
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
type,
zones
FROM azure.network.azure_firewalls
WHERE subscriptionId = '{{ subscriptionId }}';
```
</TabItem></Tabs>


## `INSERT` example

Use the following StackQL query and manifest file to create a new <code>azure_firewalls</code> resource.

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
INSERT INTO azure.network.azure_firewalls (
azureFirewallName,
resourceGroupName,
subscriptionId,
properties,
zones,
id,
location,
tags
)
SELECT 
'{{ azureFirewallName }}',
'{{ resourceGroupName }}',
'{{ subscriptionId }}',
'{{ properties }}',
'{{ zones }}',
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
        - name: applicationRuleCollections
          value:
            - - name: properties
                value:
                  - name: priority
                    value: integer
                  - name: action
                    value:
                      - name: type
                        value: []
                  - name: rules
                    value:
                      - - name: name
                          value: string
                        - name: description
                          value: string
                        - name: sourceAddresses
                          value:
                            - string
                        - name: protocols
                          value:
                            - - name: protocolType
                                value: []
                              - name: port
                                value: integer
                        - name: targetFqdns
                          value:
                            - string
                        - name: fqdnTags
                          value:
                            - string
                        - name: sourceIpGroups
                          value:
                            - string
                  - name: provisioningState
                    value: []
              - name: name
                value: string
              - name: etag
                value: string
              - name: id
                value: string
        - name: natRuleCollections
          value:
            - - name: properties
                value:
                  - name: priority
                    value: integer
                  - name: action
                    value:
                      - name: type
                        value: []
                  - name: rules
                    value:
                      - - name: name
                          value: string
                        - name: description
                          value: string
                        - name: sourceAddresses
                          value:
                            - string
                        - name: destinationAddresses
                          value:
                            - string
                        - name: destinationPorts
                          value:
                            - string
                        - name: protocols
                          value:
                            - []
                        - name: translatedAddress
                          value: string
                        - name: translatedPort
                          value: string
                        - name: translatedFqdn
                          value: string
                        - name: sourceIpGroups
                          value:
                            - string
              - name: name
                value: string
              - name: etag
                value: string
              - name: id
                value: string
        - name: networkRuleCollections
          value:
            - - name: properties
                value:
                  - name: priority
                    value: integer
                  - name: rules
                    value:
                      - - name: name
                          value: string
                        - name: description
                          value: string
                        - name: protocols
                          value:
                            - []
                        - name: sourceAddresses
                          value:
                            - string
                        - name: destinationAddresses
                          value:
                            - string
                        - name: destinationPorts
                          value:
                            - string
                        - name: destinationFqdns
                          value:
                            - string
                        - name: sourceIpGroups
                          value:
                            - string
                        - name: destinationIpGroups
                          value:
                            - string
              - name: name
                value: string
              - name: etag
                value: string
              - name: id
                value: string
        - name: ipConfigurations
          value:
            - - name: properties
                value:
                  - name: privateIPAddress
                    value: string
                  - name: subnet
                    value:
                      - name: id
                        value: string
              - name: name
                value: string
              - name: etag
                value: string
              - name: type
                value: string
              - name: id
                value: string
        - name: managementIpConfiguration
          value:
            - name: name
              value: string
            - name: etag
              value: string
            - name: type
              value: string
            - name: id
              value: string
        - name: threatIntelMode
          value: []
        - name: hubIPAddresses
          value:
            - name: publicIPs
              value:
                - name: addresses
                  value:
                    - - name: address
                        value: string
                - name: count
                  value: integer
            - name: privateIPAddress
              value: string
        - name: ipGroups
          value: []
        - name: sku
          value:
            - name: name
              value: string
            - name: tier
              value: string
        - name: additionalProperties
          value: []
        - name: autoscaleConfiguration
          value:
            - name: minCapacity
              value: integer
            - name: maxCapacity
              value: integer
    - name: zones
      value:
        - string
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

Deletes the specified <code>azure_firewalls</code> resource.

```sql
/*+ delete */
DELETE FROM azure.network.azure_firewalls
WHERE azureFirewallName = '{{ azureFirewallName }}'
AND resourceGroupName = '{{ resourceGroupName }}'
AND subscriptionId = '{{ subscriptionId }}';
```
