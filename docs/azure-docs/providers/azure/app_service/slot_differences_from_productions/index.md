---
title: slot_differences_from_productions
hide_title: false
hide_table_of_contents: false
keywords:
  - slot_differences_from_productions
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

Creates, updates, deletes, gets or lists a <code>slot_differences_from_productions</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>slot_differences_from_productions</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.app_service.slot_differences_from_productions" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="id" /> | `string` | Resource Id. |
| <CopyableCode code="name" /> | `string` | Resource Name. |
| <CopyableCode code="kind" /> | `string` | Kind of resource. |
| <CopyableCode code="properties" /> | `object` | SlotDifference resource specific properties |
| <CopyableCode code="type" /> | `string` | Resource type. |

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="list" /> | `SELECT` | <CopyableCode code="name, resourceGroupName, subscriptionId, data__preserveVnet, data__targetSlot" /> | Description for Get the difference in configuration settings between two web app slots. |

## `SELECT` examples

Description for Get the difference in configuration settings between two web app slots.


```sql
SELECT
id,
name,
kind,
properties,
type
FROM azure.app_service.slot_differences_from_productions
WHERE name = '{{ name }}'
AND resourceGroupName = '{{ resourceGroupName }}'
AND subscriptionId = '{{ subscriptionId }}'
AND data__preserveVnet = '{{ data__preserveVnet }}'
AND data__targetSlot = '{{ data__targetSlot }}';
```