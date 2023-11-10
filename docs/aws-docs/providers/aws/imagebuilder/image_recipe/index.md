---
title: image_recipe
hide_title: false
hide_table_of_contents: false
keywords:
  - image_recipe
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
Gets an individual <code>image_recipe</code> resource

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>image_recipe</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>image_recipe</td></tr>
<tr><td><b>Id</b></td><td><code>aws.imagebuilder.image_recipe</code></td></tr>
</tbody></table>

## Fields
<table><tbody>
<tr><th>Name</th><th>Datatype</th><th>Description</th></tr>
<tr><td><code>arn</code></td><td><code>string</code></td><td>The Amazon Resource Name (ARN) of the image recipe.</td></tr>
<tr><td><code>name</code></td><td><code>string</code></td><td>The name of the image recipe.</td></tr>
<tr><td><code>description</code></td><td><code>string</code></td><td>The description of the image recipe.</td></tr>
<tr><td><code>version</code></td><td><code>string</code></td><td>The version of the image recipe.</td></tr>
<tr><td><code>components</code></td><td><code>array</code></td><td>The components of the image recipe.</td></tr>
<tr><td><code>block_device_mappings</code></td><td><code>array</code></td><td>The block device mappings to apply when creating images from this recipe.</td></tr>
<tr><td><code>parent_image</code></td><td><code>string</code></td><td>The parent image of the image recipe.</td></tr>
<tr><td><code>working_directory</code></td><td><code>string</code></td><td>The working directory to be used during build and test workflows.</td></tr>
<tr><td><code>additional_instance_configuration</code></td><td><code>object</code></td><td>Specify additional settings and launch scripts for your build instances.</td></tr>
<tr><td><code>tags</code></td><td><code>object</code></td><td>The tags of the image recipe.</td></tr>
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
block_device_mappings,
parent_image,
working_directory,
additional_instance_configuration,
tags
FROM aws.imagebuilder.image_recipe
WHERE region = 'us-east-1'
AND data__Identifier = '<Arn>'
```
