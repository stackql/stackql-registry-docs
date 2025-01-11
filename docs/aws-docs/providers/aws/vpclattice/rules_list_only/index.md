---
title: rules_list_only
hide_title: false
hide_table_of_contents: false
keywords:
  - rules_list_only
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

Lists <code>rules</code> in a region or regions, for all properties use <a href="/providers/aws/serviceName/rules/"><code>rules</code></a>

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>rules_list_only</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>Creates a listener rule. Each listener has a default rule for checking connection requests, but you can define additional rules. Each rule consists of a priority, one or more actions, and one or more conditions.</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="aws.vpclattice.rules_list_only" /></td></tr>
</tbody></table>

## Fields
<table><tbody><tr><th>Name</th><th>Datatype</th><th>Description</th></tr><tr><td><CopyableCode code="arn" /></td><td><code>string</code></td><td></td></tr>
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
Lists all <code>rules</code> in a region.
```sql
SELECT
region,
arn
FROM aws.vpclattice.rules_list_only
WHERE region = 'us-east-1';
```


## Permissions

For permissions required to operate on the <code>rules_list_only</code> resource, see <a href="/providers/aws/vpclattice/rules/#permissions"><code>rules</code></a>

