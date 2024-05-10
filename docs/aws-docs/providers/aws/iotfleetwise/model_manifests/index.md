---
title: model_manifests
hide_title: false
hide_table_of_contents: false
keywords:
  - model_manifests
  - iotfleetwise
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


Used to retrieve a list of <code>model_manifests</code> in a region or to create or delete a <code>model_manifests</code> resource, use <code>model_manifest</code> to read or update an individual resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>model_manifests</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>Definition of AWS::IoTFleetWise::ModelManifest Resource Type</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="aws.iotfleetwise.model_manifests" /></td></tr>
</tbody></table>

## Fields
<table><tbody>
<tr><th>Name</th><th>Datatype</th><th>Description</th></tr>
<tr><td><CopyableCode code="name" /></td><td><code>string</code></td><td></td></tr>
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
name
FROM aws.iotfleetwise.model_manifests
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
 "Name": "{{ Name }}",
 "SignalCatalogArn": "{{ SignalCatalogArn }}"
}
>>>
--required properties only
INSERT INTO aws.iotfleetwise.model_manifests (
 Name,
 SignalCatalogArn,
 region
)
SELECT 
{{ .Name }},
 {{ .SignalCatalogArn }},
'us-east-1';
```
</TabItem>
<TabItem value="all">

```sql
<<<json
{
 "Description": "{{ Description }}",
 "Name": "{{ Name }}",
 "Nodes": [
  "{{ Nodes[0] }}"
 ],
 "SignalCatalogArn": "{{ SignalCatalogArn }}",
 "Status": "{{ Status }}",
 "Tags": [
  {
   "Key": "{{ Key }}",
   "Value": "{{ Value }}"
  }
 ]
}
>>>
--all properties
INSERT INTO aws.iotfleetwise.model_manifests (
 Description,
 Name,
 Nodes,
 SignalCatalogArn,
 Status,
 Tags,
 region
)
SELECT 
 {{ .Description }},
 {{ .Name }},
 {{ .Nodes }},
 {{ .SignalCatalogArn }},
 {{ .Status }},
 {{ .Tags }},
 'us-east-1';
```
</TabItem>
</Tabs>

## `DELETE` Example

```sql
DELETE FROM aws.iotfleetwise.model_manifests
WHERE data__Identifier = '<Name>'
AND region = 'us-east-1';
```

## Permissions

To operate on the <code>model_manifests</code> resource, the following permissions are required:

### Create
```json
iotfleetwise:CreateModelManifest,
iotfleetwise:GetModelManifest,
iotfleetwise:UpdateModelManifest,
iotfleetwise:ListModelManifestNodes,
iotfleetwise:ListTagsForResource,
iotfleetwise:TagResource
```

### Delete
```json
iotfleetwise:DeleteModelManifest,
iotfleetwise:GetModelManifest
```

### List
```json
iotfleetwise:ListModelManifests
```

