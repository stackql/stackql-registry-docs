---
title: associations
hide_title: false
hide_table_of_contents: false
keywords:
  - associations
  - ssm
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


Used to retrieve a list of <code>associations</code> in a region or to create or delete a <code>associations</code> resource, use <code>association</code> to read or update an individual resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>associations</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>The AWS::SSM::Association resource associates an SSM document in AWS Systems Manager with EC2 instances that contain a configuration agent to process the document.</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="aws.ssm.associations" /></td></tr>
</tbody></table>

## Fields
<table><tbody>
<tr><th>Name</th><th>Datatype</th><th>Description</th></tr>
<tr><td><CopyableCode code="association_id" /></td><td><code>string</code></td><td>Unique identifier of the association.</td></tr>
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
association_id
FROM aws.ssm.associations
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
 "Name": "{{ Name }}"
}
>>>
--required properties only
INSERT INTO aws.ssm.associations (
 Name,
 region
)
SELECT 
{{ Name }},
'us-east-1';
```

</TabItem>
<TabItem value="all">

```sql
<<<json
{
 "AssociationName": "{{ AssociationName }}",
 "CalendarNames": [
  "{{ CalendarNames[0] }}"
 ],
 "ScheduleExpression": "{{ ScheduleExpression }}",
 "MaxErrors": "{{ MaxErrors }}",
 "Parameters": {},
 "InstanceId": "{{ InstanceId }}",
 "WaitForSuccessTimeoutSeconds": "{{ WaitForSuccessTimeoutSeconds }}",
 "MaxConcurrency": "{{ MaxConcurrency }}",
 "ComplianceSeverity": "{{ ComplianceSeverity }}",
 "Targets": [
  {
   "Values": [
    "{{ Values[0] }}"
   ],
   "Key": "{{ Key }}"
  }
 ],
 "SyncCompliance": "{{ SyncCompliance }}",
 "OutputLocation": {
  "S3Location": {
   "OutputS3KeyPrefix": "{{ OutputS3KeyPrefix }}",
   "OutputS3Region": "{{ OutputS3Region }}",
   "OutputS3BucketName": "{{ OutputS3BucketName }}"
  }
 },
 "ScheduleOffset": "{{ ScheduleOffset }}",
 "Name": "{{ Name }}",
 "ApplyOnlyAtCronInterval": "{{ ApplyOnlyAtCronInterval }}",
 "DocumentVersion": "{{ DocumentVersion }}",
 "AutomationTargetParameterName": "{{ AutomationTargetParameterName }}"
}
>>>
--all properties
INSERT INTO aws.ssm.associations (
 AssociationName,
 CalendarNames,
 ScheduleExpression,
 MaxErrors,
 Parameters,
 InstanceId,
 WaitForSuccessTimeoutSeconds,
 MaxConcurrency,
 ComplianceSeverity,
 Targets,
 SyncCompliance,
 OutputLocation,
 ScheduleOffset,
 Name,
 ApplyOnlyAtCronInterval,
 DocumentVersion,
 AutomationTargetParameterName,
 region
)
SELECT 
 {{ AssociationName }},
 {{ CalendarNames }},
 {{ ScheduleExpression }},
 {{ MaxErrors }},
 {{ Parameters }},
 {{ InstanceId }},
 {{ WaitForSuccessTimeoutSeconds }},
 {{ MaxConcurrency }},
 {{ ComplianceSeverity }},
 {{ Targets }},
 {{ SyncCompliance }},
 {{ OutputLocation }},
 {{ ScheduleOffset }},
 {{ Name }},
 {{ ApplyOnlyAtCronInterval }},
 {{ DocumentVersion }},
 {{ AutomationTargetParameterName }},
 'us-east-1';
```

</TabItem>
</Tabs>

## `DELETE` Example

```sql
DELETE FROM aws.ssm.associations
WHERE data__Identifier = '<AssociationId>'
AND region = 'us-east-1';
```

## Permissions

To operate on the <code>associations</code> resource, the following permissions are required:

### Create
```json
ec2:DescribeInstanceStatus,
iam:PassRole,
iam:CreateServiceLinkedRole,
ssm:CreateAssociation,
ssm:DescribeAssociation,
ssm:GetCalendarState
```

### List
```json
ssm:ListAssociations
```

### Delete
```json
ssm:DeleteAssociation
```

