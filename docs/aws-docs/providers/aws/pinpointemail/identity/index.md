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
<tr><td><b>Description</b></td><td>identity</td></tr>
<tr><td><b>Id</b></td><td><code>aws.pinpointemail.identity</code></td></tr>
</tbody></table>

## Fields
<table><tbody>
<tr><th>Name</th><th>Datatype</th><th>Description</th></tr>
<tr><td><code>id</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>identity_dn_srecord_name3</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>identity_dn_srecord_name1</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>identity_dn_srecord_name2</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>identity_dn_srecord_value3</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>identity_dn_srecord_value2</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>identity_dn_srecord_value1</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>feedback_forwarding_enabled</code></td><td><code>boolean</code></td><td></td></tr>
<tr><td><code>dkim_signing_enabled</code></td><td><code>boolean</code></td><td></td></tr>
<tr><td><code>tags</code></td><td><code>array</code></td><td></td></tr>
<tr><td><code>name</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>mail_from_attributes</code></td><td><code>object</code></td><td></td></tr>
<tr><td><code>region</code></td><td><code>string</code></td><td>AWS region.</td></tr>

</tbody></table>

## Methods
Currently only <code>SELECT</code> is supported for this resource resource.

## Example
```sql
SELECT
region,
id,
identity_dn_srecord_name3,
identity_dn_srecord_name1,
identity_dn_srecord_name2,
identity_dn_srecord_value3,
identity_dn_srecord_value2,
identity_dn_srecord_value1,
feedback_forwarding_enabled,
dkim_signing_enabled,
tags,
name,
mail_from_attributes
FROM aws.pinpointemail.identity
WHERE region = 'us-east-1'
AND data__Identifier = '<Id>'
```
