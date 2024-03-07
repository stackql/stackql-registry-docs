---
title: report_definitions
hide_title: false
hide_table_of_contents: false
keywords:
  - report_definitions
  - cur
  - aws
  - stackql
  - infrastructure-as-code
  - configuration-as-data
  - cloud inventory
description: Query, deploy and manage AWS resources using SQL
custom_edit_url: null
image: /img/providers/aws/stackql-aws-provider-featured-image.png
---
Retrieves a list of <code>report_definitions</code> in a region

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>report_definitions</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>report_definitions</td></tr>
<tr><td><b>Id</b></td><td><code>awscc.cur.report_definitions</code></td></tr>
</tbody></table>

## Fields
<table><tbody>
<tr><th>Name</th><th>Datatype</th><th>Description</th></tr>
<tr><td><code>report_name</code></td><td><code>string</code></td><td>The name of the report that you want to create. The name must be unique, is case sensitive, and can't include spaces.</td></tr>
<tr><td><code>region</code></td><td><code>string</code></td><td>AWS region.</td></tr>

</tbody></table>

## Methods
Currently only <code>SELECT</code> is supported for this resource resource.

## Permissions

To operate on the <code>report_definitions</code> resource, the following permissions are required:

### Create
```json
cur:PutReportDefinition
```

### List
```json
cur:DescribeReportDefinitions
```


## Example
```sql
SELECT
region,
report_name
FROM awscc.cur.report_definitions
WHERE region = 'us-east-1'
```
