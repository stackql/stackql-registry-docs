---
title: state_machine_aliases_list_only
hide_title: false
hide_table_of_contents: false
keywords:
  - state_machine_aliases_list_only
  - stepfunctions
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

Lists <code>state_machine_aliases</code> in a region or regions, for all properties use <a href="/providers/aws/serviceName/state_machine_aliases/"><code>state_machine_aliases</code></a>

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>state_machine_aliases_list_only</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>Resource schema for StateMachineAlias</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="aws.stepfunctions.state_machine_aliases_list_only" /></td></tr>
</tbody></table>

## Fields
<table><tbody><tr><th>Name</th><th>Datatype</th><th>Description</th></tr><tr><td><CopyableCode code="arn" /></td><td><code>string</code></td><td>The ARN of the alias.</td></tr>
<tr><td><CopyableCode code="name" /></td><td><code>string</code></td><td>The alias name.</td></tr>
<tr><td><CopyableCode code="description" /></td><td><code>string</code></td><td>An optional description of the alias.</td></tr>
<tr><td><CopyableCode code="routing_configuration" /></td><td><code>array</code></td><td>The routing configuration of the alias. One or two versions can be mapped to an alias to split StartExecution requests of the same state machine.</td></tr>
<tr><td><CopyableCode code="deployment_preference" /></td><td><code>object</code></td><td>The settings to enable gradual state machine deployments.</td></tr>
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
Lists all <code>state_machine_aliases</code> in a region.
```sql
SELECT
region,
arn
FROM aws.stepfunctions.state_machine_aliases_list_only
WHERE region = 'us-east-1';
```


## Permissions

For permissions required to operate on the <code>state_machine_aliases_list_only</code> resource, see <a href="/providers/aws/stepfunctions/state_machine_aliases/#permissions"><code>state_machine_aliases</code></a>


