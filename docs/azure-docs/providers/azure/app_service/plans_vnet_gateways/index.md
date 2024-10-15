---
title: plans_vnet_gateways
hide_title: false
hide_table_of_contents: false
keywords:
  - plans_vnet_gateways
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

Creates, updates, deletes, gets or lists a <code>plans_vnet_gateways</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>plans_vnet_gateways</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.app_service.plans_vnet_gateways" /></td></tr>
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
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="gatewayName, name, resourceGroupName, subscriptionId, vnetName" /> | Description for Get a Virtual Network gateway. |
| <CopyableCode code="update" /> | `REPLACE` | <CopyableCode code="gatewayName, name, resourceGroupName, subscriptionId, vnetName" /> | Description for Update a Virtual Network gateway. |

## `SELECT` examples

Description for Get a Virtual Network gateway.


```sql
SELECT
id,
name,
kind,
properties,
type
FROM azure.app_service.plans_vnet_gateways
WHERE gatewayName = '{{ gatewayName }}'
AND name = '{{ name }}'
AND resourceGroupName = '{{ resourceGroupName }}'
AND subscriptionId = '{{ subscriptionId }}'
AND vnetName = '{{ vnetName }}';
```
## `REPLACE` example

Replaces all fields in the specified <code>plans_vnet_gateways</code> resource.

```sql
/*+ update */
REPLACE azure.app_service.plans_vnet_gateways
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
