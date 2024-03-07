---
title: report_plans
hide_title: false
hide_table_of_contents: false
keywords:
  - report_plans
  - backup
  - aws
  - stackql
  - infrastructure-as-code
  - configuration-as-data
  - cloud inventory
description: Query, deploy and manage AWS resources using SQL
custom_edit_url: null
image: /img/providers/aws/stackql-aws-provider-featured-image.png
---
Retrieves a list of <code>report_plans</code> in a region

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>report_plans</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>report_plans</td></tr>
<tr><td><b>Id</b></td><td><code>awscc.backup.report_plans</code></td></tr>
</tbody></table>

## Fields
<table><tbody>
<tr><th>Name</th><th>Datatype</th><th>Description</th></tr>
<tr><td><code>report_plan_arn</code></td><td><code>string</code></td><td>An Amazon Resource Name (ARN) that uniquely identifies a resource. The format of the ARN depends on the resource type.</td></tr>
<tr><td><code>region</code></td><td><code>string</code></td><td>AWS region.</td></tr>

</tbody></table>

## Methods
Currently only <code>SELECT</code> is supported for this resource resource.

## Example
```sql
SELECT
region,
report_plan_arn
FROM awscc.backup.report_plans
WHERE region = 'us-east-1'
```

## Permissions

To operate on the <code>report_plans</code> resource, the following permissions are required:

### Create
```json
backup:CreateReportPlan,
backup:DescribeReportPlan,
backup:ListTags,
backup:TagResource,
iam:CreateServiceLinkedRole
```

### List
```json
backup:ListReportPlans
```

