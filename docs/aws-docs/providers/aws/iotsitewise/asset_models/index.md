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
import Tabs from '@theme/Tabs';
import TabItem from '@theme/TabItem';

Creates, updates, deletes or gets an <code>asset_model</code> resource or lists <code>asset_models</code> in a region

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>asset_models</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>Resource schema for AWS::IoTSiteWise::AssetModel</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="aws.iotsitewise.asset_models" /></td></tr>
</tbody></table>

## Fields
<table><tbody><tr><th>Name</th><th>Datatype</th><th>Description</th></tr><tr><td><CopyableCode code="asset_model_id" /></td><td><code>string</code></td><td>The ID of the asset model.</td></tr>
<tr><td><CopyableCode code="asset_model_type" /></td><td><code>string</code></td><td>The type of the asset model (ASSET_MODEL OR COMPONENT_MODEL)</td></tr>
<tr><td><CopyableCode code="asset_model_external_id" /></td><td><code>string</code></td><td>The external ID of the asset model.</td></tr>
<tr><td><CopyableCode code="asset_model_arn" /></td><td><code>string</code></td><td>The ARN of the asset model, which has the following format.</td></tr>
<tr><td><CopyableCode code="asset_model_name" /></td><td><code>string</code></td><td>A unique, friendly name for the asset model.</td></tr>
<tr><td><CopyableCode code="asset_model_description" /></td><td><code>string</code></td><td>A description for the asset model.</td></tr>
<tr><td><CopyableCode code="asset_model_properties" /></td><td><code>array</code></td><td>The property definitions of the asset model. You can specify up to 200 properties per asset model.</td></tr>
<tr><td><CopyableCode code="asset_model_composite_models" /></td><td><code>array</code></td><td>The composite asset models that are part of this asset model. Composite asset models are asset models that contain specific properties.</td></tr>
<tr><td><CopyableCode code="asset_model_hierarchies" /></td><td><code>array</code></td><td>The hierarchy definitions of the asset model. Each hierarchy specifies an asset model whose assets can be children of any other assets created from this asset model. You can specify up to 10 hierarchies per asset model.</td></tr>
<tr><td><CopyableCode code="tags" /></td><td><code>array</code></td><td>A list of key-value pairs that contain metadata for the asset model.</td></tr>
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
    <td><CopyableCode code="AssetModelName, region" /></td>
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
    <td><CopyableCode code="list_resources" /></td>
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
Gets all <code>asset_models</code> in a region.
```sql
SELECT
region,
asset_model_id,
asset_model_type,
asset_model_external_id,
asset_model_arn,
asset_model_name,
asset_model_description,
asset_model_properties,
asset_model_composite_models,
asset_model_hierarchies,
tags
FROM aws.iotsitewise.asset_models
WHERE region = 'us-east-1';
```
Gets all properties from an individual <code>asset_model</code>.
```sql
SELECT
region,
asset_model_id,
asset_model_type,
asset_model_external_id,
asset_model_arn,
asset_model_name,
asset_model_description,
asset_model_properties,
asset_model_composite_models,
asset_model_hierarchies,
tags
FROM aws.iotsitewise.asset_models
WHERE region = 'us-east-1' AND data__Identifier = '<AssetModelId>';
```

## `INSERT` example

