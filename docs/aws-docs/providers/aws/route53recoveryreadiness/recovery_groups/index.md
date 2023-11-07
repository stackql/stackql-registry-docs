---
title: recovery_groups
hide_title: false
hide_table_of_contents: false
keywords:
  - recovery_groups
  - route53recoveryreadiness
  - aws
  - stackql
  - infrastructure-as-code
  - configuration-as-data
  - cloud inventory
description: Query, deploy and manage AWS resources using SQL
custom_edit_url: null
image: /img/providers/aws/stackql-aws-provider-featured-image.png
---
Retrieves a list of <code>recovery_groups</code> in a region

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>recovery_groups</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
null
<tr><td><b>Id</b></td><td><code>aws.route53recoveryreadiness.recovery_groups</code></td></tr>
</tbody></table>

## Fields
<table><tbody>
<tr><th>Name</th><th>Datatype</th><th>Description</th></tr>
<tr><td><code>RecoveryGroupName</code></td><td><code>string</code></td><td>The name of the recovery group to create.</td></tr>
<tr><td><code>Cells</code></td><td><code>array</code></td><td>A list of the cell Amazon Resource Names (ARNs) in the recovery group.</td></tr>
<tr><td><code>RecoveryGroupArn</code></td><td><code>string</code></td><td>A collection of tags associated with a resource.</td></tr>
<tr><td><code>Tags</code></td><td><code>array</code></td><td>A collection of tags associated with a resource.</td></tr>

</tbody></table>

## Methods
Currently only <code>SELECT</code> is supported for this resource resource.

## Example
<pre>
SELECT * 
FROM aws.route53recoveryreadiness.recovery_groups
WHERE region = 'us-east-1'
</pre>
