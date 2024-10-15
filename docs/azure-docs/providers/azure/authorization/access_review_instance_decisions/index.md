---
title: access_review_instance_decisions
hide_title: false
hide_table_of_contents: false
keywords:
  - access_review_instance_decisions
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

Creates, updates, deletes, gets or lists a <code>access_review_instance_decisions</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>access_review_instance_decisions</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.authorization.access_review_instance_decisions" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="id" /> | `string` | The access review decision id. |
| <CopyableCode code="name" /> | `string` | The access review decision name. |
| <CopyableCode code="properties" /> | `object` | Approval Step. |
| <CopyableCode code="type" /> | `string` | The resource type. |

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="list" /> | `SELECT` | <CopyableCode code="id, scheduleDefinitionId, subscriptionId" /> | Get access review instance decisions |

## `SELECT` examples

Get access review instance decisions


```sql
SELECT
id,
name,
properties,
type
FROM azure.authorization.access_review_instance_decisions
WHERE id = '{{ id }}'
AND scheduleDefinitionId = '{{ scheduleDefinitionId }}'
AND subscriptionId = '{{ subscriptionId }}';
```