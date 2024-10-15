---
title: network_trace_operation_slots
hide_title: false
hide_table_of_contents: false
keywords:
  - network_trace_operation_slots
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

Creates, updates, deletes, gets or lists a <code>network_trace_operation_slots</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>network_trace_operation_slots</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.app_service.network_trace_operation_slots" /></td></tr>
</tbody></table>

## Fields
`SELECT` not supported for this resource, use `SHOW METHODS` to view available operations for the resource.


## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="name, operationId, resourceGroupName, slot, subscriptionId" /> | Description for Gets a named operation for a network trace capturing (or deployment slot, if specified). |

## `SELECT` examples

Description for Gets a named operation for a network trace capturing (or deployment slot, if specified).


```sql
SELECT

FROM azure.app_service.network_trace_operation_slots
WHERE name = '{{ name }}'
AND operationId = '{{ operationId }}'
AND resourceGroupName = '{{ resourceGroupName }}'
AND slot = '{{ slot }}'
AND subscriptionId = '{{ subscriptionId }}';
```