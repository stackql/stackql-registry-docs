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

import CopyableCode from '@site/src/components/CopyableCode/CopyableCode';
import Tabs from '@theme/Tabs';
import TabItem from '@theme/TabItem';


Gets or updates an individual <code>data_source</code> resource, use <code>data_sources</code> to retrieve a list of resources or to create or delete a resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>data_source</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>Definition of the AWS::QuickSight::DataSource Resource Type.</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="aws.quicksight.data_source" /></td></tr>
</tbody></table>

## Fields
<table><tbody>
<tr><th>Name</th><th>Datatype</th><th>Description</th></tr>
<tr><td><CopyableCode code="alternate_data_source_parameters" /></td><td><code>array</code></td><td>&lt;p&gt;A set of alternate data source parameters that you want to share for the credentials&lt;br&#x2F;&gt;            stored with this data source. The credentials are applied in tandem with the data source&lt;br&#x2F;&gt;            parameters when you copy a data source by using a create or update request. The API&lt;br&#x2F;&gt;            operation compares the &lt;code&gt;DataSourceParameters&lt;&#x2F;code&gt; structure that's in the request&lt;br&#x2F;&gt;            with the structures in the &lt;code&gt;AlternateDataSourceParameters&lt;&#x2F;code&gt; allow list. If the&lt;br&#x2F;&gt;            structures are an exact match, the request is allowed to use the credentials from this&lt;br&#x2F;&gt;            existing data source. If the &lt;code&gt;AlternateDataSourceParameters&lt;&#x2F;code&gt; list is null,&lt;br&#x2F;&gt;            the &lt;code&gt;Credentials&lt;&#x2F;code&gt; originally used with this &lt;code&gt;DataSourceParameters&lt;&#x2F;code&gt;&lt;br&#x2F;&gt;            are automatically allowed.&lt;&#x2F;p&gt;</td></tr>
<tr><td><CopyableCode code="arn" /></td><td><code>string</code></td><td>&lt;p&gt;The Amazon Resource Name (ARN) of the data source.&lt;&#x2F;p&gt;</td></tr>
<tr><td><CopyableCode code="aws_account_id" /></td><td><code>string</code></td><td></td></tr>
<tr><td><CopyableCode code="created_time" /></td><td><code>string</code></td><td>&lt;p&gt;The time that this data source was created.&lt;&#x2F;p&gt;</td></tr>
<tr><td><CopyableCode code="credentials" /></td><td><code>object</code></td><td></td></tr>
<tr><td><CopyableCode code="data_source_id" /></td><td><code>string</code></td><td></td></tr>
<tr><td><CopyableCode code="data_source_parameters" /></td><td><code>object</code></td><td></td></tr>
<tr><td><CopyableCode code="error_info" /></td><td><code>object</code></td><td></td></tr>
<tr><td><CopyableCode code="last_updated_time" /></td><td><code>string</code></td><td>&lt;p&gt;The last time that this data source was updated.&lt;&#x2F;p&gt;</td></tr>
<tr><td><CopyableCode code="name" /></td><td><code>string</code></td><td>&lt;p&gt;A display name for the data source.&lt;&#x2F;p&gt;</td></tr>
<tr><td><CopyableCode code="permissions" /></td><td><code>array</code></td><td>&lt;p&gt;A list of resource permissions on the data source.&lt;&#x2F;p&gt;</td></tr>
<tr><td><CopyableCode code="ssl_properties" /></td><td><code>object</code></td><td></td></tr>
<tr><td><CopyableCode code="status" /></td><td><code>string</code></td><td></td></tr>
<tr><td><CopyableCode code="tags" /></td><td><code>array</code></td><td>&lt;p&gt;Contains a map of the key-value pairs for the resource tag or tags assigned to the data source.&lt;&#x2F;p&gt;</td></tr>
<tr><td><CopyableCode code="type" /></td><td><code>string</code></td><td></td></tr>
<tr><td><CopyableCode code="vpc_connection_properties" /></td><td><code>object</code></td><td></td></tr>
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
    <td><CopyableCode code="update_resource" /></td>
    <td><code>UPDATE</code></td>
    <td><CopyableCode code="data__Identifier, data__PatchDocument, region" /></td>
  </tr>
  <tr>
    <td><CopyableCode code="get_resource" /></td>
    <td><code>SELECT</code></td>
    <td><CopyableCode code="data__Identifier, region" /></td>
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
WHERE region = 'us-east-1' AND data__Identifier = '<AwsAccountId>|<DataSourceId>';
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

