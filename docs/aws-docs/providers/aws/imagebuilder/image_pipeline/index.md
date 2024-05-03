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

import CopyableCode from '@site/src/components/CopyableCode/CopyableCode';

Gets or operates on an individual <code>image_pipeline</code> resource, use <code>image_pipelines</code> to retrieve a list of resources or to create a resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>image_pipeline</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>Resource schema for AWS::ImageBuilder::ImagePipeline</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="aws.imagebuilder.image_pipeline" /></td></tr>
</tbody></table>

## Fields
<table><tbody>
<tr><th>Name</th><th>Datatype</th><th>Description</th></tr>
<tr><td><CopyableCode code="arn" /></td><td><code>string</code></td><td>The Amazon Resource Name (ARN) of the image pipeline.</td></tr>
<tr><td><CopyableCode code="name" /></td><td><code>string</code></td><td>The name of the image pipeline.</td></tr>
<tr><td><CopyableCode code="description" /></td><td><code>string</code></td><td>The description of the image pipeline.</td></tr>
<tr><td><CopyableCode code="image_tests_configuration" /></td><td><code>object</code></td><td>The image tests configuration of the image pipeline.</td></tr>
<tr><td><CopyableCode code="status" /></td><td><code>string</code></td><td>The status of the image pipeline.</td></tr>
<tr><td><CopyableCode code="schedule" /></td><td><code>object</code></td><td>The schedule of the image pipeline.</td></tr>
<tr><td><CopyableCode code="image_recipe_arn" /></td><td><code>string</code></td><td>The Amazon Resource Name (ARN) of the image recipe that defines how images are configured, tested, and assessed.</td></tr>
<tr><td><CopyableCode code="container_recipe_arn" /></td><td><code>string</code></td><td>The Amazon Resource Name (ARN) of the container recipe that defines how images are configured and tested.</td></tr>
<tr><td><CopyableCode code="distribution_configuration_arn" /></td><td><code>string</code></td><td>The Amazon Resource Name (ARN) of the distribution configuration associated with this image pipeline.</td></tr>
<tr><td><CopyableCode code="infrastructure_configuration_arn" /></td><td><code>string</code></td><td>The Amazon Resource Name (ARN) of the infrastructure configuration associated with this image pipeline.</td></tr>
<tr><td><CopyableCode code="workflows" /></td><td><code>array</code></td><td>Workflows to define the image build process</td></tr>
<tr><td><CopyableCode code="enhanced_image_metadata_enabled" /></td><td><code>boolean</code></td><td>Collects additional information about the image being created, including the operating system (OS) version and package list.</td></tr>
<tr><td><CopyableCode code="image_scanning_configuration" /></td><td><code>object</code></td><td>Contains settings for vulnerability scans.</td></tr>
<tr><td><CopyableCode code="execution_role" /></td><td><code>string</code></td><td>The execution role name&#x2F;ARN for the image build, if provided</td></tr>
<tr><td><CopyableCode code="tags" /></td><td><code>object</code></td><td>The tags of this image pipeline.</td></tr>
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
    <td><CopyableCode code="update_resource" /></td>
    <td><code>UPDATE</code></td>
    <td><CopyableCode code="data__Identifier, data__PatchDocument, region" /></td>
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

