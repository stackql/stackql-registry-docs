---
title: layer_version
hide_title: false
hide_table_of_contents: false
keywords:
  - layer_version
  - lambda
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

Gets or operates on an individual <code>layer_version</code> resource, use <code>layer_versions</code> to retrieve a list of resources or to create a resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>layer_version</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>Resource Type definition for AWS::Lambda::LayerVersion</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="aws.lambda.layer_version" /></td></tr>
</tbody></table>

## Fields
<table><tbody>
<tr><th>Name</th><th>Datatype</th><th>Description</th></tr>
<tr><td><CopyableCode code="compatible_runtimes" /></td><td><code>array</code></td><td>A list of compatible function runtimes. Used for filtering with ListLayers and ListLayerVersions.</td></tr>
<tr><td><CopyableCode code="license_info" /></td><td><code>string</code></td><td>The layer's software license.</td></tr>
<tr><td><CopyableCode code="description" /></td><td><code>string</code></td><td>The description of the version.</td></tr>
<tr><td><CopyableCode code="layer_name" /></td><td><code>string</code></td><td>The name or Amazon Resource Name (ARN) of the layer.</td></tr>
<tr><td><CopyableCode code="content" /></td><td><code>object</code></td><td>The function layer archive.</td></tr>
<tr><td><CopyableCode code="layer_version_arn" /></td><td><code>string</code></td><td></td></tr>
<tr><td><CopyableCode code="compatible_architectures" /></td><td><code>array</code></td><td>A list of compatible instruction set architectures.</td></tr>
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
    <td><CopyableCode code="delete_resource" /></td>
    <td><code>DELETE</code></td>
    <td><CopyableCode code="data__Identifier, region" /></td>
  </tr>
  <tr>
    <td><CopyableCode code="get_resource" /></td>
    <td><code>SELECT</code></td>
    <td><CopyableCode code="data__Identifier, region" /></td>
  </tr>
</tbody></table>

## `SELECT` Example
```sql
SELECT
region,
compatible_runtimes,
license_info,
description,
layer_name,
content,
layer_version_arn,
compatible_architectures
FROM aws.lambda.layer_version
WHERE data__Identifier = '<LayerVersionArn>';
```

## Permissions

To operate on the <code>layer_version</code> resource, the following permissions are required:

### Read
```json
lambda:GetLayerVersion
```

### Delete
```json
lambda:GetLayerVersion,
lambda:DeleteLayerVersion
```

