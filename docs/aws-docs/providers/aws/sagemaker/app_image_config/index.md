---
title: app_image_config
hide_title: false
hide_table_of_contents: false
keywords:
  - app_image_config
  - sagemaker
  - aws
  - stackql
  - infrastructure-as-code
  - configuration-as-data
  - cloud inventory
description: Query, deploy and manage AWS resources using SQL
custom_edit_url: null
image: /img/providers/aws/stackql-aws-provider-featured-image.png
---
Gets or operates on an individual <code>app_image_config</code> resource, use <code>app_image_configs</code> to retrieve a list of resources or to create a resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>app_image_config</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>Resource Type definition for AWS::SageMaker::AppImageConfig</td></tr>
<tr><td><b>Id</b></td><td><code>aws.sagemaker.app_image_config</code></td></tr>
</tbody></table>

## Fields
<table><tbody>
<tr><th>Name</th><th>Datatype</th><th>Description</th></tr>
<tr><td><code>app_image_config_arn</code></td><td><code>string</code></td><td>The Amazon Resource Name (ARN) of the AppImageConfig.</td></tr>
<tr><td><code>app_image_config_name</code></td><td><code>string</code></td><td>The Name of the AppImageConfig.</td></tr>
<tr><td><code>kernel_gateway_image_config</code></td><td><code>object</code></td><td>The KernelGatewayImageConfig.</td></tr>
<tr><td><code>jupyter_lab_app_image_config</code></td><td><code>object</code></td><td>The JupyterLabAppImageConfig.</td></tr>
<tr><td><code>code_editor_app_image_config</code></td><td><code>object</code></td><td>The CodeEditorAppImageConfig.</td></tr>
<tr><td><code>tags</code></td><td><code>array</code></td><td>A list of tags to apply to the AppImageConfig.</td></tr>
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
    <td><code>update_resource</code></td>
    <td><code>UPDATE</code></td>
    <td><code>data__Identifier, data__PatchDocument, region</code></td>
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
app_image_config_arn,
app_image_config_name,
kernel_gateway_image_config,
jupyter_lab_app_image_config,
code_editor_app_image_config,
tags
FROM aws.sagemaker.app_image_config
WHERE data__Identifier = '<AppImageConfigName>';
```

## Permissions

To operate on the <code>app_image_config</code> resource, the following permissions are required:

### Read
```json
sagemaker:DescribeAppImageConfig
```

### Update
```json
sagemaker:UpdateAppImageConfig,
sagemaker:DescribeAppImageConfig
```

### Delete
```json
sagemaker:DeleteAppImageConfig,
sagemaker:DescribeAppImageConfig
```

