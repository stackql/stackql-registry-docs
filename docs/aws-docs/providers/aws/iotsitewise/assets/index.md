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


Used to retrieve a list of <code>assets</code> in a region or to create or delete a <code>assets</code> resource, use <code>asset</code> to read or update an individual resource.

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
    <td><CopyableCode code="delete_resource" /></td>
    <td><code>DELETE</code></td>
    <td><CopyableCode code="data__Identifier, region" /></td>
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
WHERE region = 'us-east-1';
```

## `INSERT` Example

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
-- asset.iql (required properties only)
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
-- asset.iql (all properties)
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

## `DELETE` Example

```sql
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

