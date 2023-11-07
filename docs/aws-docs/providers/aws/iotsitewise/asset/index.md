---
title: asset
hide_title: false
hide_table_of_contents: false
keywords:
  - asset
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
Gets an individual <code>asset</code> resource

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>asset</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
null
<tr><td><b>Id</b></td><td><code>aws.iotsitewise.asset</code></td></tr>
</tbody></table>

## Fields
<table><tbody>
<tr><th>Name</th><th>Datatype</th><th>Description</th></tr>
<tr><td><code>AssetId</code></td><td><code>string</code></td><td>The ID of the asset</td></tr>
<tr><td><code>AssetModelId</code></td><td><code>string</code></td><td>The ID of the asset model from which to create the asset.</td></tr>
<tr><td><code>AssetArn</code></td><td><code>string</code></td><td>The ARN of the asset</td></tr>
<tr><td><code>AssetName</code></td><td><code>string</code></td><td>A unique, friendly name for the asset.</td></tr>
<tr><td><code>AssetDescription</code></td><td><code>string</code></td><td>A description for the asset</td></tr>
<tr><td><code>AssetProperties</code></td><td><code>array</code></td><td></td></tr>
<tr><td><code>AssetHierarchies</code></td><td><code>array</code></td><td></td></tr>
<tr><td><code>Tags</code></td><td><code>array</code></td><td>A list of key-value pairs that contain metadata for the asset.</td></tr>

</tbody></table>

## Methods
Currently only <code>SELECT</code> is supported for this resource resource.

## Example
<pre>
SELECT * 
FROM aws.iotsitewise.asset
WHERE region = 'us-east-1' AND data__Identifier = '&lt;AssetId&gt;'
</pre>
