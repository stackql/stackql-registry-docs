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
<table><tbody><tr><th>Name</th><th>Datatype</th><th>Description</th></tr><tr><td><CopyableCode code="bucket_name" /></td><td><code>string</code></td><td>Specifies a name for the bucket. The bucket name must contain only lowercase letters, numbers, and hyphens (-). A directory bucket name must be unique in the chosen Availability Zone. The bucket name must also follow the format 'bucket_base_name--az_id--x-s3' (for example, 'DOC-EXAMPLE-BUCKET--usw2-az1--x-s3'). If you don't specify a name, AWS CloudFormation generates a unique physical ID and uses that ID for the bucket name.</td></tr>
<tr><td><CopyableCode code="location_name" /></td><td><code>string</code></td><td>Specifies the AZ ID of the Availability Zone where the directory bucket will be created. An example AZ ID value is 'use1-az5'.</td></tr>
<tr><td><CopyableCode code="data_redundancy" /></td><td><code>string</code></td><td>Specifies the number of Availability Zone that's used for redundancy for the bucket.</td></tr>
<tr><td><CopyableCode code="arn" /></td><td><code>string</code></td><td>Returns the Amazon Resource Name (ARN) of the specified bucket.</td></tr>
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
    <td><CopyableCode code="LocationName, DataRedundancy, region" /></td>
  </tr>
  <tr>
    <td><CopyableCode code="delete_resource" /></td>
    <td><code>DELETE</code></td>
    <td><CopyableCode code="data__Identifier, region" /></td>
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
data_redundancy,
arn
FROM aws.s3express.directory_buckets
WHERE region = 'us-east-1';
```
Gets all properties from an individual <code>directory_bucket</code>.
```sql
SELECT
region,
bucket_name,
location_name,
data_redundancy,
arn
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
 region
)
SELECT 
 '{{ BucketName }}',
 '{{ LocationName }}',
 '{{ DataRedundancy }}',
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
s3express:CreateBucket,
s3express:ListAllMyDirectoryBuckets
```

### Read
```json
s3express:ListAllMyDirectoryBuckets
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

