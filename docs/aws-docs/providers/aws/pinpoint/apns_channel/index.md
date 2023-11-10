---
title: apns_channel
hide_title: false
hide_table_of_contents: false
keywords:
  - apns_channel
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
Gets an individual <code>apns_channel</code> resource

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>apns_channel</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>apns_channel</td></tr>
<tr><td><b>Id</b></td><td><code>aws.pinpoint.apns_channel</code></td></tr>
</tbody></table>

## Fields
<table><tbody>
<tr><th>Name</th><th>Datatype</th><th>Description</th></tr>
<tr><td><code>id</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>bundle_id</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>private_key</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>enabled</code></td><td><code>boolean</code></td><td></td></tr>
<tr><td><code>default_authentication_method</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>token_key</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>application_id</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>team_id</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>certificate</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>token_key_id</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>region</code></td><td><code>string</code></td><td>AWS region.</td></tr>

</tbody></table>

## Methods
Currently only <code>SELECT</code> is supported for this resource resource.

## Example
```sql
SELECT
region,
id,
bundle_id,
private_key,
enabled,
default_authentication_method,
token_key,
application_id,
team_id,
certificate,
token_key_id
FROM aws.pinpoint.apns_channel
WHERE region = 'us-east-1'
AND data__Identifier = '<Id>'
```
