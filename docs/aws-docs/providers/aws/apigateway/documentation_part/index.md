---
title: documentation_part
hide_title: false
hide_table_of_contents: false
keywords:
  - documentation_part
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
Gets an individual <code>documentation_part</code> resource

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>documentation_part</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
null
<tr><td><b>Id</b></td><td><code>aws.apigateway.documentation_part</code></td></tr>
</tbody></table>

## Fields
<table><tbody>
<tr><th>Name</th><th>Datatype</th><th>Description</th></tr>
<tr><td><code>DocumentationPartId</code></td><td><code>string</code></td><td>The identifier of the documentation Part.</td></tr><tr><td><code>Location</code></td><td><code>undefined</code></td><td>The location of the API entity that the documentation applies to.</td></tr><tr><td><code>Properties</code></td><td><code>string</code></td><td>The documentation content map of the targeted API entity.</td></tr><tr><td><code>RestApiId</code></td><td><code>string</code></td><td>Identifier of the targeted API entity</td></tr>
</tbody></table>

## Methods
Currently only <code>SELECT</code> is supported for this resource resource.

## Example
<pre>
SELECT * 
FROM aws.apigateway.documentation_part
WHERE region = 'us-east-1' AND data__Identifier = '{DocumentationPartId}' AND data__Identifier = '{RestApiId}'
</pre>
