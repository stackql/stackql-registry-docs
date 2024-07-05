---
title: policies_list_only
hide_title: false
hide_table_of_contents: false
keywords:
  - policies_list_only
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

Lists <code>policies</code> in a region or regions, for all properties use <a href="/providers/aws/serviceName/policies/"><code>policies</code></a>

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>policies_list_only</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>Creates an AWS Firewall Manager policy.</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="aws.fms.policies_list_only" /></td></tr>
</tbody></table>

## Fields
<table><tbody><tr><th>Name</th><th>Datatype</th><th>Description</th></tr><tr><td><CopyableCode code="exclude_map" /></td><td><code>object</code></td><td>An FMS includeMap or excludeMap.</td></tr>
<tr><td><CopyableCode code="exclude_resource_tags" /></td><td><code>boolean</code></td><td></td></tr>
<tr><td><CopyableCode code="include_map" /></td><td><code>object</code></td><td>An FMS includeMap or excludeMap.</td></tr>
<tr><td><CopyableCode code="id" /></td><td><code>string</code></td><td></td></tr>
<tr><td><CopyableCode code="policy_name" /></td><td><code>string</code></td><td></td></tr>
<tr><td><CopyableCode code="policy_description" /></td><td><code>string</code></td><td></td></tr>
<tr><td><CopyableCode code="remediation_enabled" /></td><td><code>boolean</code></td><td></td></tr>
<tr><td><CopyableCode code="resource_tags" /></td><td><code>array</code></td><td></td></tr>
<tr><td><CopyableCode code="resource_type" /></td><td><code>string</code></td><td>An AWS resource type</td></tr>
<tr><td><CopyableCode code="resource_type_list" /></td><td><code>array</code></td><td></td></tr>
<tr><td><CopyableCode code="resource_set_ids" /></td><td><code>array</code></td><td></td></tr>
<tr><td><CopyableCode code="security_service_policy_data" /></td><td><code>object</code></td><td>Firewall security service policy data.</td></tr>
<tr><td><CopyableCode code="arn" /></td><td><code>string</code></td><td>A resource ARN.</td></tr>
<tr><td><CopyableCode code="delete_all_policy_resources" /></td><td><code>boolean</code></td><td></td></tr>
<tr><td><CopyableCode code="resources_clean_up" /></td><td><code>boolean</code></td><td></td></tr>
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
Lists all <code>policies</code> in a region.
```sql
SELECT
region,
id
FROM aws.fms.policies_list_only
WHERE region = 'us-east-1';
```


## Permissions

For permissions required to operate on the <code>policies_list_only</code> resource, see <a href="/providers/aws/fms/policies/#permissions"><code>policies</code></a>


