---
title: enabled_control
hide_title: false
hide_table_of_contents: false
keywords:
  - enabled_control
  - controltower
  - aws
  - stackql
  - infrastructure-as-code
  - configuration-as-data
  - cloud inventory
description: Query, deploy and manage AWS resources using SQL
custom_edit_url: null
image: /img/providers/aws/stackql-aws-provider-featured-image.png
---
Gets an individual <code>enabled_control</code> resource

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>enabled_control</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
null
<tr><td><b>Id</b></td><td><code>aws.controltower.enabled_control</code></td></tr>
</tbody></table>

## Fields
<table><tbody>
<tr><th>Name</th><th>Datatype</th><th>Description</th></tr>
<tr><td><code>ControlIdentifier</code></td><td><code>string</code></td><td>Arn of the control.</td></tr>
<tr><td><code>TargetIdentifier</code></td><td><code>string</code></td><td>Arn for Organizational unit to which the control needs to be applied</td></tr>

</tbody></table>

## Methods
Currently only <code>SELECT</code> is supported for this resource resource.

## Example
<pre>
SELECT * 
FROM aws.controltower.enabled_control
WHERE region = 'us-east-1' AND data__Identifier = '&lt;TargetIdentifier&gt;' AND data__Identifier = '&lt;ControlIdentifier&gt;'
</pre>
