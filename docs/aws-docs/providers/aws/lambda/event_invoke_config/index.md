---
title: event_invoke_config
hide_title: false
hide_table_of_contents: false
keywords:
  - event_invoke_config
  - lambda
  - aws
  - stackql
  - infrastructure-as-code
  - configuration-as-data
  - cloud inventory
description: Query, deploy and manage AWS resources using SQL
custom_edit_url: null
image: /img/providers/aws/stackql-aws-provider-featured-image.png
---
Gets an individual <code>event_invoke_config</code> resource

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>event_invoke_config</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
null
<tr><td><b>Id</b></td><td><code>aws.lambda.event_invoke_config</code></td></tr>
</tbody></table>

## Fields
<table><tbody>
<tr><th>Name</th><th>Datatype</th><th>Description</th></tr>
<tr><td><code>FunctionName</code></td><td><code>string</code></td><td></td></tr><tr><td><code>MaximumRetryAttempts</code></td><td><code>integer</code></td><td></td></tr><tr><td><code>Qualifier</code></td><td><code>string</code></td><td></td></tr><tr><td><code>DestinationConfig</code></td><td><code>undefined</code></td><td></td></tr><tr><td><code>Id</code></td><td><code>string</code></td><td></td></tr><tr><td><code>MaximumEventAgeInSeconds</code></td><td><code>integer</code></td><td></td></tr>
</tbody></table>

## Methods
Currently only <code>SELECT</code> is supported for this resource resource.

## Example
<pre>
SELECT * 
FROM aws.lambda.event_invoke_config
WHERE region = 'us-east-1' AND data__Identifier = '<Id>'
</pre>
