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

import CopyableCode from '@site/src/components/CopyableCode/CopyableCode';
import Tabs from '@theme/Tabs';
import TabItem from '@theme/TabItem';


Gets or updates an individual <code>data_set</code> resource, use <code>data_sets</code> to retrieve a list of resources or to create or delete a resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>data_set</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>Definition of the AWS::QuickSight::DataSet Resource Type.</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="aws.quicksight.data_set" /></td></tr>
</tbody></table>

## Fields
<table><tbody>
<tr><th>Name</th><th>Datatype</th><th>Description</th></tr>
<tr><td><CopyableCode code="arn" /></td><td><code>string</code></td><td>&lt;p&gt;The Amazon Resource Name (ARN) of the resource.&lt;&#x2F;p&gt;</td></tr>
<tr><td><CopyableCode code="aws_account_id" /></td><td><code>string</code></td><td></td></tr>
<tr><td><CopyableCode code="column_groups" /></td><td><code>array</code></td><td>&lt;p&gt;Groupings of columns that work together in certain QuickSight features. Currently, only geospatial hierarchy is supported.&lt;&#x2F;p&gt;</td></tr>
<tr><td><CopyableCode code="column_level_permission_rules" /></td><td><code>array</code></td><td></td></tr>
<tr><td><CopyableCode code="consumed_spice_capacity_in_bytes" /></td><td><code>number</code></td><td>&lt;p&gt;The amount of SPICE capacity used by this dataset. This is 0 if the dataset isn't&lt;br&#x2F;&gt;            imported into SPICE.&lt;&#x2F;p&gt;</td></tr>
<tr><td><CopyableCode code="created_time" /></td><td><code>string</code></td><td>&lt;p&gt;The time that this dataset was created.&lt;&#x2F;p&gt;</td></tr>
<tr><td><CopyableCode code="data_set_id" /></td><td><code>string</code></td><td></td></tr>
<tr><td><CopyableCode code="dataset_parameters" /></td><td><code>array</code></td><td>&lt;p&gt;The parameters declared in the dataset.&lt;&#x2F;p&gt;</td></tr>
<tr><td><CopyableCode code="field_folders" /></td><td><code>object</code></td><td></td></tr>
<tr><td><CopyableCode code="import_mode" /></td><td><code>string</code></td><td></td></tr>
<tr><td><CopyableCode code="last_updated_time" /></td><td><code>string</code></td><td>&lt;p&gt;The last time that this dataset was updated.&lt;&#x2F;p&gt;</td></tr>
<tr><td><CopyableCode code="logical_table_map" /></td><td><code>object</code></td><td></td></tr>
<tr><td><CopyableCode code="name" /></td><td><code>string</code></td><td>&lt;p&gt;The display name for the dataset.&lt;&#x2F;p&gt;</td></tr>
<tr><td><CopyableCode code="output_columns" /></td><td><code>array</code></td><td>&lt;p&gt;The list of columns after all transforms. These columns are available in templates,&lt;br&#x2F;&gt;            analyses, and dashboards.&lt;&#x2F;p&gt;</td></tr>
<tr><td><CopyableCode code="permissions" /></td><td><code>array</code></td><td>&lt;p&gt;A list of resource permissions on the dataset.&lt;&#x2F;p&gt;</td></tr>
<tr><td><CopyableCode code="physical_table_map" /></td><td><code>object</code></td><td></td></tr>
<tr><td><CopyableCode code="row_level_permission_data_set" /></td><td><code>object</code></td><td></td></tr>
<tr><td><CopyableCode code="row_level_permission_tag_configuration" /></td><td><code>object</code></td><td></td></tr>
<tr><td><CopyableCode code="tags" /></td><td><code>array</code></td><td>&lt;p&gt;Contains a map of the key-value pairs for the resource tag or tags assigned to the dataset.&lt;&#x2F;p&gt;</td></tr>
<tr><td><CopyableCode code="ingestion_wait_policy" /></td><td><code>object</code></td><td></td></tr>
<tr><td><CopyableCode code="data_set_usage_configuration" /></td><td><code>object</code></td><td></td></tr>
<tr><td><CopyableCode code="data_set_refresh_properties" /></td><td><code>object</code></td><td></td></tr>
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
FROM aws.quicksight.data_set
WHERE region = 'us-east-1' AND data__Identifier = '<AwsAccountId>|<DataSetId>';
```


## Permissions

To operate on the <code>data_set</code> resource, the following permissions are required:

### Read
```json
quicksight:DescribeDataSet,
quicksight:DescribeDataSetPermissions,
quicksight:ListTagsForResource,
quicksight:DescribeDataSetRefreshProperties
```

### Update
```json
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
quicksight:DeleteDataSetRefreshProperties
```

