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


Used to retrieve a list of <code>report_definitions</code> in a region or to create or delete a <code>report_definitions</code> resource, use <code>report_definition</code> to read or update an individual resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>report_definitions</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>The AWS::CUR::ReportDefinition resource creates a Cost & Usage Report with user-defined settings. You can use this resource to define settings like time granularity (hourly, daily, monthly), file format (Parquet, CSV), and S3 bucket for delivery of these reports.</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="aws.cur.report_definitions" /></td></tr>
</tbody></table>

## Fields
<table><tbody>
<tr><th>Name</th><th>Datatype</th><th>Description</th></tr>
<tr><td><CopyableCode code="report_name" /></td><td><code>string</code></td><td>The name of the report that you want to create. The name must be unique, is case sensitive, and can't include spaces.</td></tr>
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
    <td><CopyableCode code="create_resource" /></td>
    <td><code>INSERT</code></td>
    <td><CopyableCode code="data__DesiredState, region" /></td>
  </tr>
  <tr>
    <td><CopyableCode code="delete_resource" /></td>
    <td><code>DELETE</code></td>
    <td><CopyableCode code="data__Identifier, region" /></td>
  </tr>
  <tr>
    <td><CopyableCode code="list_resource" /></td>
    <td><code>SELECT</code></td>
    <td><CopyableCode code="region" /></td>
  </tr>
</tbody></table>

## `SELECT` Example
```sql
SELECT
region,
report_name
FROM aws.cur.report_definitions
WHERE region = 'us-east-1';
```

## `INSERT` Example

<Tabs
    defaultValue="required"
    values={[
      { label: 'Required Properties', value: 'required', },
      { label: 'All Properties', value: 'all', },
    ]
}>
<TabItem value="required">

```sql
<<<json
{
 "ReportName": "{{ ReportName }}",
 "TimeUnit": "{{ TimeUnit }}",
 "Format": "{{ Format }}",
 "Compression": "{{ Compression }}",
 "S3Bucket": "{{ S3Bucket }}",
 "S3Prefix": "{{ S3Prefix }}",
 "S3Region": "{{ S3Region }}",
 "RefreshClosedReports": "{{ RefreshClosedReports }}",
 "ReportVersioning": "{{ ReportVersioning }}"
}
>>>
--required properties only
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
{{ .ReportName }},
 {{ .TimeUnit }},
 {{ .Format }},
 {{ .Compression }},
 {{ .S3Bucket }},
 {{ .S3Prefix }},
 {{ .S3Region }},
 {{ .RefreshClosedReports }},
 {{ .ReportVersioning }},
'us-east-1';
```
</TabItem>
<TabItem value="all">

```sql
<<<json
{
 "ReportName": "{{ ReportName }}",
 "TimeUnit": "{{ TimeUnit }}",
 "Format": "{{ Format }}",
 "Compression": "{{ Compression }}",
 "AdditionalSchemaElements": [
  "{{ AdditionalSchemaElements[0] }}"
 ],
 "S3Bucket": "{{ S3Bucket }}",
 "S3Prefix": "{{ S3Prefix }}",
 "S3Region": "{{ S3Region }}",
 "AdditionalArtifacts": [
  "{{ AdditionalArtifacts[0] }}"
 ],
 "RefreshClosedReports": "{{ RefreshClosedReports }}",
 "ReportVersioning": "{{ ReportVersioning }}",
 "BillingViewArn": "{{ BillingViewArn }}"
}
>>>
--all properties
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
 {{ .ReportName }},
 {{ .TimeUnit }},
 {{ .Format }},
 {{ .Compression }},
 {{ .AdditionalSchemaElements }},
 {{ .S3Bucket }},
 {{ .S3Prefix }},
 {{ .S3Region }},
 {{ .AdditionalArtifacts }},
 {{ .RefreshClosedReports }},
 {{ .ReportVersioning }},
 {{ .BillingViewArn }},
 'us-east-1';
```
</TabItem>
</Tabs>

## `DELETE` Example

```sql
DELETE FROM aws.cur.report_definitions
WHERE data__Identifier = '<ReportName>'
AND region = 'us-east-1';
```

## Permissions

To operate on the <code>report_definitions</code> resource, the following permissions are required:

### Create
```json
cur:PutReportDefinition
```

### Delete
```json
cur:DescribeReportDefinitions,
cur:DeleteReportDefinition
```

### List
```json
cur:DescribeReportDefinitions
```

