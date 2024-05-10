---
title: canaries
hide_title: false
hide_table_of_contents: false
keywords:
  - canaries
  - synthetics
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


Used to retrieve a list of <code>canaries</code> in a region or to create or delete a <code>canaries</code> resource, use <code>canary</code> to read or update an individual resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>canaries</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>Resource Type definition for AWS::Synthetics::Canary</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="aws.synthetics.canaries" /></td></tr>
</tbody></table>

## Fields
<table><tbody>
<tr><th>Name</th><th>Datatype</th><th>Description</th></tr>
<tr><td><CopyableCode code="name" /></td><td><code>string</code></td><td>Name of the canary.</td></tr>
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
name
FROM aws.synthetics.canaries
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
 "Name": "{{ Name }}",
 "Code": {
  "S3Bucket": "{{ S3Bucket }}",
  "S3Key": "{{ S3Key }}",
  "S3ObjectVersion": "{{ S3ObjectVersion }}",
  "Script": "{{ Script }}",
  "Handler": "{{ Handler }}",
  "SourceLocationArn": "{{ SourceLocationArn }}"
 },
 "ArtifactS3Location": "{{ ArtifactS3Location }}",
 "Schedule": {
  "Expression": "{{ Expression }}",
  "DurationInSeconds": "{{ DurationInSeconds }}"
 },
 "ExecutionRoleArn": "{{ ExecutionRoleArn }}",
 "RuntimeVersion": "{{ RuntimeVersion }}"
}
>>>
--required properties only
INSERT INTO aws.synthetics.canaries (
 Name,
 Code,
 ArtifactS3Location,
 Schedule,
 ExecutionRoleArn,
 RuntimeVersion,
 region
)
SELECT 
{{ Name }},
 {{ Code }},
 {{ ArtifactS3Location }},
 {{ Schedule }},
 {{ ExecutionRoleArn }},
 {{ RuntimeVersion }},
'us-east-1';
```

</TabItem>
<TabItem value="all">

```sql
<<<json
{
 "Name": "{{ Name }}",
 "Code": {
  "S3Bucket": "{{ S3Bucket }}",
  "S3Key": "{{ S3Key }}",
  "S3ObjectVersion": "{{ S3ObjectVersion }}",
  "Script": "{{ Script }}",
  "Handler": "{{ Handler }}",
  "SourceLocationArn": "{{ SourceLocationArn }}"
 },
 "ArtifactS3Location": "{{ ArtifactS3Location }}",
 "ArtifactConfig": {
  "S3Encryption": {
   "EncryptionMode": "{{ EncryptionMode }}",
   "KmsKeyArn": "{{ KmsKeyArn }}"
  }
 },
 "Schedule": {
  "Expression": "{{ Expression }}",
  "DurationInSeconds": "{{ DurationInSeconds }}"
 },
 "ExecutionRoleArn": "{{ ExecutionRoleArn }}",
 "RuntimeVersion": "{{ RuntimeVersion }}",
 "SuccessRetentionPeriod": "{{ SuccessRetentionPeriod }}",
 "FailureRetentionPeriod": "{{ FailureRetentionPeriod }}",
 "Tags": [
  {
   "Key": "{{ Key }}",
   "Value": "{{ Value }}"
  }
 ],
 "VPCConfig": {
  "VpcId": "{{ VpcId }}",
  "SubnetIds": [
   "{{ SubnetIds[0] }}"
  ],
  "SecurityGroupIds": [
   "{{ SecurityGroupIds[0] }}"
  ]
 },
 "RunConfig": {
  "TimeoutInSeconds": "{{ TimeoutInSeconds }}",
  "MemoryInMB": "{{ MemoryInMB }}",
  "ActiveTracing": "{{ ActiveTracing }}",
  "EnvironmentVariables": {}
 },
 "StartCanaryAfterCreation": "{{ StartCanaryAfterCreation }}",
 "VisualReference": {
  "BaseCanaryRunId": "{{ BaseCanaryRunId }}",
  "BaseScreenshots": [
   {
    "ScreenshotName": "{{ ScreenshotName }}",
    "IgnoreCoordinates": [
     "{{ IgnoreCoordinates[0] }}"
    ]
   }
  ]
 },
 "DeleteLambdaResourcesOnCanaryDeletion": "{{ DeleteLambdaResourcesOnCanaryDeletion }}"
}
>>>
--all properties
INSERT INTO aws.synthetics.canaries (
 Name,
 Code,
 ArtifactS3Location,
 ArtifactConfig,
 Schedule,
 ExecutionRoleArn,
 RuntimeVersion,
 SuccessRetentionPeriod,
 FailureRetentionPeriod,
 Tags,
 VPCConfig,
 RunConfig,
 StartCanaryAfterCreation,
 VisualReference,
 DeleteLambdaResourcesOnCanaryDeletion,
 region
)
SELECT 
 {{ Name }},
 {{ Code }},
 {{ ArtifactS3Location }},
 {{ ArtifactConfig }},
 {{ Schedule }},
 {{ ExecutionRoleArn }},
 {{ RuntimeVersion }},
 {{ SuccessRetentionPeriod }},
 {{ FailureRetentionPeriod }},
 {{ Tags }},
 {{ VPCConfig }},
 {{ RunConfig }},
 {{ StartCanaryAfterCreation }},
 {{ VisualReference }},
 {{ DeleteLambdaResourcesOnCanaryDeletion }},
 'us-east-1';
```

</TabItem>
</Tabs>

## `DELETE` Example

```sql
DELETE FROM aws.synthetics.canaries
WHERE data__Identifier = '<Name>'
AND region = 'us-east-1';
```

## Permissions

To operate on the <code>canaries</code> resource, the following permissions are required:

### Create
```json
synthetics:CreateCanary,
synthetics:StartCanary,
synthetics:GetCanary,
synthetics:TagResource,
s3:CreateBucket,
s3:GetObject,
s3:GetObjectVersion,
s3:PutBucketEncryption,
s3:PutEncryptionConfiguration,
s3:GetBucketLocation,
lambda:CreateFunction,
lambda:AddPermission,
lambda:PublishVersion,
lambda:UpdateFunctionConfiguration,
lambda:GetFunctionConfiguration,
lambda:GetLayerVersionByArn,
lambda:GetLayerVersion,
lambda:PublishLayerVersion,
ec2:DescribeVpcs,
ec2:DescribeSubnets,
ec2:DescribeSecurityGroups,
iam:PassRole
```

### Delete
```json
synthetics:DeleteCanary,
synthetics:GetCanary
```

### List
```json
synthetics:DescribeCanaries
```

