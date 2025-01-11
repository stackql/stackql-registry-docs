---
title: directory_buckets
hide_title: false
hide_table_of_contents: false
keywords:
  - directory_buckets
  - s3express
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

Creates, updates, deletes or gets a <code>directory_bucket</code> resource or lists <code>directory_buckets</code> in a region

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>directory_buckets</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>Resource Type definition for AWS::S3Express::DirectoryBucket.</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="aws.s3express.directory_buckets" /></td></tr>
</tbody></table>

## Fields
<table><tbody><tr><th>Name</th><th>Datatype</th><th>Description</th></tr><tr><td><CopyableCode code="bucket_name" /></td><td><code>string</code></td><td>Specifies a name for the bucket. The bucket name must contain only lowercase letters, numbers, and hyphens (-). A directory bucket name must be unique in the chosen Availability Zone or Local Zone. The bucket name must also follow the format 'bucket_base_name--zone_id--x-s3'. The zone_id can be the ID of an Availability Zone or a Local Zone. If you don't specify a name, AWS CloudFormation generates a unique physical ID and uses that ID for the bucket name.</td></tr>
<tr><td><CopyableCode code="location_name" /></td><td><code>string</code></td><td>Specifies the Zone ID of the Availability Zone or Local Zone where the directory bucket will be created. An example Availability Zone ID value is 'use1-az5'.</td></tr>
<tr><td><CopyableCode code="availability_zone_name" /></td><td><code>string</code></td><td>Returns the code for the Availability Zone or Local Zone where the directory bucket was created. An example for the code of an Availability Zone is 'us-east-1f'.</td></tr>
<tr><td><CopyableCode code="data_redundancy" /></td><td><code>string</code></td><td>Specifies the number of Availability Zone or Local Zone that's used for redundancy for the bucket.</td></tr>
<tr><td><CopyableCode code="arn" /></td><td><code>string</code></td><td>Returns the Amazon Resource Name (ARN) of the specified bucket.</td></tr>
<tr><td><CopyableCode code="bucket_encryption" /></td><td><code>object</code></td><td>Specifies default encryption for a bucket using server-side encryption with Amazon S3 managed keys (SSE-S3) or AWS KMS keys (SSE-KMS).</td></tr>
<tr><td><CopyableCode code="lifecycle_configuration" /></td><td><code>object</code></td><td>Lifecycle rules that define how Amazon S3 Express manages objects during their lifetime.</td></tr>
<tr><td><CopyableCode code="region" /></td><td><code>string</code></td><td>AWS region.</td></tr>
</tbody></table>

For more information, see <a href="https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-s3express-directorybucket.html"><code>AWS::S3Express::DirectoryBucket</code></a>.

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
    <td><CopyableCode code="LocationName, DataRedundancy, region" /></td>
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
Gets all <code>directory_buckets</code> in a region.
```sql
SELECT
region,
bucket_name,
location_name,
availability_zone_name,
data_redundancy,
arn,
bucket_encryption,
lifecycle_configuration
FROM aws.s3express.directory_buckets
WHERE region = 'us-east-1';
```
Gets all properties from an individual <code>directory_bucket</code>.
```sql
SELECT
region,
bucket_name,
location_name,
availability_zone_name,
data_redundancy,
arn,
bucket_encryption,
lifecycle_configuration
FROM aws.s3express.directory_buckets
WHERE region = 'us-east-1' AND data__Identifier = '<BucketName>';
```

## `INSERT` example

Use the following StackQL query and manifest file to create a new <code>directory_bucket</code> resource, using [__`stack-deploy`__](https://pypi.org/project/stack-deploy/).

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
INSERT INTO aws.s3express.directory_buckets (
 LocationName,
 DataRedundancy,
 region
)
SELECT 
'{{ LocationName }}',
 '{{ DataRedundancy }}',
'{{ region }}';
```
</TabItem>
<TabItem value="all">

```sql
/*+ create */
INSERT INTO aws.s3express.directory_buckets (
 BucketName,
 LocationName,
 DataRedundancy,
 BucketEncryption,
 LifecycleConfiguration,
 region
)
SELECT 
 '{{ BucketName }}',
 '{{ LocationName }}',
 '{{ DataRedundancy }}',
 '{{ BucketEncryption }}',
 '{{ LifecycleConfiguration }}',
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
  - name: directory_bucket
    props:
      - name: BucketName
        value: '{{ BucketName }}'
      - name: LocationName
        value: '{{ LocationName }}'
      - name: DataRedundancy
        value: '{{ DataRedundancy }}'
      - name: BucketEncryption
        value:
          ServerSideEncryptionConfiguration:
            - BucketKeyEnabled: '{{ BucketKeyEnabled }}'
              ServerSideEncryptionByDefault:
                KMSMasterKeyID: '{{ KMSMasterKeyID }}'
                SSEAlgorithm: '{{ SSEAlgorithm }}'
      - name: LifecycleConfiguration
        value:
          Rules:
            - AbortIncompleteMultipartUpload:
                DaysAfterInitiation: '{{ DaysAfterInitiation }}'
              ExpirationInDays: '{{ ExpirationInDays }}'
              Id: '{{ Id }}'
              Prefix: '{{ Prefix }}'
              Status: '{{ Status }}'
              ObjectSizeGreaterThan: '{{ ObjectSizeGreaterThan }}'
              ObjectSizeLessThan: '{{ ObjectSizeLessThan }}'

```
</TabItem>
</Tabs>

## `DELETE` example

```sql
/*+ delete */
DELETE FROM aws.s3express.directory_buckets
WHERE data__Identifier = '<BucketName>'
AND region = 'us-east-1';
```

## Permissions

To operate on the <code>directory_buckets</code> resource, the following permissions are required:

### Create
```json
kms:GenerateDataKey,
kms:Decrypt,
s3express:CreateBucket,
s3express:ListAllMyDirectoryBuckets,
s3express:PutEncryptionConfiguration,
s3express:PutLifecycleConfiguration
```

### Read
```json
s3express:ListAllMyDirectoryBuckets,
ec2:DescribeAvailabilityZones,
s3express:GetEncryptionConfiguration,
s3express:GetLifecycleConfiguration
```

### Update
```json
kms:GenerateDataKey,
kms:Decrypt,
s3express:PutEncryptionConfiguration,
s3express:PutLifecycleConfiguration
```

### Delete
```json
s3express:DeleteBucket,
s3express:ListAllMyDirectoryBuckets
```

### List
```json
s3express:ListAllMyDirectoryBuckets
```
