---
title: event_invoke_configs
hide_title: false
hide_table_of_contents: false
keywords:
  - event_invoke_configs
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
Retrieves a list of <code>event_invoke_configs</code> in a region

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>event_invoke_configs</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>event_invoke_configs</td></tr>
<tr><td><b>Id</b></td><td><code>aws.lambda.event_invoke_configs</code></td></tr>
</tbody></table>

## Fields
<table><tbody>
<tr><th>Name</th><th>Datatype</th><th>Description</th></tr>
<tr><td><code>FunctionName</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>MaximumRetryAttempts</code></td><td><code>integer</code></td><td></td></tr>
<tr><td><code>Qualifier</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>DestinationConfig</code></td><td><code>object</code></td><td></td></tr>
<tr><td><code>Id</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>MaximumEventAgeInSeconds</code></td><td><code>integer</code></td><td></td></tr>

</tbody></table>

## Methods
Currently only <code>SELECT</code> is supported for this resource resource.

## Example
<pre>
SELECT *<br/>FROM aws.lambda.event_invoke_configs<br/>WHERE region = 'us-east-1'
</pre>
