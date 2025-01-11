---
title: container_recipe_tags
hide_title: false
hide_table_of_contents: false
keywords:
  - container_recipe_tags
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
import Tabs from '@theme/Tabs';
import TabItem from '@theme/TabItem';

Expands all tag keys and values for <code>container_recipes</code> in a region

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>container_recipe_tags</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>Resource schema for AWS::ImageBuilder::ContainerRecipe</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="aws.imagebuilder.container_recipe_tags" /></td></tr>
</tbody></table>

## Fields
<table><tbody><tr><th>Name</th><th>Datatype</th><th>Description</th></tr><tr><td><CopyableCode code="arn" /></td><td><code>string</code></td><td>The Amazon Resource Name (ARN) of the container recipe.</td></tr>
<tr><td><CopyableCode code="name" /></td><td><code>string</code></td><td>The name of the container recipe.</td></tr>
<tr><td><CopyableCode code="description" /></td><td><code>string</code></td><td>The description of the container recipe.</td></tr>
<tr><td><CopyableCode code="version" /></td><td><code>string</code></td><td>The semantic version of the container recipe (&lt;major&gt;.&lt;minor&gt;.&lt;patch&gt;).</td></tr>
<tr><td><CopyableCode code="components" /></td><td><code>array</code></td><td>Components for build and test that are included in the container recipe.</td></tr>
<tr><td><CopyableCode code="instance_configuration" /></td><td><code>object</code></td><td>A group of options that can be used to configure an instance for building and testing container images.</td></tr>
<tr><td><CopyableCode code="dockerfile_template_data" /></td><td><code>string</code></td><td>Dockerfiles are text documents that are used to build Docker containers, and ensure that they contain all of the elements required by the application running inside. The template data consists of contextual variables where Image Builder places build information or scripts, based on your container image recipe.</td></tr>
<tr><td><CopyableCode code="dockerfile_template_uri" /></td><td><code>string</code></td><td>The S3 URI for the Dockerfile that will be used to build your container image.</td></tr>
<tr><td><CopyableCode code="platform_override" /></td><td><code>string</code></td><td>Specifies the operating system platform when you use a custom source image.</td></tr>
<tr><td><CopyableCode code="container_type" /></td><td><code>string</code></td><td>Specifies the type of container, such as Docker.</td></tr>
<tr><td><CopyableCode code="image_os_version_override" /></td><td><code>string</code></td><td>Specifies the operating system version for the source image.</td></tr>
<tr><td><CopyableCode code="target_repository" /></td><td><code>object</code></td><td>The destination repository for the container image.</td></tr>
<tr><td><CopyableCode code="kms_key_id" /></td><td><code>string</code></td><td>Identifies which KMS key is used to encrypt the container image.</td></tr>
<tr><td><CopyableCode code="parent_image" /></td><td><code>string</code></td><td>The source image for the container recipe.</td></tr>
<tr><td><CopyableCode code="working_directory" /></td><td><code>string</code></td><td>The working directory to be used during build and test workflows.</td></tr>
<tr><td><CopyableCode code="tag_key" /></td><td><code>string</code></td><td>Tag key.</td></tr>
<tr><td><CopyableCode code="tag_value" /></td><td><code>string</code></td><td>Tag value.</td></tr>
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
    <td><CopyableCode code="list_resources" /></td>
    <td><code>SELECT</code></td>
    <td><CopyableCode code="region" /></td>
  </tr>
</tbody></table>

## `SELECT` examples
Expands tags for all <code>container_recipes</code> in a region.
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
tag_key,
tag_value
FROM aws.imagebuilder.container_recipe_tags
WHERE region = 'us-east-1';
```


## Permissions

For permissions required to operate on the <code>container_recipe_tags</code> resource, see <a href="/providers/aws/imagebuilder/container_recipes/#permissions"><code>container_recipes</code></a>

