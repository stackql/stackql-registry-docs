---
title: resource_policies_list_only
hide_title: false
hide_table_of_contents: false
keywords:
  - resource_policies_list_only
  - ssm
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

Lists <code>resource_policies</code> in a region or regions, for all properties use <a href="/providers/aws/serviceName/resource_policies/"><code>resource_policies</code></a>

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>resource_policies_list_only</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>Resource Type definition for AWS::SSM::ResourcePolicy</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="aws.ssm.resource_policies_list_only" /></td></tr>
</tbody></table>

## Fields
<table><tbody><tr><th>Name</th><th>Datatype</th><th>Description</th></tr><tr><td><CopyableCode code="resource_arn" /></td><td><code>string</code></td><td>Arn of OpsItemGroup etc.</td></tr>
<tr><td><CopyableCode code="policy" /></td><td><code>object</code></td><td>Actual policy statement.</td></tr>
<tr><td><CopyableCode code="policy_id" /></td><td><code>string</code></td><td>An unique identifier within the policies of a resource.</td></tr>
<tr><td><CopyableCode code="policy_hash" /></td><td><code>string</code></td><td>A snapshot identifier for the policy over time.</td></tr>
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
Lists all <code>resource_policies</code> in a region.
```sql
SELECT
region,
policy_id,
resource_arn
FROM aws.ssm.resource_policies_list_only
WHERE region = 'us-east-1';
```


## Permissions

For permissions required to operate on the <code>resource_policies_list_only</code> resource, see <a href="/providers/aws/ssm/resource_policies/#permissions"><code>resource_policies</code></a>


