---
title: routing_control
hide_title: false
hide_table_of_contents: false
keywords:
  - routing_control
  - route53recoverycontrol
  - aws
  - stackql
  - infrastructure-as-code
  - configuration-as-data
  - cloud inventory
description: Query, deploy and manage AWS resources using SQL
custom_edit_url: null
image: /img/providers/aws/stackql-aws-provider-featured-image.png
---
Gets an individual <code>routing_control</code> resource

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>routing_control</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>aws.route53recoverycontrol.routing_control</code></td></tr>
</tbody></table>

## Fields
<table><tbody>
<tr><th>Name</th><th>Datatype</th><th>Description</th></tr>
<tr><td><code>RoutingControlArn</code></td><td><code>string</code></td><td>The Amazon Resource Name (ARN) of the routing control.</td></tr><tr><td><code>ControlPanelArn</code></td><td><code>string</code></td><td>The Amazon Resource Name (ARN) of the control panel.</td></tr><tr><td><code>Name</code></td><td><code>string</code></td><td>The name of the routing control. You can use any non-white space character in the name.</td></tr><tr><td><code>Status</code></td><td><code>string</code></td><td>The deployment status of the routing control. Status can be one of the following: PENDING, DEPLOYED, PENDING_DELETION.</td></tr><tr><td><code>ClusterArn</code></td><td><code>string</code></td><td>Arn associated with Control Panel</td></tr>
</tbody></table>

## Methods
Currently only <code>SELECT</code> is supported for this resource resource.

## Example
<pre>
SELECT * 
FROM aws.route53recoverycontrol.routing_control
WHERE region = 'us-east-1' AND data__Identifier = '{RoutingControlArn}'
</pre>
