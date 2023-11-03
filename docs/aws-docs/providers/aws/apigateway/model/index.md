---
title: model
hide_title: false
hide_table_of_contents: false
keywords:
  - model
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
Gets an individual <code>model</code> resource

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>model</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
null
<tr><td><b>Id</b></td><td><code>aws.apigateway.model</code></td></tr>
</tbody></table>

## Fields
<table><tbody>
<tr><th>Name</th><th>Datatype</th><th>Description</th></tr>
<tr><td><code>ContentType</code></td><td><code>string</code></td><td>The content type for the model.</td></tr><tr><td><code>Description</code></td><td><code>string</code></td><td>A description that identifies this model.</td></tr><tr><td><code>Name</code></td><td><code>string</code></td><td>A name for the model. If you don't specify a name, AWS CloudFormation generates a unique physical ID and uses that ID for the model name.</td></tr><tr><td><code>RestApiId</code></td><td><code>string</code></td><td>The ID of a REST API with which to associate this model.</td></tr><tr><td><code>Schema</code></td><td><code>string</code></td><td></td></tr>
</tbody></table>

## Methods
Currently only <code>SELECT</code> is supported for this resource resource.

## Example
<pre>
SELECT * 
FROM aws.apigateway.model
WHERE region = 'us-east-1' AND data__Identifier = '<RestApiId>' AND data__Identifier = '<Name>'
</pre>
