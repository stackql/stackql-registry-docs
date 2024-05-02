---
title: partner_account
hide_title: false
hide_table_of_contents: false
keywords:
  - partner_account
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
Gets or operates on an individual <code>partner_account</code> resource, use <code>partner_accounts</code> to retrieve a list of resources or to create a resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>partner_account</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>Create and manage partner account</td></tr>
<tr><td><b>Id</b></td><td><code>aws.iotwireless.partner_account</code></td></tr>
</tbody></table>

## Fields
<table><tbody>
<tr><th>Name</th><th>Datatype</th><th>Description</th></tr>
<tr><td><code>sidewalk</code></td><td><code>object</code></td><td>The Sidewalk account credentials.</td></tr>
<tr><td><code>partner_account_id</code></td><td><code>string</code></td><td>The partner account ID to disassociate from the AWS account</td></tr>
<tr><td><code>partner_type</code></td><td><code>string</code></td><td>The partner type</td></tr>
<tr><td><code>sidewalk_response</code></td><td><code>object</code></td><td>The Sidewalk account credentials.</td></tr>
<tr><td><code>account_linked</code></td><td><code>boolean</code></td><td>Whether the partner account is linked to the AWS account.</td></tr>
<tr><td><code>sidewalk_update</code></td><td><code>object</code></td><td>The Sidewalk account credentials.</td></tr>
<tr><td><code>fingerprint</code></td><td><code>string</code></td><td>The fingerprint of the Sidewalk application server private key.</td></tr>
<tr><td><code>arn</code></td><td><code>string</code></td><td>PartnerAccount arn. Returned after successful create.</td></tr>
<tr><td><code>tags</code></td><td><code>array</code></td><td>A list of key-value pairs that contain metadata for the destination.</td></tr>
<tr><td><code>region</code></td><td><code>string</code></td><td>AWS region.</td></tr>

</tbody></table>

## Methods

<table><tbody>
  <tr>
    <th>Name</th>
    <th>Accessible by</th>
    <th>Required Params</th>
  </tr>
  <tr>
    <td><code>update_resource</code></td>
    <td><code>UPDATE</code></td>
    <td><code>data__Identifier, data__PatchDocument, region</code></td>
  </tr>
  <tr>
    <td><code>delete_resource</code></td>
    <td><code>DELETE</code></td>
    <td><code>data__Identifier, region</code></td>
  </tr>
  <tr>
    <td><code>get_resource</code></td>
    <td><code>SELECT</code></td>
    <td><code>data__Identifier, region</code></td>
  </tr>
</tbody></table>

## `SELECT` Example
```sql
SELECT
region,
sidewalk,
partner_account_id,
partner_type,
sidewalk_response,
account_linked,
sidewalk_update,
fingerprint,
arn,
tags
FROM aws.iotwireless.partner_account
WHERE data__Identifier = '<PartnerAccountId>';
```

## Permissions

To operate on the <code>partner_account</code> resource, the following permissions are required:

### Read
```json
iotwireless:GetPartnerAccount,
iotwireless:ListTagsForResource
```

### Update
```json
iotwireless:UpdatePartnerAccount,
iotwireless:UntagResource,
iotwireless:ListTagsForResource
```

### Delete
```json
iotwireless:DisassociateAwsAccountFromPartnerAccount
```

