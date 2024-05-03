---
title: report_definition
hide_title: false
hide_table_of_contents: false
keywords:
  - report_definition
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

import CopyableCode from '@site/src/components/CopyableCode/CopyableCode';

Gets or operates on an individual <code>report_definition</code> resource, use <code>report_definitions</code> to retrieve a list of resources or to create a resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>report_definition</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>The AWS::CUR::ReportDefinition resource creates a Cost & Usage Report with user-defined settings. You can use this resource to define settings like time granularity (hourly, daily, monthly), file format (Parquet, CSV), and S3 bucket for delivery of these reports.</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="aws.cur.report_definition" /></td></tr>
</tbody></table>

## Fields
<table><tbody>
<tr><th>Name</th><th>Datatype</th><th>Description</th></tr>
<tr><td><CopyableCode code="report_name" /></td><td><code>string</code></td><td>The name of the report that you want to create. The name must be unique, is case sensitive, and can't include spaces.</td></tr>
<tr><td><CopyableCode code="time_unit" /></td><td><code>string</code></td><td>The granularity of the line items in the report.</td></tr>
<tr><td><CopyableCode code="format" /></td><td><code>string</code></td><td>The format that AWS saves the report in.</td></tr>
<tr><td><CopyableCode code="compression" /></td><td><code>string</code></td><td>The compression format that AWS uses for the report.</td></tr>
<tr><td><CopyableCode code="additional_schema_elements" /></td><td><code>array</code></td><td>A list of strings that indicate additional content that Amazon Web Services includes in the report, such as individual resource IDs.</td></tr>
<tr><td><CopyableCode code="s3_bucket" /></td><td><code>string</code></td><td>The S3 bucket where AWS delivers the report.</td></tr>
<tr><td><CopyableCode code="s3_prefix" /></td><td><code>string</code></td><td>The prefix that AWS adds to the report name when AWS delivers the report. Your prefix can't include spaces.</td></tr>
<tr><td><CopyableCode code="s3_region" /></td><td><code>string</code></td><td>The region of the S3 bucket that AWS delivers the report into.</td></tr>
<tr><td><CopyableCode code="additional_artifacts" /></td><td><code>array</code></td><td>A list of manifests that you want Amazon Web Services to create for this report.</td></tr>
<tr><td><CopyableCode code="refresh_closed_reports" /></td><td><code>boolean</code></td><td>Whether you want Amazon Web Services to update your reports after they have been finalized if Amazon Web Services detects charges related to previous months. These charges can include refunds, credits, or support fees.</td></tr>
<tr><td><CopyableCode code="report_versioning" /></td><td><code>string</code></td><td>Whether you want Amazon Web Services to overwrite the previous version of each report or to deliver the report in addition to the previous versions.</td></tr>
<tr><td><CopyableCode code="billing_view_arn" /></td><td><code>string</code></td><td>The Amazon resource name of the billing view. You can get this value by using the billing view service public APIs.</td></tr>
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
report_name,
time_unit,
format,
compression,
additional_schema_elements,
s3_bucket,
s3_prefix,
s3_region,
additional_artifacts,
refresh_closed_reports,
report_versioning,
billing_view_arn
FROM aws.cur.report_definition
WHERE data__Identifier = '<ReportName>';
```

## Permissions

To operate on the <code>report_definition</code> resource, the following permissions are required:

### Read
```json
cur:DescribeReportDefinitions
```

### Update
```json
cur:DescribeReportDefinitions,
cur:ModifyReportDefinition
```

### Delete
```json
cur:DescribeReportDefinitions,
cur:DeleteReportDefinition
```

