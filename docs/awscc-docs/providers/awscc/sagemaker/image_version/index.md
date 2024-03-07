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
<tr><td><b>Id</b></td><td><code>awscc.sagemaker.image_version</code></td></tr>
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
<tr><td><code>alias</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>aliases</code></td><td><code>array</code></td><td></td></tr>
<tr><td><code>vendor_guidance</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>job_type</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>m_lframework</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>programming_lang</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>processor</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>horovod</code></td><td><code>boolean</code></td><td></td></tr>
<tr><td><code>release_notes</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>region</code></td><td><code>string</code></td><td>AWS region.</td></tr>

</tbody></table>

## Methods
Currently only <code>SELECT</code> is supported for this resource resource.

## Permissions

To operate on the <code>image_version</code> resource, the following permissions are required:

### Read
<pre>
sagemaker:DescribeImageVersion</pre>

### Update
<pre>
sagemaker:UpdateImageVersion,
sagemaker:DescribeImageVersion,
sagemaker:ListAliases</pre>

### Delete
<pre>
sagemaker:DeleteImageVersion,
sagemaker:DescribeImageVersion</pre>


## Example
```sql
SELECT
region,
image_name,
image_arn,
image_version_arn,
base_image,
container_image,
version,
alias,
aliases,
vendor_guidance,
job_type,
m_lframework,
programming_lang,
processor,
horovod,
release_notes
FROM awscc.sagemaker.image_version
WHERE region = 'us-east-1'
AND data__Identifier = '&lt;ImageVersionArn&gt;'
```
