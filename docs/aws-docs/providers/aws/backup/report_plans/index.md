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

Creates, updates, deletes or gets a <code>report_plan</code> resource or lists <code>report_plans</code> in a region

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>report_plans</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>Contains detailed information about a report plan in AWS Backup Audit Manager.</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="aws.backup.report_plans" /></td></tr>
</tbody></table>

## Fields
<table><tbody><tr><th>Name</th><th>Datatype</th><th>Description</th></tr><tr><td><CopyableCode code="report_plan_name" /></td><td><code>string</code></td><td>The unique name of the report plan. The name must be between 1 and 256 characters, starting with a letter, and consisting of letters (a-z, A-Z), numbers (0-9), and underscores (_).</td></tr>
<tr><td><CopyableCode code="report_plan_arn" /></td><td><code>string</code></td><td>An Amazon Resource Name (ARN) that uniquely identifies a resource. The format of the ARN depends on the resource type.</td></tr>
<tr><td><CopyableCode code="report_plan_description" /></td><td><code>string</code></td><td>An optional description of the report plan with a maximum of 1,024 characters.</td></tr>
<tr><td><CopyableCode code="report_plan_tags" /></td><td><code>array</code></td><td>Metadata that you can assign to help organize the report plans that you create. Each tag is a key-value pair.</td></tr>
<tr><td><CopyableCode code="report_delivery_channel" /></td><td><code>object</code></td><td>A structure that contains information about where and how to deliver your reports, specifically your Amazon S3 bucket name, S3 key prefix, and the formats of your reports.</td></tr>
<tr><td><CopyableCode code="report_setting" /></td><td><code>object</code></td><td>Identifies the report template for the report. Reports are built using a report template.</td></tr>
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
    <td><CopyableCode code="ReportDeliveryChannel, ReportSetting, region" /></td>
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
Gets all <code>report_plans</code> in a region.
```sql
SELECT
region,
report_plan_name,
report_plan_arn,
report_plan_description,
report_plan_tags,
report_delivery_channel,
report_setting
FROM aws.backup.report_plans
WHERE region = 'us-east-1';
```
Gets all properties from an individual <code>report_plan</code>.
```sql
SELECT
region,
report_plan_name,
report_plan_arn,
report_plan_description,
report_plan_tags,
report_delivery_channel,
report_setting
FROM aws.backup.report_plans
WHERE region = 'us-east-1' AND data__Identifier = '<ReportPlanArn>';
```

## `INSERT` example

Use the following StackQL query and manifest file to create a new <code>report_plan</code> resource, using [__`stack-deploy`__](https://pypi.org/project/stack-deploy/).

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
INSERT INTO aws.backup.report_plans (
 ReportDeliveryChannel,
 ReportSetting,
 region
)
SELECT 
'{{ ReportDeliveryChannel }}',
 '{{ ReportSetting }}',
'{{ region }}';
```
</TabItem>
<TabItem value="all">

```sql
/*+ create */
INSERT INTO aws.backup.report_plans (
 ReportPlanName,
 ReportPlanDescription,
 ReportPlanTags,
 ReportDeliveryChannel,
 ReportSetting,
 region
)
SELECT 
 '{{ ReportPlanName }}',
 '{{ ReportPlanDescription }}',
 '{{ ReportPlanTags }}',
 '{{ ReportDeliveryChannel }}',
 '{{ ReportSetting }}',
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
  - name: report_plan
    props:
      - name: ReportPlanName
        value: '{{ ReportPlanName }}'
      - name: ReportPlanDescription
        value: '{{ ReportPlanDescription }}'
      - name: ReportPlanTags
        value:
          - Key: '{{ Key }}'
            Value: '{{ Value }}'
      - name: ReportDeliveryChannel
        value:
          Formats:
            - '{{ Formats[0] }}'
          S3BucketName: '{{ S3BucketName }}'
          S3KeyPrefix: '{{ S3KeyPrefix }}'
      - name: ReportSetting
        value:
          ReportTemplate: '{{ ReportTemplate }}'
          FrameworkArns:
            - '{{ FrameworkArns[0] }}'
          Accounts:
            - '{{ Accounts[0] }}'
          OrganizationUnits:
            - '{{ OrganizationUnits[0] }}'
          Regions:
            - '{{ Regions[0] }}'

```
</TabItem>
</Tabs>

## `DELETE` example

```sql
/*+ delete */
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

### Read
```json
backup:DescribeReportPlan,
backup:ListTags
```

### Update
```json
backup:DescribeReportPlan,
backup:UpdateReportPlan,
backup:ListTags,
backup:UntagResource,
backup:TagResource
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

