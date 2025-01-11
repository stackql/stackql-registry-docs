---
title: data_set_tags
hide_title: false
hide_table_of_contents: false
keywords:
  - data_set_tags
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

Expands all tag keys and values for <code>data_sets</code> in a region

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>data_set_tags</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>Definition of the AWS::QuickSight::DataSet Resource Type.</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="aws.quicksight.data_set_tags" /></td></tr>
</tbody></table>

## Fields
<table><tbody><tr><th>Name</th><th>Datatype</th><th>Description</th></tr><tr><td><CopyableCode code="physical_table_map" /></td><td><code>object</code></td><td></td></tr>
<tr><td><CopyableCode code="created_time" /></td><td><code>string</code></td><td><p>The time that this dataset was created.</p></td></tr>
<tr><td><CopyableCode code="field_folders" /></td><td><code>object</code></td><td></td></tr>
<tr><td><CopyableCode code="last_updated_time" /></td><td><code>string</code></td><td><p>The last time that this dataset was updated.</p></td></tr>
<tr><td><CopyableCode code="data_set_id" /></td><td><code>string</code></td><td></td></tr>
<tr><td><CopyableCode code="folder_arns" /></td><td><code>array</code></td><td><p>When you create the dataset, Amazon QuickSight adds the dataset to these folders.</p></td></tr>
<tr><td><CopyableCode code="consumed_spice_capacity_in_bytes" /></td><td><code>number</code></td><td><p>The amount of SPICE capacity used by this dataset. This is 0 if the dataset isn't<br />imported into SPICE.</p></td></tr>
<tr><td><CopyableCode code="performance_configuration" /></td><td><code>object</code></td><td></td></tr>
<tr><td><CopyableCode code="row_level_permission_data_set" /></td><td><code>object</code></td><td><p>Information about a dataset that contains permissions for row-level security (RLS).<br />The permissions dataset maps fields to users or groups. For more information, see<br /><a href="https://docs.aws.amazon.com/quicksight/latest/user/restrict-access-to-a-data-set-using-row-level-security.html">Using Row-Level Security (RLS) to Restrict Access to a Dataset</a> in the <i>Amazon QuickSight User<br />Guide</i>.</p><br /><p>The option to deny permissions by setting <code>PermissionPolicy</code> to <code>DENY_ACCESS</code> is<br />not supported for new RLS datasets.</p></td></tr>
<tr><td><CopyableCode code="data_set_refresh_properties" /></td><td><code>object</code></td><td><p>The refresh properties of a dataset.</p></td></tr>
<tr><td><CopyableCode code="row_level_permission_tag_configuration" /></td><td><code>object</code></td><td><p>The configuration of tags on a dataset to set row-level security. </p></td></tr>
<tr><td><CopyableCode code="ingestion_wait_policy" /></td><td><code>object</code></td><td><p>Wait policy to use when creating/updating dataset. Default is to wait for SPICE ingestion to finish with timeout of 36 hours.</p></td></tr>
<tr><td><CopyableCode code="column_level_permission_rules" /></td><td><code>array</code></td><td><p>A set of one or more definitions of a <code><br /><a href="https://docs.aws.amazon.com/quicksight/latest/APIReference/API_ColumnLevelPermissionRule.html">ColumnLevelPermissionRule</a><br /></code>.</p></td></tr>
<tr><td><CopyableCode code="name" /></td><td><code>string</code></td><td><p>The display name for the dataset.</p></td></tr>
<tr><td><CopyableCode code="column_groups" /></td><td><code>array</code></td><td><p>Groupings of columns that work together in certain Amazon QuickSight features. Currently, only geospatial hierarchy is supported.</p></td></tr>
<tr><td><CopyableCode code="import_mode" /></td><td><code>string</code></td><td></td></tr>
<tr><td><CopyableCode code="dataset_parameters" /></td><td><code>array</code></td><td><p>The parameter declarations of the dataset.</p></td></tr>
<tr><td><CopyableCode code="logical_table_map" /></td><td><code>object</code></td><td></td></tr>
<tr><td><CopyableCode code="aws_account_id" /></td><td><code>string</code></td><td></td></tr>
<tr><td><CopyableCode code="data_set_usage_configuration" /></td><td><code>object</code></td><td><p>The usage configuration to apply to child datasets that reference this dataset as a source.</p></td></tr>
<tr><td><CopyableCode code="permissions" /></td><td><code>array</code></td><td><p>A list of resource permissions on the dataset.</p></td></tr>
<tr><td><CopyableCode code="output_columns" /></td><td><code>array</code></td><td><p>The list of columns after all transforms. These columns are available in templates,<br />analyses, and dashboards.</p></td></tr>
<tr><td><CopyableCode code="arn" /></td><td><code>string</code></td><td><p>The Amazon Resource Name (ARN) of the resource.</p></td></tr>
<tr><td><CopyableCode code="tag_key" /></td><td><code>string</code></td><td>Tag key.</td></tr>
<tr><td><CopyableCode code="tag_value" /></td><td><code>string</code></td><td>Tag value.</td></tr>
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
    <td><CopyableCode code="list_resources" /></td>
    <td><code>SELECT</code></td>
    <td><CopyableCode code="region" /></td>
  </tr>
</tbody></table>

## `SELECT` examples
Expands tags for all <code>data_sets</code> in a region.
```sql
SELECT
region,
physical_table_map,
created_time,
field_folders,
last_updated_time,
data_set_id,
folder_arns,
consumed_spice_capacity_in_bytes,
performance_configuration,
row_level_permission_data_set,
data_set_refresh_properties,
row_level_permission_tag_configuration,
ingestion_wait_policy,
column_level_permission_rules,
name,
column_groups,
import_mode,
dataset_parameters,
logical_table_map,
aws_account_id,
data_set_usage_configuration,
permissions,
output_columns,
arn,
tag_key,
tag_value
FROM aws.quicksight.data_set_tags
WHERE region = 'us-east-1';
```


## Permissions

For permissions required to operate on the <code>data_set_tags</code> resource, see <a href="/providers/aws/quicksight/data_sets/#permissions"><code>data_sets</code></a>

