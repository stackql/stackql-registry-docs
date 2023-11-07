---
title: asset_models
hide_title: false
hide_table_of_contents: false
keywords:
  - asset_models
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
Retrieves a list of <code>asset_models</code> in a region

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>asset_models</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
null
<tr><td><b>Id</b></td><td><code>aws.iotsitewise.asset_models</code></td></tr>
</tbody></table>

## Fields
<table><tbody>
<tr><th>Name</th><th>Datatype</th><th>Description</th></tr>
<tr><td><code>AssetModelId</code></td><td><code>string</code></td><td>The ID of the asset model.</td></tr>
<tr><td><code>AssetModelArn</code></td><td><code>string</code></td><td>The ARN of the asset model, which has the following format.</td></tr>
<tr><td><code>AssetModelName</code></td><td><code>string</code></td><td>A unique, friendly name for the asset model.</td></tr>
<tr><td><code>AssetModelDescription</code></td><td><code>string</code></td><td>A description for the asset model.</td></tr>
<tr><td><code>AssetModelProperties</code></td><td><code>array</code></td><td>The property definitions of the asset model. You can specify up to 200 properties per asset model.</td></tr>
<tr><td><code>AssetModelCompositeModels</code></td><td><code>array</code></td><td>The composite asset models that are part of this asset model. Composite asset models are asset models that contain specific properties.</td></tr>
<tr><td><code>AssetModelHierarchies</code></td><td><code>array</code></td><td>The hierarchy definitions of the asset model. Each hierarchy specifies an asset model whose assets can be children of any other assets created from this asset model. You can specify up to 10 hierarchies per asset model.</td></tr>
<tr><td><code>Tags</code></td><td><code>array</code></td><td>A list of key-value pairs that contain metadata for the asset model.</td></tr>

</tbody></table>

## Methods
Currently only <code>SELECT</code> is supported for this resource resource.

## Example
<pre>
SELECT * 
FROM aws.iotsitewise.asset_models
WHERE region = 'us-east-1'
</pre>
