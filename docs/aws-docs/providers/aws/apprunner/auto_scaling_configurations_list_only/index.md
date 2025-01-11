---
title: auto_scaling_configurations_list_only
hide_title: false
hide_table_of_contents: false
keywords:
  - auto_scaling_configurations_list_only
  - apprunner
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

Lists <code>auto_scaling_configurations</code> in a region or regions, for all properties use <a href="/providers/aws/serviceName/auto_scaling_configurations/"><code>auto_scaling_configurations</code></a>

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>auto_scaling_configurations_list_only</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>Describes an AWS App Runner automatic configuration resource that enables automatic scaling of instances used to process web requests. You can share an auto scaling configuration across multiple services.</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="aws.apprunner.auto_scaling_configurations_list_only" /></td></tr>
</tbody></table>

## Fields
<table><tbody><tr><th>Name</th><th>Datatype</th><th>Description</th></tr><tr><td><CopyableCode code="auto_scaling_configuration_arn" /></td><td><code>string</code></td><td>The Amazon Resource Name (ARN) of this auto scaling configuration.</td></tr>
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
Lists all <code>auto_scaling_configurations</code> in a region.
```sql
SELECT
region,
auto_scaling_configuration_arn
FROM aws.apprunner.auto_scaling_configurations_list_only
WHERE region = 'us-east-1';
```


## Permissions

For permissions required to operate on the <code>auto_scaling_configurations_list_only</code> resource, see <a href="/providers/aws/apprunner/auto_scaling_configurations/#permissions"><code>auto_scaling_configurations</code></a>

