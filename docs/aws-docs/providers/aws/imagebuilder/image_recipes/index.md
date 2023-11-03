---
title: image_recipes
hide_title: false
hide_table_of_contents: false
keywords:
  - image_recipes
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
Retrieves a list of <code>image_recipes</code> in a region

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>image_recipes</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>aws.imagebuilder.image_recipes</code></td></tr>
</tbody></table>

## Fields
<table><tbody>
<tr><th>Name</th><th>Datatype</th><th>Description</th></tr>
<tr><td><code>Arn</code></td><td><code>string</code></td><td>The Amazon Resource Name (ARN) of the image recipe.</td></tr><tr><td><code>Name</code></td><td><code>string</code></td><td>The name of the image recipe.</td></tr><tr><td><code>Description</code></td><td><code>string</code></td><td>The description of the image recipe.</td></tr><tr><td><code>Version</code></td><td><code>string</code></td><td>The version of the image recipe.</td></tr><tr><td><code>Components</code></td><td><code>array</code></td><td>The components of the image recipe.</td></tr><tr><td><code>BlockDeviceMappings</code></td><td><code>array</code></td><td>The block device mappings to apply when creating images from this recipe.</td></tr><tr><td><code>ParentImage</code></td><td><code>string</code></td><td>The parent image of the image recipe.</td></tr><tr><td><code>WorkingDirectory</code></td><td><code>string</code></td><td>The working directory to be used during build and test workflows.</td></tr><tr><td><code>AdditionalInstanceConfiguration</code></td><td><code>undefined</code></td><td>Specify additional settings and launch scripts for your build instances.</td></tr><tr><td><code>Tags</code></td><td><code>object</code></td><td>The tags of the image recipe.</td></tr>
</tbody></table>

## Methods
Currently only <code>SELECT</code> is supported for this resource resource.

## Example
<pre>
SELECT * 
FROM aws.imagebuilder.image_recipes
WHERE region = 'us-east-1'
</pre>
