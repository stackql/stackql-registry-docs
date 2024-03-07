---
title: asset_model
hide_title: false
hide_table_of_contents: false
keywords:
  - asset_model
  - iotsitewise
  - aws
  - stackql
  - infrastructure-as-code
  - configuration-as-data
  - cloud inventory
description: Query, deploy and manage AWS resources using SQL
custom_edit_url: null
image: /img/providers/aws/stackql-aws-provider-featured-image.png
---
Gets an individual <code>asset_model</code> resource

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>asset_model</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>asset_model</td></tr>
<tr><td><b>Id</b></td><td><code>awscc.iotsitewise.asset_model</code></td></tr>
</tbody></table>

## Fields
<table><tbody>
<tr><th>Name</th><th>Datatype</th><th>Description</th></tr>
<tr><td><code>asset_model_id</code></td><td><code>string</code></td><td>The ID of the asset model.</td></tr>
<tr><td><code>asset_model_arn</code></td><td><code>string</code></td><td>The ARN of the asset model, which has the following format.</td></tr>
<tr><td><code>asset_model_name</code></td><td><code>string</code></td><td>A unique, friendly name for the asset model.</td></tr>
<tr><td><code>asset_model_description</code></td><td><code>string</code></td><td>A description for the asset model.</td></tr>
<tr><td><code>asset_model_properties</code></td><td><code>array</code></td><td>The property definitions of the asset model. You can specify up to 200 properties per asset model.</td></tr>
<tr><td><code>asset_model_composite_models</code></td><td><code>array</code></td><td>The composite asset models that are part of this asset model. Composite asset models are asset models that contain specific properties.</td></tr>
<tr><td><code>asset_model_hierarchies</code></td><td><code>array</code></td><td>The hierarchy definitions of the asset model. Each hierarchy specifies an asset model whose assets can be children of any other assets created from this asset model. You can specify up to 10 hierarchies per asset model.</td></tr>
<tr><td><code>tags</code></td><td><code>array</code></td><td>A list of key-value pairs that contain metadata for the asset model.</td></tr>
<tr><td><code>region</code></td><td><code>string</code></td><td>AWS region.</td></tr>

</tbody></table>

## Methods
Currently only <code>SELECT</code> is supported for this resource resource.

## Permissions

To operate on the <code>asset_model</code> resource, the following permissions are required:

### Read
<pre>
iotsitewise:DescribeAssetModel,
iotsitewise:ListTagsForResource</pre>

### Update
<pre>
iotsitewise:DescribeAssetModel,
iotsitewise:ListTagsForResource,
iotsitewise:TagResource,
iotsitewise:UntagResource,
iotsitewise:UpdateAssetModel</pre>

### Delete
<pre>
iotsitewise:DescribeAssetModel,
iotsitewise:DeleteAssetModel</pre>


## Example
```sql
SELECT
region,
asset_model_id,
asset_model_arn,
asset_model_name,
asset_model_description,
asset_model_properties,
asset_model_composite_models,
asset_model_hierarchies,
tags
FROM awscc.iotsitewise.asset_model
WHERE region = 'us-east-1'
AND data__Identifier = '&lt;AssetModelId&gt;'
```
