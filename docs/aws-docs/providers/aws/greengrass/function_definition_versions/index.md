---
title: function_definition_versions
hide_title: false
hide_table_of_contents: false
keywords:
  - function_definition_versions
  - greengrass
  - aws
  - stackql
  - infrastructure-as-code
  - configuration-as-data
  - cloud inventory
description: Query, deploy and manage AWS resources using SQL
custom_edit_url: null
image: /img/providers/aws/stackql-aws-provider-featured-image.png
---
Retrieves a list of <code>function_definition_versions</code> in a region

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>function_definition_versions</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>function_definition_versions</td></tr>
<tr><td><b>Id</b></td><td><code>aws.greengrass.function_definition_versions</code></td></tr>
</tbody></table>

## Fields
<table><tbody>
<tr><th>Name</th><th>Datatype</th><th>Description</th></tr>
<tr><td><code>Id</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>DefaultConfig</code></td><td><code>object</code></td><td></td></tr>
<tr><td><code>Functions</code></td><td><code>array</code></td><td></td></tr>
<tr><td><code>FunctionDefinitionId</code></td><td><code>string</code></td><td></td></tr>

</tbody></table>

## Methods
Currently only <code>SELECT</code> is supported for this resource resource.

## Example
<pre>
SELECT *<br/>FROM aws.greengrass.function_definition_versions<br/>WHERE region = 'us-east-1'
</pre>
