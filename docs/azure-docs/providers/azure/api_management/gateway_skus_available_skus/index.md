---
title: gateway_skus_available_skus
hide_title: false
hide_table_of_contents: false
keywords:
  - gateway_skus_available_skus
  - api_management
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

Creates, updates, deletes, gets or lists a <code>gateway_skus_available_skus</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>gateway_skus_available_skus</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.api_management.gateway_skus_available_skus" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="capacity" /> | `object` | Describes scaling information of a SKU. |
| <CopyableCode code="resourceType" /> | `string` | The type of resource the SKU applies to. |
| <CopyableCode code="sku" /> | `object` | Describes an available API Management SKU for gateways. |

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="list" /> | `SELECT` | <CopyableCode code="gatewayName, resourceGroupName, subscriptionId" /> | Gets all available SKU for a given API Management gateway |

## `SELECT` examples

Gets all available SKU for a given API Management gateway


```sql
SELECT
capacity,
resourceType,
sku
FROM azure.api_management.gateway_skus_available_skus
WHERE gatewayName = '{{ gatewayName }}'
AND resourceGroupName = '{{ resourceGroupName }}'
AND subscriptionId = '{{ subscriptionId }}';
```