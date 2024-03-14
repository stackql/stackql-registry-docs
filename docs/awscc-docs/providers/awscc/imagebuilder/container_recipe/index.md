---
title: container_recipe
hide_title: false
hide_table_of_contents: false
keywords:
  - container_recipe
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
Gets an individual <code>container_recipe</code> resource

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>container_recipe</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>container_recipe</td></tr>
<tr><td><b>Id</b></td><td><code>awscc.imagebuilder.container_recipe</code></td></tr>
</tbody></table>

## Fields
<table><tbody>
<tr><th>Name</th><th>Datatype</th><th>Description</th></tr>
<tr><td><code>arn</code></td><td><code>string</code></td><td>The Amazon Resource Name (ARN) of the container recipe.</td></tr>
<tr><td><code>name</code></td><td><code>string</code></td><td>The name of the container recipe.</td></tr>
<tr><td><code>description</code></td><td><code>string</code></td><td>The description of the container recipe.</td></tr>
<tr><td><code>version</code></td><td><code>string</code></td><td>The semantic version of the container recipe (&lt;major&gt;.&lt;minor&gt;.&lt;patch&gt;).</td></tr>
<tr><td><code>components</code></td><td><code>array</code></td><td>Components for build and test that are included in the container recipe.</td></tr>
<tr><td><code>instance_configuration</code></td><td><code>object</code></td><td>A group of options that can be used to configure an instance for building and testing container images.</td></tr>
<tr><td><code>dockerfile_template_data</code></td><td><code>string</code></td><td>Dockerfiles are text documents that are used to build Docker containers, and ensure that they contain all of the elements required by the application running inside. The template data consists of contextual variables where Image Builder places build information or scripts, based on your container image recipe.</td></tr>
<tr><td><code>dockerfile_template_uri</code></td><td><code>string</code></td><td>The S3 URI for the Dockerfile that will be used to build your container image.</td></tr>
<tr><td><code>platform_override</code></td><td><code>string</code></td><td>Specifies the operating system platform when you use a custom source image.</td></tr>
<tr><td><code>container_type</code></td><td><code>string</code></td><td>Specifies the type of container, such as Docker.</td></tr>
<tr><td><code>image_os_version_override</code></td><td><code>string</code></td><td>Specifies the operating system version for the source image.</td></tr>
<tr><td><code>target_repository</code></td><td><code>object</code></td><td>The destination repository for the container image.</td></tr>
<tr><td><code>kms_key_id</code></td><td><code>string</code></td><td>Identifies which KMS key is used to encrypt the container image.</td></tr>
<tr><td><code>parent_image</code></td><td><code>string</code></td><td>The source image for the container recipe.</td></tr>
<tr><td><code>working_directory</code></td><td><code>string</code></td><td>The working directory to be used during build and test workflows.</td></tr>
<tr><td><code>tags</code></td><td><code>object</code></td><td>Tags that are attached to the container recipe.</td></tr>
<tr><td><code>region</code></td><td><code>string</code></td><td>AWS region.</td></tr>

</tbody></table>

## Methods
Currently only <code>SELECT</code> is supported for this resource resource.

## Example
```sql
SELECT
region,
arn,
name,
description,
version,
components,
instance_configuration,
dockerfile_template_data,
dockerfile_template_uri,
platform_override,
container_type,
image_os_version_override,
target_repository,
kms_key_id,
parent_image,
working_directory,
tags
FROM awscc.imagebuilder.container_recipe
WHERE data__Identifier = '<Arn>';
```

## Permissions

To operate on the <code>container_recipe</code> resource, the following permissions are required:

### Read
```json
imagebuilder:GetContainerRecipe
```

### Delete
```json
imagebuilder:UnTagResource,
imagebuilder:GetContainerRecipe,
imagebuilder:DeleteContainerRecipe
```

