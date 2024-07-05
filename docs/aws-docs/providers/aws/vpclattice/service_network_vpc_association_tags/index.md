---
title: service_network_vpc_association_tags
hide_title: false
hide_table_of_contents: false
keywords:
  - service_network_vpc_association_tags
  - vpclattice
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

Expands all tag keys and values for <code>service_network_vpc_associations</code> in a region

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>service_network_vpc_association_tags</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>Associates a VPC with a service network.</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="aws.vpclattice.service_network_vpc_association_tags" /></td></tr>
</tbody></table>

## Fields
<table><tbody><tr><th>Name</th><th>Datatype</th><th>Description</th></tr><tr><td><CopyableCode code="arn" /></td><td><code>string</code></td><td></td></tr>
<tr><td><CopyableCode code="created_at" /></td><td><code>string</code></td><td></td></tr>
<tr><td><CopyableCode code="security_group_ids" /></td><td><code>array</code></td><td></td></tr>
<tr><td><CopyableCode code="id" /></td><td><code>string</code></td><td></td></tr>
<tr><td><CopyableCode code="service_network_arn" /></td><td><code>string</code></td><td></td></tr>
<tr><td><CopyableCode code="service_network_id" /></td><td><code>string</code></td><td></td></tr>
<tr><td><CopyableCode code="service_network_identifier" /></td><td><code>string</code></td><td></td></tr>
<tr><td><CopyableCode code="service_network_name" /></td><td><code>string</code></td><td></td></tr>
<tr><td><CopyableCode code="status" /></td><td><code>string</code></td><td></td></tr>
<tr><td><CopyableCode code="vpc_id" /></td><td><code>string</code></td><td></td></tr>
<tr><td><CopyableCode code="vpc_identifier" /></td><td><code>string</code></td><td></td></tr>
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
Expands tags for all <code>service_network_vpc_associations</code> in a region.
```sql
SELECT
region,
arn,
created_at,
security_group_ids,
id,
service_network_arn,
service_network_id,
service_network_identifier,
service_network_name,
status,
vpc_id,
vpc_identifier,
tag_key,
tag_value
FROM aws.vpclattice.service_network_vpc_association_tags
WHERE region = 'us-east-1';
```


## Permissions

For permissions required to operate on the <code>service_network_vpc_association_tags</code> resource, see <a href="/providers/aws/vpclattice/service_network_vpc_associations/#permissions"><code>service_network_vpc_associations</code></a>


