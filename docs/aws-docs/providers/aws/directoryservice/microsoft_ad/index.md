---
title: microsoft_ad
hide_title: false
hide_table_of_contents: false
keywords:
  - microsoft_ad
  - directoryservice
  - aws
  - stackql
  - infrastructure-as-code
  - configuration-as-data
  - cloud inventory
description: Query, deploy and manage AWS resources using SQL
custom_edit_url: null
image: /img/providers/aws/stackql-aws-provider-featured-image.png
---
Gets an individual <code>microsoft_ad</code> resource

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>microsoft_ad</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>microsoft_ad</td></tr>
<tr><td><b>Id</b></td><td><code>aws.directoryservice.microsoft_ad</code></td></tr>
</tbody></table>

## Fields
<table><tbody>
<tr><th>Name</th><th>Datatype</th><th>Description</th></tr>
<tr><td><code>id</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>alias</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>dns_ip_addresses</code></td><td><code>array</code></td><td></td></tr>
<tr><td><code>create_alias</code></td><td><code>boolean</code></td><td></td></tr>
<tr><td><code>edition</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>enable_sso</code></td><td><code>boolean</code></td><td></td></tr>
<tr><td><code>name</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>password</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>short_name</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>vpc_settings</code></td><td><code>object</code></td><td></td></tr>
<tr><td><code>region</code></td><td><code>string</code></td><td>AWS region.</td></tr>

</tbody></table>

## Methods
Currently only <code>SELECT</code> is supported for this resource resource.

## Example
```sql
SELECT
region,
id,
alias,
dns_ip_addresses,
create_alias,
edition,
enable_sso,
name,
password,
short_name,
vpc_settings
FROM aws.directoryservice.microsoft_ad
WHERE region = 'us-east-1'
AND data__Identifier = '&lt;Id&gt;'
```
