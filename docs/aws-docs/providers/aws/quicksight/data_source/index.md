---
title: data_source
hide_title: false
hide_table_of_contents: false
keywords:
  - data_source
  - quicksight
  - aws
  - stackql
  - infrastructure-as-code
  - configuration-as-data
  - cloud inventory
description: Query, deploy and manage AWS resources using SQL
custom_edit_url: null
image: /img/providers/aws/stackql-aws-provider-featured-image.png
---
Gets an individual <code>data_source</code> resource

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>data_source</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>Definition of the AWS::QuickSight::DataSource Resource Type.</td></tr>
<tr><td><b>Id</b></td><td><code>aws.quicksight.data_source</code></td></tr>
</tbody></table>

## Fields
<table><tbody>
<tr><th>Name</th><th>Datatype</th><th>Description</th></tr>
<tr><td><code>alternate_data_source_parameters</code></td><td><code>array</code></td><td>&lt;p&gt;A set of alternate data source parameters that you want to share for the credentials&lt;br&#x2F;&gt;            stored with this data source. The credentials are applied in tandem with the data source&lt;br&#x2F;&gt;            parameters when you copy a data source by using a create or update request. The API&lt;br&#x2F;&gt;            operation compares the &lt;code&gt;DataSourceParameters&lt;&#x2F;code&gt; structure that's in the request&lt;br&#x2F;&gt;            with the structures in the &lt;code&gt;AlternateDataSourceParameters&lt;&#x2F;code&gt; allow list. If the&lt;br&#x2F;&gt;            structures are an exact match, the request is allowed to use the credentials from this&lt;br&#x2F;&gt;            existing data source. If the &lt;code&gt;AlternateDataSourceParameters&lt;&#x2F;code&gt; list is null,&lt;br&#x2F;&gt;            the &lt;code&gt;Credentials&lt;&#x2F;code&gt; originally used with this &lt;code&gt;DataSourceParameters&lt;&#x2F;code&gt;&lt;br&#x2F;&gt;            are automatically allowed.&lt;&#x2F;p&gt;</td></tr>
<tr><td><code>arn</code></td><td><code>string</code></td><td>&lt;p&gt;The Amazon Resource Name (ARN) of the data source.&lt;&#x2F;p&gt;</td></tr>
<tr><td><code>aws_account_id</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>created_time</code></td><td><code>string</code></td><td>&lt;p&gt;The time that this data source was created.&lt;&#x2F;p&gt;</td></tr>
<tr><td><code>credentials</code></td><td><code>object</code></td><td></td></tr>
<tr><td><code>data_source_id</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>data_source_parameters</code></td><td><code>object</code></td><td></td></tr>
<tr><td><code>error_info</code></td><td><code>object</code></td><td></td></tr>
<tr><td><code>last_updated_time</code></td><td><code>string</code></td><td>&lt;p&gt;The last time that this data source was updated.&lt;&#x2F;p&gt;</td></tr>
<tr><td><code>name</code></td><td><code>string</code></td><td>&lt;p&gt;A display name for the data source.&lt;&#x2F;p&gt;</td></tr>
<tr><td><code>permissions</code></td><td><code>array</code></td><td>&lt;p&gt;A list of resource permissions on the data source.&lt;&#x2F;p&gt;</td></tr>
<tr><td><code>ssl_properties</code></td><td><code>object</code></td><td></td></tr>
<tr><td><code>status</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>tags</code></td><td><code>array</code></td><td>&lt;p&gt;Contains a map of the key-value pairs for the resource tag or tags assigned to the data source.&lt;&#x2F;p&gt;</td></tr>
<tr><td><code>type</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>vpc_connection_properties</code></td><td><code>object</code></td><td></td></tr>
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
alternate_data_source_parameters,
arn,
aws_account_id,
created_time,
credentials,
data_source_id,
data_source_parameters,
error_info,
last_updated_time,
name,
permissions,
ssl_properties,
status,
tags,
type,
vpc_connection_properties
FROM aws.quicksight.data_source
WHERE data__Identifier = '<AwsAccountId>|<DataSourceId>';
```

## Permissions

To operate on the <code>data_source</code> resource, the following permissions are required:

### Read
```json
quicksight:DescribeDataSource,
quicksight:DescribeDataSourcePermissions,
quicksight:ListTagsForResource
```

### Update
```json
quicksight:DescribeDataSource,
quicksight:DescribeDataSourcePermissions,
quicksight:UpdateDataSource,
quicksight:UpdateDataSourcePermissions,
quicksight:TagResource,
quicksight:UntagResource,
quicksight:ListTagsForResource
```

### Delete
```json
quicksight:DescribeDataSource,
quicksight:DescribeDataSourcePermissions,
quicksight:DeleteDataSource,
quicksight:ListTagsForResource
```

