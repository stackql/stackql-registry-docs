---
title: target_account_configurations_list_only
hide_title: false
hide_table_of_contents: false
keywords:
  - target_account_configurations_list_only
  - fis
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

Lists <code>target_account_configurations</code> in a region or regions, for all properties use <a href="/providers/aws/serviceName/target_account_configurations/"><code>target_account_configurations</code></a>

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>target_account_configurations_list_only</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>Resource schema for AWS::FIS::TargetAccountConfiguration</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="aws.fis.target_account_configurations_list_only" /></td></tr>
</tbody></table>

## Fields
<table><tbody><tr><th>Name</th><th>Datatype</th><th>Description</th></tr><tr><td><CopyableCode code="experiment_template_id" /></td><td><code>string</code></td><td>The ID of the experiment template.</td></tr>
<tr><td><CopyableCode code="account_id" /></td><td><code>string</code></td><td>The AWS account ID of the target account.</td></tr>
<tr><td><CopyableCode code="role_arn" /></td><td><code>string</code></td><td>The Amazon Resource Name (ARN) of an IAM role for the target account.</td></tr>
<tr><td><CopyableCode code="description" /></td><td><code>string</code></td><td>The description of the target account.</td></tr>
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
Lists all <code>target_account_configurations</code> in a region.
```sql
SELECT
region,
experiment_template_id,
account_id
FROM aws.fis.target_account_configurations_list_only
WHERE region = 'us-east-1';
```


## Permissions

For permissions required to operate on the <code>target_account_configurations_list_only</code> resource, see <a href="/providers/aws/fis/target_account_configurations/#permissions"><code>target_account_configurations</code></a>


