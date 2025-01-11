---
title: logging_configurations_list_only
hide_title: false
hide_table_of_contents: false
keywords:
  - logging_configurations_list_only
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

Lists <code>logging_configurations</code> in a region or regions, for all properties use <a href="/providers/aws/serviceName/logging_configurations/"><code>logging_configurations</code></a>

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>logging_configurations_list_only</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>A WAFv2 Logging Configuration Resource Provider</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="aws.wafv2.logging_configurations_list_only" /></td></tr>
</tbody></table>

## Fields
<table><tbody><tr><th>Name</th><th>Datatype</th><th>Description</th></tr><tr><td><CopyableCode code="resource_arn" /></td><td><code>string</code></td><td>The Amazon Resource Name (ARN) of the web ACL that you want to associate with LogDestinationConfigs.</td></tr>
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
Lists all <code>logging_configurations</code> in a region.
```sql
SELECT
region,
resource_arn
FROM aws.wafv2.logging_configurations_list_only
;
```


## Permissions

For permissions required to operate on the <code>logging_configurations_list_only</code> resource, see <a href="/providers/aws/wafv2/logging_configurations/#permissions"><code>logging_configurations</code></a>

