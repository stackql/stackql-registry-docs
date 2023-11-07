---
title: logging_configuration
hide_title: false
hide_table_of_contents: false
keywords:
  - logging_configuration
  - ivschat
  - aws
  - stackql
  - infrastructure-as-code
  - configuration-as-data
  - cloud inventory
description: Query, deploy and manage AWS resources using SQL
custom_edit_url: null
image: /img/providers/aws/stackql-aws-provider-featured-image.png
---
Gets an individual <code>logging_configuration</code> resource

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>logging_configuration</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>logging_configuration</td></tr>
<tr><td><b>Id</b></td><td><code>aws.ivschat.logging_configuration</code></td></tr>
</tbody></table>

## Fields
<table><tbody>
<tr><th>Name</th><th>Datatype</th><th>Description</th></tr>
<tr><td><code>Arn</code></td><td><code>string</code></td><td>LoggingConfiguration ARN is automatically generated on creation and assigned as the unique identifier.</td></tr>
<tr><td><code>Id</code></td><td><code>string</code></td><td>The system-generated ID of the logging configuration.</td></tr>
<tr><td><code>DestinationConfiguration</code></td><td><code>undefined</code></td><td></td></tr>
<tr><td><code>Name</code></td><td><code>string</code></td><td>The name of the logging configuration. The value does not need to be unique.</td></tr>
<tr><td><code>State</code></td><td><code>string</code></td><td>The state of the logging configuration. When the state is ACTIVE, the configuration is ready to log chat content.</td></tr>
<tr><td><code>Tags</code></td><td><code>array</code></td><td>An array of key-value pairs to apply to this resource.</td></tr>

</tbody></table>

## Methods
Currently only <code>SELECT</code> is supported for this resource resource.

## Example
<pre>
SELECT *<br/>FROM aws.ivschat.logging_configuration<br/>WHERE region = 'us-east-1'<br/>AND data__Identifier = '&lt;Arn&gt;'
</pre>
