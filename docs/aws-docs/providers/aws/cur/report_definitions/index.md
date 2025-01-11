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

import CopyableCode from '@site/src/components/CopyableCode/CopyableCode';
import Tabs from '@theme/Tabs';
import TabItem from '@theme/TabItem';

Creates, updates, deletes or gets a <code>report_definition</code> resource or lists <code>report_definitions</code> in a region

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>report_definitions</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>The AWS::CUR::ReportDefinition resource creates a Cost & Usage Report with user-defined settings. You can use this resource to define settings like time granularity (hourly, daily, monthly), file format (Parquet, CSV), and S3 bucket for delivery of these reports.</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="aws.cur.report_definitions" /></td></tr>
</tbody></table>

## Fields
<table><tbody><tr><th>Name</th><th>Datatype</th><th>Description</th></tr><tr><td><CopyableCode code="report_name" /></td><td><code>string</code></td><td>The name of the report that you want to create. The name must be unique, is case sensitive, and can't include spaces.</td></tr>
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

For more information, see <a href="https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-cur-reportdefinition.html"><code>AWS::CUR::ReportDefinition</code></a>.

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
    <td><CopyableCode code="ReportName, TimeUnit, Format, Compression, S3Bucket, S3Prefix, S3Region, RefreshClosedReports, ReportVersioning, region" /></td>
  </tr>
  <tr>
    <td><CopyableCode code="delete_resource" /></td>
    <td><code>DELETE</code></td>
    <td><CopyableCode code="data__Identifier, region" /></td>
  </tr>
  <tr>
    <td><CopyableCode code="update_resource" /></td>
    <td><code>UPDATE</code></td>
    <td><CopyableCode code="data__Identifier, data__PatchDocument, region" /></td>
  </tr>
  <tr>
    <td><CopyableCode code="list_resources" /></td>
    <td><code>SELECT</code></td>
    <td><CopyableCode code="region" /></td>
  </tr>
  <tr>
    <td><CopyableCode code="get_resource" /></td>
    <td><code>SELECT</code></td>
    <td><CopyableCode code="data__Identifier, region" /></td>
  </tr>
</tbody></table>

## `SELECT` examples
Gets all <code>report_definitions</code> in a region.
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
FROM aws.cur.report_definitions
WHERE region = 'us-east-1';
```
Gets all properties from an individual <code>report_definition</code>.
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
FROM aws.cur.report_definitions
WHERE region = 'us-east-1' AND data__Identifier = '<ReportName>';
```

## `INSERT` example

Use the following StackQL query and manifest file to create a new <code>report_definition</code> resource, using [__`stack-deploy`__](https://pypi.org/project/stack-deploy/).

<Tabs
    defaultValue="required"
    values={[
      { label: 'Required Properties', value: 'required', },
      { label: 'All Properties', value: 'all', },
      { label: 'Manifest', value: 'manifest', },
    ]
}>
<TabItem value="required">

```sql
/*+ create */
INSERT INTO aws.cur.report_definitions (
 ReportName,
 TimeUnit,
 Format,
 Compression,
 S3Bucket,
 S3Prefix,
 S3Region,
 RefreshClosedReports,
 ReportVersioning,
 region
)
SELECT 
'{{ ReportName }}',
 '{{ TimeUnit }}',
 '{{ Format }}',
 '{{ Compression }}',
 '{{ S3Bucket }}',
 '{{ S3Prefix }}',
 '{{ S3Region }}',
 '{{ RefreshClosedReports }}',
 '{{ ReportVersioning }}',
'{{ region }}';
```
</TabItem>
<TabItem value="all">

```sql
/*+ create */
INSERT INTO aws.cur.report_definitions (
 ReportName,
 TimeUnit,
 Format,
 Compression,
 AdditionalSchemaElements,
 S3Bucket,
 S3Prefix,
 S3Region,
 AdditionalArtifacts,
 RefreshClosedReports,
 ReportVersioning,
 BillingViewArn,
 region
)
SELECT 
 '{{ ReportName }}',
 '{{ TimeUnit }}',
 '{{ Format }}',
 '{{ Compression }}',
 '{{ AdditionalSchemaElements }}',
 '{{ S3Bucket }}',
 '{{ S3Prefix }}',
 '{{ S3Region }}',
 '{{ AdditionalArtifacts }}',
 '{{ RefreshClosedReports }}',
 '{{ ReportVersioning }}',
 '{{ BillingViewArn }}',
 '{{ region }}';
```
</TabItem>
<TabItem value="manifest">

```yaml
version: 1
name: stack name
description: stack description
providers:
  - aws
globals:
  - name: region
    value: '{{ vars.AWS_REGION }}'
resources:
  - name: report_definition
    props:
      - name: ReportName
        value: '{{ ReportName }}'
      - name: TimeUnit
        value: '{{ TimeUnit }}'
      - name: Format
        value: '{{ Format }}'
      - name: Compression
        value: '{{ Compression }}'
      - name: AdditionalSchemaElements
        value:
          - '{{ AdditionalSchemaElements[0] }}'
      - name: S3Bucket
        value: '{{ S3Bucket }}'
      - name: S3Prefix
        value: '{{ S3Prefix }}'
      - name: S3Region
        value: '{{ S3Region }}'
      - name: AdditionalArtifacts
        value:
          - '{{ AdditionalArtifacts[0] }}'
      - name: RefreshClosedReports
        value: '{{ RefreshClosedReports }}'
      - name: ReportVersioning
        value: '{{ ReportVersioning }}'
      - name: BillingViewArn
        value: '{{ BillingViewArn }}'

```
</TabItem>
</Tabs>

## `DELETE` example

```sql
/*+ delete */
DELETE FROM aws.cur.report_definitions
WHERE data__Identifier = '<ReportName>'
AND region = 'us-east-1';
```

## Permissions

To operate on the <code>report_definitions</code> resource, the following permissions are required:

### Create
```json
cur:PutReportDefinition,
cur:DescribeReportDefinitions
```

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
cur:DeleteReportDefinition
```

### List
```json
cur:DescribeReportDefinitions
```
