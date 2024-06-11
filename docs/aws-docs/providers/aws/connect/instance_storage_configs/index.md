---
title: instance_storage_configs
hide_title: false
hide_table_of_contents: false
keywords:
  - instance_storage_configs
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

Creates, updates, deletes or gets an <code>instance_storage_config</code> resource or lists <code>instance_storage_configs</code> in a region

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>instance_storage_configs</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>Resource Type definition for AWS::Connect::InstanceStorageConfig</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="aws.connect.instance_storage_configs" /></td></tr>
</tbody></table>

## Fields
<table><tbody><tr><th>Name</th><th>Datatype</th><th>Description</th></tr><tr><td><CopyableCode code="instance_arn" /></td><td><code>string</code></td><td>Connect Instance ID with which the storage config will be associated</td></tr>
<tr><td><CopyableCode code="resource_type" /></td><td><code>Specifies the type of storage resource available for the instance</code></td><td></td></tr>
<tr><td><CopyableCode code="association_id" /></td><td><code>An associationID is automatically generated when a storage config is associated with an instance</code></td><td></td></tr>
<tr><td><CopyableCode code="storage_type" /></td><td><code>Specifies the storage type to be associated with the instance</code></td><td></td></tr>
<tr><td><CopyableCode code="s3_config" /></td><td><code>undefined</code></td><td></td></tr>
<tr><td><CopyableCode code="kinesis_video_stream_config" /></td><td><code>undefined</code></td><td></td></tr>
<tr><td><CopyableCode code="kinesis_stream_config" /></td><td><code>undefined</code></td><td></td></tr>
<tr><td><CopyableCode code="kinesis_firehose_config" /></td><td><code>undefined</code></td><td></td></tr>
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
    <td><CopyableCode code="InstanceArn, ResourceType, StorageType, region" /></td>
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
    <td><CopyableCode code="list_resource" /></td>
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
List all <code>instance_storage_configs</code> in a region.
```sql
SELECT
region,
instance_arn,
association_id,
resource_type
FROM aws.connect.instance_storage_configs
WHERE region = 'us-east-1';
```
Gets all properties from an <code>instance_storage_config</code>.
```sql
SELECT
region,
instance_arn,
resource_type,
association_id,
storage_type,
s3_config,
kinesis_video_stream_config,
kinesis_stream_config,
kinesis_firehose_config
FROM aws.connect.instance_storage_configs
WHERE region = 'us-east-1' AND data__Identifier = '<InstanceArn>|<AssociationId>|<ResourceType>';
```


## `INSERT` example

Use the following StackQL query and manifest file to create a new <code>instance_storage_config</code> resource, using [__`stack-deploy`__](https://pypi.org/project/stack-deploy/).

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
INSERT INTO aws.connect.instance_storage_configs (
 InstanceArn,
 ResourceType,
 StorageType,
 region
)
SELECT 
'{{ InstanceArn }}',
 '{{ ResourceType }}',
 '{{ StorageType }}',
'{{ region }}';
```
</TabItem>
<TabItem value="all">

```sql
/*+ create */
INSERT INTO aws.connect.instance_storage_configs (
 InstanceArn,
 ResourceType,
 StorageType,
 S3Config,
 KinesisVideoStreamConfig,
 KinesisStreamConfig,
 KinesisFirehoseConfig,
 region
)
SELECT 
 '{{ InstanceArn }}',
 '{{ ResourceType }}',
 '{{ StorageType }}',
 '{{ S3Config }}',
 '{{ KinesisVideoStreamConfig }}',
 '{{ KinesisStreamConfig }}',
 '{{ KinesisFirehoseConfig }}',
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
  - name: instance_storage_config
    props:
      - name: InstanceArn
        value: '{{ InstanceArn }}'
      - name: ResourceType
        value: '{{ ResourceType }}'
      - name: StorageType
        value: '{{ StorageType }}'
      - name: S3Config
        value:
          BucketName: '{{ BucketName }}'
          BucketPrefix: '{{ BucketPrefix }}'
          EncryptionConfig:
            EncryptionType: '{{ EncryptionType }}'
            KeyId: '{{ KeyId }}'
      - name: KinesisVideoStreamConfig
        value:
          Prefix: null
          RetentionPeriodHours: null
          EncryptionConfig: null
      - name: KinesisStreamConfig
        value:
          StreamArn: '{{ StreamArn }}'
      - name: KinesisFirehoseConfig
        value:
          FirehoseArn: '{{ FirehoseArn }}'

```
</TabItem>
</Tabs>

## `DELETE` example

```sql
/*+ delete */
DELETE FROM aws.connect.instance_storage_configs
WHERE data__Identifier = '<InstanceArn|AssociationId|ResourceType>'
AND region = 'us-east-1';
```

## Permissions

To operate on the <code>instance_storage_configs</code> resource, the following permissions are required:

### Create
```json
connect:AssociateInstanceStorageConfig,
connect:DescribeInstance,
ds:DescribeDirectories,
s3:GetBucketAcl,
s3:GetBucketLocation,
iam:PutRolePolicy,
kinesis:DescribeStream,
kms:DescribeKey,
kms:CreateGrant,
firehose:DescribeDeliveryStream
```

### Read
```json
connect:DescribeInstanceStorageConfig,
connect:ListInstanceStorageConfigs,
connect:DescribeInstance,
ds:DescribeDirectories,
s3:GetBucketAcl,
s3:GetBucketLocation
```

### Update
```json
connect:UpdateInstanceStorageConfig,
ds:DescribeDirectories,
s3:GetBucketAcl,
s3:GetBucketLocation,
kinesis:DescribeStream,
iam:PutRolePolicy,
kms:DescribeKey,
kms:CreateGrant,
kms:RetireGrant,
firehose:DescribeDeliveryStream
```

### Delete
```json
connect:DisassociateInstanceStorageConfig,
connect:DescribeInstance,
s3:GetBucketAcl,
s3:GetBucketLocation,
kms:RetireGrant
```

### List
```json
connect:DescribeInstance,
connect:ListInstanceStorageConfigs,
ds:DescribeDirectories
```

