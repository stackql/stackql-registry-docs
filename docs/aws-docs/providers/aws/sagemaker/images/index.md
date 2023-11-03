---
title: images
hide_title: false
hide_table_of_contents: false
keywords:
  - images
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
Retrieves a list of <code>images</code> in a region

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>images</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>aws.sagemaker.images</code></td></tr>
</tbody></table>

## Fields
<table><tbody>
<tr><th>Name</th><th>Datatype</th><th>Description</th></tr>
<tr><td><code>ImageName</code></td><td><code>undefined</code></td><td></td></tr><tr><td><code>ImageArn</code></td><td><code>undefined</code></td><td></td></tr><tr><td><code>ImageRoleArn</code></td><td><code>undefined</code></td><td></td></tr><tr><td><code>ImageDisplayName</code></td><td><code>undefined</code></td><td></td></tr><tr><td><code>ImageDescription</code></td><td><code>undefined</code></td><td></td></tr><tr><td><code>Tags</code></td><td><code>array</code></td><td>An array of key-value pairs to apply to this resource.</td></tr>
</tbody></table>

## Methods
Currently only <code>SELECT</code> is supported for this resource resource.

## Example
```sql
SELECT * 
FROM aws.sagemaker.images
WHERE region = 'us-east-1'
```
