---
title: state_machines
hide_title: false
hide_table_of_contents: false
keywords:
  - state_machines
  - stepfunctions
  - aws
  - stackql
  - infrastructure-as-code
  - configuration-as-data
  - cloud inventory
description: Query, deploy and manage AWS resources using SQL
custom_edit_url: null
image: /img/providers/aws/stackql-aws-provider-featured-image.png
---
Retrieves a list of <code>state_machines</code> in a region

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>state_machines</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
null
<tr><td><b>Id</b></td><td><code>aws.stepfunctions.state_machines</code></td></tr>
</tbody></table>

## Fields
<table><tbody>
<tr><th>Name</th><th>Datatype</th><th>Description</th></tr>
<tr><td><code>Arn</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>Name</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>DefinitionString</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>RoleArn</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>StateMachineName</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>StateMachineType</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>LoggingConfiguration</code></td><td><code>undefined</code></td><td></td></tr>
<tr><td><code>TracingConfiguration</code></td><td><code>undefined</code></td><td></td></tr>
<tr><td><code>DefinitionS3Location</code></td><td><code>undefined</code></td><td></td></tr>
<tr><td><code>DefinitionSubstitutions</code></td><td><code>undefined</code></td><td></td></tr>
<tr><td><code>Definition</code></td><td><code>undefined</code></td><td></td></tr>
<tr><td><code>Tags</code></td><td><code>array</code></td><td></td></tr>

</tbody></table>

## Methods
Currently only <code>SELECT</code> is supported for this resource resource.

## Example
<pre>
SELECT * 
FROM aws.stepfunctions.state_machines
WHERE region = 'us-east-1'
</pre>
