---
title: logging_configuration
hide_title: false
hide_table_of_contents: false
keywords:
  - logging_configuration
  - wafv2
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
<tr><td><b>Id</b></td><td><code>aws.wafv2.logging_configuration</code></td></tr>
</tbody></table>

## Fields
<table><tbody>
<tr><th>Name</th><th>Datatype</th><th>Description</th></tr>
<tr><td><code>ResourceArn</code></td><td><code>string</code></td><td>The Amazon Resource Name (ARN) of the web ACL that you want to associate with LogDestinationConfigs.</td></tr>
<tr><td><code>LogDestinationConfigs</code></td><td><code>array</code></td><td>The Amazon Resource Names (ARNs) of the logging destinations that you want to associate with the web ACL.</td></tr>
<tr><td><code>RedactedFields</code></td><td><code>array</code></td><td>The parts of the request that you want to keep out of the logs. For example, if you redact the HEADER field, the HEADER field in the firehose will be xxx.</td></tr>
<tr><td><code>ManagedByFirewallManager</code></td><td><code>boolean</code></td><td>Indicates whether the logging configuration was created by AWS Firewall Manager, as part of an AWS WAF policy configuration. If true, only Firewall Manager can modify or delete the configuration.</td></tr>
<tr><td><code>LoggingFilter</code></td><td><code>object</code></td><td>Filtering that specifies which web requests are kept in the logs and which are dropped. You can filter on the rule action and on the web request labels that were applied by matching rules during web ACL evaluation.</td></tr>

</tbody></table>

## Methods
Currently only <code>SELECT</code> is supported for this resource resource.

## Example
<pre>
SELECT * 
FROM aws.wafv2.logging_configuration
WHERE region = 'us-east-1' AND data__Identifier = '&lt;ResourceArn&gt;'
</pre>
