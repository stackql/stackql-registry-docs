---
title: ip_sets
hide_title: false
hide_table_of_contents: false
keywords:
  - ip_sets
  - wafv2
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

Used to retrieve a list of <code>ip_sets</code> in a region or create a <code>ip_sets</code> resource, use <code>ip_set</code> to operate on an individual resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>ip_sets</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>Contains a list of IP addresses. This can be either IPV4 or IPV6. The list will be mutually</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="aws.wafv2.ip_sets" /></td></tr>
</tbody></table>

## Fields
<table><tbody>
<tr><th>Name</th><th>Datatype</th><th>Description</th></tr>
<tr><td><CopyableCode code="name" /></td><td><code>undefined</code></td><td></td></tr>
<tr><td><CopyableCode code="id" /></td><td><code>undefined</code></td><td></td></tr>
<tr><td><CopyableCode code="scope" /></td><td><code>undefined</code></td><td></td></tr>
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
    <td><CopyableCode code="create_resource" /></td>
    <td><code>INSERT</code></td>
    <td><CopyableCode code="data__DesiredState, region" /></td>
  </tr>
  <tr>
    <td><CopyableCode code="list_resource" /></td>
    <td><code>SELECT</code></td>
    <td><CopyableCode code="region" /></td>
  </tr>
</tbody></table>

## `SELECT` Example
```sql
SELECT
region,
name,
id,
scope
FROM aws.wafv2.ip_sets

```

## Permissions

To operate on the <code>ip_sets</code> resource, the following permissions are required:

### Create
```json
wafv2:CreateIPSet,
wafv2:GetIPSet,
wafv2:ListTagsForResource
```

### List
```json
wafv2:listIPSets
```

