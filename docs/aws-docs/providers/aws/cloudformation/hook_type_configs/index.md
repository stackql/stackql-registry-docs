---
title: hook_type_configs
hide_title: false
hide_table_of_contents: false
keywords:
  - hook_type_configs
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

Used to retrieve a list of <code>hook_type_configs</code> in a region or create a <code>hook_type_configs</code> resource, use <code>hook_type_config</code> to operate on an individual resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>hook_type_configs</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>Specifies the configuration data for a registered hook in CloudFormation Registry.</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="aws.cloudformation.hook_type_configs" /></td></tr>
</tbody></table>

## Fields
<table><tbody>
<tr><th>Name</th><th>Datatype</th><th>Description</th></tr>
<tr><td><CopyableCode code="configuration_arn" /></td><td><code>string</code></td><td>The Amazon Resource Name (ARN) for the configuration data, in this account and region.</td></tr>
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
configuration_arn
FROM aws.cloudformation.hook_type_configs
WHERE region = 'us-east-1'
```

## Permissions

To operate on the <code>hook_type_configs</code> resource, the following permissions are required:

### Create
```json
cloudformation:SetTypeConfiguration
```

### List
```json
cloudformation:ListTypes,
cloudformation:BatchDescribeTypeConfigurations
```

