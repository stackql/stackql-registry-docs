---
title: db_proxy_target_group
hide_title: false
hide_table_of_contents: false
keywords:
  - db_proxy_target_group
  - rds
  - aws
  - stackql
  - infrastructure-as-code
  - configuration-as-data
  - cloud inventory
description: Query, deploy and manage AWS resources using SQL
custom_edit_url: null
image: /img/providers/aws/stackql-aws-provider-featured-image.png
---
Gets an individual <code>db_proxy_target_group</code> resource

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>db_proxy_target_group</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>db_proxy_target_group</td></tr>
<tr><td><b>Id</b></td><td><code>aws.rds.db_proxy_target_group</code></td></tr>
</tbody></table>

## Fields
<table><tbody>
<tr><th>Name</th><th>Datatype</th><th>Description</th></tr>
<tr><td><code>DBProxyName</code></td><td><code>string</code></td><td>The identifier for the proxy.</td></tr>
<tr><td><code>TargetGroupArn</code></td><td><code>string</code></td><td>The Amazon Resource Name (ARN) representing the target group.</td></tr>
<tr><td><code>TargetGroupName</code></td><td><code>string</code></td><td>The identifier for the DBProxyTargetGroup</td></tr>
<tr><td><code>ConnectionPoolConfigurationInfo</code></td><td><code>object</code></td><td></td></tr>
<tr><td><code>DBInstanceIdentifiers</code></td><td><code>array</code></td><td></td></tr>
<tr><td><code>DBClusterIdentifiers</code></td><td><code>array</code></td><td></td></tr>

</tbody></table>

## Methods
Currently only <code>SELECT</code> is supported for this resource resource.

## Example
<pre>
SELECT *<br/>FROM aws.rds.db_proxy_target_group<br/>WHERE region = 'us-east-1'<br/>AND data__Identifier = '&lt;TargetGroupArn&gt;'
</pre>
