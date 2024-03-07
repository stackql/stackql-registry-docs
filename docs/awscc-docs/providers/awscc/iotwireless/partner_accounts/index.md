---
title: partner_accounts
hide_title: false
hide_table_of_contents: false
keywords:
  - partner_accounts
  - iotwireless
  - aws
  - stackql
  - infrastructure-as-code
  - configuration-as-data
  - cloud inventory
description: Query, deploy and manage AWS resources using SQL
custom_edit_url: null
image: /img/providers/aws/stackql-aws-provider-featured-image.png
---
Retrieves a list of <code>partner_accounts</code> in a region

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>partner_accounts</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>partner_accounts</td></tr>
<tr><td><b>Id</b></td><td><code>awscc.iotwireless.partner_accounts</code></td></tr>
</tbody></table>

## Fields
<table><tbody>
<tr><th>Name</th><th>Datatype</th><th>Description</th></tr>
<tr><td><code>partner_account_id</code></td><td><code>string</code></td><td>The partner account ID to disassociate from the AWS account</td></tr>
<tr><td><code>region</code></td><td><code>string</code></td><td>AWS region.</td></tr>

</tbody></table>

## Methods
Currently only <code>SELECT</code> is supported for this resource resource.

## Permissions

To operate on the <code>partner_accounts</code> resource, the following permissions are required:

### Create
<pre>
iotwireless:AssociateAwsAccountWithPartnerAccount,
iotwireless:TagResource,
iotwireless:ListTagsForResource</pre>

### List
<pre>
iotwireless:ListPartnerAccounts,
iotwireless:ListTagsForResource</pre>


## Example
```sql
SELECT
region,
partner_account_id
FROM awscc.iotwireless.partner_accounts
WHERE region = 'us-east-1'
```
