---
title: nat_rules
hide_title: false
hide_table_of_contents: false
keywords:
  - nat_rules
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

Creates, updates, deletes, gets or lists a <code>nat_rules</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>nat_rules</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.network.nat_rules" /></td></tr>
</tbody></table>

## Fields
<Tabs
    defaultValue="view"
    values={[
        { label: 'vw_nat_rules', value: 'view', },
        { label: 'nat_rules', value: 'resource', },
    ]
}>
<TabItem value="view">

| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="id" /> | `text` | Resource ID. |
| <CopyableCode code="name" /> | `text` | The name of the resource that is unique within a resource group. This name can be used to access the resource. |
| <CopyableCode code="egress_vpn_site_link_connections" /> | `text` | field from the `properties` object |
| <CopyableCode code="etag" /> | `text` | A unique read-only string that changes whenever the resource is updated. |
| <CopyableCode code="external_mappings" /> | `text` | field from the `properties` object |
| <CopyableCode code="gatewayName" /> | `text` | field from the `properties` object |
| <CopyableCode code="ingress_vpn_site_link_connections" /> | `text` | field from the `properties` object |
| <CopyableCode code="internal_mappings" /> | `text` | field from the `properties` object |
| <CopyableCode code="ip_configuration_id" /> | `text` | field from the `properties` object |
| <CopyableCode code="mode" /> | `text` | field from the `properties` object |
| <CopyableCode code="natRuleName" /> | `text` | field from the `properties` object |
| <CopyableCode code="provisioning_state" /> | `text` | field from the `properties` object |
| <CopyableCode code="resourceGroupName" /> | `text` | field from the `properties` object |
| <CopyableCode code="subscriptionId" /> | `text` | field from the `properties` object |
| <CopyableCode code="type" /> | `text` | Resource type. |
</TabItem>
<TabItem value="resource">

| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="id" /> | `string` | Resource ID. |
| <CopyableCode code="name" /> | `string` | The name of the resource that is unique within a resource group. This name can be used to access the resource. |
| <CopyableCode code="etag" /> | `string` | A unique read-only string that changes whenever the resource is updated. |
| <CopyableCode code="properties" /> | `object` | Parameters for VpnGatewayNatRule. |
| <CopyableCode code="type" /> | `string` | Resource type. |
</TabItem></Tabs>

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="gatewayName, natRuleName, resourceGroupName, subscriptionId" /> | Retrieves the details of a nat ruleGet. |
| <CopyableCode code="list_by_vpn_gateway" /> | `SELECT` | <CopyableCode code="gatewayName, resourceGroupName, subscriptionId" /> | Retrieves all nat rules for a particular virtual wan vpn gateway. |
| <CopyableCode code="create_or_update" /> | `INSERT` | <CopyableCode code="gatewayName, natRuleName, resourceGroupName, subscriptionId" /> | Creates a nat rule to a scalable vpn gateway if it doesn't exist else updates the existing nat rules. |
| <CopyableCode code="delete" /> | `DELETE` | <CopyableCode code="gatewayName, natRuleName, resourceGroupName, subscriptionId" /> | Deletes a nat rule. |

## `SELECT` examples

Retrieves all nat rules for a particular virtual wan vpn gateway.

<Tabs
    defaultValue="view"
    values={[
        { label: 'vw_nat_rules', value: 'view', },
        { label: 'nat_rules', value: 'resource', },
    ]
}>
<TabItem value="view">

```sql
SELECT
id,
name,
egress_vpn_site_link_connections,
etag,
external_mappings,
gatewayName,
ingress_vpn_site_link_connections,
internal_mappings,
ip_configuration_id,
mode,
natRuleName,
provisioning_state,
resourceGroupName,
subscriptionId,
type
FROM azure.network.vw_nat_rules
WHERE gatewayName = '{{ gatewayName }}'
AND resourceGroupName = '{{ resourceGroupName }}'
AND subscriptionId = '{{ subscriptionId }}';
```
</TabItem>
<TabItem value="resource">


```sql
SELECT
id,
name,
etag,
properties,
type
FROM azure.network.nat_rules
WHERE gatewayName = '{{ gatewayName }}'
AND resourceGroupName = '{{ resourceGroupName }}'
AND subscriptionId = '{{ subscriptionId }}';
```
</TabItem></Tabs>


## `INSERT` example

Use the following StackQL query and manifest file to create a new <code>nat_rules</code> resource.

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
INSERT INTO azure.network.nat_rules (
gatewayName,
natRuleName,
resourceGroupName,
subscriptionId,
properties,
name,
id
)
SELECT 
'{{ gatewayName }}',
'{{ natRuleName }}',
'{{ resourceGroupName }}',
'{{ subscriptionId }}',
'{{ properties }}',
'{{ name }}',
'{{ id }}'
;
```
</TabItem>
<TabItem value="manifest">

```yaml
- name: your_resource_model_name
  props:
    - name: properties
      value:
        - name: provisioningState
          value: []
        - name: type
          value: string
        - name: mode
          value: string
        - name: internalMappings
          value:
            - - name: addressSpace
                value: string
              - name: portRange
                value: string
        - name: externalMappings
          value:
            - - name: addressSpace
                value: string
              - name: portRange
                value: string
        - name: ipConfigurationId
          value: string
        - name: egressVpnSiteLinkConnections
          value:
            - - name: id
                value: string
        - name: ingressVpnSiteLinkConnections
          value:
            - - name: id
                value: string
    - name: name
      value: string
    - name: etag
      value: string
    - name: type
      value: string
    - name: id
      value: string

```
</TabItem>
</Tabs>

## `DELETE` example

Deletes the specified <code>nat_rules</code> resource.

```sql
/*+ delete */
DELETE FROM azure.network.nat_rules
WHERE gatewayName = '{{ gatewayName }}'
AND natRuleName = '{{ natRuleName }}'
AND resourceGroupName = '{{ resourceGroupName }}'
AND subscriptionId = '{{ subscriptionId }}';
```
