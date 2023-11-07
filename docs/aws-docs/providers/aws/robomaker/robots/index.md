---
title: robots
hide_title: false
hide_table_of_contents: false
keywords:
  - robots
  - robomaker
  - aws
  - stackql
  - infrastructure-as-code
  - configuration-as-data
  - cloud inventory
description: Query, deploy and manage AWS resources using SQL
custom_edit_url: null
image: /img/providers/aws/stackql-aws-provider-featured-image.png
---
Retrieves a list of <code>robots</code> in a region

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>robots</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
null
<tr><td><b>Id</b></td><td><code>aws.robomaker.robots</code></td></tr>
</tbody></table>

## Fields
<table><tbody>
<tr><th>Name</th><th>Datatype</th><th>Description</th></tr>
<tr><td><code>Arn</code></td><td><code>undefined</code></td><td></td></tr>
<tr><td><code>Fleet</code></td><td><code>string</code></td><td>The Amazon Resource Name (ARN) of the fleet.</td></tr>
<tr><td><code>Architecture</code></td><td><code>string</code></td><td>The target architecture of the robot.</td></tr>
<tr><td><code>GreengrassGroupId</code></td><td><code>string</code></td><td>The Greengrass group id.</td></tr>
<tr><td><code>Tags</code></td><td><code>undefined</code></td><td></td></tr>
<tr><td><code>Name</code></td><td><code>string</code></td><td>The name for the robot.</td></tr>

</tbody></table>

## Methods
Currently only <code>SELECT</code> is supported for this resource resource.

## Example
<pre>
SELECT * 
FROM aws.robomaker.robots
WHERE region = 'us-east-1'
</pre>
