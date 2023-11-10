---
title: control_panel
hide_title: false
hide_table_of_contents: false
keywords:
  - control_panel
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
Gets an individual <code>control_panel</code> resource

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>control_panel</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>control_panel</td></tr>
<tr><td><b>Id</b></td><td><code>aws.route53recoverycontrol.control_panel</code></td></tr>
</tbody></table>

## Fields
<table><tbody>
<tr><th>Name</th><th>Datatype</th><th>Description</th></tr>
<tr><td><code>cluster_arn</code></td><td><code>string</code></td><td>Cluster to associate with the Control Panel</td></tr>
<tr><td><code>control_panel_arn</code></td><td><code>string</code></td><td>The Amazon Resource Name (ARN) of the cluster.</td></tr>
<tr><td><code>name</code></td><td><code>string</code></td><td>The name of the control panel. You can use any non-white space character in the name.</td></tr>
<tr><td><code>status</code></td><td><code>string</code></td><td>The deployment status of control panel. Status can be one of the following: PENDING, DEPLOYED, PENDING_DELETION.</td></tr>
<tr><td><code>default_control_panel</code></td><td><code>boolean</code></td><td>A flag that Amazon Route 53 Application Recovery Controller sets to true to designate the default control panel for a cluster. When you create a cluster, Amazon Route 53 Application Recovery Controller creates a control panel, and sets this flag for that control panel. If you create a control panel yourself, this flag is set to false.</td></tr>
<tr><td><code>routing_control_count</code></td><td><code>integer</code></td><td>Count of associated routing controls</td></tr>
<tr><td><code>tags</code></td><td><code>array</code></td><td>A collection of tags associated with a resource</td></tr>
<tr><td><code>region</code></td><td><code>string</code></td><td>AWS region.</td></tr>

</tbody></table>

## Methods
Currently only <code>SELECT</code> is supported for this resource resource.

## Example
```sql
SELECT
region,
cluster_arn,
control_panel_arn,
name,
status,
default_control_panel,
routing_control_count,
tags
FROM aws.route53recoverycontrol.control_panel
WHERE region = 'us-east-1'
AND data__Identifier = '&lt;ControlPanelArn&gt;'
```
