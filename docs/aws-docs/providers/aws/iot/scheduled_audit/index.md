---
title: scheduled_audit
hide_title: false
hide_table_of_contents: false
keywords:
  - scheduled_audit
  - iot
  - aws
  - stackql
  - infrastructure-as-code
  - configuration-as-data
  - cloud inventory
description: Query, deploy and manage AWS resources using SQL
custom_edit_url: null
image: /img/providers/aws/stackql-aws-provider-featured-image.png
---
Gets an individual <code>scheduled_audit</code> resource

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>scheduled_audit</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>Scheduled audits can be used to specify the checks you want to perform during an audit and how often the audit should be run.</td></tr>
<tr><td><b>Id</b></td><td><code>aws.iot.scheduled_audit</code></td></tr>
</tbody></table>

## Fields
<table><tbody>
<tr><th>Name</th><th>Datatype</th><th>Description</th></tr>
<tr><td><code>scheduled_audit_name</code></td><td><code>string</code></td><td>The name you want to give to the scheduled audit.</td></tr>
<tr><td><code>frequency</code></td><td><code>string</code></td><td>How often the scheduled audit takes place. Can be one of DAILY, WEEKLY, BIWEEKLY, or MONTHLY.</td></tr>
<tr><td><code>day_of_month</code></td><td><code>string</code></td><td>The day of the month on which the scheduled audit takes place. Can be 1 through 31 or LAST. This field is required if the frequency parameter is set to MONTHLY.</td></tr>
<tr><td><code>day_of_week</code></td><td><code>string</code></td><td>The day of the week on which the scheduled audit takes place. Can be one of SUN, MON, TUE,WED, THU, FRI, or SAT. This field is required if the frequency parameter is set to WEEKLY or BIWEEKLY.</td></tr>
<tr><td><code>target_check_names</code></td><td><code>array</code></td><td>Which checks are performed during the scheduled audit. Checks must be enabled for your account.</td></tr>
<tr><td><code>scheduled_audit_arn</code></td><td><code>string</code></td><td>The ARN (Amazon resource name) of the scheduled audit.</td></tr>
<tr><td><code>tags</code></td><td><code>array</code></td><td>An array of key-value pairs to apply to this resource.</td></tr>
<tr><td><code>region</code></td><td><code>string</code></td><td>AWS region.</td></tr>

</tbody></table>

## Methods

<table><tbody>
  <tr>
    <th>Name</th>
    <th>Accessible by</th>
    <th>Required Params</th>
  </tr>
  <tr>
    <td><code>update_resource</code></td>
    <td><code>UPDATE</code></td>
    <td><code>data__Identifier, data__PatchDocument, region</code></td>
  </tr>
  <tr>
    <td><code>delete_resource</code></td>
    <td><code>DELETE</code></td>
    <td><code>data__Identifier, region</code></td>
  </tr>
  <tr>
    <td><code>get_resource</code></td>
    <td><code>SELECT</code></td>
    <td><code>data__Identifier, region</code></td>
  </tr>
</tbody></table>

## `SELECT` Example
```sql
SELECT
region,
scheduled_audit_name,
frequency,
day_of_month,
day_of_week,
target_check_names,
scheduled_audit_arn,
tags
FROM aws.iot.scheduled_audit
WHERE data__Identifier = '<ScheduledAuditName>';
```

## Permissions

To operate on the <code>scheduled_audit</code> resource, the following permissions are required:

### Read
```json
iot:DescribeScheduledAudit,
iot:ListTagsForResource
```

### Update
```json
iot:UpdateScheduledAudit,
iot:ListTagsForResource,
iot:UntagResource,
iot:TagResource
```

### Delete
```json
iot:DescribeScheduledAudit,
iot:DeleteScheduledAudit
```

