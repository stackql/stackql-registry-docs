---
title: plans_hybrid_connection_keys
hide_title: false
hide_table_of_contents: false
keywords:
  - plans_hybrid_connection_keys
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

Creates, updates, deletes, gets or lists a <code>plans_hybrid_connection_keys</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>plans_hybrid_connection_keys</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.app_service.plans_hybrid_connection_keys" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="id" /> | `string` | Resource Id. |
| <CopyableCode code="name" /> | `string` | Resource Name. |
| <CopyableCode code="kind" /> | `string` | Kind of resource. |
| <CopyableCode code="properties" /> | `object` | HybridConnectionKey resource specific properties |
| <CopyableCode code="type" /> | `string` | Resource type. |

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="list" /> | `SELECT` | <CopyableCode code="name, namespaceName, relayName, resourceGroupName, subscriptionId" /> | Description for Get the send key name and value of a Hybrid Connection. |

## `SELECT` examples

Description for Get the send key name and value of a Hybrid Connection.


```sql
SELECT
id,
name,
kind,
properties,
type
FROM azure.app_service.plans_hybrid_connection_keys
WHERE name = '{{ name }}'
AND namespaceName = '{{ namespaceName }}'
AND relayName = '{{ relayName }}'
AND resourceGroupName = '{{ resourceGroupName }}'
AND subscriptionId = '{{ subscriptionId }}';
```