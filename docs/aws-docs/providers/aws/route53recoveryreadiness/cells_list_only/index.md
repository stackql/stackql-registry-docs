---
title: cells_list_only
hide_title: false
hide_table_of_contents: false
keywords:
  - cells_list_only
  - route53recoveryreadiness
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

Lists <code>cells</code> in a region or regions, for all properties use <a href="/providers/aws/serviceName/cells/"><code>cells</code></a>

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>cells_list_only</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>The API Schema for AWS Route53 Recovery Readiness Cells.</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="aws.route53recoveryreadiness.cells_list_only" /></td></tr>
</tbody></table>

## Fields
<table><tbody><tr><th>Name</th><th>Datatype</th><th>Description</th></tr><tr><td><CopyableCode code="cell_name" /></td><td><code>string</code></td><td>The name of the cell to create.</td></tr>
<tr><td><CopyableCode code="cell_arn" /></td><td><code>string</code></td><td>The Amazon Resource Name (ARN) of the cell.</td></tr>
<tr><td><CopyableCode code="cells" /></td><td><code>array</code></td><td>A list of cell Amazon Resource Names (ARNs) contained within this cell, for use in nested cells. For example, Availability Zones within specific Regions.</td></tr>
<tr><td><CopyableCode code="parent_readiness_scopes" /></td><td><code>array</code></td><td>The readiness scope for the cell, which can be a cell Amazon Resource Name (ARN) or a recovery group ARN. This is a list but currently can have only one element.</td></tr>
<tr><td><CopyableCode code="tags" /></td><td><code>array</code></td><td>A collection of tags associated with a resource</td></tr>
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
Lists all <code>cells</code> in a region.
```sql
SELECT
region,
cell_name
FROM aws.route53recoveryreadiness.cells_list_only
WHERE region = 'us-east-1';
```


## Permissions

For permissions required to operate on the <code>cells_list_only</code> resource, see <a href="/providers/aws/route53recoveryreadiness/cells/#permissions"><code>cells</code></a>


