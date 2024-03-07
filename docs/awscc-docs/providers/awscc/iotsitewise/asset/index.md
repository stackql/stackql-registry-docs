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
<tr><td><b>Description</b></td><td>asset</td></tr>
<tr><td><b>Id</b></td><td><code>awscc.iotsitewise.asset</code></td></tr>
</tbody></table>

## Fields
<table><tbody>
<tr><th>Name</th><th>Datatype</th><th>Description</th></tr>
<tr><td><code>asset_id</code></td><td><code>string</code></td><td>The ID of the asset</td></tr>
<tr><td><code>asset_model_id</code></td><td><code>string</code></td><td>The ID of the asset model from which to create the asset.</td></tr>
<tr><td><code>asset_arn</code></td><td><code>string</code></td><td>The ARN of the asset</td></tr>
<tr><td><code>asset_name</code></td><td><code>string</code></td><td>A unique, friendly name for the asset.</td></tr>
<tr><td><code>asset_description</code></td><td><code>string</code></td><td>A description for the asset</td></tr>
<tr><td><code>asset_properties</code></td><td><code>array</code></td><td></td></tr>
<tr><td><code>asset_hierarchies</code></td><td><code>array</code></td><td></td></tr>
<tr><td><code>tags</code></td><td><code>array</code></td><td>A list of key-value pairs that contain metadata for the asset.</td></tr>
<tr><td><code>region</code></td><td><code>string</code></td><td>AWS region.</td></tr>

</tbody></table>

## Methods
Currently only <code>SELECT</code> is supported for this resource resource.

## Example
```sql
SELECT
region,
asset_id,
asset_model_id,
asset_arn,
asset_name,
asset_description,
asset_properties,
asset_hierarchies,
tags
FROM awscc.iotsitewise.asset
WHERE region = 'us-east-1'
AND data__Identifier = '{AssetId}';
```

## Permissions

To operate on the <code>asset</code> resource, the following permissions are required:

### Read
```json
iotsitewise:DescribeAsset,
iotsitewise:DescribeAssetModel,
iotsitewise:ListAssociatedAssets,
iotsitewise:ListTagsForResource
```

### Update
```json
iotsitewise:AssociateAssets,
iotsitewise:DescribeAsset,
iotsitewise:DescribeAssetModel,
iotsitewise:DisassociateAssets,
iotsitewise:ListAssociatedAssets,
iotsitewise:ListTagsForResource,
iotsitewise:TagResource,
iotsitewise:UpdateAsset,
iotsitewise:UpdateAssetProperty,
iotsitewise:UntagResource
```

### Delete
```json
iotsitewise:DeleteAsset,
iotsitewise:DescribeAsset,
iotsitewise:DescribeAssetModel,
iotsitewise:DisassociateAssets,
iotsitewise:ListAssociatedAssets,
iotsitewise:ListTagsForResource
```

