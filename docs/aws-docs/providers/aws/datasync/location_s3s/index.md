---
title: location_s3s
hide_title: false
hide_table_of_contents: false
keywords:
  - location_s3s
  - datasync
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

Creates, updates, deletes or gets a <code>location_s3</code> resource or lists <code>location_s3s</code> in a region

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>location_s3s</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>Resource schema for AWS::DataSync::LocationS3</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="aws.datasync.location_s3s" /></td></tr>
</tbody></table>

## Fields
<table><tbody><tr><th>Name</th><th>Datatype</th><th>Description</th></tr><tr><td><CopyableCode code="s3_config" /></td><td><code>object</code></td><td>The Amazon Resource Name (ARN) of the AWS IAM role that is used to access an Amazon S3 bucket.</td></tr>
<tr><td><CopyableCode code="s3_bucket_arn" /></td><td><code>string</code></td><td>The Amazon Resource Name (ARN) of the Amazon S3 bucket.</td></tr>
<tr><td><CopyableCode code="subdirectory" /></td><td><code>string</code></td><td>A subdirectory in the Amazon S3 bucket. This subdirectory in Amazon S3 is used to read data from the S3 source location or write data to the S3 destination.</td></tr>
<tr><td><CopyableCode code="s3_storage_class" /></td><td><code>string</code></td><td>The Amazon S3 storage class you want to store your files in when this location is used as a task destination.</td></tr>
<tr><td><CopyableCode code="tags" /></td><td><code>array</code></td><td>An array of key-value pairs to apply to this resource.</td></tr>
<tr><td><CopyableCode code="location_arn" /></td><td><code>string</code></td><td>The Amazon Resource Name (ARN) of the Amazon S3 bucket location.</td></tr>
<tr><td><CopyableCode code="location_uri" /></td><td><code>string</code></td><td>The URL of the S3 location that was described.</td></tr>
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
    <td><CopyableCode code="S3Config, region" /></td>
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
Gets all <code>location_s3s</code> in a region.
```sql
SELECT
region,
s3_config,
s3_bucket_arn,
subdirectory,
s3_storage_class,
tags,
location_arn,
location_uri
FROM aws.datasync.location_s3s
WHERE region = 'us-east-1';
```
Gets all properties from an individual <code>location_s3</code>.
```sql
SELECT
region,
s3_config,
s3_bucket_arn,
subdirectory,
s3_storage_class,
tags,
location_arn,
location_uri
FROM aws.datasync.location_s3s
WHERE region = 'us-east-1' AND data__Identifier = '<LocationArn>';
```

## `INSERT` example

Use the following StackQL query and manifest file to create a new <code>location_s3</code> resource, using [__`stack-deploy`__](https://pypi.org/project/stack-deploy/).

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
INSERT INTO aws.datasync.location_s3s (
 S3Config,
 region
)
SELECT 
'{{ S3Config }}',
'{{ region }}';
```
</TabItem>
<TabItem value="all">

```sql
/*+ create */
INSERT INTO aws.datasync.location_s3s (
 S3Config,
 S3BucketArn,
 Subdirectory,
 S3StorageClass,
 Tags,
 region
)
SELECT 
 '{{ S3Config }}',
 '{{ S3BucketArn }}',
 '{{ Subdirectory }}',
 '{{ S3StorageClass }}',
 '{{ Tags }}',
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
  - name: location_s3
    props:
      - name: S3Config
        value:
          BucketAccessRoleArn: '{{ BucketAccessRoleArn }}'
      - name: S3BucketArn
        value: '{{ S3BucketArn }}'
      - name: Subdirectory
        value: '{{ Subdirectory }}'
      - name: S3StorageClass
        value: '{{ S3StorageClass }}'
      - name: Tags
        value:
          - Key: '{{ Key }}'
            Value: '{{ Value }}'

```
</TabItem>
</Tabs>

## `DELETE` example

```sql
/*+ delete */
DELETE FROM aws.datasync.location_s3s
WHERE data__Identifier = '<LocationArn>'
AND region = 'us-east-1';
```

## Permissions

To operate on the <code>location_s3s</code> resource, the following permissions are required:

### Create
```json
datasync:CreateLocationS3,
datasync:DescribeLocationS3,
datasync:ListTagsForResource,
datasync:TagResource,
s3:ListAllMyBuckets,
s3:ListBucket,
iam:GetRole,
iam:PassRole
```

### Read
```json
datasync:DescribeLocationS3,
datasync:ListTagsForResource
```

### Update
```json
datasync:DescribeLocationS3,
datasync:ListTagsForResource,
datasync:TagResource,
datasync:UntagResource
```

### Delete
```json
datasync:DeleteLocation
```

### List
```json
datasync:ListLocations
```

