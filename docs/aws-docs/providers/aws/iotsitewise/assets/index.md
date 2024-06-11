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
import Tabs from '@theme/Tabs';
import TabItem from '@theme/TabItem';

Creates, updates, deletes or gets an <code>asset</code> resource or lists <code>assets</code> in a region

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>assets</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>Resource schema for AWS::IoTSiteWise::Asset</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="aws.iotsitewise.assets" /></td></tr>
</tbody></table>

## Fields
<table><tbody><tr><th>Name</th><th>Datatype</th><th>Description</th></tr><tr><td><CopyableCode code="asset_id" /></td><td><code>string</code></td><td>The ID of the asset</td></tr>
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
    <td><CopyableCode code="create_resource" /></td>
    <td><code>INSERT</code></td>
    <td><CopyableCode code="AssetName, AssetModelId, region" /></td>
  </tr>
  <tr>
    <td><CopyableCode code="delete_resource" /></td>
    <td><code>DELETE</code></td>
    <td><CopyableCode code="data__Identifier, region" /></td>
  </tr>
  <tr>
    <td><CopyableCode code="update_resource" /></td>
    <td><code>UPDATE</code></td>
    <td><CopyableCode code="data__Identifier, data__PatchDocument, region" /></td>
  </tr>
  <tr>
    <td><CopyableCode code="list_resource" /></td>
    <td><code>SELECT</code></td>
    <td><CopyableCode code="region" /></td>
  </tr>
  <tr>
    <td><CopyableCode code="get_resource" /></td>
    <td><code>SELECT</code></td>
    <td><CopyableCode code="data__Identifier, region" /></td>
  </tr>
</tbody></table>

## `SELECT` examples
List all <code>assets</code> in a region.
```sql
SELECT
region,
asset_id
FROM aws.iotsitewise.assets
WHERE region = 'us-east-1';
```
Gets all properties from an <code>asset</code>.
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
FROM aws.iotsitewise.assets
WHERE region = 'us-east-1' AND data__Identifier = '<AssetId>';
```


## `INSERT` example

Use the following StackQL query and manifest file to create a new <code>asset</code> resource, using [__`stack-deploy`__](https://pypi.org/project/stack-deploy/).

<Tabs
    defaultValue="required"
    values={[
      { label: 'Required Properties', value: 'required', },
      { label: 'All Properties', value: 'all', },
      { label: 'Manifest', value: 'manifest', },
    ]
}>
<TabItem value="required">

```sql
/*+ create */
INSERT INTO aws.iotsitewise.assets (
 AssetModelId,
 AssetName,
 region
)
SELECT 
'{{ AssetModelId }}',
 '{{ AssetName }}',
'{{ region }}';
```
</TabItem>
<TabItem value="all">

```sql
/*+ create */
INSERT INTO aws.iotsitewise.assets (
 AssetExternalId,
 AssetModelId,
 AssetName,
 AssetDescription,
 AssetProperties,
 AssetHierarchies,
 Tags,
 region
)
SELECT 
 '{{ AssetExternalId }}',
 '{{ AssetModelId }}',
 '{{ AssetName }}',
 '{{ AssetDescription }}',
 '{{ AssetProperties }}',
 '{{ AssetHierarchies }}',
 '{{ Tags }}',
 '{{ region }}';
```
</TabItem>
<TabItem value="manifest">

```yaml
version: 1
name: stack name
description: stack description
providers:
  - aws
globals:
  - name: region
    value: '{{ vars.AWS_REGION }}'
resources:
  - name: asset
    props:
      - name: AssetExternalId
        value: '{{ AssetExternalId }}'
      - name: AssetModelId
        value: '{{ AssetModelId }}'
      - name: AssetName
        value: '{{ AssetName }}'
      - name: AssetDescription
        value: '{{ AssetDescription }}'
      - name: AssetProperties
        value:
          - Id: '{{ Id }}'
            ExternalId: '{{ ExternalId }}'
            LogicalId: '{{ LogicalId }}'
            Alias: '{{ Alias }}'
            NotificationState: '{{ NotificationState }}'
            Unit: '{{ Unit }}'
      - name: AssetHierarchies
        value:
          - Id: '{{ Id }}'
            ExternalId: '{{ ExternalId }}'
            LogicalId: '{{ LogicalId }}'
            ChildAssetId: '{{ ChildAssetId }}'
      - name: Tags
        value:
          - Key: '{{ Key }}'
            Value: '{{ Value }}'

```
</TabItem>
</Tabs>

## `DELETE` example

```sql
/*+ delete */
DELETE FROM aws.iotsitewise.assets
WHERE data__Identifier = '<AssetId>'
AND region = 'us-east-1';
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

### List
```json
iotsitewise:ListAssetModels,
iotsitewise:ListAssets
```

