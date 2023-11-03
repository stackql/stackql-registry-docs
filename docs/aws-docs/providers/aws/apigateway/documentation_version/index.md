---
title: documentation_version
hide_title: false
hide_table_of_contents: false
keywords:
  - documentation_version
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
Gets an individual <code>documentation_version</code> resource

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>documentation_version</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
null
<tr><td><b>Id</b></td><td><code>aws.apigateway.documentation_version</code></td></tr>
</tbody></table>

## Fields
<table><tbody>
<tr><th>Name</th><th>Datatype</th><th>Description</th></tr>
<tr><td><code>Description</code></td><td><code>string</code></td><td>The description of the API documentation snapshot.</td></tr><tr><td><code>DocumentationVersion</code></td><td><code>string</code></td><td>The version identifier of the API documentation snapshot.</td></tr><tr><td><code>RestApiId</code></td><td><code>string</code></td><td>The identifier of the API.</td></tr>
</tbody></table>

## Methods
Currently only <code>SELECT</code> is supported for this resource resource.

## Example
<pre>
SELECT * 
FROM aws.apigateway.documentation_version
WHERE region = 'us-east-1' AND data__Identifier = '<DocumentationVersion>' AND data__Identifier = '<RestApiId>'
</pre>
