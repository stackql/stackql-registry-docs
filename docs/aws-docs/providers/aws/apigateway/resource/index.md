---
title: resource
hide_title: false
hide_table_of_contents: false
keywords:
  - resource
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
Gets an individual <code>resource</code> resource

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>resource</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>resource</td></tr>
<tr><td><b>Id</b></td><td><code>aws.apigateway.resource</code></td></tr>
</tbody></table>

## Fields
<table><tbody>
<tr><th>Name</th><th>Datatype</th><th>Description</th></tr>
<tr><td><code>ResourceId</code></td><td><code>string</code></td><td>A unique primary identifier for a Resource</td></tr>
<tr><td><code>RestApiId</code></td><td><code>string</code></td><td>The ID of the RestApi resource in which you want to create this resource..</td></tr>
<tr><td><code>ParentId</code></td><td><code>string</code></td><td>The parent resource's identifier.</td></tr>
<tr><td><code>PathPart</code></td><td><code>string</code></td><td>The last path segment for this resource.</td></tr>

</tbody></table>

## Methods
Currently only <code>SELECT</code> is supported for this resource resource.

## Example
<pre>
SELECT *<br/>FROM aws.apigateway.resource<br/>WHERE region = 'us-east-1'<br/>AND data__Identifier = '&lt;RestApiId&gt;'<br/>AND data__Identifier = '&lt;ResourceId&gt;'
</pre>
