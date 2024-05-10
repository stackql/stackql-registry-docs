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


Used to retrieve a list of <code>tables</code> in a region or to create or delete a <code>tables</code> resource, use <code>table</code> to read or update an individual resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>tables</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>The AWS::Timestream::Table resource creates a Timestream Table.</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="aws.timestream.tables" /></td></tr>
</tbody></table>

## Fields
<table><tbody>
<tr><th>Name</th><th>Datatype</th><th>Description</th></tr>
<tr><td><CopyableCode code="database_name" /></td><td><code>string</code></td><td>The name for the database which the table to be created belongs to.</td></tr>
<tr><td><CopyableCode code="table_name" /></td><td><code>string</code></td><td>The name for the table. If you don't specify a name, AWS CloudFormation generates a unique physical ID and uses that ID for the table name.</td></tr>
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
database_name,
table_name
FROM aws.timestream.tables
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
 "DatabaseName": "{{ DatabaseName }}"
}
>>>
--required properties only
INSERT INTO aws.timestream.tables (
 DatabaseName,
 region
)
SELECT 
{{ .DatabaseName }},
'us-east-1';
```
</TabItem>
<TabItem value="all">

```sql
<<<json
{
 "DatabaseName": "{{ DatabaseName }}",
 "TableName": "{{ TableName }}",
 "RetentionProperties": {
  "MemoryStoreRetentionPeriodInHours": "{{ MemoryStoreRetentionPeriodInHours }}",
  "MagneticStoreRetentionPeriodInDays": "{{ MagneticStoreRetentionPeriodInDays }}"
 },
 "Schema": {
  "CompositePartitionKey": [
   {
    "Type": "{{ Type }}",
    "Name": "{{ Name }}",
    "EnforcementInRecord": "{{ EnforcementInRecord }}"
   }
  ]
 },
 "MagneticStoreWriteProperties": {
  "EnableMagneticStoreWrites": "{{ EnableMagneticStoreWrites }}",
  "MagneticStoreRejectedDataLocation": {
   "S3Configuration": {
    "BucketName": "{{ BucketName }}",
    "ObjectKeyPrefix": "{{ ObjectKeyPrefix }}",
    "EncryptionOption": "{{ EncryptionOption }}",
    "KmsKeyId": "{{ KmsKeyId }}"
   }
  }
 },
 "Tags": [
  {
   "Key": "{{ Key }}",
   "Value": "{{ Value }}"
  }
 ]
}
>>>
--all properties
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
 {{ .DatabaseName }},
 {{ .TableName }},
 {{ .RetentionProperties }},
 {{ .Schema }},
 {{ .MagneticStoreWriteProperties }},
 {{ .Tags }},
 'us-east-1';
```
</TabItem>
</Tabs>

## `DELETE` Example

```sql
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

