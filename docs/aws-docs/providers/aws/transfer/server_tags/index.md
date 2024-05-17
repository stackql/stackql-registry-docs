---
title: server_tags
hide_title: false
hide_table_of_contents: false
keywords:
  - server_tags
  - transfer
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


Details of a Transfer family server tags

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>server_tags</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>Details of a Transfer family server tags</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="aws.transfer.server_tags" /></td></tr>
</tbody></table>

## Fields
<table><tbody>
<tr><th>Name</th><th>Datatype</th><th>Description</th></tr>
<tr><td><CopyableCode code="data___server_id" /></td><td><code>string</code></td><td>The server id</td></tr>
<tr><td><CopyableCode code="region" /></td><td><code>string</code></td><td></td></tr>
<tr><td><CopyableCode code="key" /></td><td><code>string</code></td><td>The key of the tag</td></tr>
<tr><td><CopyableCode code="value" /></td><td><code>string</code></td><td>The value of the tag</td></tr>
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
    <td><CopyableCode code="view" /></td>
    <td><code>SELECT</code></td>
    <td><CopyableCode code="region" /></td>
  </tr>
</tbody></table>

## `SELECT` Example
```sql
SELECT
region,
data___server_id,
region,
key,
value
FROM aws.transfer.server_tags
WHERE region = '<region>' AND data__ServerId = '<s-serverid>';
```





