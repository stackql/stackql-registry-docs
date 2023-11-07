---
title: enabled_controls
hide_title: false
hide_table_of_contents: false
keywords:
  - enabled_controls
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
Retrieves a list of <code>enabled_controls</code> in a region

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>enabled_controls</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>enabled_controls</td></tr>
<tr><td><b>Id</b></td><td><code>aws.controltower.enabled_controls</code></td></tr>
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
FROM aws.controltower.enabled_controls
WHERE region = 'us-east-1'
</pre>
