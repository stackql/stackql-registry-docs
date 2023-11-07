---
title: rotations
hide_title: false
hide_table_of_contents: false
keywords:
  - rotations
  - ssmcontacts
  - aws
  - stackql
  - infrastructure-as-code
  - configuration-as-data
  - cloud inventory
description: Query, deploy and manage AWS resources using SQL
custom_edit_url: null
image: /img/providers/aws/stackql-aws-provider-featured-image.png
---
Retrieves a list of <code>rotations</code> in a region

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>rotations</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>rotations</td></tr>
<tr><td><b>Id</b></td><td><code>aws.ssmcontacts.rotations</code></td></tr>
</tbody></table>

## Fields
<table><tbody>
<tr><th>Name</th><th>Datatype</th><th>Description</th></tr>
<tr><td><code>Name</code></td><td><code>string</code></td><td>Name of the Rotation</td></tr>
<tr><td><code>ContactIds</code></td><td><code>array</code></td><td>Members of the rotation</td></tr>
<tr><td><code>StartTime</code></td><td><code>string</code></td><td>Start time of the first shift of Oncall Schedule</td></tr>
<tr><td><code>TimeZoneId</code></td><td><code>string</code></td><td>TimeZone Identifier for the Oncall Schedule</td></tr>
<tr><td><code>Recurrence</code></td><td><code>object</code></td><td></td></tr>
<tr><td><code>Tags</code></td><td><code>array</code></td><td></td></tr>
<tr><td><code>Arn</code></td><td><code>string</code></td><td>The Amazon Resource Name (ARN) of the rotation.</td></tr>

</tbody></table>

## Methods
Currently only <code>SELECT</code> is supported for this resource resource.

## Example
<pre>
SELECT *<br/>FROM aws.ssmcontacts.rotations<br/>WHERE region = 'us-east-1'
</pre>
