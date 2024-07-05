---
title: applications
hide_title: false
hide_table_of_contents: false
keywords:
  - applications
  - emrserverless
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

Creates, updates, deletes or gets an <code>application</code> resource or lists <code>applications</code> in a region

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>applications</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>Resource schema for AWS::EMRServerless::Application Type</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="aws.emrserverless.applications" /></td></tr>
</tbody></table>

## Fields
<table><tbody><tr><th>Name</th><th>Datatype</th><th>Description</th></tr><tr><td><CopyableCode code="architecture" /></td><td><code>string</code></td><td>The cpu architecture of an application.</td></tr>
<tr><td><CopyableCode code="name" /></td><td><code>string</code></td><td>User friendly Application name.</td></tr>
<tr><td><CopyableCode code="release_label" /></td><td><code>string</code></td><td>EMR release label.</td></tr>
<tr><td><CopyableCode code="type" /></td><td><code>string</code></td><td>The type of the application</td></tr>
<tr><td><CopyableCode code="initial_capacity" /></td><td><code>array</code></td><td>Initial capacity initialized when an Application is started.</td></tr>
<tr><td><CopyableCode code="maximum_capacity" /></td><td><code>object</code></td><td>Maximum allowed cumulative resources for an Application. No new resources will be created once the limit is hit.</td></tr>
<tr><td><CopyableCode code="tags" /></td><td><code>array</code></td><td>Tag map with key and value</td></tr>
<tr><td><CopyableCode code="auto_start_configuration" /></td><td><code>object</code></td><td>Configuration for Auto Start of Application.</td></tr>
<tr><td><CopyableCode code="auto_stop_configuration" /></td><td><code>object</code></td><td>Configuration for Auto Stop of Application.</td></tr>
<tr><td><CopyableCode code="image_configuration" /></td><td><code>object</code></td><td>The image configuration.</td></tr>
<tr><td><CopyableCode code="monitoring_configuration" /></td><td><code>object</code></td><td>Monitoring configuration for batch and interactive JobRun.</td></tr>
<tr><td><CopyableCode code="runtime_configuration" /></td><td><code>array</code></td><td>Runtime configuration for batch and interactive JobRun.</td></tr>
<tr><td><CopyableCode code="network_configuration" /></td><td><code>object</code></td><td>Network Configuration for customer VPC connectivity.</td></tr>
<tr><td><CopyableCode code="arn" /></td><td><code>string</code></td><td>The Amazon Resource Name (ARN) of the EMR Serverless Application.</td></tr>
<tr><td><CopyableCode code="application_id" /></td><td><code>string</code></td><td>The ID of the EMR Serverless Application.</td></tr>
<tr><td><CopyableCode code="worker_type_specifications" /></td><td><code>object</code></td><td>The key-value pairs that specify worker type to WorkerTypeSpecificationInput. This parameter must contain all valid worker types for a Spark or Hive application. Valid worker types include Driver and Executor for Spark applications and HiveDriver and TezTask for Hive applications. You can either set image details in this parameter for each worker type, or in imageConfiguration for all worker types.</td></tr>
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
    <td><CopyableCode code="ReleaseLabel, Type, region" /></td>
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
Gets all <code>applications</code> in a region.
```sql
SELECT
region,
architecture,
name,
release_label,
type,
initial_capacity,
maximum_capacity,
tags,
auto_start_configuration,
auto_stop_configuration,
image_configuration,
monitoring_configuration,
runtime_configuration,
network_configuration,
arn,
application_id,
worker_type_specifications
FROM aws.emrserverless.applications
WHERE region = 'us-east-1';
```
Gets all properties from an individual <code>application</code>.
```sql
SELECT
region,
architecture,
name,
release_label,
type,
initial_capacity,
maximum_capacity,
tags,
auto_start_configuration,
auto_stop_configuration,
image_configuration,
monitoring_configuration,
runtime_configuration,
network_configuration,
arn,
application_id,
worker_type_specifications
FROM aws.emrserverless.applications
WHERE region = 'us-east-1' AND data__Identifier = '<ApplicationId>';
```

## `INSERT` example

