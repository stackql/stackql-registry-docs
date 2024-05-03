---
title: refresh_schedules
hide_title: false
hide_table_of_contents: false
keywords:
  - refresh_schedules
  - quicksight
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

Used to retrieve a list of <code>refresh_schedules</code> in a region or create a <code>refresh_schedules</code> resource, use <code>refresh_schedule</code> to operate on an individual resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>refresh_schedules</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>Definition of the AWS::QuickSight::RefreshSchedule Resource Type.</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="aws.quicksight.refresh_schedules" /></td></tr>
</tbody></table>

## Fields
<table><tbody>
<tr><th>Name</th><th>Datatype</th><th>Description</th></tr>
<tr><td><CopyableCode code="aws_account_id" /></td><td><code>string</code></td><td></td></tr>
<tr><td><CopyableCode code="data_set_id" /></td><td><code>string</code></td><td></td></tr>
<tr><td><CopyableCode code="schedule/schedule_id" /></td><td><code>string</code></td><td>&lt;p&gt;An unique identifier for the refresh schedule.&lt;&#x2F;p&gt;</td></tr>
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
    <td><CopyableCode code="create_resource" /></td>
    <td><code>INSERT</code></td>
    <td><CopyableCode code="data__DesiredState, region" /></td>
  </tr>
  <tr>
    <td><CopyableCode code="list_resource" /></td>
    <td><code>SELECT</code></td>
    <td><CopyableCode code="region" /></td>
  </tr>
</tbody></table>

## `SELECT` Example
```sql
SELECT
region,
aws_account_id,
data_set_id,
schedule/schedule_id
FROM aws.quicksight.refresh_schedules
WHERE region = 'us-east-1'
```

## Permissions

To operate on the <code>refresh_schedules</code> resource, the following permissions are required:

### Create
```json
quicksight:CreateRefreshSchedule,
quicksight:DescribeRefreshSchedule
```

### List
```json
quicksight:ListRefreshSchedules
```

