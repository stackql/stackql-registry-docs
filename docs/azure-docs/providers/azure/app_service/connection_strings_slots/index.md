---
title: connection_strings_slots
hide_title: false
hide_table_of_contents: false
keywords:
  - connection_strings_slots
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

Creates, updates, deletes, gets or lists a <code>connection_strings_slots</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>connection_strings_slots</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.app_service.connection_strings_slots" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="id" /> | `string` | Resource Id. |
| <CopyableCode code="name" /> | `string` | Resource Name. |
| <CopyableCode code="kind" /> | `string` | Kind of resource. |
| <CopyableCode code="properties" /> | `object` | Connection strings. |
| <CopyableCode code="type" /> | `string` | Resource type. |

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="list" /> | `SELECT` | <CopyableCode code="name, resourceGroupName, slot, subscriptionId" /> | Description for Gets the connection strings of an app. |
| <CopyableCode code="update" /> | `REPLACE` | <CopyableCode code="name, resourceGroupName, slot, subscriptionId" /> | Description for Replaces the connection strings of an app. |

## `SELECT` examples

Description for Gets the connection strings of an app.


```sql
SELECT
id,
name,
kind,
properties,
type
FROM azure.app_service.connection_strings_slots
WHERE name = '{{ name }}'
AND resourceGroupName = '{{ resourceGroupName }}'
AND slot = '{{ slot }}'
AND subscriptionId = '{{ subscriptionId }}';
```
## `REPLACE` example

Replaces all fields in the specified <code>connection_strings_slots</code> resource.

```sql
/*+ update */
REPLACE azure.app_service.connection_strings_slots
SET 
kind = '{{ kind }}',
properties = '{{ properties }}'
WHERE 
name = '{{ name }}'
AND resourceGroupName = '{{ resourceGroupName }}'
AND slot = '{{ slot }}'
AND subscriptionId = '{{ subscriptionId }}';
```
