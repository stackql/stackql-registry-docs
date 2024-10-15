---
title: access_review_history_definition_instances
hide_title: false
hide_table_of_contents: false
keywords:
  - access_review_history_definition_instances
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

Creates, updates, deletes, gets or lists a <code>access_review_history_definition_instances</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>access_review_history_definition_instances</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.authorization.access_review_history_definition_instances" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="id" /> | `string` | The access review history definition instance id. |
| <CopyableCode code="name" /> | `string` | The access review history definition instance unique id. |
| <CopyableCode code="properties" /> | `object` | Access Review History Definition Instance properties. |
| <CopyableCode code="type" /> | `string` | The resource type. |

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="list" /> | `SELECT` | <CopyableCode code="historyDefinitionId, subscriptionId" /> | Get access review history definition instances by definition Id |
| <CopyableCode code="generate_download_uri" /> | `EXEC` | <CopyableCode code="historyDefinitionId, instanceId, subscriptionId" /> | Generates a uri which can be used to retrieve review history data. This URI has a TTL of 1 day and can be retrieved by fetching the accessReviewHistoryDefinition object. |

## `SELECT` examples

Get access review history definition instances by definition Id


```sql
SELECT
id,
name,
properties,
type
FROM azure.authorization.access_review_history_definition_instances
WHERE historyDefinitionId = '{{ historyDefinitionId }}'
AND subscriptionId = '{{ subscriptionId }}';
```