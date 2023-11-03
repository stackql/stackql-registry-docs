---
title: topic_rule_destinations
hide_title: false
hide_table_of_contents: false
keywords:
  - topic_rule_destinations
  - iot
  - aws
  - stackql
  - infrastructure-as-code
  - configuration-as-data
  - cloud inventory
description: Query, deploy and manage AWS resources using SQL
custom_edit_url: null
image: /img/providers/aws/stackql-aws-provider-featured-image.png
---
Retrieves a list of <code>topic_rule_destinations</code> in a region

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>topic_rule_destinations</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
null
<tr><td><b>Id</b></td><td><code>aws.iot.topic_rule_destinations</code></td></tr>
</tbody></table>

## Fields
<table><tbody>
<tr><th>Name</th><th>Datatype</th><th>Description</th></tr>
<tr><td><code>Arn</code></td><td><code>string</code></td><td>Amazon Resource Name (ARN).</td></tr><tr><td><code>Status</code></td><td><code>undefined</code></td><td>The status of the TopicRuleDestination.</td></tr><tr><td><code>HttpUrlProperties</code></td><td><code>undefined</code></td><td>HTTP URL destination properties.</td></tr><tr><td><code>StatusReason</code></td><td><code>string</code></td><td>The reasoning for the current status of the TopicRuleDestination.</td></tr><tr><td><code>VpcProperties</code></td><td><code>undefined</code></td><td>VPC destination properties.</td></tr>
</tbody></table>

## Methods
Currently only <code>SELECT</code> is supported for this resource resource.

## Example
<pre>
SELECT * 
FROM aws.iot.topic_rule_destinations
WHERE region = 'us-east-1'
</pre>
