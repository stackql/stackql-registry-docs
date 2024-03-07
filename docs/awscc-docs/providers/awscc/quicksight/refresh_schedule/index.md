---
title: refresh_schedule
hide_title: false
hide_table_of_contents: false
keywords:
  - refresh_schedule
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
Gets an individual <code>refresh_schedule</code> resource

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>refresh_schedule</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>refresh_schedule</td></tr>
<tr><td><b>Id</b></td><td><code>awscc.quicksight.refresh_schedule</code></td></tr>
</tbody></table>

## Fields
<table><tbody>
<tr><th>Name</th><th>Datatype</th><th>Description</th></tr>
<tr><td><code>arn</code></td><td><code>string</code></td><td>&lt;p&gt;The Amazon Resource Name (ARN) of the data source.&lt;&#x2F;p&gt;</td></tr>
<tr><td><code>aws_account_id</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>data_set_id</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>schedule</code></td><td><code>object</code></td><td></td></tr>
<tr><td><code>region</code></td><td><code>string</code></td><td>AWS region.</td></tr>

</tbody></table>

## Methods
Currently only <code>SELECT</code> is supported for this resource resource.

## Example
```sql
SELECT
region,
arn,
aws_account_id,
data_set_id,
schedule
FROM awscc.quicksight.refresh_schedule
WHERE region = 'us-east-1'
AND data__Identifier = '{AwsAccountId}';
AND data__Identifier = '{DataSetId}';
AND data__Identifier = '{Schedule/ScheduleId}';
```

## Permissions

To operate on the <code>refresh_schedule</code> resource, the following permissions are required:

### Update
```json
quicksight:UpdateRefreshSchedule,
quicksight:DescribeRefreshSchedule
```

### Delete
```json
quicksight:DeleteRefreshSchedule,
quicksight:DescribeRefreshSchedule
```

### Read
```json
quicksight:DescribeRefreshSchedule
```

