---
title: decoder_manifests
hide_title: false
hide_table_of_contents: false
keywords:
  - decoder_manifests
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


Used to retrieve a list of <code>decoder_manifests</code> in a region or to create or delete a <code>decoder_manifests</code> resource, use <code>decoder_manifest</code> to read or update an individual resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>decoder_manifests</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>Definition of AWS::IoTFleetWise::DecoderManifest Resource Type</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="aws.iotfleetwise.decoder_manifests" /></td></tr>
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
FROM aws.iotfleetwise.decoder_manifests
WHERE region = 'us-east-1';
```

## `INSERT` Example

Use the following StackQL query and manifest file to create a new <code>decoder_manifest</code> resource, using [__`stack-deploy`__](https://pypi.org/project/stack-deploy/).

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
-- decoder_manifest.iql (required properties only)
INSERT INTO aws.iotfleetwise.decoder_manifests (
 ModelManifestArn,
 Name,
 region
)
SELECT 
'{{ ModelManifestArn }}',
 '{{ Name }}',
'{{ region }}';
```
</TabItem>
<TabItem value="all">

```sql
-- decoder_manifest.iql (all properties)
INSERT INTO aws.iotfleetwise.decoder_manifests (
 Description,
 ModelManifestArn,
 Name,
 NetworkInterfaces,
 SignalDecoders,
 Status,
 Tags,
 region
)
SELECT 
 '{{ Description }}',
 '{{ ModelManifestArn }}',
 '{{ Name }}',
 '{{ NetworkInterfaces }}',
 '{{ SignalDecoders }}',
 '{{ Status }}',
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
  - name: decoder_manifest
    props:
      - name: Description
        value: '{{ Description }}'
      - name: ModelManifestArn
        value: '{{ ModelManifestArn }}'
      - name: Name
        value: '{{ Name }}'
      - name: NetworkInterfaces
        value:
          - null
      - name: SignalDecoders
        value:
          - null
      - name: Status
        value: '{{ Status }}'
      - name: Tags
        value:
          - Key: '{{ Key }}'
            Value: '{{ Value }}'

```
</TabItem>
</Tabs>

## `DELETE` Example

```sql
DELETE FROM aws.iotfleetwise.decoder_manifests
WHERE data__Identifier = '<Name>'
AND region = 'us-east-1';
```

## Permissions

To operate on the <code>decoder_manifests</code> resource, the following permissions are required:

### Create
```json
iotfleetwise:CreateDecoderManifest,
iotfleetwise:GetDecoderManifest,
iotfleetwise:UpdateDecoderManifest,
iotfleetwise:ListDecoderManifestSignals,
iotfleetwise:ListDecoderManifestNetworkInterfaces,
iotfleetwise:ListTagsForResource,
iotfleetwise:TagResource
```

### Delete
```json
iotfleetwise:DeleteDecoderManifest,
iotfleetwise:GetDecoderManifest
```

### List
```json
iotfleetwise:ListDecoderManifests
```

