---
title: table
hide_title: false
hide_table_of_contents: false
keywords:
  - table
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
Gets or operates on an individual <code>table</code> resource, use <code>tables</code> to retrieve a list of resources or to create a resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>table</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>The AWS::Timestream::Table resource creates a Timestream Table.</td></tr>
<tr><td><b>Id</b></td><td><code>aws.timestream.table</code></td></tr>
</tbody></table>

## Fields
<table><tbody>
<tr><th>Name</th><th>Datatype</th><th>Description</th></tr>
<tr><td><code>arn</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>name</code></td><td><code>string</code></td><td>The table name exposed as a read-only attribute.</td></tr>
<tr><td><code>database_name</code></td><td><code>string</code></td><td>The name for the database which the table to be created belongs to.</td></tr>
<tr><td><code>table_name</code></td><td><code>string</code></td><td>The name for the table. If you don't specify a name, AWS CloudFormation generates a unique physical ID and uses that ID for the table name.</td></tr>
<tr><td><code>retention_properties</code></td><td><code>object</code></td><td>The retention duration of the memory store and the magnetic store.</td></tr>
<tr><td><code>schema</code></td><td><code>object</code></td><td>A Schema specifies the expected data model of the table.</td></tr>
<tr><td><code>magnetic_store_write_properties</code></td><td><code>object</code></td><td>The properties that determine whether magnetic store writes are enabled.</td></tr>
<tr><td><code>tags</code></td><td><code>array</code></td><td>An array of key-value pairs to apply to this resource.</td></tr>
<tr><td><code>region</code></td><td><code>string</code></td><td>AWS region.</td></tr>

</tbody></table>

## Methods

<table><tbody>
  <tr>
    <th>Name</th>
    <th>Accessible by</th>
    <th>Required Params</th>
  </tr>
  <tr>
    <td><code>update_resource</code></td>
    <td><code>UPDATE</code></td>
    <td><code>data__Identifier, data__PatchDocument, region</code></td>
  </tr>
  <tr>
    <td><code>delete_resource</code></td>
    <td><code>DELETE</code></td>
    <td><code>data__Identifier, region</code></td>
  </tr>
  <tr>
    <td><code>get_resource</code></td>
    <td><code>SELECT</code></td>
    <td><code>data__Identifier, region</code></td>
  </tr>
</tbody></table>

## `SELECT` Example
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
FROM aws.timestream.table
WHERE data__Identifier = '<DatabaseName>|<TableName>';
```

## Permissions

To operate on the <code>table</code> resource, the following permissions are required:

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

