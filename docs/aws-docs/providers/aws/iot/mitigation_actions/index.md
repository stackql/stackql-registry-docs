---
title: mitigation_actions
hide_title: false
hide_table_of_contents: false
keywords:
  - mitigation_actions
  - iot
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

Used to retrieve a list of <code>mitigation_actions</code> in a region or create a <code>mitigation_actions</code> resource, use <code>mitigation_action</code> to operate on an individual resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>mitigation_actions</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>Mitigation actions can be used to take actions to mitigate issues that were found in an Audit finding or Detect violation.</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="aws.iot.mitigation_actions" /></td></tr>
</tbody></table>

## Fields
<table><tbody>
<tr><th>Name</th><th>Datatype</th><th>Description</th></tr>
<tr><td><CopyableCode code="action_name" /></td><td><code>string</code></td><td>A unique identifier for the mitigation action.</td></tr>
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
action_name
FROM aws.iot.mitigation_actions
WHERE region = 'us-east-1'
```

## Permissions

To operate on the <code>mitigation_actions</code> resource, the following permissions are required:

### Create
```json
iot:CreateMitigationAction,
iot:DescribeMitigationAction,
iot:TagResource,
iam:PassRole
```

### List
```json
iot:ListMitigationActions
```

