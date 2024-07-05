---
title: vehicles
hide_title: false
hide_table_of_contents: false
keywords:
  - vehicles
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

Creates, updates, deletes or gets a <code>vehicle</code> resource or lists <code>vehicles</code> in a region

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>vehicles</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>Definition of AWS::IoTFleetWise::Vehicle Resource Type</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="aws.iotfleetwise.vehicles" /></td></tr>
</tbody></table>

## Fields
<table><tbody><tr><th>Name</th><th>Datatype</th><th>Description</th></tr><tr><td><CopyableCode code="arn" /></td><td><code>string</code></td><td></td></tr>
<tr><td><CopyableCode code="association_behavior" /></td><td><code>string</code></td><td></td></tr>
<tr><td><CopyableCode code="attributes" /></td><td><code>object</code></td><td></td></tr>
<tr><td><CopyableCode code="creation_time" /></td><td><code>string</code></td><td></td></tr>
<tr><td><CopyableCode code="decoder_manifest_arn" /></td><td><code>string</code></td><td></td></tr>
<tr><td><CopyableCode code="name" /></td><td><code>string</code></td><td></td></tr>
<tr><td><CopyableCode code="last_modification_time" /></td><td><code>string</code></td><td></td></tr>
<tr><td><CopyableCode code="model_manifest_arn" /></td><td><code>string</code></td><td></td></tr>
<tr><td><CopyableCode code="tags" /></td><td><code>array</code></td><td></td></tr>
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
    <td><CopyableCode code="Name, DecoderManifestArn, ModelManifestArn, region" /></td>
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
Gets all <code>vehicles</code> in a region.
```sql
SELECT
region,
arn,
association_behavior,
attributes,
creation_time,
decoder_manifest_arn,
name,
last_modification_time,
model_manifest_arn,
tags
FROM aws.iotfleetwise.vehicles
WHERE region = 'us-east-1';
```
Gets all properties from an individual <code>vehicle</code>.
```sql
SELECT
region,
arn,
association_behavior,
attributes,
creation_time,
decoder_manifest_arn,
name,
last_modification_time,
model_manifest_arn,
tags
FROM aws.iotfleetwise.vehicles
WHERE region = 'us-east-1' AND data__Identifier = '<Name>';
```

## `INSERT` example

Use the following StackQL query and manifest file to create a new <code>vehicle</code> resource, using [__`stack-deploy`__](https://pypi.org/project/stack-deploy/).

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
INSERT INTO aws.iotfleetwise.vehicles (
 DecoderManifestArn,
 Name,
 ModelManifestArn,
 region
)
SELECT 
'{{ DecoderManifestArn }}',
 '{{ Name }}',
 '{{ ModelManifestArn }}',
'{{ region }}';
```
</TabItem>
<TabItem value="all">

```sql
/*+ create */
INSERT INTO aws.iotfleetwise.vehicles (
 AssociationBehavior,
 Attributes,
 DecoderManifestArn,
 Name,
 ModelManifestArn,
 Tags,
 region
)
SELECT 
 '{{ AssociationBehavior }}',
 '{{ Attributes }}',
 '{{ DecoderManifestArn }}',
 '{{ Name }}',
 '{{ ModelManifestArn }}',
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
  - name: vehicle
    props:
      - name: AssociationBehavior
        value: '{{ AssociationBehavior }}'
      - name: Attributes
        value: {}
      - name: DecoderManifestArn
        value: '{{ DecoderManifestArn }}'
      - name: Name
        value: '{{ Name }}'
      - name: ModelManifestArn
        value: '{{ ModelManifestArn }}'
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
DELETE FROM aws.iotfleetwise.vehicles
WHERE data__Identifier = '<Name>'
AND region = 'us-east-1';
```

## Permissions

To operate on the <code>vehicles</code> resource, the following permissions are required:

### Create
```json
iotfleetwise:GetVehicle,
iotfleetwise:CreateVehicle,
iot:CreateThing,
iot:DescribeThing,
iotfleetwise:ListTagsForResource,
iotfleetwise:ListVehicles,
iotfleetwise:TagResource
```

### Read
```json
iotfleetwise:GetVehicle,
iotfleetwise:ListTagsForResource
```

### Update
```json
iotfleetwise:GetVehicle,
iotfleetwise:UpdateVehicle,
iotfleetwise:ListTagsForResource,
iotfleetwise:TagResource,
iotfleetwise:UntagResource
```

### Delete
```json
iotfleetwise:GetVehicle,
iotfleetwise:DeleteVehicle
```

### List
```json
iotfleetwise:ListVehicles
```

