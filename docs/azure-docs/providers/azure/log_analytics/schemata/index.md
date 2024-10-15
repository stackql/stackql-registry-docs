---
title: schemata
hide_title: false
hide_table_of_contents: false
keywords:
  - schemata
  - log_analytics
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

Creates, updates, deletes, gets or lists a <code>schemata</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>schemata</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.log_analytics.schemata" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="name" /> | `string` | The name of the schema. |
| <CopyableCode code="displayName" /> | `string` | The display name of the schema. |
| <CopyableCode code="facet" /> | `boolean` | The boolean that indicates whether or not the field is a facet. |
| <CopyableCode code="indexed" /> | `boolean` | The boolean that indicates the field is searchable as free text. |
| <CopyableCode code="ownerType" /> | `array` | The array of workflows containing the field. |
| <CopyableCode code="stored" /> | `boolean` | The boolean that indicates whether or not the field is stored. |
| <CopyableCode code="type" /> | `string` | The type. |

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="resourceGroupName, subscriptionId, workspaceName" /> | Gets the schema for a given workspace. |

## `SELECT` examples

Gets the schema for a given workspace.


```sql
SELECT
name,
displayName,
facet,
indexed,
ownerType,
stored,
type
FROM azure.log_analytics.schemata
WHERE resourceGroupName = '{{ resourceGroupName }}'
AND subscriptionId = '{{ subscriptionId }}'
AND workspaceName = '{{ workspaceName }}';
```