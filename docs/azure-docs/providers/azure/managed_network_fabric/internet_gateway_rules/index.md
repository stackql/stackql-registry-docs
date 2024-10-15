---
title: internet_gateway_rules
hide_title: false
hide_table_of_contents: false
keywords:
  - internet_gateway_rules
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

Creates, updates, deletes, gets or lists a <code>internet_gateway_rules</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>internet_gateway_rules</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.managed_network_fabric.internet_gateway_rules" /></td></tr>
</tbody></table>

## Fields
<Tabs
    defaultValue="view"
    values={[
        { label: 'vw_internet_gateway_rules', value: 'view', },
        { label: 'internet_gateway_rules', value: 'resource', },
    ]
}>
<TabItem value="view">

| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="annotation" /> | `text` | field from the `properties` object |
| <CopyableCode code="internetGatewayRuleName" /> | `text` | field from the `properties` object |
| <CopyableCode code="internet_gateway_ids" /> | `text` | field from the `properties` object |
| <CopyableCode code="location" /> | `text` | The geo-location where the resource lives |
| <CopyableCode code="provisioning_state" /> | `text` | field from the `properties` object |
| <CopyableCode code="resourceGroupName" /> | `text` | field from the `properties` object |
| <CopyableCode code="rule_properties" /> | `text` | field from the `properties` object |
| <CopyableCode code="subscriptionId" /> | `text` | field from the `properties` object |
| <CopyableCode code="tags" /> | `text` | Resource tags. |
</TabItem>
<TabItem value="resource">

| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="location" /> | `string` | The geo-location where the resource lives |
| <CopyableCode code="properties" /> | `object` | Internet Gateway Rule Properties defines the resource properties. |
| <CopyableCode code="tags" /> | `object` | Resource tags. |
</TabItem></Tabs>

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="internetGatewayRuleName, resourceGroupName, subscriptionId" /> | Gets an Internet Gateway Rule resource. |
| <CopyableCode code="list_by_resource_group" /> | `SELECT` | <CopyableCode code="resourceGroupName, subscriptionId" /> | Implements Internet Gateway Rules list by resource group GET method. |
| <CopyableCode code="list_by_subscription" /> | `SELECT` | <CopyableCode code="subscriptionId" /> | List all Internet Gateway rules in the given subscription. |
| <CopyableCode code="create" /> | `INSERT` | <CopyableCode code="internetGatewayRuleName, resourceGroupName, subscriptionId, data__properties" /> | Creates an Internet Gateway rule resource. |
| <CopyableCode code="delete" /> | `DELETE` | <CopyableCode code="internetGatewayRuleName, resourceGroupName, subscriptionId" /> | Implements Internet Gateway Rules DELETE method. |
| <CopyableCode code="update" /> | `UPDATE` | <CopyableCode code="internetGatewayRuleName, resourceGroupName, subscriptionId" /> | API to update certain properties of the Internet Gateway Rule resource. |

## `SELECT` examples

List all Internet Gateway rules in the given subscription.

<Tabs
    defaultValue="view"
    values={[
        { label: 'vw_internet_gateway_rules', value: 'view', },
        { label: 'internet_gateway_rules', value: 'resource', },
    ]
}>
<TabItem value="view">

```sql
SELECT
annotation,
internetGatewayRuleName,
internet_gateway_ids,
location,
provisioning_state,
resourceGroupName,
rule_properties,
subscriptionId,
tags
FROM azure.managed_network_fabric.vw_internet_gateway_rules
WHERE subscriptionId = '{{ subscriptionId }}';
```
</TabItem>
<TabItem value="resource">


```sql
SELECT
location,
properties,
tags
FROM azure.managed_network_fabric.internet_gateway_rules
WHERE subscriptionId = '{{ subscriptionId }}';
```
</TabItem></Tabs>


## `INSERT` example

Use the following StackQL query and manifest file to create a new <code>internet_gateway_rules</code> resource.

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
INSERT INTO azure.managed_network_fabric.internet_gateway_rules (
internetGatewayRuleName,
resourceGroupName,
subscriptionId,
data__properties,
tags,
location,
properties
)
SELECT 
'{{ internetGatewayRuleName }}',
'{{ resourceGroupName }}',
'{{ subscriptionId }}',
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
        - name: ruleProperties
          value:
            - name: action
              value: string
            - name: addressList
              value:
                - string
        - name: provisioningState
          value: []
        - name: internetGatewayIds
          value:
            - string

```
</TabItem>
</Tabs>

## `UPDATE` example

Updates a <code>internet_gateway_rules</code> resource.

```sql
/*+ update */
UPDATE azure.managed_network_fabric.internet_gateway_rules
SET 
tags = '{{ tags }}'
WHERE 
internetGatewayRuleName = '{{ internetGatewayRuleName }}'
AND resourceGroupName = '{{ resourceGroupName }}'
AND subscriptionId = '{{ subscriptionId }}';
```

## `DELETE` example

Deletes the specified <code>internet_gateway_rules</code> resource.

```sql
/*+ delete */
DELETE FROM azure.managed_network_fabric.internet_gateway_rules
WHERE internetGatewayRuleName = '{{ internetGatewayRuleName }}'
AND resourceGroupName = '{{ resourceGroupName }}'
AND subscriptionId = '{{ subscriptionId }}';
```
