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

import CopyableCode from '@site/src/components/CopyableCode/CopyableCode';

Gets or operates on an individual <code>asset</code> resource, use <code>assets</code> to retrieve a list of resources or to create a resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>asset</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>Resource schema for AWS::IoTSiteWise::Asset</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="aws.iotsitewise.asset" /></td></tr>
</tbody></table>

## Fields
<table><tbody>
<tr><th>Name</th><th>Datatype</th><th>Description</th></tr>
<tr><td><CopyableCode code="asset_id" /></td><td><code>string</code></td><td>The ID of the asset</td></tr>
<tr><td><CopyableCode code="asset_external_id" /></td><td><code>string</code></td><td>The External ID of the asset</td></tr>
<tr><td><CopyableCode code="asset_model_id" /></td><td><code>string</code></td><td>The ID of the asset model from which to create the asset.</td></tr>
<tr><td><CopyableCode code="asset_arn" /></td><td><code>string</code></td><td>The ARN of the asset</td></tr>
<tr><td><CopyableCode code="asset_name" /></td><td><code>string</code></td><td>A unique, friendly name for the asset.</td></tr>
<tr><td><CopyableCode code="asset_description" /></td><td><code>string</code></td><td>A description for the asset</td></tr>
<tr><td><CopyableCode code="asset_properties" /></td><td><code>array</code></td><td></td></tr>
<tr><td><CopyableCode code="asset_hierarchies" /></td><td><code>array</code></td><td></td></tr>
<tr><td><CopyableCode code="tags" /></td><td><code>array</code></td><td>A list of key-value pairs that contain metadata for the asset.</td></tr>
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
    <td><CopyableCode code="delete_resource" /></td>
    <td><code>DELETE</code></td>
    <td><CopyableCode code="data__Identifier, region" /></td>
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
asset_id,
asset_external_id,
asset_model_id,
asset_arn,
asset_name,
asset_description,
asset_properties,
asset_hierarchies,
tags
FROM aws.iotsitewise.asset
WHERE data__Identifier = '<AssetId>';
```

## Permissions

To operate on the <code>asset</code> resource, the following permissions are required:

### Read
```json
iotsitewise:DescribeAsset,
iotsitewise:DescribeAssetModel,
iotsitewise:ListAssociatedAssets,
iotsitewise:ListAssetModelProperties,
iotsitewise:ListAssetModelCompositeModels,
iotsitewise:ListAssetProperties,
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
iotsitewise:ListAssetModelProperties,
iotsitewise:ListAssetProperties,
iotsitewise:ListAssetModelCompositeModels,
iotsitewise:UntagResource
```

### Delete
```json
iotsitewise:DeleteAsset,
iotsitewise:DescribeAsset,
iotsitewise:DescribeAssetModel,
iotsitewise:DisassociateAssets,
iotsitewise:ListAssociatedAssets,
iotsitewise:ListAssetProperties,
iotsitewise:ListTagsForResource,
iotsitewise:ListAssetModelCompositeModels,
iotsitewise:ListAssetModelProperties,
iotsitewise:ListAssetProperties
```

