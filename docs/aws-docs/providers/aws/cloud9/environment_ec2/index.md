---
title: environment_ec2
hide_title: false
hide_table_of_contents: false
keywords:
  - environment_ec2
  - cloud9
  - aws
  - stackql
  - infrastructure-as-code
  - configuration-as-data
  - cloud inventory
description: Query, deploy and manage AWS resources using SQL
custom_edit_url: null
image: /img/providers/aws/stackql-aws-provider-featured-image.png
---
Gets an individual <code>environment_ec2</code> resource

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>environment_ec2</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
null
<tr><td><b>Id</b></td><td><code>aws.cloud9.environment_ec2</code></td></tr>
</tbody></table>

## Fields
<table><tbody>
<tr><th>Name</th><th>Datatype</th><th>Description</th></tr>
<tr><td><code>Repositories</code></td><td><code>array</code></td><td></td></tr>
<tr><td><code>OwnerArn</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>Description</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>ConnectionType</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>AutomaticStopTimeMinutes</code></td><td><code>integer</code></td><td></td></tr>
<tr><td><code>ImageId</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>SubnetId</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>Id</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>Arn</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>InstanceType</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>Tags</code></td><td><code>array</code></td><td></td></tr>
<tr><td><code>Name</code></td><td><code>string</code></td><td></td></tr>

</tbody></table>

## Methods
Currently only <code>SELECT</code> is supported for this resource resource.

## Example
<pre>
SELECT * 
FROM aws.cloud9.environment_ec2
WHERE region = 'us-east-1' AND data__Identifier = '&lt;Id&gt;'
</pre>
