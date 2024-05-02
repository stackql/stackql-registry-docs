---
title: tables
hide_title: false
hide_table_of_contents: false
keywords:
  - tables
  - dynamodb
  - aws
  - stackql
  - infrastructure-as-code
  - configuration-as-data
  - cloud inventory
description: Query, deploy and manage AWS resources using SQL
custom_edit_url: null
image: /img/providers/aws/stackql-aws-provider-featured-image.png
---
Retrieves a list of <code>tables</code> in a region

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>tables</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>The ``AWS::DynamoDB::Table`` resource creates a DDB table. For more information, see &#91;CreateTable&#93;(https:&#x2F;&#x2F;docs.aws.amazon.com&#x2F;amazondynamodb&#x2F;latest&#x2F;APIReference&#x2F;API_CreateTable.html) in the *API Reference*.&lt;br&#x2F;&gt; You should be aware of the following behaviors when working with DDB tables:&lt;br&#x2F;&gt;  +   CFNlong typically creates DDB tables in parallel. However, if your template includes multiple DDB tables with indexes, you must declare dependencies so that the tables are created sequentially. DDBlong limits the number of tables with secondary indexes that are in the creating state. If you create multiple tables with indexes at the same time, DDB returns an error and the stack operation fails. For an example, see &#91;DynamoDB Table with a DependsOn Attribute&#93;(https:&#x2F;&#x2F;docs.aws.amazon.com&#x2F;AWSCloudFormation&#x2F;latest&#x2F;UserGuide&#x2F;aws-resource-dynamodb-table.html#aws-resource-dynamodb-table--examples--DynamoDB_Table_with_a_DependsOn_Attribute).&lt;br&#x2F;&gt;  &lt;br&#x2F;&gt;   Our guidance is to use the latest schema documented here for your CFNlong templates. This schema supports the provisioning of all table settings below. When using this schema in your CFNlong templates, please ensure that your Identity and Access Management (IAM) policies are updated with appropriate permissions to allow for the authorization of these setting changes.</td></tr>
<tr><td><b>Id</b></td><td><code>aws.dynamodb.tables</code></td></tr>
</tbody></table>

## Fields
<table><tbody>
<tr><th>Name</th><th>Datatype</th><th>Description</th></tr>
<tr><td><code>table_name</code></td><td><code>string</code></td><td>A name for the table. If you don't specify a name, CFNlong generates a unique physical ID and uses that ID for the table name. For more information, see &#91;Name Type&#93;(https:&#x2F;&#x2F;docs.aws.amazon.com&#x2F;AWSCloudFormation&#x2F;latest&#x2F;UserGuide&#x2F;aws-properties-name.html).&lt;br&#x2F;&gt;  If you specify a name, you cannot perform updates that require replacement of this resource. You can perform updates that require no or some interruption. If you must replace the resource, specify a new name.</td></tr>
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
    <td><code>create_resource</code></td>
    <td><code>INSERT</code></td>
    <td><code>data__DesiredState, region</code></td>
  </tr>
  <tr>
    <td><code>list_resource</code></td>
    <td><code>SELECT</code></td>
    <td><code>region</code></td>
  </tr>
</tbody></table>

## `SELECT` Example
```sql
SELECT
region,
table_name
FROM aws.dynamodb.tables
WHERE region = 'us-east-1'
```

## Permissions

To operate on the <code>tables</code> resource, the following permissions are required:

### Create
```json
dynamodb:CreateTable,
dynamodb:DescribeImport,
dynamodb:DescribeTable,
dynamodb:DescribeTimeToLive,
dynamodb:UpdateTimeToLive,
dynamodb:UpdateContributorInsights,
dynamodb:UpdateContinuousBackups,
dynamodb:DescribeContinuousBackups,
dynamodb:DescribeContributorInsights,
dynamodb:EnableKinesisStreamingDestination,
dynamodb:DisableKinesisStreamingDestination,
dynamodb:DescribeKinesisStreamingDestination,
dynamodb:ImportTable,
dynamodb:ListTagsOfResource,
dynamodb:TagResource,
dynamodb:UpdateTable,
dynamodb:GetResourcePolicy,
dynamodb:PutResourcePolicy,
kinesis:DescribeStream,
kinesis:PutRecords,
iam:CreateServiceLinkedRole,
kms:CreateGrant,
kms:Decrypt,
kms:DescribeKey,
kms:ListAliases,
kms:Encrypt,
kms:RevokeGrant,
logs:CreateLogGroup,
logs:CreateLogStream,
logs:DescribeLogGroups,
logs:DescribeLogStreams,
logs:PutLogEvents,
logs:PutRetentionPolicy,
s3:GetObject,
s3:GetObjectMetadata,
s3:ListBucket
```

### List
```json
dynamodb:ListTables
```