Use the following StackQL query and manifest file to create a new <code>application</code> resource, using [__`stack-deploy`__](https://pypi.org/project/stack-deploy/).

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
INSERT INTO aws.emrserverless.applications (
 ReleaseLabel,
 Type,
 region
)
SELECT 
'{{ ReleaseLabel }}',
 '{{ Type }}',
'{{ region }}';
```
</TabItem>
<TabItem value="all">

```sql
/*+ create */
INSERT INTO aws.emrserverless.applications (
 Architecture,
 Name,
 ReleaseLabel,
 Type,
 InitialCapacity,
 MaximumCapacity,
 Tags,
 AutoStartConfiguration,
 AutoStopConfiguration,
 ImageConfiguration,
 MonitoringConfiguration,
 RuntimeConfiguration,
 NetworkConfiguration,
 WorkerTypeSpecifications,
 region
)
SELECT 
 '{{ Architecture }}',
 '{{ Name }}',
 '{{ ReleaseLabel }}',
 '{{ Type }}',
 '{{ InitialCapacity }}',
 '{{ MaximumCapacity }}',
 '{{ Tags }}',
 '{{ AutoStartConfiguration }}',
 '{{ AutoStopConfiguration }}',
 '{{ ImageConfiguration }}',
 '{{ MonitoringConfiguration }}',
 '{{ RuntimeConfiguration }}',
 '{{ NetworkConfiguration }}',
 '{{ WorkerTypeSpecifications }}',
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
  - name: application
    props:
      - name: Architecture
        value: '{{ Architecture }}'
      - name: Name
        value: '{{ Name }}'
      - name: ReleaseLabel
        value: '{{ ReleaseLabel }}'
      - name: Type
        value: '{{ Type }}'
      - name: InitialCapacity
        value:
          - Key: '{{ Key }}'
            Value:
              WorkerCount: '{{ WorkerCount }}'
              WorkerConfiguration:
                Cpu: '{{ Cpu }}'
                Memory: '{{ Memory }}'
                Disk: '{{ Disk }}'
      - name: MaximumCapacity
        value:
          Cpu: null
          Memory: null
          Disk: null
      - name: Tags
        value:
          - Key: '{{ Key }}'
            Value: '{{ Value }}'
      - name: AutoStartConfiguration
        value:
          Enabled: '{{ Enabled }}'
      - name: AutoStopConfiguration
        value:
          Enabled: '{{ Enabled }}'
          IdleTimeoutMinutes: '{{ IdleTimeoutMinutes }}'
      - name: ImageConfiguration
        value:
          ImageUri: '{{ ImageUri }}'
      - name: MonitoringConfiguration
        value:
          S3MonitoringConfiguration: null
          ManagedPersistenceMonitoringConfiguration: null
          CloudWatchLoggingConfiguration: null
      - name: RuntimeConfiguration
        value:
          - Classification: '{{ Classification }}'
            Properties: {}
            Configurations:
              - null
      - name: NetworkConfiguration
        value:
          SubnetIds:
            - '{{ SubnetIds[0] }}'
          SecurityGroupIds:
            - '{{ SecurityGroupIds[0] }}'
      - name: WorkerTypeSpecifications
        value: {}

```
</TabItem>
</Tabs>

## `DELETE` example

```sql
/*+ delete */
DELETE FROM aws.emrserverless.applications
WHERE data__Identifier = '<ApplicationId>'
AND region = 'us-east-1';
```

## Permissions

To operate on the <code>applications</code> resource, the following permissions are required:

### Create
```json
kms:Create*,
kms:Describe*,
kms:Enable*,
kms:List*,
kms:Put*,
kms:Update*,
kms:Revoke*,
kms:Disable*,
kms:Get*,
kms:Delete*,
kms:ScheduleKeyDeletion,
kms:CancelKeyDeletion,
kms:GenerateDataKey,
kms:TagResource,
kms:UntagResource,
kms:Decrypt,
emr-serverless:CreateApplication,
emr-serverless:TagResource,
emr-serverless:GetApplication,
iam:CreateServiceLinkedRole,
ec2:CreateNetworkInterface,
ecr:BatchGetImage,
ecr:DescribeImages,
ecr:GetDownloadUrlForLayer
```

### Read
```json
emr-serverless:GetApplication
```

### Update
```json
emr-serverless:UpdateApplication,
emr-serverless:TagResource,
emr-serverless:UntagResource,
emr-serverless:GetApplication,
ec2:CreateNetworkInterface,
ecr:BatchGetImage,
ecr:DescribeImages,
ecr:GetDownloadUrlForLayer,
kms:Create*,
kms:Describe*,
kms:Enable*,
kms:List*,
kms:Put*,
kms:Update*,
kms:Revoke*,
kms:Disable*,
kms:Get*,
kms:Delete*,
kms:ScheduleKeyDeletion,
kms:CancelKeyDeletion,
kms:GenerateDataKey,
kms:TagResource,
kms:UntagResource,
kms:Decrypt
```

### Delete
```json
emr-serverless:DeleteApplication,
emr-serverless:GetApplication
```

### List
```json
emr-serverless:ListApplications
```

