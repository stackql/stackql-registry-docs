---
title: image_recipe_tags
hide_title: false
hide_table_of_contents: false
keywords:
  - image_recipe_tags
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

Expands all tag keys and values for <code>image_recipes</code> in a region

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>image_recipe_tags</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>Resource schema for AWS::ImageBuilder::ImageRecipe</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="aws.imagebuilder.image_recipe_tags" /></td></tr>
</tbody></table>

## Fields
<table><tbody><tr><th>Name</th><th>Datatype</th><th>Description</th></tr><tr><td><CopyableCode code="arn" /></td><td><code>string</code></td><td>The Amazon Resource Name (ARN) of the image recipe.</td></tr>
<tr><td><CopyableCode code="name" /></td><td><code>string</code></td><td>The name of the image recipe.</td></tr>
<tr><td><CopyableCode code="description" /></td><td><code>string</code></td><td>The description of the image recipe.</td></tr>
<tr><td><CopyableCode code="version" /></td><td><code>string</code></td><td>The version of the image recipe.</td></tr>
<tr><td><CopyableCode code="components" /></td><td><code>array</code></td><td>The components of the image recipe.</td></tr>
<tr><td><CopyableCode code="block_device_mappings" /></td><td><code>array</code></td><td>The block device mappings to apply when creating images from this recipe.</td></tr>
<tr><td><CopyableCode code="parent_image" /></td><td><code>string</code></td><td>The parent image of the image recipe.</td></tr>
<tr><td><CopyableCode code="working_directory" /></td><td><code>string</code></td><td>The working directory to be used during build and test workflows.</td></tr>
<tr><td><CopyableCode code="additional_instance_configuration" /></td><td><code>object</code></td><td>Specify additional settings and launch scripts for your build instances.</td></tr>
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
Expands tags for all <code>image_recipes</code> in a region.
```sql
SELECT
region,
arn,
name,
description,
version,
components,
block_device_mappings,
parent_image,
working_directory,
additional_instance_configuration,
tag_key,
tag_value
FROM aws.imagebuilder.image_recipe_tags
WHERE region = 'us-east-1';
```


## Permissions

For permissions required to operate on the <code>image_recipe_tags</code> resource, see <a href="/providers/aws/imagebuilder/image_recipes/#permissions"><code>image_recipes</code></a>


