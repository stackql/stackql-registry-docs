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


Used to retrieve a list of <code>instance_storage_configs</code> in a region or to create or delete a <code>instance_storage_configs</code> resource, use <code>instance_storage_config</code> to read or update an individual resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>instance_storage_configs</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>Resource Type definition for AWS::Connect::InstanceStorageConfig</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="aws.connect.instance_storage_configs" /></td></tr>
</tbody></table>

## Fields
<table><tbody>
<tr><th>Name</th><th>Datatype</th><th>Description</th></tr>
<tr><td><CopyableCode code="instance_arn" /></td><td><code>string</code></td><td>Connect Instance ID with which the storage config will be associated</td></tr>
<tr><td><CopyableCode code="association_id" /></td><td><code>undefined</code></td><td></td></tr>
<tr><td><CopyableCode code="resource_type" /></td><td><code>undefined</code></td><td></td></tr>
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
instance_arn,
association_id,
resource_type
FROM aws.connect.instance_storage_configs
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
 "InstanceArn": "{{ InstanceArn }}",
 "ResourceType": "{{ ResourceType }}",
 "StorageType": "{{ StorageType }}"
}
>>>
--required properties only
INSERT INTO aws.connect.instance_storage_configs (
 InstanceArn,
 ResourceType,
 StorageType,
 region
)
SELECT 
{{ InstanceArn }},
 {{ ResourceType }},
 {{ StorageType }},
'us-east-1';
```

</TabItem>
<TabItem value="all">

```sql
<<<json
{
 "InstanceArn": "{{ InstanceArn }}",
 "ResourceType": "{{ ResourceType }}",
 "StorageType": "{{ StorageType }}",
 "S3Config": {
  "BucketName": "{{ BucketName }}",
  "BucketPrefix": "{{ BucketPrefix }}",
  "EncryptionConfig": {
   "EncryptionType": "{{ EncryptionType }}",
   "KeyId": "{{ KeyId }}"
  }
 },
 "KinesisVideoStreamConfig": {
  "Prefix": null,
  "RetentionPeriodHours": null,
  "EncryptionConfig": null
 },
 "KinesisStreamConfig": {
  "StreamArn": "{{ StreamArn }}"
 },
 "KinesisFirehoseConfig": {
  "FirehoseArn": "{{ FirehoseArn }}"
 }
}
>>>
--all properties
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
 {{ InstanceArn }},
 {{ ResourceType }},
 {{ StorageType }},
 {{ S3Config }},
 {{ KinesisVideoStreamConfig }},
 {{ KinesisStreamConfig }},
 {{ KinesisFirehoseConfig }},
 'us-east-1';
```

</TabItem>
</Tabs>

## `DELETE` Example

```sql
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

