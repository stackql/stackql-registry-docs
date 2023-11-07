---
title: suite_definition
hide_title: false
hide_table_of_contents: false
keywords:
  - suite_definition
  - iotcoredeviceadvisor
  - aws
  - stackql
  - infrastructure-as-code
  - configuration-as-data
  - cloud inventory
description: Query, deploy and manage AWS resources using SQL
custom_edit_url: null
image: /img/providers/aws/stackql-aws-provider-featured-image.png
---
Gets an individual <code>suite_definition</code> resource

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>suite_definition</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
null
<tr><td><b>Id</b></td><td><code>aws.iotcoredeviceadvisor.suite_definition</code></td></tr>
</tbody></table>

## Fields
<table><tbody>
<tr><th>Name</th><th>Datatype</th><th>Description</th></tr>
<tr><td><code>SuiteDefinitionConfiguration</code></td><td><code>object</code></td><td></td></tr>
<tr><td><code>SuiteDefinitionId</code></td><td><code>string</code></td><td>The unique identifier for the suite definition.</td></tr>
<tr><td><code>SuiteDefinitionArn</code></td><td><code>string</code></td><td>The Amazon Resource name for the suite definition.</td></tr>
<tr><td><code>SuiteDefinitionVersion</code></td><td><code>string</code></td><td>The suite definition version of a test suite.</td></tr>
<tr><td><code>Tags</code></td><td><code>array</code></td><td>An array of key-value pairs to apply to this resource.</td></tr>

</tbody></table>

## Methods
Currently only <code>SELECT</code> is supported for this resource resource.

## Example
<pre>
SELECT * 
FROM aws.iotcoredeviceadvisor.suite_definition
WHERE region = 'us-east-1' AND data__Identifier = '&lt;SuiteDefinitionId&gt;'
</pre>
