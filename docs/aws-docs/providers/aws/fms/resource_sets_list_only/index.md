---
title: resource_sets_list_only
hide_title: false
hide_table_of_contents: false
keywords:
  - resource_sets_list_only
  - fms
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

Lists <code>resource_sets</code> in a region or regions, for all properties use <a href="/providers/aws/serviceName/resource_sets/"><code>resource_sets</code></a>

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>resource_sets_list_only</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>Creates an AWS Firewall Manager resource set.</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="aws.fms.resource_sets_list_only" /></td></tr>
</tbody></table>

## Fields
<table><tbody><tr><th>Name</th><th>Datatype</th><th>Description</th></tr><tr><td><CopyableCode code="id" /></td><td><code>string</code></td><td>A Base62 ID</td></tr>
<tr><td><CopyableCode code="name" /></td><td><code>string</code></td><td></td></tr>
<tr><td><CopyableCode code="description" /></td><td><code>string</code></td><td></td></tr>
<tr><td><CopyableCode code="resource_type_list" /></td><td><code>array</code></td><td></td></tr>
<tr><td><CopyableCode code="resources" /></td><td><code>array</code></td><td></td></tr>
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
Lists all <code>resource_sets</code> in a region.
```sql
SELECT
region,
id
FROM aws.fms.resource_sets_list_only
WHERE region = 'us-east-1';
```


## Permissions

For permissions required to operate on the <code>resource_sets_list_only</code> resource, see <a href="/providers/aws/fms/resource_sets/#permissions"><code>resource_sets</code></a>


