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

Use the following StackQL query and manifest file to create a new <code>canary</code> resource, using <a ref="https://pypi.org/project/stack-deploy/" target="_blank"><code><b>stack-deploy</b></code></a>.

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
-- canary.iql (required properties only)
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
-- canary.iql (all properties)
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

