---
title: hours_of_operations
hide_title: false
hide_table_of_contents: false
keywords:
  - hours_of_operations
  - connect
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

Creates, updates, deletes or gets a <code>hours_of_operation</code> resource or lists <code>hours_of_operations</code> in a region

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>hours_of_operations</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>Resource Type definition for AWS::Connect::HoursOfOperation</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="aws.connect.hours_of_operations" /></td></tr>
</tbody></table>

## Fields
<table><tbody><tr><th>Name</th><th>Datatype</th><th>Description</th></tr><tr><td><CopyableCode code="instance_arn" /></td><td><code>string</code></td><td>The identifier of the Amazon Connect instance.</td></tr>
<tr><td><CopyableCode code="name" /></td><td><code>string</code></td><td>The name of the hours of operation.</td></tr>
<tr><td><CopyableCode code="description" /></td><td><code>string</code></td><td>The description of the hours of operation.</td></tr>
<tr><td><CopyableCode code="time_zone" /></td><td><code>string</code></td><td>The time zone of the hours of operation.</td></tr>
<tr><td><CopyableCode code="config" /></td><td><code>array</code></td><td>Configuration information for the hours of operation: day, start time, and end time.</td></tr>
<tr><td><CopyableCode code="hours_of_operation_arn" /></td><td><code>string</code></td><td>The Amazon Resource Name (ARN) for the hours of operation.</td></tr>
<tr><td><CopyableCode code="tags" /></td><td><code>array</code></td><td>One or more tags.</td></tr>
<tr><td><CopyableCode code="hours_of_operation_overrides" /></td><td><code>array</code></td><td>One or more hours of operation overrides assigned to an hour of operation.</td></tr>
<tr><td><CopyableCode code="region" /></td><td><code>string</code></td><td>AWS region.</td></tr>
</tbody></table>

For more information, see <a href="https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-connect-hoursofoperation.html"><code>AWS::Connect::HoursOfOperation</code></a>.

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
    <td><CopyableCode code="InstanceArn, Name, TimeZone, Config, region" /></td>
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
Gets all <code>hours_of_operations</code> in a region.
```sql
SELECT
region,
instance_arn,
name,
description,
time_zone,
config,
hours_of_operation_arn,
tags,
hours_of_operation_overrides
FROM aws.connect.hours_of_operations
WHERE region = 'us-east-1';
```
Gets all properties from an individual <code>hours_of_operation</code>.
```sql
SELECT
region,
instance_arn,
name,
description,
time_zone,
config,
hours_of_operation_arn,
tags,
hours_of_operation_overrides
FROM aws.connect.hours_of_operations
WHERE region = 'us-east-1' AND data__Identifier = '<HoursOfOperationArn>';
```

## `INSERT` example

Use the following StackQL query and manifest file to create a new <code>hours_of_operation</code> resource, using [__`stack-deploy`__](https://pypi.org/project/stack-deploy/).

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
INSERT INTO aws.connect.hours_of_operations (
 InstanceArn,
 Name,
 TimeZone,
 Config,
 region
)
SELECT 
'{{ InstanceArn }}',
 '{{ Name }}',
 '{{ TimeZone }}',
 '{{ Config }}',
'{{ region }}';
```
</TabItem>
<TabItem value="all">

```sql
/*+ create */
INSERT INTO aws.connect.hours_of_operations (
 InstanceArn,
 Name,
 Description,
 TimeZone,
 Config,
 Tags,
 HoursOfOperationOverrides,
 region
)
SELECT 
 '{{ InstanceArn }}',
 '{{ Name }}',
 '{{ Description }}',
 '{{ TimeZone }}',
 '{{ Config }}',
 '{{ Tags }}',
 '{{ HoursOfOperationOverrides }}',
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
  - name: hours_of_operation
    props:
      - name: InstanceArn
        value: '{{ InstanceArn }}'
      - name: Name
        value: '{{ Name }}'
      - name: Description
        value: '{{ Description }}'
      - name: TimeZone
        value: '{{ TimeZone }}'
      - name: Config
        value:
          - Day: '{{ Day }}'
            StartTime:
              Hours: '{{ Hours }}'
              Minutes: '{{ Minutes }}'
            EndTime: null
      - name: Tags
        value:
          - Key: '{{ Key }}'
            Value: '{{ Value }}'
      - name: HoursOfOperationOverrides
        value:
          - OverrideName: '{{ OverrideName }}'
            OverrideDescription: '{{ OverrideDescription }}'
            EffectiveFrom: '{{ EffectiveFrom }}'
            EffectiveTill: '{{ EffectiveTill }}'
            OverrideConfig:
              - Day: '{{ Day }}'
                StartTime:
                  Hours: '{{ Hours }}'
                  Minutes: '{{ Minutes }}'
                EndTime: null
            HoursOfOperationOverrideId: '{{ HoursOfOperationOverrideId }}'

```
</TabItem>
</Tabs>

## `DELETE` example

```sql
/*+ delete */
DELETE FROM aws.connect.hours_of_operations
WHERE data__Identifier = '<HoursOfOperationArn>'
AND region = 'us-east-1';
```

## Permissions

To operate on the <code>hours_of_operations</code> resource, the following permissions are required:

### Create
```json
connect:CreateHoursOfOperation,
connect:TagResource,
connect:CreateHoursOfOperationOverride
```

### Read
```json
connect:DescribeHoursOfOperation,
connect:ListHoursOfOperationOverrides
```

### Delete
```json
connect:DeleteHoursOfOperation,
connect:UntagResource
```

### Update
```json
connect:UpdateHoursOfOperation,
connect:CreateHoursOfOperationOverride,
connect:UpdateHoursOfOperationOverride,
connect:DeleteHoursOfOperationOverride,
connect:ListHoursOfOperationOverrides,
connect:TagResource,
connect:UntagResource
```

### List
```json
connect:ListHoursOfOperations
```
