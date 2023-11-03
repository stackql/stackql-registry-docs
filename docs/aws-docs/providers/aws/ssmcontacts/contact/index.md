---
title: contact
hide_title: false
hide_table_of_contents: false
keywords:
  - contact
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
Gets an individual <code>contact</code> resource

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>contact</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
null
<tr><td><b>Id</b></td><td><code>aws.ssmcontacts.contact</code></td></tr>
</tbody></table>

## Fields
<table><tbody>
<tr><th>Name</th><th>Datatype</th><th>Description</th></tr>
<tr><td><code>Alias</code></td><td><code>string</code></td><td>Alias of the contact. String value with 20 to 256 characters. Only alphabetical, numeric characters, dash, or underscore allowed.</td></tr><tr><td><code>DisplayName</code></td><td><code>string</code></td><td>Name of the contact. String value with 3 to 256 characters. Only alphabetical, space, numeric characters, dash, or underscore allowed.</td></tr><tr><td><code>Type</code></td><td><code>string</code></td><td>Contact type, which specify type of contact. Currently supported values: “PERSONAL”, “SHARED”, “OTHER“.</td></tr><tr><td><code>Plan</code></td><td><code>array</code></td><td>The stages that an escalation plan or engagement plan engages contacts and contact methods in.</td></tr><tr><td><code>Arn</code></td><td><code>string</code></td><td>The Amazon Resource Name (ARN) of the contact.</td></tr>
</tbody></table>

## Methods
Currently only <code>SELECT</code> is supported for this resource resource.

## Example
<pre>
SELECT * 
FROM aws.ssmcontacts.contact
WHERE region = 'us-east-1' AND data__Identifier = '{Arn}'
</pre>
