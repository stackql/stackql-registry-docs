---
title: accessor_tags
hide_title: false
hide_table_of_contents: false
keywords:
  - accessor_tags
  - managedblockchain
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

Expands all tag keys and values for <code>accessors</code> in a region

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>accessor_tags</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>Definition of AWS::ManagedBlockchain::com.amazonaws.taiga.webservice.api#Accessor Resource Type</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="aws.managedblockchain.accessor_tags" /></td></tr>
</tbody></table>

## Fields
<table><tbody><tr><th>Name</th><th>Datatype</th><th>Description</th></tr><tr><td><CopyableCode code="arn" /></td><td><code>string</code></td><td></td></tr>
<tr><td><CopyableCode code="billing_token" /></td><td><code>string</code></td><td></td></tr>
<tr><td><CopyableCode code="creation_date" /></td><td><code>string</code></td><td></td></tr>
<tr><td><CopyableCode code="id" /></td><td><code>string</code></td><td></td></tr>
<tr><td><CopyableCode code="status" /></td><td><code>string</code></td><td></td></tr>
<tr><td><CopyableCode code="accessor_type" /></td><td><code>string</code></td><td></td></tr>
<tr><td><CopyableCode code="network_type" /></td><td><code>string</code></td><td></td></tr>
<tr><td><CopyableCode code="tag_key" /></td><td><code>string</code></td><td>Tag key.</td></tr>
<tr><td><CopyableCode code="tag_value" /></td><td><code>string</code></td><td>Tag value.</td></tr>
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
Expands tags for all <code>accessors</code> in a region.
```sql
SELECT
region,
arn,
billing_token,
creation_date,
id,
status,
accessor_type,
network_type,
tag_key,
tag_value
FROM aws.managedblockchain.accessor_tags
WHERE region = 'us-east-1';
```


## Permissions

For permissions required to operate on the <code>accessor_tags</code> resource, see <a href="/providers/aws/managedblockchain/accessors/#permissions"><code>accessors</code></a>

