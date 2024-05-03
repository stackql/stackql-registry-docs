---
title: subscription_targets
hide_title: false
hide_table_of_contents: false
keywords:
  - subscription_targets
  - datazone
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

Used to retrieve a list of <code>subscription_targets</code> in a region or create a <code>subscription_targets</code> resource, use <code>subscription_target</code> to operate on an individual resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>subscription_targets</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>Subscription targets enables one to access the data to which you have subscribed in your projects.</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="aws.datazone.subscription_targets" /></td></tr>
</tbody></table>

## Fields
<table><tbody>
<tr><th>Name</th><th>Datatype</th><th>Description</th></tr>
<tr><td><CopyableCode code="domain_id" /></td><td><code>string</code></td><td>The ID of the Amazon DataZone domain in which subscription target is created.</td></tr>
<tr><td><CopyableCode code="environment_id" /></td><td><code>string</code></td><td>The ID of the environment in which subscription target is created.</td></tr>
<tr><td><CopyableCode code="id" /></td><td><code>string</code></td><td>The ID of the subscription target.</td></tr>
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
    <td><CopyableCode code="create_resource" /></td>
    <td><code>INSERT</code></td>
    <td><CopyableCode code="data__DesiredState, region" /></td>
  </tr>
  <tr>
    <td><CopyableCode code="list_resource" /></td>
    <td><code>SELECT</code></td>
    <td><CopyableCode code="region" /></td>
  </tr>
</tbody></table>

## `SELECT` Example
```sql
SELECT
region,
domain_id,
environment_id,
id
FROM aws.datazone.subscription_targets
WHERE region = 'us-east-1'
```

## Permissions

To operate on the <code>subscription_targets</code> resource, the following permissions are required:

### Create
```json
datazone:CreateSubscriptionTarget,
datazone:GetSubscriptionTarget,
iam:PassRole
```

### List
```json
datazone:ListSubscriptionTargets
```

