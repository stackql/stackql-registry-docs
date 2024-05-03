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

import CopyableCode from '@site/src/components/CopyableCode/CopyableCode';

Used to retrieve a list of <code>asset_models</code> in a region or create a <code>asset_models</code> resource, use <code>asset_model</code> to operate on an individual resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>asset_models</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>Resource schema for AWS::IoTSiteWise::AssetModel</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="aws.iotsitewise.asset_models" /></td></tr>
</tbody></table>

## Fields
<table><tbody>
<tr><th>Name</th><th>Datatype</th><th>Description</th></tr>
<tr><td><CopyableCode code="asset_model_id" /></td><td><code>string</code></td><td>The ID of the asset model.</td></tr>
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
    <td><CopyableCode code="create_resource" /></td>
    <td><code>INSERT</code></td>
    <td><CopyableCode code="data__DesiredState, region" /></td>
  </tr>
  <tr>
    <td><CopyableCode code="list_resource" /></td>
    <td><code>SELECT</code></td>
    <td><CopyableCode code="region" /></td>
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

