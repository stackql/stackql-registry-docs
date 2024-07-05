---
title: hook_type_configs_list_only
hide_title: false
hide_table_of_contents: false
keywords:
  - hook_type_configs_list_only
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
import Tabs from '@theme/Tabs';
import TabItem from '@theme/TabItem';

Lists <code>hook_type_configs</code> in a region or regions, for all properties use <a href="/providers/aws/serviceName/hook_type_configs/"><code>hook_type_configs</code></a>

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>hook_type_configs_list_only</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>Specifies the configuration data for a registered hook in CloudFormation Registry.</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="aws.cloudformation.hook_type_configs_list_only" /></td></tr>
</tbody></table>

## Fields
<table><tbody><tr><th>Name</th><th>Datatype</th><th>Description</th></tr><tr><td><CopyableCode code="type_arn" /></td><td><code>string</code></td><td>The Amazon Resource Name (ARN) of the type without version number.</td></tr>
<tr><td><CopyableCode code="type_name" /></td><td><code>string</code></td><td>The name of the type being registered.<br />We recommend that type names adhere to the following pattern: company_or_organization::service::type.</td></tr>
<tr><td><CopyableCode code="configuration_arn" /></td><td><code>string</code></td><td>The Amazon Resource Name (ARN) for the configuration data, in this account and region.</td></tr>
<tr><td><CopyableCode code="configuration" /></td><td><code>string</code></td><td>The configuration data for the extension, in this account and region.</td></tr>
<tr><td><CopyableCode code="configuration_alias" /></td><td><code>string</code></td><td>An alias by which to refer to this extension configuration data.</td></tr>
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
Lists all <code>hook_type_configs</code> in a region.
```sql
SELECT
region,
configuration_arn
FROM aws.cloudformation.hook_type_configs_list_only
WHERE region = 'us-east-1';
```


## Permissions

For permissions required to operate on the <code>hook_type_configs_list_only</code> resource, see <a href="/providers/aws/cloudformation/hook_type_configs/#permissions"><code>hook_type_configs</code></a>


