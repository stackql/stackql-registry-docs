---
title: playback_key_pairs
hide_title: false
hide_table_of_contents: false
keywords:
  - playback_key_pairs
  - ivs
  - aws
  - stackql
  - infrastructure-as-code
  - configuration-as-data
  - cloud inventory
description: Query, deploy and manage AWS resources using SQL
custom_edit_url: null
image: /img/providers/aws/stackql-aws-provider-featured-image.png
---
Retrieves a list of <code>playback_key_pairs</code> in a region

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>playback_key_pairs</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>playback_key_pairs</td></tr>
<tr><td><b>Id</b></td><td><code>aws.ivs.playback_key_pairs</code></td></tr>
</tbody></table>

## Fields
<table><tbody>
<tr><th>Name</th><th>Datatype</th><th>Description</th></tr>
<tr><td><code>Name</code></td><td><code>string</code></td><td>An arbitrary string (a nickname) assigned to a playback key pair that helps the customer identify that resource. The value does not need to be unique.</td></tr>
<tr><td><code>PublicKeyMaterial</code></td><td><code>string</code></td><td>The public portion of a customer-generated key pair.</td></tr>
<tr><td><code>Fingerprint</code></td><td><code>string</code></td><td>Key-pair identifier.</td></tr>
<tr><td><code>Arn</code></td><td><code>string</code></td><td>Key-pair identifier.</td></tr>
<tr><td><code>Tags</code></td><td><code>array</code></td><td>A list of key-value pairs that contain metadata for the asset model.</td></tr>

</tbody></table>

## Methods
Currently only <code>SELECT</code> is supported for this resource resource.

## Example
<pre>
SELECT *<br/>FROM aws.ivs.playback_key_pairs<br/>WHERE region = 'us-east-1'
</pre>
