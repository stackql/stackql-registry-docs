---
title: inbound_security_rules
hide_title: false
hide_table_of_contents: false
keywords:
  - inbound_security_rules
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

Creates, updates, deletes, gets or lists a <code>inbound_security_rules</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>inbound_security_rules</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.network.inbound_security_rules" /></td></tr>
</tbody></table>

## Fields
<Tabs
    defaultValue="view"
    values={[
        { label: 'vw_inbound_security_rules', value: 'view', },
        { label: 'inbound_security_rules', value: 'resource', },
    ]
}>
<TabItem value="view">

| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="id" /> | `text` | Resource ID. |
| <CopyableCode code="name" /> | `text` | Name of security rule collection. |
| <CopyableCode code="etag" /> | `text` | A unique read-only string that changes whenever the resource is updated. |
| <CopyableCode code="networkVirtualApplianceName" /> | `text` | field from the `properties` object |
| <CopyableCode code="provisioning_state" /> | `text` | field from the `properties` object |
| <CopyableCode code="resourceGroupName" /> | `text` | field from the `properties` object |
| <CopyableCode code="ruleCollectionName" /> | `text` | field from the `properties` object |
| <CopyableCode code="rule_type" /> | `text` | field from the `properties` object |
| <CopyableCode code="rules" /> | `text` | field from the `properties` object |
| <CopyableCode code="subscriptionId" /> | `text` | field from the `properties` object |
| <CopyableCode code="type" /> | `text` | NVA inbound security rule type. |
</TabItem>
<TabItem value="resource">

| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="id" /> | `string` | Resource ID. |
| <CopyableCode code="name" /> | `string` | Name of security rule collection. |
| <CopyableCode code="etag" /> | `string` | A unique read-only string that changes whenever the resource is updated. |
| <CopyableCode code="properties" /> | `object` | Properties of the Inbound Security Rules resource. |
| <CopyableCode code="type" /> | `string` | NVA inbound security rule type. |
</TabItem></Tabs>

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="networkVirtualApplianceName, resourceGroupName, ruleCollectionName, subscriptionId" /> | Retrieves the available specified Network Virtual Appliance Inbound Security Rules Collection. |
| <CopyableCode code="create_or_update" /> | `INSERT` | <CopyableCode code="networkVirtualApplianceName, resourceGroupName, ruleCollectionName, subscriptionId" /> | Creates or updates the specified Network Virtual Appliance Inbound Security Rules. |

## `SELECT` examples

Retrieves the available specified Network Virtual Appliance Inbound Security Rules Collection.

<Tabs
    defaultValue="view"
    values={[
        { label: 'vw_inbound_security_rules', value: 'view', },
        { label: 'inbound_security_rules', value: 'resource', },
    ]
}>
<TabItem value="view">

```sql
SELECT
id,
name,
etag,
networkVirtualApplianceName,
provisioning_state,
resourceGroupName,
ruleCollectionName,
rule_type,
rules,
subscriptionId,
type
FROM azure.network.vw_inbound_security_rules
WHERE networkVirtualApplianceName = '{{ networkVirtualApplianceName }}'
AND resourceGroupName = '{{ resourceGroupName }}'
AND ruleCollectionName = '{{ ruleCollectionName }}'
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
FROM azure.network.inbound_security_rules
WHERE networkVirtualApplianceName = '{{ networkVirtualApplianceName }}'
AND resourceGroupName = '{{ resourceGroupName }}'
AND ruleCollectionName = '{{ ruleCollectionName }}'
AND subscriptionId = '{{ subscriptionId }}';
```
</TabItem></Tabs>


## `INSERT` example

Use the following StackQL query and manifest file to create a new <code>inbound_security_rules</code> resource.

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
INSERT INTO azure.network.inbound_security_rules (
networkVirtualApplianceName,
resourceGroupName,
ruleCollectionName,
subscriptionId,
properties,
name,
id
)
SELECT 
'{{ networkVirtualApplianceName }}',
'{{ resourceGroupName }}',
'{{ ruleCollectionName }}',
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
        - name: ruleType
          value: string
        - name: rules
          value:
            - - name: name
                value: string
              - name: protocol
                value: string
              - name: sourceAddressPrefix
                value: string
              - name: destinationPortRange
                value: integer
              - name: destinationPortRanges
                value:
                  - string
              - name: appliesOn
                value:
                  - string
        - name: provisioningState
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
