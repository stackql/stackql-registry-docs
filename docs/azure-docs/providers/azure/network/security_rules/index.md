---
title: security_rules
hide_title: false
hide_table_of_contents: false
keywords:
  - security_rules
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

Creates, updates, deletes, gets or lists a <code>security_rules</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>security_rules</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.network.security_rules" /></td></tr>
</tbody></table>

## Fields
<Tabs
    defaultValue="view"
    values={[
        { label: 'vw_security_rules', value: 'view', },
        { label: 'security_rules', value: 'resource', },
    ]
}>
<TabItem value="view">

| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="id" /> | `text` | Resource ID. |
| <CopyableCode code="name" /> | `text` | The name of the resource that is unique within a resource group. This name can be used to access the resource. |
| <CopyableCode code="description" /> | `text` | field from the `properties` object |
| <CopyableCode code="access" /> | `text` | field from the `properties` object |
| <CopyableCode code="destination_address_prefix" /> | `text` | field from the `properties` object |
| <CopyableCode code="destination_address_prefixes" /> | `text` | field from the `properties` object |
| <CopyableCode code="destination_application_security_groups" /> | `text` | field from the `properties` object |
| <CopyableCode code="destination_port_range" /> | `text` | field from the `properties` object |
| <CopyableCode code="destination_port_ranges" /> | `text` | field from the `properties` object |
| <CopyableCode code="direction" /> | `text` | field from the `properties` object |
| <CopyableCode code="etag" /> | `text` | A unique read-only string that changes whenever the resource is updated. |
| <CopyableCode code="networkSecurityGroupName" /> | `text` | field from the `properties` object |
| <CopyableCode code="priority" /> | `text` | field from the `properties` object |
| <CopyableCode code="protocol" /> | `text` | field from the `properties` object |
| <CopyableCode code="provisioning_state" /> | `text` | field from the `properties` object |
| <CopyableCode code="resourceGroupName" /> | `text` | field from the `properties` object |
| <CopyableCode code="securityRuleName" /> | `text` | field from the `properties` object |
| <CopyableCode code="source_address_prefix" /> | `text` | field from the `properties` object |
| <CopyableCode code="source_address_prefixes" /> | `text` | field from the `properties` object |
| <CopyableCode code="source_application_security_groups" /> | `text` | field from the `properties` object |
| <CopyableCode code="source_port_range" /> | `text` | field from the `properties` object |
| <CopyableCode code="source_port_ranges" /> | `text` | field from the `properties` object |
| <CopyableCode code="subscriptionId" /> | `text` | field from the `properties` object |
| <CopyableCode code="type" /> | `text` | The type of the resource. |
</TabItem>
<TabItem value="resource">

| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="id" /> | `string` | Resource ID. |
| <CopyableCode code="name" /> | `string` | The name of the resource that is unique within a resource group. This name can be used to access the resource. |
| <CopyableCode code="etag" /> | `string` | A unique read-only string that changes whenever the resource is updated. |
| <CopyableCode code="properties" /> | `object` | Security rule resource. |
| <CopyableCode code="type" /> | `string` | The type of the resource. |
</TabItem></Tabs>

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="networkSecurityGroupName, resourceGroupName, securityRuleName, subscriptionId" /> | Get the specified network security rule. |
| <CopyableCode code="list" /> | `SELECT` | <CopyableCode code="networkSecurityGroupName, resourceGroupName, subscriptionId" /> | Gets all security rules in a network security group. |
| <CopyableCode code="create_or_update" /> | `INSERT` | <CopyableCode code="networkSecurityGroupName, resourceGroupName, securityRuleName, subscriptionId" /> | Creates or updates a security rule in the specified network security group. |
| <CopyableCode code="delete" /> | `DELETE` | <CopyableCode code="networkSecurityGroupName, resourceGroupName, securityRuleName, subscriptionId" /> | Deletes the specified network security rule. |

## `SELECT` examples

Gets all security rules in a network security group.

<Tabs
    defaultValue="view"
    values={[
        { label: 'vw_security_rules', value: 'view', },
        { label: 'security_rules', value: 'resource', },
    ]
}>
<TabItem value="view">

```sql
SELECT
id,
name,
description,
access,
destination_address_prefix,
destination_address_prefixes,
destination_application_security_groups,
destination_port_range,
destination_port_ranges,
direction,
etag,
networkSecurityGroupName,
priority,
protocol,
provisioning_state,
resourceGroupName,
securityRuleName,
source_address_prefix,
source_address_prefixes,
source_application_security_groups,
source_port_range,
source_port_ranges,
subscriptionId,
type
FROM azure.network.vw_security_rules
WHERE networkSecurityGroupName = '{{ networkSecurityGroupName }}'
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
FROM azure.network.security_rules
WHERE networkSecurityGroupName = '{{ networkSecurityGroupName }}'
AND resourceGroupName = '{{ resourceGroupName }}'
AND subscriptionId = '{{ subscriptionId }}';
```
</TabItem></Tabs>


## `INSERT` example

Use the following StackQL query and manifest file to create a new <code>security_rules</code> resource.

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
INSERT INTO azure.network.security_rules (
networkSecurityGroupName,
resourceGroupName,
securityRuleName,
subscriptionId,
properties,
name,
type,
id
)
SELECT 
'{{ networkSecurityGroupName }}',
'{{ resourceGroupName }}',
'{{ securityRuleName }}',
'{{ subscriptionId }}',
'{{ properties }}',
'{{ name }}',
'{{ type }}',
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
        - name: description
          value: string
        - name: protocol
          value: string
        - name: sourcePortRange
          value: string
        - name: destinationPortRange
          value: string
        - name: sourceAddressPrefix
          value: string
        - name: sourceAddressPrefixes
          value:
            - string
        - name: sourceApplicationSecurityGroups
          value:
            - - name: properties
                value:
                  - name: resourceGuid
                    value: string
                  - name: provisioningState
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
        - name: destinationAddressPrefix
          value: string
        - name: destinationAddressPrefixes
          value:
            - string
        - name: destinationApplicationSecurityGroups
          value:
            - - name: etag
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
        - name: sourcePortRanges
          value:
            - string
        - name: destinationPortRanges
          value:
            - string
        - name: access
          value: []
        - name: priority
          value: integer
        - name: direction
          value: []
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

Deletes the specified <code>security_rules</code> resource.

```sql
/*+ delete */
DELETE FROM azure.network.security_rules
WHERE networkSecurityGroupName = '{{ networkSecurityGroupName }}'
AND resourceGroupName = '{{ resourceGroupName }}'
AND securityRuleName = '{{ securityRuleName }}'
AND subscriptionId = '{{ subscriptionId }}';
```
