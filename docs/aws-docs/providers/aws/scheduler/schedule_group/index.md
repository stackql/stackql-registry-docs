---
title: schedule_group
hide_title: false
hide_table_of_contents: false
keywords:
  - schedule_group
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

Gets or operates on an individual <code>schedule_group</code> resource, use <code>schedule_groups</code> to retrieve a list of resources or to create a resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>schedule_group</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>Definition of AWS::Scheduler::ScheduleGroup Resource Type</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="aws.scheduler.schedule_group" /></td></tr>
</tbody></table>

## Fields
<table><tbody>
<tr><th>Name</th><th>Datatype</th><th>Description</th></tr>
<tr><td><CopyableCode code="arn" /></td><td><code>string</code></td><td>The Amazon Resource Name (ARN) of the schedule group.</td></tr>
<tr><td><CopyableCode code="creation_date" /></td><td><code>string</code></td><td>The time at which the schedule group was created.</td></tr>
<tr><td><CopyableCode code="last_modification_date" /></td><td><code>string</code></td><td>The time at which the schedule group was last modified.</td></tr>
<tr><td><CopyableCode code="name" /></td><td><code>string</code></td><td></td></tr>
<tr><td><CopyableCode code="state" /></td><td><code>string</code></td><td></td></tr>
<tr><td><CopyableCode code="tags" /></td><td><code>array</code></td><td>The list of tags to associate with the schedule group.</td></tr>
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
    <td><CopyableCode code="update_resource" /></td>
    <td><code>UPDATE</code></td>
    <td><CopyableCode code="data__Identifier, data__PatchDocument, region" /></td>
  </tr>
  <tr>
    <td><CopyableCode code="delete_resource" /></td>
    <td><code>DELETE</code></td>
    <td><CopyableCode code="data__Identifier, region" /></td>
  </tr>
  <tr>
    <td><CopyableCode code="get_resource" /></td>
    <td><code>SELECT</code></td>
    <td><CopyableCode code="data__Identifier, region" /></td>
  </tr>
</tbody></table>

## `SELECT` Example
```sql
SELECT
region,
arn,
creation_date,
last_modification_date,
name,
state,
tags
FROM aws.scheduler.schedule_group
WHERE data__Identifier = '<Name>';
```

## Permissions

To operate on the <code>schedule_group</code> resource, the following permissions are required:

### Read
```json
scheduler:GetScheduleGroup,
scheduler:ListTagsForResource
```

### Update
```json
scheduler:TagResource,
scheduler:UntagResource,
scheduler:ListTagsForResource,
scheduler:GetScheduleGroup
```

### Delete
```json
scheduler:DeleteScheduleGroup,
scheduler:GetScheduleGroup,
scheduler:DeleteSchedule
```

