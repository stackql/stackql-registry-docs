---
title: maintenance_window_targets
hide_title: false
hide_table_of_contents: false
keywords:
  - maintenance_window_targets
  - ssm
  - aws
  - stackql
  - infrastructure-as-code
  - configuration-as-data
  - cloud inventory
description: Query, deploy and manage AWS resources using SQL
custom_edit_url: null
image: /img/providers/aws/stackql-aws-provider-featured-image.png
---
Retrieves a list of <code>maintenance_window_targets</code> in a region

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>maintenance_window_targets</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>maintenance_window_targets</td></tr>
<tr><td><b>Id</b></td><td><code>aws.ssm.maintenance_window_targets</code></td></tr>
</tbody></table>

## Fields
<table><tbody>
<tr><th>Name</th><th>Datatype</th><th>Description</th></tr>
<tr><td><code>OwnerInformation</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>Description</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>WindowId</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>ResourceType</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>Targets</code></td><td><code>array</code></td><td></td></tr>
<tr><td><code>Id</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>Name</code></td><td><code>string</code></td><td></td></tr>

</tbody></table>

## Methods
Currently only <code>SELECT</code> is supported for this resource resource.

## Example
<pre>
SELECT *<br/>FROM aws.ssm.maintenance_window_targets<br/>WHERE region = 'us-east-1'
</pre>
