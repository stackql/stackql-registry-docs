---
title: image
hide_title: false
hide_table_of_contents: false
keywords:
  - image
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
Gets an individual <code>image</code> resource

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>image</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>image</td></tr>
<tr><td><b>Id</b></td><td><code>awscc.imagebuilder.image</code></td></tr>
</tbody></table>

## Fields
<table><tbody>
<tr><th>Name</th><th>Datatype</th><th>Description</th></tr>
<tr><td><code>arn</code></td><td><code>string</code></td><td>The Amazon Resource Name (ARN) of the image.</td></tr>
<tr><td><code>name</code></td><td><code>string</code></td><td>The name of the image.</td></tr>
<tr><td><code>image_tests_configuration</code></td><td><code>object</code></td><td>The image tests configuration used when creating this image.</td></tr>
<tr><td><code>image_recipe_arn</code></td><td><code>string</code></td><td>The Amazon Resource Name (ARN) of the image recipe that defines how images are configured, tested, and assessed.</td></tr>
<tr><td><code>container_recipe_arn</code></td><td><code>string</code></td><td>The Amazon Resource Name (ARN) of the container recipe that defines how images are configured and tested.</td></tr>
<tr><td><code>distribution_configuration_arn</code></td><td><code>string</code></td><td>The Amazon Resource Name (ARN) of the distribution configuration.</td></tr>
<tr><td><code>infrastructure_configuration_arn</code></td><td><code>string</code></td><td>The Amazon Resource Name (ARN) of the infrastructure configuration.</td></tr>
<tr><td><code>workflows</code></td><td><code>array</code></td><td>Workflows to define the image build process</td></tr>
<tr><td><code>image_id</code></td><td><code>string</code></td><td>The AMI ID of the EC2 AMI in current region.</td></tr>
<tr><td><code>image_uri</code></td><td><code>string</code></td><td>URI for containers created in current Region with default ECR image tag</td></tr>
<tr><td><code>enhanced_image_metadata_enabled</code></td><td><code>boolean</code></td><td>Collects additional information about the image being created, including the operating system (OS) version and package list.</td></tr>
<tr><td><code>image_scanning_configuration</code></td><td><code>object</code></td><td>Contains settings for vulnerability scans.</td></tr>
<tr><td><code>execution_role</code></td><td><code>string</code></td><td>The execution role name&#x2F;ARN for the image build, if provided</td></tr>
<tr><td><code>tags</code></td><td><code>object</code></td><td>The tags associated with the image.</td></tr>
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
image_tests_configuration,
image_recipe_arn,
container_recipe_arn,
distribution_configuration_arn,
infrastructure_configuration_arn,
workflows,
image_id,
image_uri,
enhanced_image_metadata_enabled,
image_scanning_configuration,
execution_role,
tags
FROM awscc.imagebuilder.image
WHERE data__Identifier = '<Arn>';
```

## Permissions

To operate on the <code>image</code> resource, the following permissions are required:

### Read
```json
imagebuilder:GetImage
```

### Delete
```json
imagebuilder:GetImage,
imagebuilder:DeleteImage,
imagebuilder:UnTagResource,
imagebuilder:CancelImageCreation
```

