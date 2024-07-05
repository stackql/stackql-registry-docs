---
title: keys_list_only
hide_title: false
hide_table_of_contents: false
keywords:
  - keys_list_only
  - paymentcryptography
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

Lists <code>keys</code> in a region or regions, for all properties use <a href="/providers/aws/serviceName/keys/"><code>keys</code></a>

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>keys_list_only</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>Definition of AWS::PaymentCryptography::Key Resource Type</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="aws.paymentcryptography.keys_list_only" /></td></tr>
</tbody></table>

## Fields
<table><tbody><tr><th>Name</th><th>Datatype</th><th>Description</th></tr><tr><td><CopyableCode code="enabled" /></td><td><code>boolean</code></td><td></td></tr>
<tr><td><CopyableCode code="exportable" /></td><td><code>boolean</code></td><td></td></tr>
<tr><td><CopyableCode code="key_attributes" /></td><td><code>object</code></td><td></td></tr>
<tr><td><CopyableCode code="key_check_value_algorithm" /></td><td><code>string</code></td><td></td></tr>
<tr><td><CopyableCode code="key_identifier" /></td><td><code>string</code></td><td></td></tr>
<tr><td><CopyableCode code="key_origin" /></td><td><code>string</code></td><td>Defines the source of a key</td></tr>
<tr><td><CopyableCode code="key_state" /></td><td><code>string</code></td><td>Defines the state of a key</td></tr>
<tr><td><CopyableCode code="tags" /></td><td><code>array</code></td><td></td></tr>
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
Lists all <code>keys</code> in a region.
```sql
SELECT
region,
key_identifier
FROM aws.paymentcryptography.keys_list_only
WHERE region = 'us-east-1';
```


## Permissions

For permissions required to operate on the <code>keys_list_only</code> resource, see <a href="/providers/aws/paymentcryptography/keys/#permissions"><code>keys</code></a>


