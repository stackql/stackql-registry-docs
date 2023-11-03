---
title: dimension
hide_title: false
hide_table_of_contents: false
keywords:
  - dimension
  - iot
  - aws
  - stackql
  - infrastructure-as-code
  - configuration-as-data
  - cloud inventory
description: Query, deploy and manage AWS resources using SQL
custom_edit_url: null
image: /img/providers/aws/stackql-aws-provider-featured-image.png
---
Gets an individual <code>dimension</code> resource

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>dimension</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
null
<tr><td><b>Id</b></td><td><code>aws.iot.dimension</code></td></tr>
</tbody></table>

## Fields
<table><tbody>
<tr><th>Name</th><th>Datatype</th><th>Description</th></tr>
<tr><td><code>Name</code></td><td><code>string</code></td><td>A unique identifier for the dimension.</td></tr><tr><td><code>Type</code></td><td><code>string</code></td><td>Specifies the type of the dimension.</td></tr><tr><td><code>StringValues</code></td><td><code>array</code></td><td>Specifies the value or list of values for the dimension.</td></tr><tr><td><code>Tags</code></td><td><code>array</code></td><td>Metadata that can be used to manage the dimension.</td></tr><tr><td><code>Arn</code></td><td><code>string</code></td><td>The ARN (Amazon resource name) of the created dimension.</td></tr>
</tbody></table>

## Methods
Currently only <code>SELECT</code> is supported for this resource resource.

## Example
<pre>
SELECT * 
FROM aws.iot.dimension
WHERE region = 'us-east-1' AND data__Identifier = '<Name>'
</pre>
