---
title: premier_add_on_slots
hide_title: false
hide_table_of_contents: false
keywords:
  - premier_add_on_slots
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

Creates, updates, deletes, gets or lists a <code>premier_add_on_slots</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>premier_add_on_slots</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.app_service.premier_add_on_slots" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="id" /> | `string` | Resource Id. |
| <CopyableCode code="name" /> | `string` | Resource Name. |
| <CopyableCode code="kind" /> | `string` | Kind of resource. |
| <CopyableCode code="location" /> | `string` | Resource Location. |
| <CopyableCode code="properties" /> | `object` | PremierAddOn resource specific properties |
| <CopyableCode code="tags" /> | `object` | Resource tags. |
| <CopyableCode code="type" /> | `string` | Resource type. |

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="name, premierAddOnName, resourceGroupName, slot, subscriptionId" /> | Description for Gets a named add-on of an app. |
| <CopyableCode code="list" /> | `SELECT` | <CopyableCode code="name, resourceGroupName, slot, subscriptionId" /> | Description for Gets the premier add-ons of an app. |
| <CopyableCode code="delete" /> | `DELETE` | <CopyableCode code="name, premierAddOnName, resourceGroupName, slot, subscriptionId" /> | Description for Delete a premier add-on from an app. |
| <CopyableCode code="update" /> | `UPDATE` | <CopyableCode code="name, premierAddOnName, resourceGroupName, slot, subscriptionId" /> | Description for Updates a named add-on of an app. |

## `SELECT` examples

Description for Gets the premier add-ons of an app.


```sql
SELECT
id,
name,
kind,
location,
properties,
tags,
type
FROM azure.app_service.premier_add_on_slots
WHERE name = '{{ name }}'
AND resourceGroupName = '{{ resourceGroupName }}'
AND slot = '{{ slot }}'
AND subscriptionId = '{{ subscriptionId }}';
```
## `UPDATE` example

Updates a <code>premier_add_on_slots</code> resource.

```sql
/*+ update */
UPDATE azure.app_service.premier_add_on_slots
SET 
kind = '{{ kind }}',
properties = '{{ properties }}'
WHERE 
name = '{{ name }}'
AND premierAddOnName = '{{ premierAddOnName }}'
AND resourceGroupName = '{{ resourceGroupName }}'
AND slot = '{{ slot }}'
AND subscriptionId = '{{ subscriptionId }}';
```

## `DELETE` example

Deletes the specified <code>premier_add_on_slots</code> resource.

```sql
/*+ delete */
DELETE FROM azure.app_service.premier_add_on_slots
WHERE name = '{{ name }}'
AND premierAddOnName = '{{ premierAddOnName }}'
AND resourceGroupName = '{{ resourceGroupName }}'
AND slot = '{{ slot }}'
AND subscriptionId = '{{ subscriptionId }}';
```
