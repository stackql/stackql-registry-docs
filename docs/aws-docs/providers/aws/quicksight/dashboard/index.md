---
title: dashboard
hide_title: false
hide_table_of_contents: false
keywords:
  - dashboard
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
Gets an individual <code>dashboard</code> resource

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>dashboard</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>dashboard</td></tr>
<tr><td><b>Id</b></td><td><code>aws.quicksight.dashboard</code></td></tr>
</tbody></table>

## Fields
<table><tbody>
<tr><th>Name</th><th>Datatype</th><th>Description</th></tr>
<tr><td><code>arn</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>aws_account_id</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>created_time</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>dashboard_id</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>dashboard_publish_options</code></td><td><code>object</code></td><td></td></tr>
<tr><td><code>definition</code></td><td><code>object</code></td><td></td></tr>
<tr><td><code>last_published_time</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>last_updated_time</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>name</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>parameters</code></td><td><code>object</code></td><td></td></tr>
<tr><td><code>permissions</code></td><td><code>array</code></td><td></td></tr>
<tr><td><code>source_entity</code></td><td><code>object</code></td><td></td></tr>
<tr><td><code>tags</code></td><td><code>array</code></td><td></td></tr>
<tr><td><code>theme_arn</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>version</code></td><td><code>object</code></td><td></td></tr>
<tr><td><code>version_description</code></td><td><code>string</code></td><td></td></tr>
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
created_time,
dashboard_id,
dashboard_publish_options,
definition,
last_published_time,
last_updated_time,
name,
parameters,
permissions,
source_entity,
tags,
theme_arn,
version,
version_description
FROM aws.quicksight.dashboard
WHERE region = 'us-east-1'
AND data__Identifier = '<AwsAccountId>'
AND data__Identifier = '<DashboardId>'
```
