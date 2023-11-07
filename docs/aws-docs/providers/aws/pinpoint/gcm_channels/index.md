---
title: gcm_channels
hide_title: false
hide_table_of_contents: false
keywords:
  - gcm_channels
  - pinpoint
  - aws
  - stackql
  - infrastructure-as-code
  - configuration-as-data
  - cloud inventory
description: Query, deploy and manage AWS resources using SQL
custom_edit_url: null
image: /img/providers/aws/stackql-aws-provider-featured-image.png
---
Retrieves a list of <code>gcm_channels</code> in a region

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>gcm_channels</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>gcm_channels</td></tr>
<tr><td><b>Id</b></td><td><code>aws.pinpoint.gcm_channels</code></td></tr>
</tbody></table>

## Fields
<table><tbody>
<tr><th>Name</th><th>Datatype</th><th>Description</th></tr>
<tr><td><code>Id</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>ApiKey</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>Enabled</code></td><td><code>boolean</code></td><td></td></tr>
<tr><td><code>ApplicationId</code></td><td><code>string</code></td><td></td></tr>

</tbody></table>

## Methods
Currently only <code>SELECT</code> is supported for this resource resource.

## Example
<pre>
SELECT *<br/>FROM aws.pinpoint.gcm_channels<br/>WHERE region = 'us-east-1'
</pre>
