---
title: assets
hide_title: false
hide_table_of_contents: false
keywords:
  - assets
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

Used to retrieve a list of <code>assets</code> in a region or create a <code>assets</code> resource, use <code>asset</code> to operate on an individual resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>assets</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>Resource schema for AWS::IoTSiteWise::Asset</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="aws.iotsitewise.assets" /></td></tr>
</tbody></table>

## Fields
<table><tbody>
<tr><th>Name</th><th>Datatype</th><th>Description</th></tr>
<tr><td><CopyableCode code="asset_id" /></td><td><code>string</code></td><td>The ID of the asset</td></tr>
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
asset_id
FROM aws.iotsitewise.assets
WHERE region = 'us-east-1'
```

## Permissions

To operate on the <code>assets</code> resource, the following permissions are required:

### Create
```json
iotsitewise:AssociateAssets,
iotsitewise:CreateAsset,
iotsitewise:DescribeAsset,
iotsitewise:DescribeAssetModel,
iotsitewise:ListAssociatedAssets,
iotsitewise:ListTagsForResource,
iotsitewise:TagResource,
iotsitewise:ListAssetModelProperties,
iotsitewise:ListAssetProperties,
iotsitewise:ListAssetModelCompositeModels,
iotsitewise:UpdateAssetProperty
```

### List
```json
iotsitewise:ListAssetModels,
iotsitewise:ListAssets
```

