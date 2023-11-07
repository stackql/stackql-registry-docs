---
title: dedicated_ip_pool
hide_title: false
hide_table_of_contents: false
keywords:
  - dedicated_ip_pool
  - ses
  - aws
  - stackql
  - infrastructure-as-code
  - configuration-as-data
  - cloud inventory
description: Query, deploy and manage AWS resources using SQL
custom_edit_url: null
image: /img/providers/aws/stackql-aws-provider-featured-image.png
---
Gets an individual <code>dedicated_ip_pool</code> resource

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>dedicated_ip_pool</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>dedicated_ip_pool</td></tr>
<tr><td><b>Id</b></td><td><code>aws.ses.dedicated_ip_pool</code></td></tr>
</tbody></table>

## Fields
<table><tbody>
<tr><th>Name</th><th>Datatype</th><th>Description</th></tr>
<tr><td><code>PoolName</code></td><td><code>string</code></td><td>The name of the dedicated IP pool.</td></tr>
<tr><td><code>ScalingMode</code></td><td><code>string</code></td><td>Specifies whether the dedicated IP pool is managed or not. The default value is STANDARD.</td></tr>

</tbody></table>

## Methods
Currently only <code>SELECT</code> is supported for this resource resource.

## Example
<pre>
SELECT *<br/>FROM aws.ses.dedicated_ip_pool<br/>WHERE region = 'us-east-1'<br/>AND data__Identifier = '&lt;PoolName&gt;'
</pre>
