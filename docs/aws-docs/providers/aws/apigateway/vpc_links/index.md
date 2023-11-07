---
title: vpc_links
hide_title: false
hide_table_of_contents: false
keywords:
  - vpc_links
  - apigateway
  - aws
  - stackql
  - infrastructure-as-code
  - configuration-as-data
  - cloud inventory
description: Query, deploy and manage AWS resources using SQL
custom_edit_url: null
image: /img/providers/aws/stackql-aws-provider-featured-image.png
---
Retrieves a list of <code>vpc_links</code> in a region

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>vpc_links</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>vpc_links</td></tr>
<tr><td><b>Id</b></td><td><code>aws.apigateway.vpc_links</code></td></tr>
</tbody></table>

## Fields
<table><tbody>
<tr><th>Name</th><th>Datatype</th><th>Description</th></tr>
<tr><td><code>Name</code></td><td><code>string</code></td><td>A name for the VPC link.</td></tr>
<tr><td><code>Description</code></td><td><code>string</code></td><td>A description of the VPC link.</td></tr>
<tr><td><code>Tags</code></td><td><code>array</code></td><td>An array of arbitrary tags (key-value pairs) to associate with the stage.</td></tr>
<tr><td><code>TargetArns</code></td><td><code>array</code></td><td>The ARN of network load balancer of the VPC targeted by the VPC link. The network load balancer must be owned by the same AWS account of the API owner.</td></tr>
<tr><td><code>VpcLinkId</code></td><td><code>string</code></td><td>The ID of the instance that backs VPC link.</td></tr>

</tbody></table>

## Methods
Currently only <code>SELECT</code> is supported for this resource resource.

## Example
<pre>
SELECT * 
FROM aws.apigateway.vpc_links
WHERE region = 'us-east-1'
</pre>
