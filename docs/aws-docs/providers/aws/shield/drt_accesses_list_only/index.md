---
title: drt_accesses_list_only
hide_title: false
hide_table_of_contents: false
keywords:
  - drt_accesses_list_only
  - shield
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

Lists <code>drt_accesses</code> in a region or regions, for all properties use <a href="/providers/aws/serviceName/drt_accesses/"><code>drt_accesses</code></a>

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>drt_accesses_list_only</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>Config the role and list of Amazon S3 log buckets used by the Shield Response Team (SRT) to access your AWS account while assisting with attack mitigation.</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="aws.shield.drt_accesses_list_only" /></td></tr>
</tbody></table>

## Fields
<table><tbody><tr><th>Name</th><th>Datatype</th><th>Description</th></tr><tr><td><CopyableCode code="account_id" /></td><td><code>string</code></td><td></td></tr>
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
Lists all <code>drt_accesses</code> in a region.
```sql
SELECT
region,
account_id
FROM aws.shield.drt_accesses_list_only
;
```


## Permissions

For permissions required to operate on the <code>drt_accesses_list_only</code> resource, see <a href="/providers/aws/shield/drt_accesses/#permissions"><code>drt_accesses</code></a>

