---
title: plans_hybrid_connections
hide_title: false
hide_table_of_contents: false
keywords:
  - plans_hybrid_connections
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

Creates, updates, deletes, gets or lists a <code>plans_hybrid_connections</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>plans_hybrid_connections</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.app_service.plans_hybrid_connections" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="id" /> | `string` | Resource Id. |
| <CopyableCode code="name" /> | `string` | Resource Name. |
| <CopyableCode code="kind" /> | `string` | Kind of resource. |
| <CopyableCode code="properties" /> | `object` | HybridConnection resource specific properties |
| <CopyableCode code="type" /> | `string` | Resource type. |

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="name, namespaceName, relayName, resourceGroupName, subscriptionId" /> | Description for Retrieve a Hybrid Connection in use in an App Service plan. |
| <CopyableCode code="list" /> | `SELECT` | <CopyableCode code="name, resourceGroupName, subscriptionId" /> | Description for Retrieve all Hybrid Connections in use in an App Service plan. |
| <CopyableCode code="delete" /> | `DELETE` | <CopyableCode code="name, namespaceName, relayName, resourceGroupName, subscriptionId" /> | Description for Delete a Hybrid Connection in use in an App Service plan. |

## `SELECT` examples

Description for Retrieve all Hybrid Connections in use in an App Service plan.


```sql
SELECT
id,
name,
kind,
properties,
type
FROM azure.app_service.plans_hybrid_connections
WHERE name = '{{ name }}'
AND resourceGroupName = '{{ resourceGroupName }}'
AND subscriptionId = '{{ subscriptionId }}';
```
## `DELETE` example

Deletes the specified <code>plans_hybrid_connections</code> resource.

```sql
/*+ delete */
DELETE FROM azure.app_service.plans_hybrid_connections
WHERE name = '{{ name }}'
AND namespaceName = '{{ namespaceName }}'
AND relayName = '{{ relayName }}'
AND resourceGroupName = '{{ resourceGroupName }}'
AND subscriptionId = '{{ subscriptionId }}';
```
