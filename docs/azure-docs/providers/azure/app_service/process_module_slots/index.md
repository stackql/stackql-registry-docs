---
title: process_module_slots
hide_title: false
hide_table_of_contents: false
keywords:
  - process_module_slots
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

Creates, updates, deletes, gets or lists a <code>process_module_slots</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>process_module_slots</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.app_service.process_module_slots" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="id" /> | `string` | Resource Id. |
| <CopyableCode code="name" /> | `string` | Resource Name. |
| <CopyableCode code="kind" /> | `string` | Kind of resource. |
| <CopyableCode code="properties" /> | `object` | ProcessModuleInfo resource specific properties |
| <CopyableCode code="type" /> | `string` | Resource type. |

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="baseAddress, name, processId, resourceGroupName, slot, subscriptionId" /> | Description for Get process information by its ID for a specific scaled-out instance in a web site. |
| <CopyableCode code="list" /> | `SELECT` | <CopyableCode code="name, processId, resourceGroupName, slot, subscriptionId" /> | Description for List module information for a process by its ID for a specific scaled-out instance in a web site. |

## `SELECT` examples

Description for List module information for a process by its ID for a specific scaled-out instance in a web site.


```sql
SELECT
id,
name,
kind,
properties,
type
FROM azure.app_service.process_module_slots
WHERE name = '{{ name }}'
AND processId = '{{ processId }}'
AND resourceGroupName = '{{ resourceGroupName }}'
AND slot = '{{ slot }}'
AND subscriptionId = '{{ subscriptionId }}';
```