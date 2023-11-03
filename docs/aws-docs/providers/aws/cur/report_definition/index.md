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
Gets an individual <code>report_definition</code> resource

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>report_definition</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>aws.cur.report_definition</code></td></tr>
</tbody></table>

## Fields
<table><tbody>
<tr><th>Name</th><th>Datatype</th><th>Description</th></tr>
<tr><td><code>ReportName</code></td><td><code>string</code></td><td>The name of the report that you want to create. The name must be unique, is case sensitive, and can't include spaces.</td></tr><tr><td><code>TimeUnit</code></td><td><code>string</code></td><td>The granularity of the line items in the report.</td></tr><tr><td><code>Format</code></td><td><code>string</code></td><td>The format that AWS saves the report in.</td></tr><tr><td><code>Compression</code></td><td><code>string</code></td><td>The compression format that AWS uses for the report.</td></tr><tr><td><code>AdditionalSchemaElements</code></td><td><code>array</code></td><td>A list of strings that indicate additional content that Amazon Web Services includes in the report, such as individual resource IDs.</td></tr><tr><td><code>S3Bucket</code></td><td><code>string</code></td><td>The S3 bucket where AWS delivers the report.</td></tr><tr><td><code>S3Prefix</code></td><td><code>string</code></td><td>The prefix that AWS adds to the report name when AWS delivers the report. Your prefix can't include spaces.</td></tr><tr><td><code>S3Region</code></td><td><code>string</code></td><td>The region of the S3 bucket that AWS delivers the report into.</td></tr><tr><td><code>AdditionalArtifacts</code></td><td><code>array</code></td><td>A list of manifests that you want Amazon Web Services to create for this report.</td></tr><tr><td><code>RefreshClosedReports</code></td><td><code>boolean</code></td><td>Whether you want Amazon Web Services to update your reports after they have been finalized if Amazon Web Services detects charges related to previous months. These charges can include refunds, credits, or support fees.</td></tr><tr><td><code>ReportVersioning</code></td><td><code>string</code></td><td>Whether you want Amazon Web Services to overwrite the previous version of each report or to deliver the report in addition to the previous versions.</td></tr><tr><td><code>BillingViewArn</code></td><td><code>string</code></td><td>The Amazon resource name of the billing view. You can get this value by using the billing view service public APIs.</td></tr>
</tbody></table>

## Methods
Currently only <code>SELECT</code> is supported for this resource resource.

## Example
```sql
SELECT * 
FROM aws.cur.report_definition
WHERE region = 'us-east-1' AND data__Identifier = '{ReportName}'
```
