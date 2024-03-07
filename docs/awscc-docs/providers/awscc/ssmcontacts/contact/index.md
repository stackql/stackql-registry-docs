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
<tr><td><b>Description</b></td><td>contact</td></tr>
<tr><td><b>Id</b></td><td><code>awscc.ssmcontacts.contact</code></td></tr>
</tbody></table>

## Fields
<table><tbody>
<tr><th>Name</th><th>Datatype</th><th>Description</th></tr>
<tr><td><code>alias</code></td><td><code>string</code></td><td>Alias of the contact. String value with 20 to 256 characters. Only alphabetical, numeric characters, dash, or underscore allowed.</td></tr>
<tr><td><code>display_name</code></td><td><code>string</code></td><td>Name of the contact. String value with 3 to 256 characters. Only alphabetical, space, numeric characters, dash, or underscore allowed.</td></tr>
<tr><td><code>type</code></td><td><code>string</code></td><td>Contact type, which specify type of contact. Currently supported values: “PERSONAL”, “SHARED”, “OTHER“.</td></tr>
<tr><td><code>plan</code></td><td><code>array</code></td><td>The stages that an escalation plan or engagement plan engages contacts and contact methods in.</td></tr>
<tr><td><code>arn</code></td><td><code>string</code></td><td>The Amazon Resource Name (ARN) of the contact.</td></tr>
<tr><td><code>region</code></td><td><code>string</code></td><td>AWS region.</td></tr>

</tbody></table>

## Methods
Currently only <code>SELECT</code> is supported for this resource resource.

## Permissions

To operate on the <code>contact</code> resource, the following permissions are required:

### Read
<pre>
ssm-contacts:GetContact</pre>

### Update
<pre>
ssm-contacts:UpdateContact,
ssm-contacts:GetContact,
ssm-contacts:AssociateContact</pre>

### Delete
<pre>
ssm-contacts:DeleteContact,
ssm-contacts:GetContact,
ssm-contacts:AssociateContact</pre>


## Example
```sql
SELECT
region,
alias,
display_name,
type,
plan,
arn
FROM awscc.ssmcontacts.contact
WHERE region = 'us-east-1'
AND data__Identifier = '&lt;Arn&gt;'
```
