---
title: report_plan
hide_title: false
hide_table_of_contents: false
keywords:
  - report_plan
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
Gets an individual <code>report_plan</code> resource

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>report_plan</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>report_plan</td></tr>
<tr><td><b>Id</b></td><td><code>aws.backup.report_plan</code></td></tr>
</tbody></table>

## Fields
<table><tbody>
<tr><th>Name</th><th>Datatype</th><th>Description</th></tr>
<tr><td><code>report_plan_name</code></td><td><code>string</code></td><td>The unique name of the report plan. The name must be between 1 and 256 characters, starting with a letter, and consisting of letters (a-z, A-Z), numbers (0-9), and underscores (_).</td></tr>
<tr><td><code>report_plan_arn</code></td><td><code>string</code></td><td>An Amazon Resource Name (ARN) that uniquely identifies a resource. The format of the ARN depends on the resource type.</td></tr>
<tr><td><code>report_plan_description</code></td><td><code>string</code></td><td>An optional description of the report plan with a maximum of 1,024 characters.</td></tr>
<tr><td><code>report_plan_tags</code></td><td><code>array</code></td><td>Metadata that you can assign to help organize the report plans that you create. Each tag is a key-value pair.</td></tr>
<tr><td><code>report_delivery_channel</code></td><td><code>object</code></td><td>A structure that contains information about where and how to deliver your reports, specifically your Amazon S3 bucket name, S3 key prefix, and the formats of your reports.</td></tr>
<tr><td><code>report_setting</code></td><td><code>object</code></td><td>Identifies the report template for the report. Reports are built using a report template.</td></tr>
<tr><td><code>region</code></td><td><code>string</code></td><td>AWS region.</td></tr>

</tbody></table>

## Methods
Currently only <code>SELECT</code> is supported for this resource resource.

## Example
```sql
SELECT
region,
report_plan_name,
report_plan_arn,
report_plan_description,
report_plan_tags,
report_delivery_channel,
report_setting
FROM aws.backup.report_plan
WHERE region = 'us-east-1'
AND data__Identifier = '&lt;ReportPlanArn&gt;'
```
