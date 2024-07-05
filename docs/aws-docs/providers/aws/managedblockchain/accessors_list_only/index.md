---
title: accessors_list_only
hide_title: false
hide_table_of_contents: false
keywords:
  - accessors_list_only
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

Lists <code>accessors</code> in a region or regions, for all properties use <a href="/providers/aws/serviceName/accessors/"><code>accessors</code></a>

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>accessors_list_only</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>Definition of AWS::ManagedBlockchain::com.amazonaws.taiga.webservice.api#Accessor Resource Type</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="aws.managedblockchain.accessors_list_only" /></td></tr>
</tbody></table>

## Fields
<table><tbody><tr><th>Name</th><th>Datatype</th><th>Description</th></tr><tr><td><CopyableCode code="arn" /></td><td><code>string</code></td><td></td></tr>
<tr><td><CopyableCode code="billing_token" /></td><td><code>string</code></td><td></td></tr>
<tr><td><CopyableCode code="creation_date" /></td><td><code>string</code></td><td></td></tr>
<tr><td><CopyableCode code="id" /></td><td><code>string</code></td><td></td></tr>
<tr><td><CopyableCode code="status" /></td><td><code>string</code></td><td></td></tr>
<tr><td><CopyableCode code="accessor_type" /></td><td><code>string</code></td><td></td></tr>
<tr><td><CopyableCode code="network_type" /></td><td><code>string</code></td><td></td></tr>
<tr><td><CopyableCode code="tags" /></td><td><code>array</code></td><td>An array of key-value pairs to apply to this resource.</td></tr>
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
Lists all <code>accessors</code> in a region.
```sql
SELECT
region,
id
FROM aws.managedblockchain.accessors_list_only
WHERE region = 'us-east-1';
```


## Permissions

For permissions required to operate on the <code>accessors_list_only</code> resource, see <a href="/providers/aws/managedblockchain/accessors/#permissions"><code>accessors</code></a>


