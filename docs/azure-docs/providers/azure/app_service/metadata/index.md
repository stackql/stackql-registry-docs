---
title: metadata
hide_title: false
hide_table_of_contents: false
keywords:
  - metadata
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

Creates, updates, deletes, gets or lists a <code>metadata</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>metadata</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.app_service.metadata" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="id" /> | `string` | Resource Id. |
| <CopyableCode code="name" /> | `string` | Resource Name. |
| <CopyableCode code="kind" /> | `string` | Kind of resource. |
| <CopyableCode code="properties" /> | `object` | Settings. |
| <CopyableCode code="type" /> | `string` | Resource type. |

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="list" /> | `SELECT` | <CopyableCode code="name, resourceGroupName, subscriptionId" /> | Description for Gets the metadata of an app. |
| <CopyableCode code="update" /> | `REPLACE` | <CopyableCode code="name, resourceGroupName, subscriptionId" /> | Description for Replaces the metadata of an app. |

## `SELECT` examples

Description for Gets the metadata of an app.


```sql
SELECT
id,
name,
kind,
properties,
type
FROM azure.app_service.metadata
WHERE name = '{{ name }}'
AND resourceGroupName = '{{ resourceGroupName }}'
AND subscriptionId = '{{ subscriptionId }}';
```
## `REPLACE` example

Replaces all fields in the specified <code>metadata</code> resource.

```sql
/*+ update */
REPLACE azure.app_service.metadata
SET 
kind = '{{ kind }}',
properties = '{{ properties }}'
WHERE 
name = '{{ name }}'
AND resourceGroupName = '{{ resourceGroupName }}'
AND subscriptionId = '{{ subscriptionId }}';
```
