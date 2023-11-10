---
title: firewall
hide_title: false
hide_table_of_contents: false
keywords:
  - firewall
  - networkfirewall
  - aws
  - stackql
  - infrastructure-as-code
  - configuration-as-data
  - cloud inventory
description: Query, deploy and manage AWS resources using SQL
custom_edit_url: null
image: /img/providers/aws/stackql-aws-provider-featured-image.png
---
Gets an individual <code>firewall</code> resource

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>firewall</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>firewall</td></tr>
<tr><td><b>Id</b></td><td><code>aws.networkfirewall.firewall</code></td></tr>
</tbody></table>

## Fields
<table><tbody>
<tr><th>Name</th><th>Datatype</th><th>Description</th></tr>
<tr><td><code>firewall_name</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>firewall_arn</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>firewall_id</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>firewall_policy_arn</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>vpc_id</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>subnet_mappings</code></td><td><code>array</code></td><td></td></tr>
<tr><td><code>delete_protection</code></td><td><code>boolean</code></td><td></td></tr>
<tr><td><code>subnet_change_protection</code></td><td><code>boolean</code></td><td></td></tr>
<tr><td><code>firewall_policy_change_protection</code></td><td><code>boolean</code></td><td></td></tr>
<tr><td><code>description</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>endpoint_ids</code></td><td><code>array</code></td><td></td></tr>
<tr><td><code>tags</code></td><td><code>array</code></td><td></td></tr>
<tr><td><code>region</code></td><td><code>string</code></td><td>AWS region.</td></tr>

</tbody></table>

## Methods
Currently only <code>SELECT</code> is supported for this resource resource.

## Example
```sql
SELECT
region,
firewall_name,
firewall_arn,
firewall_id,
firewall_policy_arn,
vpc_id,
subnet_mappings,
delete_protection,
subnet_change_protection,
firewall_policy_change_protection,
description,
endpoint_ids,
tags
FROM aws.networkfirewall.firewall
WHERE region = 'us-east-1'
AND data__Identifier = '<FirewallArn>'
```
