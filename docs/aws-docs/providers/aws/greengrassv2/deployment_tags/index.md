---
title: deployment_tags
hide_title: false
hide_table_of_contents: false
keywords:
  - deployment_tags
  - greengrassv2
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

Expands all tag keys and values for <code>deployments</code> in a region

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>deployment_tags</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>Resource for Greengrass V2 deployment.</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="aws.greengrassv2.deployment_tags" /></td></tr>
</tbody></table>

## Fields
<table><tbody><tr><th>Name</th><th>Datatype</th><th>Description</th></tr><tr><td><CopyableCode code="target_arn" /></td><td><code>string</code></td><td></td></tr>
<tr><td><CopyableCode code="parent_target_arn" /></td><td><code>string</code></td><td></td></tr>
<tr><td><CopyableCode code="deployment_id" /></td><td><code>string</code></td><td></td></tr>
<tr><td><CopyableCode code="deployment_name" /></td><td><code>string</code></td><td></td></tr>
<tr><td><CopyableCode code="components" /></td><td><code>object</code></td><td></td></tr>
<tr><td><CopyableCode code="iot_job_configuration" /></td><td><code>object</code></td><td></td></tr>
<tr><td><CopyableCode code="deployment_policies" /></td><td><code>object</code></td><td></td></tr>
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
Expands tags for all <code>deployments</code> in a region.
```sql
SELECT
region,
target_arn,
parent_target_arn,
deployment_id,
deployment_name,
components,
iot_job_configuration,
deployment_policies,
tag_key,
tag_value
FROM aws.greengrassv2.deployment_tags
WHERE region = 'us-east-1';
```


## Permissions

For permissions required to operate on the <code>deployment_tags</code> resource, see <a href="/providers/aws/greengrassv2/deployments/#permissions"><code>deployments</code></a>

