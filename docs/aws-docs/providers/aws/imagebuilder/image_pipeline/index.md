---
title: image_pipeline
hide_title: false
hide_table_of_contents: false
keywords:
  - image_pipeline
  - imagebuilder
  - aws
  - stackql
  - infrastructure-as-code
  - configuration-as-data
  - cloud inventory
description: Query, deploy and manage AWS resources using SQL
custom_edit_url: null
image: /img/providers/aws/stackql-aws-provider-featured-image.png
---
Gets an individual <code>image_pipeline</code> resource

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>image_pipeline</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>Resource schema for AWS::ImageBuilder::ImagePipeline</td></tr>
<tr><td><b>Id</b></td><td><code>aws.imagebuilder.image_pipeline</code></td></tr>
</tbody></table>

## Fields
<table><tbody>
<tr><th>Name</th><th>Datatype</th><th>Description</th></tr>
<tr><td><code>arn</code></td><td><code>string</code></td><td>The Amazon Resource Name (ARN) of the image pipeline.</td></tr>
<tr><td><code>name</code></td><td><code>string</code></td><td>The name of the image pipeline.</td></tr>
<tr><td><code>description</code></td><td><code>string</code></td><td>The description of the image pipeline.</td></tr>
<tr><td><code>image_tests_configuration</code></td><td><code>object</code></td><td>The image tests configuration of the image pipeline.</td></tr>
<tr><td><code>status</code></td><td><code>string</code></td><td>The status of the image pipeline.</td></tr>
<tr><td><code>schedule</code></td><td><code>object</code></td><td>The schedule of the image pipeline.</td></tr>
<tr><td><code>image_recipe_arn</code></td><td><code>string</code></td><td>The Amazon Resource Name (ARN) of the image recipe that defines how images are configured, tested, and assessed.</td></tr>
<tr><td><code>container_recipe_arn</code></td><td><code>string</code></td><td>The Amazon Resource Name (ARN) of the container recipe that defines how images are configured and tested.</td></tr>
<tr><td><code>distribution_configuration_arn</code></td><td><code>string</code></td><td>The Amazon Resource Name (ARN) of the distribution configuration associated with this image pipeline.</td></tr>
<tr><td><code>infrastructure_configuration_arn</code></td><td><code>string</code></td><td>The Amazon Resource Name (ARN) of the infrastructure configuration associated with this image pipeline.</td></tr>
<tr><td><code>workflows</code></td><td><code>array</code></td><td>Workflows to define the image build process</td></tr>
<tr><td><code>enhanced_image_metadata_enabled</code></td><td><code>boolean</code></td><td>Collects additional information about the image being created, including the operating system (OS) version and package list.</td></tr>
<tr><td><code>image_scanning_configuration</code></td><td><code>object</code></td><td>Contains settings for vulnerability scans.</td></tr>
<tr><td><code>execution_role</code></td><td><code>string</code></td><td>The execution role name&#x2F;ARN for the image build, if provided</td></tr>
<tr><td><code>tags</code></td><td><code>object</code></td><td>The tags of this image pipeline.</td></tr>
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
arn,
name,
description,
image_tests_configuration,
status,
schedule,
image_recipe_arn,
container_recipe_arn,
distribution_configuration_arn,
infrastructure_configuration_arn,
workflows,
enhanced_image_metadata_enabled,
image_scanning_configuration,
execution_role,
tags
FROM aws.imagebuilder.image_pipeline
WHERE data__Identifier = '<Arn>';
```

## Permissions

To operate on the <code>image_pipeline</code> resource, the following permissions are required:

### Update
```json
iam:PassRole,
imagebuilder:GetImagePipeline,
imagebuilder:UpdateImagePipeline,
imagebuilder:GetWorkflow
```

### Read
```json
imagebuilder:GetImagePipeline
```

### Delete
```json
imagebuilder:UnTagResource,
imagebuilder:GetImagePipeline,
imagebuilder:DeleteImagePipeline
```

