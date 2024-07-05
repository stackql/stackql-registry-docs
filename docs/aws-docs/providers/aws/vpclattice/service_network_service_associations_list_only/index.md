---
title: service_network_service_associations_list_only
hide_title: false
hide_table_of_contents: false
keywords:
  - service_network_service_associations_list_only
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

Lists <code>service_network_service_associations</code> in a region or regions, for all properties use <a href="/providers/aws/serviceName/service_network_service_associations/"><code>service_network_service_associations</code></a>

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>service_network_service_associations_list_only</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>Associates a service with a service network.</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="aws.vpclattice.service_network_service_associations_list_only" /></td></tr>
</tbody></table>

## Fields
<table><tbody><tr><th>Name</th><th>Datatype</th><th>Description</th></tr><tr><td><CopyableCode code="arn" /></td><td><code>string</code></td><td></td></tr>
<tr><td><CopyableCode code="created_at" /></td><td><code>string</code></td><td></td></tr>
<tr><td><CopyableCode code="dns_entry" /></td><td><code>object</code></td><td></td></tr>
<tr><td><CopyableCode code="id" /></td><td><code>string</code></td><td></td></tr>
<tr><td><CopyableCode code="service_network_arn" /></td><td><code>string</code></td><td></td></tr>
<tr><td><CopyableCode code="service_network_id" /></td><td><code>string</code></td><td></td></tr>
<tr><td><CopyableCode code="service_network_identifier" /></td><td><code>string</code></td><td></td></tr>
<tr><td><CopyableCode code="service_network_name" /></td><td><code>string</code></td><td></td></tr>
<tr><td><CopyableCode code="service_arn" /></td><td><code>string</code></td><td></td></tr>
<tr><td><CopyableCode code="service_id" /></td><td><code>string</code></td><td></td></tr>
<tr><td><CopyableCode code="service_identifier" /></td><td><code>string</code></td><td></td></tr>
<tr><td><CopyableCode code="service_name" /></td><td><code>string</code></td><td></td></tr>
<tr><td><CopyableCode code="status" /></td><td><code>string</code></td><td></td></tr>
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
Lists all <code>service_network_service_associations</code> in a region.
```sql
SELECT
region,
arn
FROM aws.vpclattice.service_network_service_associations_list_only
WHERE region = 'us-east-1';
```


## Permissions

For permissions required to operate on the <code>service_network_service_associations_list_only</code> resource, see <a href="/providers/aws/vpclattice/service_network_service_associations/#permissions"><code>service_network_service_associations</code></a>


