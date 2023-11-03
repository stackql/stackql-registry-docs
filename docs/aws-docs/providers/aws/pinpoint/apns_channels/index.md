---
title: apns_channels
hide_title: false
hide_table_of_contents: false
keywords:
  - apns_channels
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
Retrieves a list of <code>apns_channels</code> in a region

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>apns_channels</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
null
<tr><td><b>Id</b></td><td><code>aws.pinpoint.apns_channels</code></td></tr>
</tbody></table>

## Fields
<table><tbody>
<tr><th>Name</th><th>Datatype</th><th>Description</th></tr>
<tr><td><code>Id</code></td><td><code>string</code></td><td></td></tr><tr><td><code>BundleId</code></td><td><code>string</code></td><td></td></tr><tr><td><code>PrivateKey</code></td><td><code>string</code></td><td></td></tr><tr><td><code>Enabled</code></td><td><code>boolean</code></td><td></td></tr><tr><td><code>DefaultAuthenticationMethod</code></td><td><code>string</code></td><td></td></tr><tr><td><code>TokenKey</code></td><td><code>string</code></td><td></td></tr><tr><td><code>ApplicationId</code></td><td><code>string</code></td><td></td></tr><tr><td><code>TeamId</code></td><td><code>string</code></td><td></td></tr><tr><td><code>Certificate</code></td><td><code>string</code></td><td></td></tr><tr><td><code>TokenKeyId</code></td><td><code>string</code></td><td></td></tr>
</tbody></table>

## Methods
Currently only <code>SELECT</code> is supported for this resource resource.

## Example
<pre>
SELECT * 
FROM aws.pinpoint.apns_channels
WHERE region = 'us-east-1'
</pre>
