---
title: identity
hide_title: false
hide_table_of_contents: false
keywords:
  - identity
  - pinpointemail
  - aws
  - stackql
  - infrastructure-as-code
  - configuration-as-data
  - cloud inventory
description: Query, deploy and manage AWS resources using SQL
custom_edit_url: null
image: /img/providers/aws/stackql-aws-provider-featured-image.png
---
Gets an individual <code>identity</code> resource

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>identity</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>aws.pinpointemail.identity</code></td></tr>
</tbody></table>

## Fields
<table><tbody>
<tr><th>Name</th><th>Datatype</th><th>Description</th></tr>
<tr><td><code>Id</code></td><td><code>string</code></td><td></td></tr><tr><td><code>IdentityDNSRecordName3</code></td><td><code>string</code></td><td></td></tr><tr><td><code>IdentityDNSRecordName1</code></td><td><code>string</code></td><td></td></tr><tr><td><code>IdentityDNSRecordName2</code></td><td><code>string</code></td><td></td></tr><tr><td><code>IdentityDNSRecordValue3</code></td><td><code>string</code></td><td></td></tr><tr><td><code>IdentityDNSRecordValue2</code></td><td><code>string</code></td><td></td></tr><tr><td><code>IdentityDNSRecordValue1</code></td><td><code>string</code></td><td></td></tr><tr><td><code>FeedbackForwardingEnabled</code></td><td><code>boolean</code></td><td></td></tr><tr><td><code>DkimSigningEnabled</code></td><td><code>boolean</code></td><td></td></tr><tr><td><code>Tags</code></td><td><code>array</code></td><td></td></tr><tr><td><code>Name</code></td><td><code>string</code></td><td></td></tr><tr><td><code>MailFromAttributes</code></td><td><code>undefined</code></td><td></td></tr>
</tbody></table>

## Methods
Currently only <code>SELECT</code> is supported for this resource resource.

## Example
<pre>
SELECT * 
FROM aws.pinpointemail.identity
WHERE region = 'us-east-1' AND data__Identifier = '{Id}'
</pre>
