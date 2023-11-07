---
title: partner_account
hide_title: false
hide_table_of_contents: false
keywords:
  - partner_account
  - iotwireless
  - aws
  - stackql
  - infrastructure-as-code
  - configuration-as-data
  - cloud inventory
description: Query, deploy and manage AWS resources using SQL
custom_edit_url: null
image: /img/providers/aws/stackql-aws-provider-featured-image.png
---
Gets an individual <code>partner_account</code> resource

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>partner_account</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>partner_account</td></tr>
<tr><td><b>Id</b></td><td><code>aws.iotwireless.partner_account</code></td></tr>
</tbody></table>

## Fields
<table><tbody>
<tr><th>Name</th><th>Datatype</th><th>Description</th></tr>
<tr><td><code>Sidewalk</code></td><td><code>undefined</code></td><td>The Sidewalk account credentials.</td></tr>
<tr><td><code>PartnerAccountId</code></td><td><code>string</code></td><td>The partner account ID to disassociate from the AWS account</td></tr>
<tr><td><code>PartnerType</code></td><td><code>string</code></td><td>The partner type</td></tr>
<tr><td><code>SidewalkResponse</code></td><td><code>undefined</code></td><td>The Sidewalk account credentials.</td></tr>
<tr><td><code>AccountLinked</code></td><td><code>boolean</code></td><td>Whether the partner account is linked to the AWS account.</td></tr>
<tr><td><code>SidewalkUpdate</code></td><td><code>undefined</code></td><td>The Sidewalk account credentials.</td></tr>
<tr><td><code>Fingerprint</code></td><td><code>string</code></td><td>The fingerprint of the Sidewalk application server private key.</td></tr>
<tr><td><code>Arn</code></td><td><code>string</code></td><td>PartnerAccount arn. Returned after successful create.</td></tr>
<tr><td><code>Tags</code></td><td><code>array</code></td><td>A list of key-value pairs that contain metadata for the destination.</td></tr>

</tbody></table>

## Methods
Currently only <code>SELECT</code> is supported for this resource resource.

## Example
<pre>
SELECT *<br/>FROM aws.iotwireless.partner_account<br/>WHERE region = 'us-east-1'<br/>AND data__Identifier = '&lt;PartnerAccountId&gt;'
</pre>
