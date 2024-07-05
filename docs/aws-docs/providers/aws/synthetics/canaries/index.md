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

Creates, updates, deletes or gets a <code>canary</code> resource or lists <code>canaries</code> in a region

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>canaries</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>Resource Type definition for AWS::Synthetics::Canary</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="aws.synthetics.canaries" /></td></tr>
</tbody></table>

## Fields
<table><tbody><tr><th>Name</th><th>Datatype</th><th>Description</th></tr><tr><td><CopyableCode code="name" /></td><td><code>string</code></td><td>Name of the canary.</td></tr>
<tr><td><CopyableCode code="id" /></td><td><code>string</code></td><td>Id of the canary</td></tr>
<tr><td><CopyableCode code="state" /></td><td><code>string</code></td><td>State of the canary</td></tr>
<tr><td><CopyableCode code="code" /></td><td><code>object</code></td><td>Provide the canary script source</td></tr>
<tr><td><CopyableCode code="artifact_s3_location" /></td><td><code>string</code></td><td>Provide the s3 bucket output location for test results</td></tr>
<tr><td><CopyableCode code="artifact_config" /></td><td><code>object</code></td><td>Provide artifact configuration</td></tr>
<tr><td><CopyableCode code="schedule" /></td><td><code>object</code></td><td>Frequency to run your canaries</td></tr>
<tr><td><CopyableCode code="execution_role_arn" /></td><td><code>string</code></td><td>Lambda Execution role used to run your canaries</td></tr>
<tr><td><CopyableCode code="runtime_version" /></td><td><code>string</code></td><td>Runtime version of Synthetics Library</td></tr>
<tr><td><CopyableCode code="success_retention_period" /></td><td><code>integer</code></td><td>Retention period of successful canary runs represented in number of days</td></tr>
<tr><td><CopyableCode code="failure_retention_period" /></td><td><code>integer</code></td><td>Retention period of failed canary runs represented in number of days</td></tr>
<tr><td><CopyableCode code="tags" /></td><td><code>array</code></td><td></td></tr>
<tr><td><CopyableCode code="vpc_config" /></td><td><code>object</code></td><td>Provide VPC Configuration if enabled.</td></tr>
<tr><td><CopyableCode code="run_config" /></td><td><code>object</code></td><td>Provide canary run configuration</td></tr>
<tr><td><CopyableCode code="start_canary_after_creation" /></td><td><code>boolean</code></td><td>Runs canary if set to True. Default is False</td></tr>
<tr><td><CopyableCode code="visual_reference" /></td><td><code>object</code></td><td>Visual reference configuration for visual testing</td></tr>
<tr><td><CopyableCode code="delete_lambda_resources_on_canary_deletion" /></td><td><code>boolean</code></td><td>Deletes associated lambda resources created by Synthetics if set to True. Default is False</td></tr>
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
    <td><CopyableCode code="Name, Code, ArtifactS3Location, ExecutionRoleArn, Schedule, RuntimeVersion, region" /></td>
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
Gets all <code>canaries</code> in a region.
```sql
SELECT
region,
name,
id,
state,
code,
artifact_s3_location,
artifact_config,
schedule,
execution_role_arn,
runtime_version,
success_retention_period,
failure_retention_period,
tags,
vpc_config,
run_config,
start_canary_after_creation,
visual_reference,
delete_lambda_resources_on_canary_deletion
FROM aws.synthetics.canaries
WHERE region = 'us-east-1';
```
Gets all properties from an individual <code>canary</code>.
```sql
SELECT
region,
name,
id,
state,
code,
artifact_s3_location,
artifact_config,
schedule,
execution_role_arn,
runtime_version,
success_retention_period,
failure_retention_period,
tags,
vpc_config,
run_config,
start_canary_after_creation,
visual_reference,
delete_lambda_resources_on_canary_deletion
FROM aws.synthetics.canaries
WHERE region = 'us-east-1' AND data__Identifier = '<Name>';
```

## `INSERT` example

