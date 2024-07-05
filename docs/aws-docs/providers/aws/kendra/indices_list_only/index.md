---
title: indices_list_only
hide_title: false
hide_table_of_contents: false
keywords:
  - indices_list_only
  - kendra
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

Lists <code>indices</code> in a region or regions, for all properties use <a href="/providers/aws/serviceName/indices/"><code>indices</code></a>

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>indices_list_only</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>A Kendra index</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="aws.kendra.indices_list_only" /></td></tr>
</tbody></table>

## Fields
<table><tbody><tr><th>Name</th><th>Datatype</th><th>Description</th></tr><tr><td><CopyableCode code="id" /></td><td><code>string</code></td><td>Unique ID of index</td></tr>
<tr><td><CopyableCode code="arn" /></td><td><code>string</code></td><td></td></tr>
<tr><td><CopyableCode code="description" /></td><td><code>string</code></td><td>A description for the index</td></tr>
<tr><td><CopyableCode code="server_side_encryption_configuration" /></td><td><code>object</code></td><td>Server side encryption configuration</td></tr>
<tr><td><CopyableCode code="tags" /></td><td><code>array</code></td><td>Tags for labeling the index</td></tr>
<tr><td><CopyableCode code="name" /></td><td><code>string</code></td><td>Name of index</td></tr>
<tr><td><CopyableCode code="role_arn" /></td><td><code>string</code></td><td>Role Arn</td></tr>
<tr><td><CopyableCode code="edition" /></td><td><code>string</code></td><td>Edition of index</td></tr>
<tr><td><CopyableCode code="document_metadata_configurations" /></td><td><code>array</code></td><td>Document metadata configurations</td></tr>
<tr><td><CopyableCode code="capacity_units" /></td><td><code>object</code></td><td>Capacity units</td></tr>
<tr><td><CopyableCode code="user_context_policy" /></td><td><code>string</code></td><td></td></tr>
<tr><td><CopyableCode code="user_token_configurations" /></td><td><code>array</code></td><td></td></tr>
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
Lists all <code>indices</code> in a region.
```sql
SELECT
region,
id
FROM aws.kendra.indices_list_only
WHERE region = 'us-east-1';
```


## Permissions

For permissions required to operate on the <code>indices_list_only</code> resource, see <a href="/providers/aws/kendra/indices/#permissions"><code>indices</code></a>