Use the following StackQL query and manifest file to create a new <code>asset_model</code> resource, using [__`stack-deploy`__](https://pypi.org/project/stack-deploy/).

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
INSERT INTO aws.iotsitewise.asset_models (
 AssetModelName,
 region
)
SELECT 
'{{ AssetModelName }}',
'{{ region }}';
```
</TabItem>
<TabItem value="all">

```sql
/*+ create */
INSERT INTO aws.iotsitewise.asset_models (
 AssetModelType,
 AssetModelExternalId,
 AssetModelName,
 AssetModelDescription,
 AssetModelProperties,
 AssetModelCompositeModels,
 AssetModelHierarchies,
 Tags,
 region
)
SELECT 
 '{{ AssetModelType }}',
 '{{ AssetModelExternalId }}',
 '{{ AssetModelName }}',
 '{{ AssetModelDescription }}',
 '{{ AssetModelProperties }}',
 '{{ AssetModelCompositeModels }}',
 '{{ AssetModelHierarchies }}',
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
  - name: asset_model
    props:
      - name: AssetModelType
        value: '{{ AssetModelType }}'
      - name: AssetModelExternalId
        value: '{{ AssetModelExternalId }}'
      - name: AssetModelName
        value: '{{ AssetModelName }}'
      - name: AssetModelDescription
        value: '{{ AssetModelDescription }}'
      - name: AssetModelProperties
        value:
          - LogicalId: '{{ LogicalId }}'
            Id: '{{ Id }}'
            ExternalId: '{{ ExternalId }}'
            Name: '{{ Name }}'
            DataType: '{{ DataType }}'
            DataTypeSpec: '{{ DataTypeSpec }}'
            Unit: '{{ Unit }}'
            Type:
              TypeName: '{{ TypeName }}'
              Attribute:
                DefaultValue: '{{ DefaultValue }}'
              Transform:
                Expression: '{{ Expression }}'
                Variables:
                  - Name: '{{ Name }}'
                    Value:
                      PropertyLogicalId: '{{ PropertyLogicalId }}'
                      PropertyId: '{{ PropertyId }}'
                      PropertyExternalId: '{{ PropertyExternalId }}'
                      PropertyPath:
                        - Name: '{{ Name }}'
                      HierarchyLogicalId: '{{ HierarchyLogicalId }}'
                      HierarchyId: '{{ HierarchyId }}'
                      HierarchyExternalId: '{{ HierarchyExternalId }}'
              Metric:
                Expression: '{{ Expression }}'
                Variables:
                  - null
                Window:
                  Tumbling:
                    Interval: '{{ Interval }}'
                    Offset: '{{ Offset }}'
      - name: AssetModelCompositeModels
        value:
          - Id: '{{ Id }}'
            ExternalId: '{{ ExternalId }}'
            ComposedAssetModelId: '{{ ComposedAssetModelId }}'
            ParentAssetModelCompositeModelExternalId: '{{ ParentAssetModelCompositeModelExternalId }}'
            Path:
              - '{{ Path[0] }}'
            Description: '{{ Description }}'
            Name: '{{ Name }}'
            Type: '{{ Type }}'
            CompositeModelProperties:
              - null
      - name: AssetModelHierarchies
        value:
          - Id: '{{ Id }}'
            ExternalId: '{{ ExternalId }}'
            LogicalId: '{{ LogicalId }}'
            Name: '{{ Name }}'
            ChildAssetModelId: '{{ ChildAssetModelId }}'
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
DELETE FROM aws.iotsitewise.asset_models
WHERE data__Identifier = '<AssetModelId>'
AND region = 'us-east-1';
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

### Read
```json
iotsitewise:DescribeAssetModel,
iotsitewise:ListAssetModelProperties,
iotsitewise:DescribeAssetModelCompositeModel,
iotsitewise:ListAssetModelCompositeModels,
iotsitewise:ListTagsForResource
```

### Update
```json
iotsitewise:DescribeAssetModel,
iotsitewise:ListTagsForResource,
iotsitewise:TagResource,
iotsitewise:UntagResource,
iotsitewise:ListAssetModelProperties,
iotsitewise:ListAssetModelCompositeModels,
iotsitewise:CreateAssetModelCompositeModel,
iotsitewise:UpdateAssetModelCompositeModel,
iotsitewise:DeleteAssetModelCompositeModel,
iotsitewise:DescribeAssetModelCompositeModel,
iotsitewise:UpdateAssetModel
```

### Delete
```json
iotsitewise:DescribeAssetModel,
iotsitewise:DeleteAssetModel,
iotsitewise:ListAssetModelProperties,
iotsitewise:ListAssetModelCompositeModels
```

### List
```json
iotsitewise:DescribeAssetModel,
iotsitewise:ListAssetModels,
iotsitewise:ListTagsForResource,
iotsitewise:ListAssetModelProperties,
iotsitewise:ListAssetModelCompositeModels
```

