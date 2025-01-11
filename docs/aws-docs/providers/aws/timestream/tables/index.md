---
title: tables
hide_title: false
hide_table_of_contents: false
keywords:
  - tables
  - timestream
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

Creates, updates, deletes or gets a <code>table</code> resource or lists <code>tables</code> in a region

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>tables</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>The AWS::Timestream::Table resource creates a Timestream Table.</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="aws.timestream.tables" /></td></tr>
</tbody></table>

## Fields
<table><tbody><tr><th>Name</th><th>Datatype</th><th>Description</th></tr><tr><td><CopyableCode code="arn" /></td><td><code>string</code></td><td></td></tr>
<tr><td><CopyableCode code="name" /></td><td><code>string</code></td><td>The table name exposed as a read-only attribute.</td></tr>
<tr><td><CopyableCode code="database_name" /></td><td><code>string</code></td><td>The name for the database which the table to be created belongs to.</td></tr>
<tr><td><CopyableCode code="table_name" /></td><td><code>string</code></td><td>The name for the table. If you don't specify a name, AWS CloudFormation generates a unique physical ID and uses that ID for the table name.</td></tr>
<tr><td><CopyableCode code="retention_properties" /></td><td><code>object</code></td><td>The retention duration of the memory store and the magnetic store.</td></tr>
<tr><td><CopyableCode code="schema" /></td><td><code>object</code></td><td>A Schema specifies the expected data model of the table.</td></tr>
<tr><td><CopyableCode code="magnetic_store_write_properties" /></td><td><code>object</code></td><td>The properties that determine whether magnetic store writes are enabled.</td></tr>
<tr><td><CopyableCode code="tags" /></td><td><code>array</code></td><td>An array of key-value pairs to apply to this resource.</td></tr>
<tr><td><CopyableCode code="region" /></td><td><code>string</code></td><td>AWS region.</td></tr>
</tbody></table>

For more information, see <a href="https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-timestream-table.html"><code>AWS::Timestream::Table</code></a>.

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
    <td><CopyableCode code="DatabaseName, region" /></td>
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
Gets all <code>tables</code> in a region.
```sql
SELECT
region,
arn,
name,
database_name,
table_name,
retention_properties,
schema,
magnetic_store_write_properties,
tags
FROM aws.timestream.tables
WHERE region = 'us-east-1';
```
Gets all properties from an individual <code>table</code>.
```sql
SELECT
region,
arn,
name,
database_name,
table_name,
retention_properties,
schema,
magnetic_store_write_properties,
tags
FROM aws.timestream.tables
WHERE region = 'us-east-1' AND data__Identifier = '<DatabaseName>|<TableName>';
```

## `INSERT` example

Use the following StackQL query and manifest file to create a new <code>table</code> resource, using [__`stack-deploy`__](https://pypi.org/project/stack-deploy/).

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
INSERT INTO aws.timestream.tables (
 DatabaseName,
 region
)
SELECT 
'{{ DatabaseName }}',
'{{ region }}';
```
</TabItem>
<TabItem value="all">

```sql
/*+ create */
INSERT INTO aws.timestream.tables (
 DatabaseName,
 TableName,
 RetentionProperties,
 Schema,
 MagneticStoreWriteProperties,
 Tags,
 region
)
SELECT 
 '{{ DatabaseName }}',
 '{{ TableName }}',
 '{{ RetentionProperties }}',
 '{{ Schema }}',
 '{{ MagneticStoreWriteProperties }}',
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
  - name: table
    props:
      - name: DatabaseName
        value: '{{ DatabaseName }}'
      - name: TableName
        value: '{{ TableName }}'
      - name: RetentionProperties
        value:
          MemoryStoreRetentionPeriodInHours: '{{ MemoryStoreRetentionPeriodInHours }}'
          MagneticStoreRetentionPeriodInDays: '{{ MagneticStoreRetentionPeriodInDays }}'
      - name: Schema
        value:
          CompositePartitionKey:
            - Type: '{{ Type }}'
              Name: '{{ Name }}'
              EnforcementInRecord: '{{ EnforcementInRecord }}'
      - name: MagneticStoreWriteProperties
        value:
          EnableMagneticStoreWrites: '{{ EnableMagneticStoreWrites }}'
          MagneticStoreRejectedDataLocation:
            S3Configuration:
              BucketName: '{{ BucketName }}'
              ObjectKeyPrefix: '{{ ObjectKeyPrefix }}'
              EncryptionOption: '{{ EncryptionOption }}'
              KmsKeyId: '{{ KmsKeyId }}'
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
DELETE FROM aws.timestream.tables
WHERE data__Identifier = '<DatabaseName|TableName>'
AND region = 'us-east-1';
```

## Permissions

To operate on the <code>tables</code> resource, the following permissions are required:

### Create
```json
timestream:CreateTable,
timestream:DescribeEndpoints,
timestream:TagResource,
s3:PutObject,
s3:GetObject,
s3:GetBucketAcl,
kms:GenerateDataKey*,
kms:DescribeKey,
kms:Encrypt
```

### Read
```json
timestream:DescribeTable,
timestream:DescribeEndpoints,
timestream:ListTagsForResource
```

### Update
```json
timestream:UpdateTable,
timestream:DescribeEndpoints,
timestream:TagResource,
timestream:UntagResource,
s3:PutObject,
s3:GetObject,
s3:GetBucketAcl,
kms:GenerateDataKey*,
kms:DescribeKey,
kms:Encrypt
```

### Delete
```json
timestream:DeleteTable,
timestream:DescribeEndpoints,
timestream:DescribeTable
```

### List
```json
timestream:ListTables,
timestream:DescribeEndpoints
```
