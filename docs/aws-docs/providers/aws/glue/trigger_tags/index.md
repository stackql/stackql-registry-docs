---
title: trigger_tags
hide_title: false
hide_table_of_contents: false
keywords:
  - trigger_tags
  - glue
  - aws
  - stackql
  - infrastructure-as-code
  - configuration-as-data
  - cloud inventory
description: Query, deploy and manage AWS resources using SQL
custom_edit_url: null
image: /img/providers/aws/stackql-aws-provider-featured-image.png
---

import CopyableCode from '@site/src/components/CopyableCode/CopyableCode';
import Tabs from '@theme/Tabs';
import TabItem from '@theme/TabItem';

Expands all tag keys and values for <code>triggers</code> in a region

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>trigger_tags</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>Resource Type definition for AWS::Glue::Trigger</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="aws.glue.trigger_tags" /></td></tr>
</tbody></table>

## Fields
<table><tbody><tr><th>Name</th><th>Datatype</th><th>Description</th></tr><tr><td><CopyableCode code="type" /></td><td><code>string</code></td><td>The type of trigger that this is.</td></tr>
<tr><td><CopyableCode code="start_on_creation" /></td><td><code>boolean</code></td><td>Set to true to start SCHEDULED and CONDITIONAL triggers when created. True is not supported for ON_DEMAND triggers.</td></tr>
<tr><td><CopyableCode code="description" /></td><td><code>string</code></td><td>A description of this trigger.</td></tr>
<tr><td><CopyableCode code="actions" /></td><td><code>array</code></td><td>The actions initiated by this trigger.</td></tr>
<tr><td><CopyableCode code="event_batching_condition" /></td><td><code>object</code></td><td>Batch condition that must be met (specified number of events received or batch time window expired) before EventBridge event trigger fires.</td></tr>
<tr><td><CopyableCode code="workflow_name" /></td><td><code>string</code></td><td>The name of the workflow associated with the trigger.</td></tr>
<tr><td><CopyableCode code="schedule" /></td><td><code>string</code></td><td>A cron expression used to specify the schedule.</td></tr>
<tr><td><CopyableCode code="name" /></td><td><code>string</code></td><td>The name of the trigger.</td></tr>
<tr><td><CopyableCode code="predicate" /></td><td><code>object</code></td><td>The predicate of this trigger, which defines when it will fire.</td></tr>
<tr><td><CopyableCode code="tag_key" /></td><td><code>string</code></td><td>Tag key.</td></tr>
<tr><td><CopyableCode code="tag_value" /></td><td><code>string</code></td><td>Tag value.</td></tr>
<tr><td><CopyableCode code="region" /></td><td><code>string</code></td><td>AWS region.</td></tr>
</tbody></table>

## Methods

<table><tbody>
  <tr>
    <th>Name</th>
    <th>Accessible by</th>
    <th>Required Params</th>
  </tr>
  <tr>
    <td><CopyableCode code="list_resources" /></td>
    <td><code>SELECT</code></td>
    <td><CopyableCode code="region" /></td>
  </tr>
</tbody></table>

## `SELECT` examples
Expands tags for all <code>triggers</code> in a region.
```sql
SELECT
region,
type,
start_on_creation,
description,
actions,
event_batching_condition,
workflow_name,
schedule,
name,
predicate,
tag_key,
tag_value
FROM aws.glue.trigger_tags
WHERE region = 'us-east-1';
```


## Permissions

For permissions required to operate on the <code>trigger_tags</code> resource, see <a href="/providers/aws/glue/triggers/#permissions"><code>triggers</code></a>

