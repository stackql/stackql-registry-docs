---
title: type_activations_list_only
hide_title: false
hide_table_of_contents: false
keywords:
  - type_activations_list_only
  - cloudformation
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

Lists <code>type_activations</code> in a region or regions, for all properties use <a href="/providers/aws/serviceName/type_activations/"><code>type_activations</code></a>

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>type_activations_list_only</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>Enable a resource that has been published in the CloudFormation Registry.</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="aws.cloudformation.type_activations_list_only" /></td></tr>
</tbody></table>

## Fields
<table><tbody><tr><th>Name</th><th>Datatype</th><th>Description</th></tr><tr><td><CopyableCode code="arn" /></td><td><code>string</code></td><td>The Amazon Resource Name (ARN) of the extension.</td></tr>
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
Lists all <code>type_activations</code> in a region.
```sql
SELECT
region,
arn
FROM aws.cloudformation.type_activations_list_only
WHERE region = 'us-east-1';
```


## Permissions

For permissions required to operate on the <code>type_activations_list_only</code> resource, see <a href="/providers/aws/cloudformation/type_activations/#permissions"><code>type_activations</code></a>

