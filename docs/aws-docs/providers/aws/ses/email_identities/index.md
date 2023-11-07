---
title: email_identities
hide_title: false
hide_table_of_contents: false
keywords:
  - email_identities
  - ses
  - aws
  - stackql
  - infrastructure-as-code
  - configuration-as-data
  - cloud inventory
description: Query, deploy and manage AWS resources using SQL
custom_edit_url: null
image: /img/providers/aws/stackql-aws-provider-featured-image.png
---
Retrieves a list of <code>email_identities</code> in a region

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>email_identities</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>email_identities</td></tr>
<tr><td><b>Id</b></td><td><code>aws.ses.email_identities</code></td></tr>
</tbody></table>

## Fields
<table><tbody>
<tr><th>Name</th><th>Datatype</th><th>Description</th></tr>
<tr><td><code>EmailIdentity</code></td><td><code>string</code></td><td>The email address or domain to verify.</td></tr>
<tr><td><code>ConfigurationSetAttributes</code></td><td><code>undefined</code></td><td></td></tr>
<tr><td><code>DkimSigningAttributes</code></td><td><code>undefined</code></td><td></td></tr>
<tr><td><code>DkimAttributes</code></td><td><code>undefined</code></td><td></td></tr>
<tr><td><code>MailFromAttributes</code></td><td><code>undefined</code></td><td></td></tr>
<tr><td><code>FeedbackAttributes</code></td><td><code>undefined</code></td><td></td></tr>
<tr><td><code>DkimDNSTokenName1</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>DkimDNSTokenName2</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>DkimDNSTokenName3</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>DkimDNSTokenValue1</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>DkimDNSTokenValue2</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>DkimDNSTokenValue3</code></td><td><code>string</code></td><td></td></tr>

</tbody></table>

## Methods
Currently only <code>SELECT</code> is supported for this resource resource.

## Example
<pre>
SELECT * 
FROM aws.ses.email_identities
WHERE region = 'us-east-1'
</pre>