Use the following StackQL query and manifest file to create a new <code>canary</code> resource, using [__`stack-deploy`__](https://pypi.org/project/stack-deploy/).

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
'{{ Name }}',
 '{{ Code }}',
 '{{ ArtifactS3Location }}',
 '{{ Schedule }}',
 '{{ ExecutionRoleArn }}',
 '{{ RuntimeVersion }}',
'{{ region }}';
```
</TabItem>
<TabItem value="all">

```sql
/*+ create */
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
 '{{ Name }}',
 '{{ Code }}',
 '{{ ArtifactS3Location }}',
 '{{ ArtifactConfig }}',
 '{{ Schedule }}',
 '{{ ExecutionRoleArn }}',
 '{{ RuntimeVersion }}',
 '{{ SuccessRetentionPeriod }}',
 '{{ FailureRetentionPeriod }}',
 '{{ Tags }}',
 '{{ VPCConfig }}',
 '{{ RunConfig }}',
 '{{ StartCanaryAfterCreation }}',
 '{{ VisualReference }}',
 '{{ DeleteLambdaResourcesOnCanaryDeletion }}',
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
  - name: canary
    props:
      - name: Name
        value: '{{ Name }}'
      - name: Code
        value:
          S3Bucket: '{{ S3Bucket }}'
          S3Key: '{{ S3Key }}'
          S3ObjectVersion: '{{ S3ObjectVersion }}'
          Script: '{{ Script }}'
          Handler: '{{ Handler }}'
          SourceLocationArn: '{{ SourceLocationArn }}'
      - name: ArtifactS3Location
        value: '{{ ArtifactS3Location }}'
      - name: ArtifactConfig
        value:
          S3Encryption:
            EncryptionMode: '{{ EncryptionMode }}'
            KmsKeyArn: '{{ KmsKeyArn }}'
      - name: Schedule
        value:
          Expression: '{{ Expression }}'
          DurationInSeconds: '{{ DurationInSeconds }}'
      - name: ExecutionRoleArn
        value: '{{ ExecutionRoleArn }}'
      - name: RuntimeVersion
        value: '{{ RuntimeVersion }}'
      - name: SuccessRetentionPeriod
        value: '{{ SuccessRetentionPeriod }}'
      - name: FailureRetentionPeriod
        value: '{{ FailureRetentionPeriod }}'
      - name: Tags
        value:
          - Key: '{{ Key }}'
            Value: '{{ Value }}'
      - name: VPCConfig
        value:
          VpcId: '{{ VpcId }}'
          SubnetIds:
            - '{{ SubnetIds[0] }}'
          SecurityGroupIds:
            - '{{ SecurityGroupIds[0] }}'
      - name: RunConfig
        value:
          TimeoutInSeconds: '{{ TimeoutInSeconds }}'
          MemoryInMB: '{{ MemoryInMB }}'
          ActiveTracing: '{{ ActiveTracing }}'
          EnvironmentVariables: {}
      - name: StartCanaryAfterCreation
        value: '{{ StartCanaryAfterCreation }}'
      - name: VisualReference
        value:
          BaseCanaryRunId: '{{ BaseCanaryRunId }}'
          BaseScreenshots:
            - ScreenshotName: '{{ ScreenshotName }}'
              IgnoreCoordinates:
                - '{{ IgnoreCoordinates[0] }}'
      - name: DeleteLambdaResourcesOnCanaryDeletion
        value: '{{ DeleteLambdaResourcesOnCanaryDeletion }}'

```
</TabItem>
</Tabs>

## `DELETE` example

```sql
/*+ delete */
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

### Update
```json
synthetics:UpdateCanary,
synthetics:StartCanary,
synthetics:StopCanary,
synthetics:GetCanary,
synthetics:TagResource,
synthetics:UntagResource,
s3:GetObject,
s3:GetObjectVersion,
s3:PutBucketEncryption,
s3:PutEncryptionConfiguration,
s3:GetBucketLocation,
lambda:AddPermission,
lambda:PublishVersion,
lambda:UpdateFunctionConfiguration,
lambda:GetFunctionConfiguration,
lambda:GetLayerVersionByArn,
lambda:GetLayerVersion,
lambda:PublishLayerVersion,
iam:PassRole
```

### Read
```json
synthetics:GetCanary,
synthetics:DescribeCanaries,
synthetics:ListTagsForResource,
iam:ListRoles,
s3:ListAllMyBuckets,
s3:GetBucketLocation
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

