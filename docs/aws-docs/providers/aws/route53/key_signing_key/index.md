---
title: key_signing_key
hide_title: false
hide_table_of_contents: false
keywords:
  - key_signing_key
  - route53
  - aws
  - stackql
  - infrastructure-as-code
  - configuration-as-data
  - cloud inventory
description: Query, deploy and manage AWS resources using SQL
custom_edit_url: null
image: /img/providers/aws/stackql-aws-provider-featured-image.png
---
Gets an individual <code>key_signing_key</code> resource

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>key_signing_key</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>key_signing_key</td></tr>
<tr><td><b>Id</b></td><td><code>aws.route53.key_signing_key</code></td></tr>
</tbody></table>

## Fields
<table><tbody>
<tr><th>Name</th><th>Datatype</th><th>Description</th></tr>
<tr><td><code>HostedZoneId</code></td><td><code>string</code></td><td>The unique string (ID) used to identify a hosted zone.</td></tr>
<tr><td><code>Status</code></td><td><code>string</code></td><td>A string specifying the initial status of the key signing key (KSK). You can set the value to ACTIVE or INACTIVE.</td></tr>
<tr><td><code>Name</code></td><td><code>string</code></td><td>An alphanumeric string used to identify a key signing key (KSK). Name must be unique for each key signing key in the same hosted zone.</td></tr>
<tr><td><code>KeyManagementServiceArn</code></td><td><code>string</code></td><td>The Amazon resource name (ARN) for a customer managed key (CMK) in AWS Key Management Service (KMS). The KeyManagementServiceArn must be unique for each key signing key (KSK) in a single hosted zone.</td></tr>

</tbody></table>

## Methods
Currently only <code>SELECT</code> is supported for this resource resource.

## Example
<pre>
SELECT * 
FROM aws.route53.key_signing_key
WHERE region = 'us-east-1' AND data__Identifier = '&lt;HostedZoneId&gt;' AND data__Identifier = '&lt;Name&gt;'
</pre>
