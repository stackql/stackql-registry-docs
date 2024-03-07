---
title: data_set
hide_title: false
hide_table_of_contents: false
keywords:
  - data_set
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
Gets an individual <code>data_set</code> resource

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>data_set</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>data_set</td></tr>
<tr><td><b>Id</b></td><td><code>awscc.quicksight.data_set</code></td></tr>
</tbody></table>

## Fields
<table><tbody>
<tr><th>Name</th><th>Datatype</th><th>Description</th></tr>
<tr><td><code>arn</code></td><td><code>string</code></td><td>&lt;p&gt;The Amazon Resource Name (ARN) of the resource.&lt;&#x2F;p&gt;</td></tr>
<tr><td><code>aws_account_id</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>column_groups</code></td><td><code>array</code></td><td>&lt;p&gt;Groupings of columns that work together in certain QuickSight features. Currently, only geospatial hierarchy is supported.&lt;&#x2F;p&gt;</td></tr>
<tr><td><code>column_level_permission_rules</code></td><td><code>array</code></td><td></td></tr>
<tr><td><code>consumed_spice_capacity_in_bytes</code></td><td><code>number</code></td><td>&lt;p&gt;The amount of SPICE capacity used by this dataset. This is 0 if the dataset isn't&lt;br&#x2F;&gt;            imported into SPICE.&lt;&#x2F;p&gt;</td></tr>
<tr><td><code>created_time</code></td><td><code>string</code></td><td>&lt;p&gt;The time that this dataset was created.&lt;&#x2F;p&gt;</td></tr>
<tr><td><code>data_set_id</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>dataset_parameters</code></td><td><code>array</code></td><td>&lt;p&gt;The parameters declared in the dataset.&lt;&#x2F;p&gt;</td></tr>
<tr><td><code>field_folders</code></td><td><code>object</code></td><td></td></tr>
<tr><td><code>import_mode</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>last_updated_time</code></td><td><code>string</code></td><td>&lt;p&gt;The last time that this dataset was updated.&lt;&#x2F;p&gt;</td></tr>
<tr><td><code>logical_table_map</code></td><td><code>object</code></td><td></td></tr>
<tr><td><code>name</code></td><td><code>string</code></td><td>&lt;p&gt;The display name for the dataset.&lt;&#x2F;p&gt;</td></tr>
<tr><td><code>output_columns</code></td><td><code>array</code></td><td>&lt;p&gt;The list of columns after all transforms. These columns are available in templates,&lt;br&#x2F;&gt;            analyses, and dashboards.&lt;&#x2F;p&gt;</td></tr>
<tr><td><code>permissions</code></td><td><code>array</code></td><td>&lt;p&gt;A list of resource permissions on the dataset.&lt;&#x2F;p&gt;</td></tr>
<tr><td><code>physical_table_map</code></td><td><code>object</code></td><td></td></tr>
<tr><td><code>row_level_permission_data_set</code></td><td><code>object</code></td><td></td></tr>
<tr><td><code>row_level_permission_tag_configuration</code></td><td><code>object</code></td><td></td></tr>
<tr><td><code>tags</code></td><td><code>array</code></td><td>&lt;p&gt;Contains a map of the key-value pairs for the resource tag or tags assigned to the dataset.&lt;&#x2F;p&gt;</td></tr>
<tr><td><code>ingestion_wait_policy</code></td><td><code>object</code></td><td></td></tr>
<tr><td><code>data_set_usage_configuration</code></td><td><code>object</code></td><td></td></tr>
<tr><td><code>data_set_refresh_properties</code></td><td><code>object</code></td><td></td></tr>
<tr><td><code>region</code></td><td><code>string</code></td><td>AWS region.</td></tr>

</tbody></table>

## Methods
Currently only <code>SELECT</code> is supported for this resource resource.

## Permissions

To operate on the <code>data_set</code> resource, the following permissions are required:

### Read
<pre>
quicksight:DescribeDataSet,
quicksight:DescribeDataSetPermissions,
quicksight:ListTagsForResource,
quicksight:DescribeDataSetRefreshProperties</pre>

### Update
<pre>
quicksight:DescribeDataSet,
quicksight:DescribeDataSetPermissions,
quicksight:PassDataSource,
quicksight:UpdateDataSet,
quicksight:UpdateDataSetPermissions,
quicksight:PassDataSet,
quicksight:DescribeIngestion,
quicksight:ListIngestions,
quicksight:CancelIngestion,
quicksight:TagResource,
quicksight:UntagResource,
quicksight:ListTagsForResource,
quicksight:PutDataSetRefreshProperties,
quicksight:DescribeDataSetRefreshProperties,
quicksight:DeleteDataSetRefreshProperties</pre>

### Delete
<pre>
quicksight:DescribeDataSet,
quicksight:DeleteDataSet,
quicksight:ListTagsForResource,
quicksight:DescribeIngestion,
quicksight:DeleteDataSetRefreshProperties,
quicksight:DescribeDataSetRefreshProperties</pre>


## Example
```sql
SELECT
region,
arn,
aws_account_id,
column_groups,
column_level_permission_rules,
consumed_spice_capacity_in_bytes,
created_time,
data_set_id,
dataset_parameters,
field_folders,
import_mode,
last_updated_time,
logical_table_map,
name,
output_columns,
permissions,
physical_table_map,
row_level_permission_data_set,
row_level_permission_tag_configuration,
tags,
ingestion_wait_policy,
data_set_usage_configuration,
data_set_refresh_properties
FROM awscc.quicksight.data_set
WHERE region = 'us-east-1'
AND data__Identifier = '&lt;AwsAccountId&gt;'
AND data__Identifier = '&lt;DataSetId&gt;'
```
