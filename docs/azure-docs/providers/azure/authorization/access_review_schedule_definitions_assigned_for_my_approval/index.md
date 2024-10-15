---
title: access_review_schedule_definitions_assigned_for_my_approval
hide_title: false
hide_table_of_contents: false
keywords:
  - access_review_schedule_definitions_assigned_for_my_approval
  - authorization
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

Creates, updates, deletes, gets or lists a <code>access_review_schedule_definitions_assigned_for_my_approval</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>access_review_schedule_definitions_assigned_for_my_approval</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.authorization.access_review_schedule_definitions_assigned_for_my_approval" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="id" /> | `string` | The access review schedule definition id. |
| <CopyableCode code="name" /> | `string` | The access review schedule definition unique id. |
| <CopyableCode code="properties" /> | `object` | Access Review. |
| <CopyableCode code="type" /> | `string` | The resource type. |

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="list" /> | `SELECT` | <CopyableCode code="" /> | Get access review instances assigned for my approval. |

## `SELECT` examples

Get access review instances assigned for my approval.


```sql
SELECT
id,
name,
properties,
type
FROM azure.authorization.access_review_schedule_definitions_assigned_for_my_approval
;
```