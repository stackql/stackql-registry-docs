---
title: response_headers_policies
hide_title: false
hide_table_of_contents: false
keywords:
  - response_headers_policies
  - cloudfront
  - aws
  - stackql
  - infrastructure-as-code
  - configuration-as-data
  - cloud inventory
description: Query, deploy and manage AWS resources using SQL
custom_edit_url: null
image: /img/providers/aws/stackql-aws-provider-featured-image.png
---
Retrieves a list of <code>response_headers_policies</code> in a region

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>response_headers_policies</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>response_headers_policies</td></tr>
<tr><td><b>Id</b></td><td><code>aws.cloudfront.response_headers_policies</code></td></tr>
</tbody></table>

## Fields
<table><tbody>
<tr><th>Name</th><th>Datatype</th><th>Description</th></tr>
<tr><td><code>Id</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>LastModifiedTime</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>ResponseHeadersPolicyConfig</code></td><td><code>undefined</code></td><td></td></tr>

</tbody></table>

## Methods
Currently only <code>SELECT</code> is supported for this resource resource.

## Example
<pre>
SELECT * 
FROM aws.cloudfront.response_headers_policies
WHERE region = 'us-east-1'
</pre>
