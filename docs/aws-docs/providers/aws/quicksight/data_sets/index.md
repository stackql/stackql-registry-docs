---
title: data_sets
hide_title: false
hide_table_of_contents: false
keywords:
  - data_sets
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
Retrieves a list of <code>data_sets</code> in a region

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>data_sets</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
null
<tr><td><b>Id</b></td><td><code>aws.quicksight.data_sets</code></td></tr>
</tbody></table>

## Fields
<table><tbody>
<tr><th>Name</th><th>Datatype</th><th>Description</th></tr>
<tr><td><code>Arn</code></td><td><code>string</code></td><td>&lt;p&gt;The Amazon Resource Name (ARN) of the resource.&lt;&#x2F;p&gt;</td></tr>
<tr><td><code>AwsAccountId</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>ColumnGroups</code></td><td><code>array</code></td><td>&lt;p&gt;Groupings of columns that work together in certain QuickSight features. Currently, only geospatial hierarchy is supported.&lt;&#x2F;p&gt;</td></tr>
<tr><td><code>ColumnLevelPermissionRules</code></td><td><code>array</code></td><td></td></tr>
<tr><td><code>ConsumedSpiceCapacityInBytes</code></td><td><code>number</code></td><td>&lt;p&gt;The amount of SPICE capacity used by this dataset. This is 0 if the dataset isn't&lt;br&#x2F;&gt;            imported into SPICE.&lt;&#x2F;p&gt;</td></tr>
<tr><td><code>CreatedTime</code></td><td><code>string</code></td><td>&lt;p&gt;The time that this dataset was created.&lt;&#x2F;p&gt;</td></tr>
<tr><td><code>DataSetId</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>FieldFolders</code></td><td><code>undefined</code></td><td></td></tr>
<tr><td><code>ImportMode</code></td><td><code>undefined</code></td><td></td></tr>
<tr><td><code>LastUpdatedTime</code></td><td><code>string</code></td><td>&lt;p&gt;The last time that this dataset was updated.&lt;&#x2F;p&gt;</td></tr>
<tr><td><code>LogicalTableMap</code></td><td><code>undefined</code></td><td></td></tr>
<tr><td><code>Name</code></td><td><code>string</code></td><td>&lt;p&gt;The display name for the dataset.&lt;&#x2F;p&gt;</td></tr>
<tr><td><code>OutputColumns</code></td><td><code>array</code></td><td>&lt;p&gt;The list of columns after all transforms. These columns are available in templates,&lt;br&#x2F;&gt;            analyses, and dashboards.&lt;&#x2F;p&gt;</td></tr>
<tr><td><code>Permissions</code></td><td><code>array</code></td><td>&lt;p&gt;A list of resource permissions on the dataset.&lt;&#x2F;p&gt;</td></tr>
<tr><td><code>PhysicalTableMap</code></td><td><code>undefined</code></td><td></td></tr>
<tr><td><code>RowLevelPermissionDataSet</code></td><td><code>undefined</code></td><td></td></tr>
<tr><td><code>Tags</code></td><td><code>array</code></td><td>&lt;p&gt;Contains a map of the key-value pairs for the resource tag or tags assigned to the dataset.&lt;&#x2F;p&gt;</td></tr>
<tr><td><code>IngestionWaitPolicy</code></td><td><code>undefined</code></td><td></td></tr>
<tr><td><code>DataSetUsageConfiguration</code></td><td><code>undefined</code></td><td></td></tr>

</tbody></table>

## Methods
Currently only <code>SELECT</code> is supported for this resource resource.

## Example
<pre>
SELECT * 
FROM aws.quicksight.data_sets
WHERE region = 'us-east-1'
</pre>
