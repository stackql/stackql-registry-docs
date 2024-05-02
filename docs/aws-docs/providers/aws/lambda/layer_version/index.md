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
Gets an individual <code>layer_version</code> resource

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>layer_version</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>Resource Type definition for AWS::Lambda::LayerVersion</td></tr>
<tr><td><b>Id</b></td><td><code>aws.lambda.layer_version</code></td></tr>
</tbody></table>

## Fields
<table><tbody>
<tr><th>Name</th><th>Datatype</th><th>Description</th></tr>
<tr><td><code>compatible_runtimes</code></td><td><code>array</code></td><td>A list of compatible function runtimes. Used for filtering with ListLayers and ListLayerVersions.</td></tr>
<tr><td><code>license_info</code></td><td><code>string</code></td><td>The layer's software license.</td></tr>
<tr><td><code>description</code></td><td><code>string</code></td><td>The description of the version.</td></tr>
<tr><td><code>layer_name</code></td><td><code>string</code></td><td>The name or Amazon Resource Name (ARN) of the layer.</td></tr>
<tr><td><code>content</code></td><td><code>object</code></td><td>The function layer archive.</td></tr>
<tr><td><code>layer_version_arn</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>compatible_architectures</code></td><td><code>array</code></td><td>A list of compatible instruction set architectures.</td></tr>
<tr><td><code>region</code></td><td><code>string</code></td><td>AWS region.</td></tr>

</tbody></table>

## Methods

<table><tbody>
  <tr>
    <th>Name</th>
    <th>Accessible by</th>
    <th>Required Params</th>
  </tr>
  <tr>
    <td><code>delete_resource</code></td>
    <td><code>DELETE</code></td>
    <td><code>data__Identifier, region</code></td>
  </tr>
  <tr>
    <td><code>get_resource</code></td>
    <td><code>SELECT</code></td>
    <td><code>data__Identifier, region</code></td>
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

