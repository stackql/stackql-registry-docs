---
title: gateway_debug_credentials
hide_title: false
hide_table_of_contents: false
keywords:
  - gateway_debug_credentials
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

Creates, updates, deletes, gets or lists a <code>gateway_debug_credentials</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>gateway_debug_credentials</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.api_management.gateway_debug_credentials" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="token" /> | `string` | Gateway debug token. |

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="list" /> | `SELECT` | <CopyableCode code="gatewayId, resourceGroupName, serviceName, subscriptionId, data__apiId, data__purposes" /> | Create new debug credentials for gateway. |

## `SELECT` examples

Create new debug credentials for gateway.


```sql
SELECT
token
FROM azure.api_management.gateway_debug_credentials
WHERE gatewayId = '{{ gatewayId }}'
AND resourceGroupName = '{{ resourceGroupName }}'
AND serviceName = '{{ serviceName }}'
AND subscriptionId = '{{ subscriptionId }}'
AND data__apiId = '{{ data__apiId }}'
AND data__purposes = '{{ data__purposes }}';
```