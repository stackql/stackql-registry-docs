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

import CopyableCode from '@site/src/components/CopyableCode/CopyableCode';
import Tabs from '@theme/Tabs';
import TabItem from '@theme/TabItem';


Used to retrieve a list of <code>report_plans</code> in a region or to create or delete a <code>report_plans</code> resource, use <code>report_plan</code> to read or update an individual resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>report_plans</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>Contains detailed information about a report plan in AWS Backup Audit Manager.</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="aws.backup.report_plans" /></td></tr>
</tbody></table>

## Fields
<table><tbody>
<tr><th>Name</th><th>Datatype</th><th>Description</th></tr>
<tr><td><CopyableCode code="report_plan_arn" /></td><td><code>string</code></td><td>An Amazon Resource Name (ARN) that uniquely identifies a resource. The format of the ARN depends on the resource type.</td></tr>
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
report_plan_arn
FROM aws.backup.report_plans
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
 "ReportDeliveryChannel": {
  "Formats": [
   "{{ Formats[0] }}"
  ],
  "S3BucketName": "{{ S3BucketName }}",
  "S3KeyPrefix": "{{ S3KeyPrefix }}"
 },
 "ReportSetting": {
  "ReportTemplate": "{{ ReportTemplate }}",
  "FrameworkArns": [
   "{{ FrameworkArns[0] }}"
  ],
  "Accounts": [
   "{{ Accounts[0] }}"
  ],
  "OrganizationUnits": [
   "{{ OrganizationUnits[0] }}"
  ],
  "Regions": [
   "{{ Regions[0] }}"
  ]
 }
}
>>>
--required properties only
INSERT INTO aws.backup.report_plans (
 ReportDeliveryChannel,
 ReportSetting,
 region
)
SELECT 
{{ ReportDeliveryChannel }},
 {{ ReportSetting }},
'us-east-1';
```

</TabItem>
<TabItem value="all">

```sql
<<<json
{
 "ReportPlanName": "{{ ReportPlanName }}",
 "ReportPlanDescription": "{{ ReportPlanDescription }}",
 "ReportPlanTags": [
  {
   "Key": "{{ Key }}",
   "Value": "{{ Value }}"
  }
 ],
 "ReportDeliveryChannel": {
  "Formats": [
   "{{ Formats[0] }}"
  ],
  "S3BucketName": "{{ S3BucketName }}",
  "S3KeyPrefix": "{{ S3KeyPrefix }}"
 },
 "ReportSetting": {
  "ReportTemplate": "{{ ReportTemplate }}",
  "FrameworkArns": [
   "{{ FrameworkArns[0] }}"
  ],
  "Accounts": [
   "{{ Accounts[0] }}"
  ],
  "OrganizationUnits": [
   "{{ OrganizationUnits[0] }}"
  ],
  "Regions": [
   "{{ Regions[0] }}"
  ]
 }
}
>>>
--all properties
INSERT INTO aws.backup.report_plans (
 ReportPlanName,
 ReportPlanDescription,
 ReportPlanTags,
 ReportDeliveryChannel,
 ReportSetting,
 region
)
SELECT 
 {{ ReportPlanName }},
 {{ ReportPlanDescription }},
 {{ ReportPlanTags }},
 {{ ReportDeliveryChannel }},
 {{ ReportSetting }},
 'us-east-1';
```

</TabItem>
</Tabs>

## `DELETE` Example

```sql
DELETE FROM aws.backup.report_plans
WHERE data__Identifier = '<ReportPlanArn>'
AND region = 'us-east-1';
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

### Delete
```json
backup:DeleteReportPlan,
backup:DescribeReportPlan
```

### List
```json
backup:ListReportPlans
```

