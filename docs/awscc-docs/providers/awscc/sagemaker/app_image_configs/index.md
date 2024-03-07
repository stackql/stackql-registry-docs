---
title: app_image_configs
hide_title: false
hide_table_of_contents: false
keywords:
  - app_image_configs
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
Retrieves a list of <code>app_image_configs</code> in a region

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>app_image_configs</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>app_image_configs</td></tr>
<tr><td><b>Id</b></td><td><code>awscc.sagemaker.app_image_configs</code></td></tr>
</tbody></table>

## Fields
<table><tbody>
<tr><th>Name</th><th>Datatype</th><th>Description</th></tr>
<tr><td><code>app_image_config_name</code></td><td><code>string</code></td><td>The Name of the AppImageConfig.</td></tr>
<tr><td><code>region</code></td><td><code>string</code></td><td>AWS region.</td></tr>

</tbody></table>

## Methods
Currently only <code>SELECT</code> is supported for this resource resource.

## Permissions

To operate on the <code>app_image_configs</code> resource, the following permissions are required:

### Create
```json
sagemaker:CreateAppImageConfig,
sagemaker:DescribeAppImageConfig
```

### List
```json
sagemaker:ListAppImageConfigs
```


## Example
```sql
SELECT
region,
app_image_config_name
FROM awscc.sagemaker.app_image_configs
WHERE region = 'us-east-1'
```
