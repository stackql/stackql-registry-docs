---
title: vnet_connection_gateways
hide_title: false
hide_table_of_contents: false
keywords:
  - vnet_connection_gateways
  - app_service
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

Creates, updates, deletes, gets or lists a <code>vnet_connection_gateways</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>vnet_connection_gateways</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.app_service.vnet_connection_gateways" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="id" /> | `string` | Resource Id. |
| <CopyableCode code="name" /> | `string` | Resource Name. |
| <CopyableCode code="kind" /> | `string` | Kind of resource. |
| <CopyableCode code="properties" /> | `object` | VnetGateway resource specific properties |
| <CopyableCode code="type" /> | `string` | Resource type. |

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="gatewayName, name, resourceGroupName, subscriptionId, vnetName" /> | Description for Gets an app's Virtual Network gateway. |
| <CopyableCode code="create_or_update" /> | `INSERT` | <CopyableCode code="gatewayName, name, resourceGroupName, subscriptionId, vnetName" /> | Description for Adds a gateway to a connected Virtual Network (PUT) or updates it (PATCH). |
| <CopyableCode code="update" /> | `UPDATE` | <CopyableCode code="gatewayName, name, resourceGroupName, subscriptionId, vnetName" /> | Description for Adds a gateway to a connected Virtual Network (PUT) or updates it (PATCH). |

## `SELECT` examples

Description for Gets an app's Virtual Network gateway.


```sql
SELECT
id,
name,
kind,
properties,
type
FROM azure.app_service.vnet_connection_gateways
WHERE gatewayName = '{{ gatewayName }}'
AND name = '{{ name }}'
AND resourceGroupName = '{{ resourceGroupName }}'
AND subscriptionId = '{{ subscriptionId }}'
AND vnetName = '{{ vnetName }}';
```
## `INSERT` example

Use the following StackQL query and manifest file to create a new <code>vnet_connection_gateways</code> resource.

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
INSERT INTO azure.app_service.vnet_connection_gateways (
gatewayName,
name,
resourceGroupName,
subscriptionId,
vnetName,
kind,
properties
)
SELECT 
'{{ gatewayName }}',
'{{ name }}',
'{{ resourceGroupName }}',
'{{ subscriptionId }}',
'{{ vnetName }}',
'{{ kind }}',
'{{ properties }}'
;
```
</TabItem>
<TabItem value="manifest">

```yaml
- name: your_resource_model_name
  props:
    - name: id
      value: string
    - name: name
      value: string
    - name: kind
      value: string
    - name: type
      value: string
    - name: properties
      value:
        - name: vnetName
          value: string
        - name: vpnPackageUri
          value: string

```
</TabItem>
</Tabs>

## `UPDATE` example

Updates a <code>vnet_connection_gateways</code> resource.

```sql
/*+ update */
UPDATE azure.app_service.vnet_connection_gateways
SET 
kind = '{{ kind }}',
properties = '{{ properties }}'
WHERE 
gatewayName = '{{ gatewayName }}'
AND name = '{{ name }}'
AND resourceGroupName = '{{ resourceGroupName }}'
AND subscriptionId = '{{ subscriptionId }}'
AND vnetName = '{{ vnetName }}';
```
