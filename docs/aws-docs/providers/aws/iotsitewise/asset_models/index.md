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


Used to retrieve a list of <code>asset_models</code> in a region or to create or delete a <code>asset_models</code> resource, use <code>asset_model</code> to read or update an individual resource.

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
asset_model_id
FROM aws.iotsitewise.asset_models
WHERE region = 'us-east-1';
```

## `INSERT` Example

<Tabs
    defaultValue="required"
    values={[
      { label: 'Required Properties', value: 'required', },
      { label: 'All Properties', value: 'all', },
    ]
}>
<TabItem value="required">

```sql
<<<json
{
 "AssetModelName": "{{ AssetModelName }}"
}
>>>
--required properties only
INSERT INTO aws.iotsitewise.asset_models (
 AssetModelName,
 region
)
SELECT 
{{ .AssetModelName }},
'us-east-1';
```
</TabItem>
<TabItem value="all">

```sql
<<<json
{
 "AssetModelType": "{{ AssetModelType }}",
 "AssetModelExternalId": "{{ AssetModelExternalId }}",
 "AssetModelName": "{{ AssetModelName }}",
 "AssetModelDescription": "{{ AssetModelDescription }}",
 "AssetModelProperties": [
  {
   "LogicalId": "{{ LogicalId }}",
   "Id": "{{ Id }}",
   "ExternalId": "{{ ExternalId }}",
   "Name": "{{ Name }}",
   "DataType": "{{ DataType }}",
   "DataTypeSpec": "{{ DataTypeSpec }}",
   "Unit": "{{ Unit }}",
   "Type": {
    "TypeName": "{{ TypeName }}",
    "Attribute": {
     "DefaultValue": "{{ DefaultValue }}"
    },
    "Transform": {
     "Expression": "{{ Expression }}",
     "Variables": [
      {
       "Name": "{{ Name }}",
       "Value": {
        "PropertyLogicalId": "{{ PropertyLogicalId }}",
        "PropertyId": "{{ PropertyId }}",
        "PropertyExternalId": "{{ PropertyExternalId }}",
        "PropertyPath": [
         {
          "Name": "{{ Name }}"
         }
        ],
        "HierarchyLogicalId": "{{ HierarchyLogicalId }}",
        "HierarchyId": "{{ HierarchyId }}",
        "HierarchyExternalId": "{{ HierarchyExternalId }}"
       }
      }
     ]
    },
    "Metric": {
     "Expression": "{{ Expression }}",
     "Variables": [
      null
     ],
     "Window": {
      "Tumbling": {
       "Interval": "{{ Interval }}",
       "Offset": "{{ Offset }}"
      }
     }
    }
   }
  }
 ],
 "AssetModelCompositeModels": [
  {
   "Id": "{{ Id }}",
   "ExternalId": "{{ ExternalId }}",
   "ComposedAssetModelId": "{{ ComposedAssetModelId }}",
   "ParentAssetModelCompositeModelExternalId": "{{ ParentAssetModelCompositeModelExternalId }}",
   "Path": [
    "{{ Path[0] }}"
   ],
   "Description": "{{ Description }}",
   "Name": "{{ Name }}",
   "Type": "{{ Type }}",
   "CompositeModelProperties": [
    null
   ]
  }
 ],
 "AssetModelHierarchies": [
  {
   "Id": "{{ Id }}",
   "ExternalId": "{{ ExternalId }}",
   "LogicalId": "{{ LogicalId }}",
   "Name": "{{ Name }}",
   "ChildAssetModelId": "{{ ChildAssetModelId }}"
  }
 ],
 "Tags": [
  {
   "Key": "{{ Key }}",
   "Value": "{{ Value }}"
  }
 ]
}
>>>
--all properties
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
 {{ .AssetModelType }},
 {{ .AssetModelExternalId }},
 {{ .AssetModelName }},
 {{ .AssetModelDescription }},
 {{ .AssetModelProperties }},
 {{ .AssetModelCompositeModels }},
 {{ .AssetModelHierarchies }},
 {{ .Tags }},
 'us-east-1';
```
</TabItem>
</Tabs>

## `DELETE` Example

```sql
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

