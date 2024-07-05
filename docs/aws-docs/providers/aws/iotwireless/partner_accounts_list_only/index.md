---
title: partner_accounts_list_only
hide_title: false
hide_table_of_contents: false
keywords:
  - partner_accounts_list_only
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

import CopyableCode from '@site/src/components/CopyableCode/CopyableCode';
import Tabs from '@theme/Tabs';
import TabItem from '@theme/TabItem';

Lists <code>partner_accounts</code> in a region or regions, for all properties use <a href="/providers/aws/serviceName/partner_accounts/"><code>partner_accounts</code></a>

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>partner_accounts_list_only</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>Create and manage partner account</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="aws.iotwireless.partner_accounts_list_only" /></td></tr>
</tbody></table>

## Fields
<table><tbody><tr><th>Name</th><th>Datatype</th><th>Description</th></tr><tr><td><CopyableCode code="sidewalk" /></td><td><code>object</code></td><td>The Sidewalk account credentials.</td></tr>
<tr><td><CopyableCode code="partner_account_id" /></td><td><code>string</code></td><td>The partner account ID to disassociate from the AWS account</td></tr>
<tr><td><CopyableCode code="partner_type" /></td><td><code>string</code></td><td>The partner type</td></tr>
<tr><td><CopyableCode code="sidewalk_response" /></td><td><code>object</code></td><td>The Sidewalk account credentials.</td></tr>
<tr><td><CopyableCode code="account_linked" /></td><td><code>boolean</code></td><td>Whether the partner account is linked to the AWS account.</td></tr>
<tr><td><CopyableCode code="sidewalk_update" /></td><td><code>object</code></td><td>The Sidewalk account credentials.</td></tr>
<tr><td><CopyableCode code="fingerprint" /></td><td><code>string</code></td><td>The fingerprint of the Sidewalk application server private key.</td></tr>
<tr><td><CopyableCode code="arn" /></td><td><code>string</code></td><td>PartnerAccount arn. Returned after successful create.</td></tr>
<tr><td><CopyableCode code="tags" /></td><td><code>array</code></td><td>A list of key-value pairs that contain metadata for the destination.</td></tr>
<tr><td><CopyableCode code="region" /></td><td><code>string</code></td><td>AWS region.</td></tr>
</tbody></table>

## Methods

<table><tbody>
  <tr>
    <th>Name</th>
    <th>Accessible by</th>
    <th>Required Params</th>
  </tr>
  <tr>
    <td><CopyableCode code="list_resources" /></td>
    <td><code>SELECT</code></td>
    <td><CopyableCode code="region" /></td>
  </tr>
</tbody></table>

## `SELECT` examples
Lists all <code>partner_accounts</code> in a region.
```sql
SELECT
region,
partner_account_id
FROM aws.iotwireless.partner_accounts_list_only
WHERE region = 'us-east-1';
```


## Permissions

For permissions required to operate on the <code>partner_accounts_list_only</code> resource, see <a href="/providers/aws/iotwireless/partner_accounts/#permissions"><code>partner_accounts</code></a>


