---
title: faqs
hide_title: false
hide_table_of_contents: false
keywords:
  - faqs
  - kendra
  - aws
  - stackql
  - infrastructure-as-code
  - configuration-as-data
  - cloud inventory
description: Query, deploy and manage AWS resources using SQL
custom_edit_url: null
image: /img/providers/aws/stackql-aws-provider-featured-image.png
---
Retrieves a list of <code>faqs</code> in a region

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>faqs</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>aws.kendra.faqs</code></td></tr>
</tbody></table>

## Fields
<table><tbody>
<tr><th>Name</th><th>Datatype</th><th>Description</th></tr>
<tr><td><code>Id</code></td><td><code>undefined</code></td><td></td></tr><tr><td><code>IndexId</code></td><td><code>undefined</code></td><td>Index ID</td></tr><tr><td><code>Name</code></td><td><code>undefined</code></td><td>FAQ name</td></tr><tr><td><code>Description</code></td><td><code>undefined</code></td><td>FAQ description</td></tr><tr><td><code>FileFormat</code></td><td><code>undefined</code></td><td>FAQ file format</td></tr><tr><td><code>S3Path</code></td><td><code>undefined</code></td><td>FAQ S3 path</td></tr><tr><td><code>RoleArn</code></td><td><code>undefined</code></td><td>FAQ role ARN</td></tr><tr><td><code>Tags</code></td><td><code>undefined</code></td><td>Tags for labeling the FAQ</td></tr><tr><td><code>Arn</code></td><td><code>string</code></td><td></td></tr>
</tbody></table>

## Methods
Currently only <code>SELECT</code> is supported for this resource resource.

## Example
<pre>
SELECT * 
FROM aws.kendra.faqs
WHERE region = 'us-east-1'
</pre>
