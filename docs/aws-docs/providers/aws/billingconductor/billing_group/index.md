---
title: billing_group
hide_title: false
hide_table_of_contents: false
keywords:
  - billing_group
  - billingconductor
  - aws
  - stackql
  - infrastructure-as-code
  - configuration-as-data
  - cloud inventory
description: Query, deploy and manage AWS resources using SQL
custom_edit_url: null
image: /img/providers/aws/stackql-aws-provider-featured-image.png
---
Gets an individual <code>billing_group</code> resource

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>billing_group</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>billing_group</td></tr>
<tr><td><b>Id</b></td><td><code>aws.billingconductor.billing_group</code></td></tr>
</tbody></table>

## Fields
<table><tbody>
<tr><th>Name</th><th>Datatype</th><th>Description</th></tr>
<tr><td><code>Arn</code></td><td><code>string</code></td><td>Billing Group ARN</td></tr>
<tr><td><code>Name</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>Description</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>PrimaryAccountId</code></td><td><code>string</code></td><td>This account will act as a virtual payer account of the billing group</td></tr>
<tr><td><code>ComputationPreference</code></td><td><code>object</code></td><td></td></tr>
<tr><td><code>AccountGrouping</code></td><td><code>object</code></td><td></td></tr>
<tr><td><code>Size</code></td><td><code>integer</code></td><td>Number of accounts in the billing group</td></tr>
<tr><td><code>Status</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>StatusReason</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>CreationTime</code></td><td><code>integer</code></td><td>Creation timestamp in UNIX epoch time format</td></tr>
<tr><td><code>LastModifiedTime</code></td><td><code>integer</code></td><td>Latest modified timestamp in UNIX epoch time format</td></tr>
<tr><td><code>Tags</code></td><td><code>array</code></td><td></td></tr>

</tbody></table>

## Methods
Currently only <code>SELECT</code> is supported for this resource resource.

## Example
<pre>
SELECT *<br/>FROM aws.billingconductor.billing_group<br/>WHERE region = 'us-east-1'<br/>AND data__Identifier = '&lt;Arn&gt;'
</pre>
