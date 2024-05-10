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


Used to retrieve a list of <code>vehicles</code> in a region or to create or delete a <code>vehicles</code> resource, use <code>vehicle</code> to read or update an individual resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>vehicles</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>Definition of AWS::IoTFleetWise::Vehicle Resource Type</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="aws.iotfleetwise.vehicles" /></td></tr>
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
FROM aws.iotfleetwise.vehicles
WHERE region = 'us-east-1';
```

## `INSERT` Example

Use the following StackQL query and manifest file to create a new <code>vehicle</code> resource, using <a ref="https://pypi.org/project/stack-deploy/" target="_blank"><code><b>stack-deploy</b></code></a>.

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
-- vehicle.iql (required properties only)
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
-- vehicle.iql (all properties)
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

## `DELETE` Example

```sql
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

### Delete
```json
iotfleetwise:GetVehicle,
iotfleetwise:DeleteVehicle
```

### List
```json
iotfleetwise:ListVehicles
```

