---
title: response_plans_list_only
hide_title: false
hide_table_of_contents: false
keywords:
  - response_plans_list_only
  - ssmincidents
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

Lists <code>response_plans</code> in a region or regions, for all properties use <a href="/providers/aws/serviceName/response_plans/"><code>response_plans</code></a>

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>response_plans_list_only</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>Resource type definition for AWS::SSMIncidents::ResponsePlan</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="aws.ssmincidents.response_plans_list_only" /></td></tr>
</tbody></table>

## Fields
<table><tbody><tr><th>Name</th><th>Datatype</th><th>Description</th></tr><tr><td><CopyableCode code="arn" /></td><td><code>string</code></td><td>The ARN of the response plan.</td></tr>
<tr><td><CopyableCode code="name" /></td><td><code>string</code></td><td>The name of the response plan.</td></tr>
<tr><td><CopyableCode code="display_name" /></td><td><code>string</code></td><td>The display name of the response plan.</td></tr>
<tr><td><CopyableCode code="chat_channel" /></td><td><code>object</code></td><td>The chat channel configuration.</td></tr>
<tr><td><CopyableCode code="engagements" /></td><td><code>array</code></td><td>The list of engagements to use.</td></tr>
<tr><td><CopyableCode code="actions" /></td><td><code>array</code></td><td>The list of actions.</td></tr>
<tr><td><CopyableCode code="integrations" /></td><td><code>array</code></td><td>The list of integrations.</td></tr>
<tr><td><CopyableCode code="tags" /></td><td><code>array</code></td><td>The tags to apply to the response plan.</td></tr>
<tr><td><CopyableCode code="incident_template" /></td><td><code>object</code></td><td>The incident template configuration.</td></tr>
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
Lists all <code>response_plans</code> in a region.
```sql
SELECT
region,
arn
FROM aws.ssmincidents.response_plans_list_only
WHERE region = 'us-east-1';
```


## Permissions

For permissions required to operate on the <code>response_plans_list_only</code> resource, see <a href="/providers/aws/ssmincidents/response_plans/#permissions"><code>response_plans</code></a>


