---
title: schedule_group_tags
hide_title: false
hide_table_of_contents: false
keywords:
  - schedule_group_tags
  - scheduler
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

Expands all tag keys and values for <code>schedule_groups</code> in a region

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>schedule_group_tags</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>Definition of AWS::Scheduler::ScheduleGroup Resource Type</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="aws.scheduler.schedule_group_tags" /></td></tr>
</tbody></table>

## Fields
<table><tbody><tr><th>Name</th><th>Datatype</th><th>Description</th></tr><tr><td><CopyableCode code="arn" /></td><td><code>string</code></td><td>The Amazon Resource Name (ARN) of the schedule group.</td></tr>
<tr><td><CopyableCode code="creation_date" /></td><td><code>string</code></td><td>The time at which the schedule group was created.</td></tr>
<tr><td><CopyableCode code="last_modification_date" /></td><td><code>string</code></td><td>The time at which the schedule group was last modified.</td></tr>
<tr><td><CopyableCode code="name" /></td><td><code>string</code></td><td></td></tr>
<tr><td><CopyableCode code="state" /></td><td><code>string</code></td><td>Specifies the state of the schedule group.</td></tr>
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
Expands tags for all <code>schedule_groups</code> in a region.
```sql
SELECT
region,
arn,
creation_date,
last_modification_date,
name,
state,
tag_key,
tag_value
FROM aws.scheduler.schedule_group_tags
WHERE region = 'us-east-1';
```


## Permissions

For permissions required to operate on the <code>schedule_group_tags</code> resource, see <a href="/providers/aws/scheduler/schedule_groups/#permissions"><code>schedule_groups</code></a>


