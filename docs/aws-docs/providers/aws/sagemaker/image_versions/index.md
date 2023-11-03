---
title: image_versions
hide_title: false
hide_table_of_contents: false
keywords:
  - image_versions
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
Retrieves a list of <code>image_versions</code> in a region

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>image_versions</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
null
<tr><td><b>Id</b></td><td><code>aws.sagemaker.image_versions</code></td></tr>
</tbody></table>

## Fields
<table><tbody>
<tr><th>Name</th><th>Datatype</th><th>Description</th></tr>
<tr><td><code>ImageName</code></td><td><code>undefined</code></td><td></td></tr><tr><td><code>ImageArn</code></td><td><code>undefined</code></td><td></td></tr><tr><td><code>ImageVersionArn</code></td><td><code>undefined</code></td><td></td></tr><tr><td><code>BaseImage</code></td><td><code>undefined</code></td><td></td></tr><tr><td><code>ContainerImage</code></td><td><code>undefined</code></td><td></td></tr><tr><td><code>Version</code></td><td><code>undefined</code></td><td></td></tr>
</tbody></table>

## Methods
Currently only <code>SELECT</code> is supported for this resource resource.

## Example
<pre>
SELECT * 
FROM aws.sagemaker.image_versions
WHERE region = 'us-east-1'
</pre>
