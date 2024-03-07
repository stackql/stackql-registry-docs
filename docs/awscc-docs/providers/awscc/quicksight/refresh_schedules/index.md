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
Retrieves a list of <code>refresh_schedules</code> in a region

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>refresh_schedules</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>refresh_schedules</td></tr>
<tr><td><b>Id</b></td><td><code>awscc.quicksight.refresh_schedules</code></td></tr>
</tbody></table>

## Fields
<table><tbody>
<tr><th>Name</th><th>Datatype</th><th>Description</th></tr>
<tr><td><code>aws_account_id</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>data_set_id</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>schedule/schedule_id</code></td><td><code>string</code></td><td>&lt;p&gt;An unique identifier for the refresh schedule.&lt;&#x2F;p&gt;</td></tr>
<tr><td><code>region</code></td><td><code>string</code></td><td>AWS region.</td></tr>

</tbody></table>

## Methods
Currently only <code>SELECT</code> is supported for this resource resource.

## Permissions

To operate on the <code>refresh_schedules</code> resource, the following permissions are required:

### Create
<pre>
quicksight:CreateRefreshSchedule,
quicksight:DescribeRefreshSchedule</pre>

### List
<pre>
quicksight:ListRefreshSchedules</pre>


## Example
```sql
SELECT
region,
aws_account_id,
data_set_id,
schedule/schedule_id
FROM awscc.quicksight.refresh_schedules
WHERE region = 'us-east-1'
```
