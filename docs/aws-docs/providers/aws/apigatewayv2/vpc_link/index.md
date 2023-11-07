---
title: vpc_link
hide_title: false
hide_table_of_contents: false
keywords:
  - vpc_link
  - apigatewayv2
  - aws
  - stackql
  - infrastructure-as-code
  - configuration-as-data
  - cloud inventory
description: Query, deploy and manage AWS resources using SQL
custom_edit_url: null
image: /img/providers/aws/stackql-aws-provider-featured-image.png
---
Gets an individual <code>vpc_link</code> resource

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>vpc_link</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
null
<tr><td><b>Id</b></td><td><code>aws.apigatewayv2.vpc_link</code></td></tr>
</tbody></table>

## Fields
<table><tbody>
<tr><th>Name</th><th>Datatype</th><th>Description</th></tr>
<tr><td><code>VpcLinkId</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>SubnetIds</code></td><td><code>array</code></td><td></td></tr>
<tr><td><code>SecurityGroupIds</code></td><td><code>array</code></td><td></td></tr>
<tr><td><code>Tags</code></td><td><code>object</code></td><td>This resource type use map for Tags, suggest to use List of Tag</td></tr>
<tr><td><code>Name</code></td><td><code>string</code></td><td></td></tr>

</tbody></table>

## Methods
Currently only <code>SELECT</code> is supported for this resource resource.

## Example
<pre>
SELECT * 
FROM aws.apigatewayv2.vpc_link
WHERE region = 'us-east-1' AND data__Identifier = '&lt;VpcLinkId&gt;'
</pre>
