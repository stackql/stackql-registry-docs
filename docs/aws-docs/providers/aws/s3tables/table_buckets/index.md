---
title: table_buckets
hide_title: false
hide_table_of_contents: false
keywords:
  - table_buckets
  - s3tables
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

Creates, updates, deletes or gets a <code>table_bucket</code> resource or lists <code>table_buckets</code> in a region

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>table_buckets</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>Creates an Amazon S3 Tables table bucket in the same AWS Region where you create the AWS CloudFormation stack.</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="aws.s3tables.table_buckets" /></td></tr>
</tbody></table>

## Fields
<table><tbody><tr><th>Name</th><th>Datatype</th><th>Description</th></tr><tr><td><CopyableCode code="table_bucket_arn" /></td><td><code>string</code></td><td>The Amazon Resource Name (ARN) of the table bucket to which the policy applies.</td></tr>
<tr><td><CopyableCode code="table_bucket_name" /></td><td><code>string</code></td><td>A name for the table bucket.</td></tr>
<tr><td><CopyableCode code="unreferenced_file_removal" /></td><td><code>object</code></td><td>Settings governing the Unreferenced File Removal maintenance action. Unreferenced file removal identifies and deletes all objects that are not referenced by any table snapshots.</td></tr>
<tr><td><CopyableCode code="region" /></td><td><code>string</code></td><td>AWS region.</td></tr>
</tbody></table>

For more information, see <a href="https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-s3tables-tablebucket.html"><code>AWS::S3Tables::TableBucket</code></a>.

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
    <td><CopyableCode code="TableBucketName, region" /></td>
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
Gets all <code>table_buckets</code> in a region.
```sql
SELECT
region,
table_bucket_arn,
table_bucket_name,
unreferenced_file_removal
FROM aws.s3tables.table_buckets
WHERE region = 'us-east-1';
```
Gets all properties from an individual <code>table_bucket</code>.
```sql
SELECT
region,
table_bucket_arn,
table_bucket_name,
unreferenced_file_removal
FROM aws.s3tables.table_buckets
WHERE region = 'us-east-1' AND data__Identifier = '<TableBucketARN>';
```

## `INSERT` example

Use the following StackQL query and manifest file to create a new <code>table_bucket</code> resource, using [__`stack-deploy`__](https://pypi.org/project/stack-deploy/).

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
INSERT INTO aws.s3tables.table_buckets (
 TableBucketName,
 region
)
SELECT 
'{{ TableBucketName }}',
'{{ region }}';
```
</TabItem>
<TabItem value="all">

```sql
/*+ create */
INSERT INTO aws.s3tables.table_buckets (
 TableBucketName,
 UnreferencedFileRemoval,
 region
)
SELECT 
 '{{ TableBucketName }}',
 '{{ UnreferencedFileRemoval }}',
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
  - name: table_bucket
    props:
      - name: TableBucketName
        value: '{{ TableBucketName }}'
      - name: UnreferencedFileRemoval
        value:
          Status: '{{ Status }}'
          UnreferencedDays: '{{ UnreferencedDays }}'
          NoncurrentDays: '{{ NoncurrentDays }}'

```
</TabItem>
</Tabs>

## `DELETE` example

```sql
/*+ delete */
DELETE FROM aws.s3tables.table_buckets
WHERE data__Identifier = '<TableBucketARN>'
AND region = 'us-east-1';
```

## Permissions

To operate on the <code>table_buckets</code> resource, the following permissions are required:

### Create
```json
s3tables:CreateTableBucket,
s3tables:PutTableBucketMaintenanceConfiguration,
s3tables:GetTableBucket,
s3tables:GetTableBucketMaintenanceConfiguration
```

### Read
```json
s3tables:GetTableBucket,
s3tables:GetTableBucketMaintenanceConfiguration
```

### Update
```json
s3tables:PutTableBucketMaintenanceConfiguration,
s3tables:GetTableBucket,
s3tables:GetTableBucketMaintenanceConfiguration
```

### Delete
```json
s3tables:DeleteTableBucket
```

### List
```json
s3tables:ListTableBuckets
```
