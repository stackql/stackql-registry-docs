---
title: logging_configurations
hide_title: false
hide_table_of_contents: false
keywords:
  - logging_configurations
  - ivschat
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


Used to retrieve a list of <code>logging_configurations</code> in a region or to create or delete a <code>logging_configurations</code> resource, use <code>logging_configuration</code> to read or update an individual resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>logging_configurations</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>Resource type definition for AWS::IVSChat::LoggingConfiguration.</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="aws.ivschat.logging_configurations" /></td></tr>
</tbody></table>

## Fields
<table><tbody>
<tr><th>Name</th><th>Datatype</th><th>Description</th></tr>
<tr><td><CopyableCode code="arn" /></td><td><code>string</code></td><td>LoggingConfiguration ARN is automatically generated on creation and assigned as the unique identifier.</td></tr>
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
arn
FROM aws.ivschat.logging_configurations
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
 "DestinationConfiguration": {
  "CloudWatchLogs": {
   "LogGroupName": "{{ LogGroupName }}"
  },
  "Firehose": {
   "DeliveryStreamName": "{{ DeliveryStreamName }}"
  },
  "S3": {
   "BucketName": "{{ BucketName }}"
  }
 }
}
>>>
--required properties only
INSERT INTO aws.ivschat.logging_configurations (
 DestinationConfiguration,
 region
)
SELECT 
{{ .DestinationConfiguration }},
'us-east-1';
```
</TabItem>
<TabItem value="all">

```sql
<<<json
{
 "DestinationConfiguration": {
  "CloudWatchLogs": {
   "LogGroupName": "{{ LogGroupName }}"
  },
  "Firehose": {
   "DeliveryStreamName": "{{ DeliveryStreamName }}"
  },
  "S3": {
   "BucketName": "{{ BucketName }}"
  }
 },
 "Name": "{{ Name }}",
 "Tags": [
  {
   "Key": "{{ Key }}",
   "Value": "{{ Value }}"
  }
 ]
}
>>>
--all properties
INSERT INTO aws.ivschat.logging_configurations (
 DestinationConfiguration,
 Name,
 Tags,
 region
)
SELECT 
 {{ .DestinationConfiguration }},
 {{ .Name }},
 {{ .Tags }},
 'us-east-1';
```
</TabItem>
</Tabs>

## `DELETE` Example

```sql
DELETE FROM aws.ivschat.logging_configurations
WHERE data__Identifier = '<Arn>'
AND region = 'us-east-1';
```

## Permissions

To operate on the <code>logging_configurations</code> resource, the following permissions are required:

### Create
```json
ivschat:CreateLoggingConfiguration,
ivschat:GetLoggingConfiguration,
logs:CreateLogDelivery,
logs:PutResourcePolicy,
logs:DescribeResourcePolicies,
logs:DescribeLogGroups,
s3:PutBucketPolicy,
s3:GetBucketPolicy,
iam:CreateServiceLinkedRole,
firehose:TagDeliveryStream,
ivschat:TagResource
```

### Delete
```json
ivschat:DeleteLoggingConfiguration,
ivschat:GetLoggingConfiguration,
logs:DeleteLogDelivery,
logs:ListLogDeliveries,
ivschat:UntagResource,
logs:GetLogDelivery
```

### List
```json
ivschat:ListLoggingConfigurations,
ivschat:ListTagsForResource
```

