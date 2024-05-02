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
<tr><td><b>Description</b></td><td>Resource schema for AWS::IoTSiteWise::AssetModel</td></tr>
<tr><td><b>Id</b></td><td><code>aws.iotsitewise.asset_models</code></td></tr>
</tbody></table>

## Fields
<table><tbody>
<tr><th>Name</th><th>Datatype</th><th>Description</th></tr>
<tr><td><code>asset_model_id</code></td><td><code>string</code></td><td>The ID of the asset model.</td></tr>
<tr><td><code>region</code></td><td><code>string</code></td><td>AWS region.</td></tr>

</tbody></table>

## Methods

<table><tbody>
  <tr>
    <th>Name</th>
    <th>Accessible by</th>
    <th>Required Params</th>
  </tr>
  <tr>
    <td><code>create_resource</code></td>
    <td><code>INSERT</code></td>
    <td><code>data__DesiredState, region</code></td>
  </tr>
  <tr>
    <td><code>list_resource</code></td>
    <td><code>SELECT</code></td>
    <td><code>region</code></td>
  </tr>
</tbody></table>

## `SELECT` Example
```sql
SELECT
region,
asset_model_id
FROM aws.iotsitewise.asset_models
WHERE region = 'us-east-1'
```

## Permissions

To operate on the <code>asset_models</code> resource, the following permissions are required:

### Create
```json
iotsitewise:CreateAssetModel,
iotsitewise:ListTagsForResource,
iotsitewise:TagResource,
iotsitewise:DescribeAssetModel,
iotsitewise:UpdateAssetModel,
iotsitewise:ListAssetModelProperties,
iotsitewise:ListAssetModelCompositeModels,
iotsitewise:UpdateAssetModelCompositeModel,
iotsitewise:DescribeAssetModelCompositeModel,
iotsitewise:CreateAssetModelCompositeModel
```

### List
```json
iotsitewise:DescribeAssetModel,
iotsitewise:ListAssetModels,
iotsitewise:ListTagsForResource,
iotsitewise:ListAssetModelProperties,
iotsitewise:ListAssetModelCompositeModels
```

