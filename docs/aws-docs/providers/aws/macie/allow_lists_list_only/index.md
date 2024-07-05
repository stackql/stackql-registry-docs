---
title: allow_lists_list_only
hide_title: false
hide_table_of_contents: false
keywords:
  - allow_lists_list_only
  - macie
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

Lists <code>allow_lists</code> in a region or regions, for all properties use <a href="/providers/aws/serviceName/allow_lists/"><code>allow_lists</code></a>

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>allow_lists_list_only</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>Macie AllowList resource schema</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="aws.macie.allow_lists_list_only" /></td></tr>
</tbody></table>

## Fields
<table><tbody><tr><th>Name</th><th>Datatype</th><th>Description</th></tr><tr><td><CopyableCode code="name" /></td><td><code>string</code></td><td>Name of AllowList.</td></tr>
<tr><td><CopyableCode code="description" /></td><td><code>string</code></td><td>Description of AllowList.</td></tr>
<tr><td><CopyableCode code="criteria" /></td><td><code>object</code></td><td>AllowList criteria.</td></tr>
<tr><td><CopyableCode code="id" /></td><td><code>string</code></td><td>AllowList ID.</td></tr>
<tr><td><CopyableCode code="arn" /></td><td><code>string</code></td><td>AllowList ARN.</td></tr>
<tr><td><CopyableCode code="status" /></td><td><code>string</code></td><td>AllowList status.</td></tr>
<tr><td><CopyableCode code="tags" /></td><td><code>array</code></td><td>A collection of tags associated with a resource</td></tr>
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
Lists all <code>allow_lists</code> in a region.
```sql
SELECT
region,
id
FROM aws.macie.allow_lists_list_only
WHERE region = 'us-east-1';
```


## Permissions

For permissions required to operate on the <code>allow_lists_list_only</code> resource, see <a href="/providers/aws/macie/allow_lists/#permissions"><code>allow_lists</code></a>


