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

Creates, updates, deletes or gets a <code>decoder_manifest</code> resource or lists <code>decoder_manifests</code> in a region

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>decoder_manifests</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>Definition of AWS::IoTFleetWise::DecoderManifest Resource Type</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="aws.iotfleetwise.decoder_manifests" /></td></tr>
</tbody></table>

## Fields
<table><tbody><tr><th>Name</th><th>Datatype</th><th>Description</th></tr><tr><td><CopyableCode code="arn" /></td><td><code>string</code></td><td></td></tr>
<tr><td><CopyableCode code="creation_time" /></td><td><code>string</code></td><td></td></tr>
<tr><td><CopyableCode code="description" /></td><td><code>string</code></td><td></td></tr>
<tr><td><CopyableCode code="last_modification_time" /></td><td><code>string</code></td><td></td></tr>
<tr><td><CopyableCode code="model_manifest_arn" /></td><td><code>string</code></td><td></td></tr>
<tr><td><CopyableCode code="name" /></td><td><code>string</code></td><td></td></tr>
<tr><td><CopyableCode code="network_interfaces" /></td><td><code>array</code></td><td></td></tr>
<tr><td><CopyableCode code="signal_decoders" /></td><td><code>array</code></td><td></td></tr>
<tr><td><CopyableCode code="status" /></td><td><code>string</code></td><td></td></tr>
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
    <td><CopyableCode code="Name, ModelManifestArn, region" /></td>
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
Gets all <code>decoder_manifests</code> in a region.
```sql
SELECT
region,
arn,
creation_time,
description,
last_modification_time,
model_manifest_arn,
name,
network_interfaces,
signal_decoders,
status,
tags
FROM aws.iotfleetwise.decoder_manifests
WHERE region = 'us-east-1';
```
Gets all properties from an individual <code>decoder_manifest</code>.
```sql
SELECT
region,
arn,
creation_time,
description,
last_modification_time,
model_manifest_arn,
name,
network_interfaces,
signal_decoders,
status,
tags
FROM aws.iotfleetwise.decoder_manifests
WHERE region = 'us-east-1' AND data__Identifier = '<Name>';
```

## `INSERT` example

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
/*+ create */
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
/*+ create */
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

## `DELETE` example

```sql
/*+ delete */
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

### Read
```json
iotfleetwise:GetDecoderManifest,
iotfleetwise:ListDecoderManifestSignals,
iotfleetwise:ListDecoderManifestNetworkInterfaces,
iotfleetwise:ListTagsForResource
```

### Update
```json
iotfleetwise:UpdateDecoderManifest,
iotfleetwise:GetDecoderManifest,
iotfleetwise:ListDecoderManifestSignals,
iotfleetwise:ListDecoderManifestNetworkInterfaces,
iotfleetwise:ListTagsForResource,
iotfleetwise:TagResource,
iotfleetwise:UntagResource
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

