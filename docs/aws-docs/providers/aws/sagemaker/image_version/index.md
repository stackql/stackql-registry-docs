---
title: image_version
hide_title: false
hide_table_of_contents: false
keywords:
  - image_version
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
Gets an individual <code>image_version</code> resource

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>image_version</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>image_version</td></tr>
<tr><td><b>Id</b></td><td><code>aws.sagemaker.image_version</code></td></tr>
</tbody></table>

## Fields
<table><tbody>
<tr><th>Name</th><th>Datatype</th><th>Description</th></tr>
<tr><td><code>image_name</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>image_arn</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>image_version_arn</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>base_image</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>container_image</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>version</code></td><td><code>integer</code></td><td></td></tr>
<tr><td><code>region</code></td><td><code>string</code></td><td>AWS region.</td></tr>

</tbody></table>

## Methods
Currently only <code>SELECT</code> is supported for this resource resource.

## Example
```sql
SELECT
region,
image_name,
image_arn,
image_version_arn,
base_image,
container_image,
version
FROM aws.sagemaker.image_version
WHERE region = 'us-east-1'
AND data__Identifier = '&lt;ImageVersionArn&gt;'
```
