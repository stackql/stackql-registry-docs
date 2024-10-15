---
title: gateways
hide_title: false
hide_table_of_contents: false
keywords:
  - gateways
  - programmableconnectivity
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

Creates, updates, deletes, gets or lists a <code>gateways</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>gateways</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.programmableconnectivity.gateways" /></td></tr>
</tbody></table>

## Fields
<Tabs
    defaultValue="view"
    values={[
        { label: 'vw_gateways', value: 'view', },
        { label: 'gateways', value: 'resource', },
    ]
}>
<TabItem value="view">

| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="gatewayName" /> | `text` | field from the `properties` object |
| <CopyableCode code="gateway_base_url" /> | `text` | field from the `properties` object |
| <CopyableCode code="location" /> | `text` | The geo-location where the resource lives |
| <CopyableCode code="operator_api_connections" /> | `text` | field from the `properties` object |
| <CopyableCode code="provisioning_state" /> | `text` | field from the `properties` object |
| <CopyableCode code="resourceGroupName" /> | `text` | field from the `properties` object |
| <CopyableCode code="subscriptionId" /> | `text` | field from the `properties` object |
| <CopyableCode code="tags" /> | `text` | Resource tags. |
</TabItem>
<TabItem value="resource">

| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="location" /> | `string` | The geo-location where the resource lives |
| <CopyableCode code="properties" /> | `object` | Gateway resource properties |
| <CopyableCode code="tags" /> | `object` | Resource tags. |
</TabItem></Tabs>

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="gatewayName, resourceGroupName, subscriptionId" /> | Get a Gateway resource by name. |
| <CopyableCode code="list_by_resource_group" /> | `SELECT` | <CopyableCode code="resourceGroupName, subscriptionId" /> | List Gateway resources by resource group. |
| <CopyableCode code="list_by_subscription" /> | `SELECT` | <CopyableCode code="subscriptionId" /> | List Gateway resources by subscription ID. |
| <CopyableCode code="create_or_update" /> | `INSERT` | <CopyableCode code="gatewayName, resourceGroupName, subscriptionId" /> | Create or update an APC Gateway. |
| <CopyableCode code="delete" /> | `DELETE` | <CopyableCode code="gatewayName, resourceGroupName, subscriptionId" /> | Delete a Gateway. |
| <CopyableCode code="update" /> | `UPDATE` | <CopyableCode code="gatewayName, resourceGroupName, subscriptionId" /> | Update Gateway tags. |

## `SELECT` examples

List Gateway resources by subscription ID.

<Tabs
    defaultValue="view"
    values={[
        { label: 'vw_gateways', value: 'view', },
        { label: 'gateways', value: 'resource', },
    ]
}>
<TabItem value="view">

```sql
SELECT
gatewayName,
gateway_base_url,
location,
operator_api_connections,
provisioning_state,
resourceGroupName,
subscriptionId,
tags
FROM azure.programmableconnectivity.vw_gateways
WHERE subscriptionId = '{{ subscriptionId }}';
```
</TabItem>
<TabItem value="resource">


```sql
SELECT
location,
properties,
tags
FROM azure.programmableconnectivity.gateways
WHERE subscriptionId = '{{ subscriptionId }}';
```
</TabItem></Tabs>


## `INSERT` example

Use the following StackQL query and manifest file to create a new <code>gateways</code> resource.

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
INSERT INTO azure.programmableconnectivity.gateways (
gatewayName,
resourceGroupName,
subscriptionId,
properties,
tags,
location
)
SELECT 
'{{ gatewayName }}',
'{{ resourceGroupName }}',
'{{ subscriptionId }}',
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
        - name: operatorApiConnections
          value:
            - string
        - name: gatewayBaseUrl
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

Updates a <code>gateways</code> resource.

```sql
/*+ update */
UPDATE azure.programmableconnectivity.gateways
SET 
tags = '{{ tags }}'
WHERE 
gatewayName = '{{ gatewayName }}'
AND resourceGroupName = '{{ resourceGroupName }}'
AND subscriptionId = '{{ subscriptionId }}';
```

## `DELETE` example

Deletes the specified <code>gateways</code> resource.

```sql
/*+ delete */
DELETE FROM azure.programmableconnectivity.gateways
WHERE gatewayName = '{{ gatewayName }}'
AND resourceGroupName = '{{ resourceGroupName }}'
AND subscriptionId = '{{ subscriptionId }}';
```
