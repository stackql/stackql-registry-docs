---
title: ip_set
hide_title: false
hide_table_of_contents: false
keywords:
  - ip_set
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
import Tabs from '@theme/Tabs';
import TabItem from '@theme/TabItem';


Gets or updates an individual <code>ip_set</code> resource, use <code>ip_sets</code> to retrieve a list of resources or to create or delete a resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>ip_set</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>Contains a list of IP addresses. This can be either IPV4 or IPV6. The list will be mutually</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="aws.wafv2.ip_set" /></td></tr>
</tbody></table>

## Fields
<table><tbody>
<tr><th>Name</th><th>Datatype</th><th>Description</th></tr>
<tr><td><CopyableCode code="arn" /></td><td><code>string</code></td><td></td></tr>
<tr><td><CopyableCode code="description" /></td><td><code>string</code></td><td></td></tr>
<tr><td><CopyableCode code="name" /></td><td><code>string</code></td><td></td></tr>
<tr><td><CopyableCode code="id" /></td><td><code>string</code></td><td></td></tr>
<tr><td><CopyableCode code="scope" /></td><td><code>string</code></td><td></td></tr>
<tr><td><CopyableCode code="ip_address_version" /></td><td><code>string</code></td><td></td></tr>
<tr><td><CopyableCode code="addresses" /></td><td><code>array</code></td><td>List of IPAddresses.</td></tr>
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
    <td><CopyableCode code="update_resource" /></td>
    <td><code>UPDATE</code></td>
    <td><CopyableCode code="data__Identifier, data__PatchDocument, region" /></td>
  </tr>
  <tr>
    <td><CopyableCode code="get_resource" /></td>
    <td><code>SELECT</code></td>
    <td><CopyableCode code="data__Identifier, region" /></td>
  </tr>
</tbody></table>

## `SELECT` Example
```sql
SELECT
region,
arn,
description,
name,
id,
scope,
ip_address_version,
addresses,
tags
FROM aws.wafv2.ip_set
WHERE data__Identifier = '<Name>|<Id>|<Scope>';
```


## Permissions

To operate on the <code>ip_set</code> resource, the following permissions are required:

### Read
```json
wafv2:GetIPSet,
wafv2:ListTagsForResource
```

### Update
```json
wafv2:UpdateIPSet,
wafv2:GetIPSet,
wafv2:ListTagsForResource
```

