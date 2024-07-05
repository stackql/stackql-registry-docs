---
title: environments_list_only
hide_title: false
hide_table_of_contents: false
keywords:
  - environments_list_only
  - m2
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

Lists <code>environments</code> in a region or regions, for all properties use <a href="/providers/aws/serviceName/environments/"><code>environments</code></a>

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>environments_list_only</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>Represents a runtime environment that can run migrated mainframe applications.</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="aws.m2.environments_list_only" /></td></tr>
</tbody></table>

## Fields
<table><tbody><tr><th>Name</th><th>Datatype</th><th>Description</th></tr><tr><td><CopyableCode code="description" /></td><td><code>string</code></td><td>The description of the environment.</td></tr>
<tr><td><CopyableCode code="engine_type" /></td><td><code>string</code></td><td>The target platform for the environment.</td></tr>
<tr><td><CopyableCode code="engine_version" /></td><td><code>string</code></td><td>The version of the runtime engine for the environment.</td></tr>
<tr><td><CopyableCode code="environment_arn" /></td><td><code>string</code></td><td>The Amazon Resource Name (ARN) of the runtime environment.</td></tr>
<tr><td><CopyableCode code="environment_id" /></td><td><code>string</code></td><td>The unique identifier of the environment.</td></tr>
<tr><td><CopyableCode code="high_availability_config" /></td><td><code>object</code></td><td>Defines the details of a high availability configuration.</td></tr>
<tr><td><CopyableCode code="instance_type" /></td><td><code>string</code></td><td>The type of instance underlying the environment.</td></tr>
<tr><td><CopyableCode code="kms_key_id" /></td><td><code>string</code></td><td>The ID or the Amazon Resource Name (ARN) of the customer managed KMS Key used for encrypting environment-related resources.</td></tr>
<tr><td><CopyableCode code="name" /></td><td><code>string</code></td><td>The name of the environment.</td></tr>
<tr><td><CopyableCode code="preferred_maintenance_window" /></td><td><code>string</code></td><td>Configures a desired maintenance window for the environment. If you do not provide a value, a random system-generated value will be assigned.</td></tr>
<tr><td><CopyableCode code="publicly_accessible" /></td><td><code>boolean</code></td><td>Specifies whether the environment is publicly accessible.</td></tr>
<tr><td><CopyableCode code="security_group_ids" /></td><td><code>array</code></td><td>The list of security groups for the VPC associated with this environment.</td></tr>
<tr><td><CopyableCode code="storage_configurations" /></td><td><code>array</code></td><td>The storage configurations defined for the runtime environment.</td></tr>
<tr><td><CopyableCode code="subnet_ids" /></td><td><code>array</code></td><td>The unique identifiers of the subnets assigned to this runtime environment.</td></tr>
<tr><td><CopyableCode code="tags" /></td><td><code>object</code></td><td>Tags associated to this environment.</td></tr>
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
Lists all <code>environments</code> in a region.
```sql
SELECT
region,
environment_arn
FROM aws.m2.environments_list_only
WHERE region = 'us-east-1';
```


## Permissions

For permissions required to operate on the <code>environments_list_only</code> resource, see <a href="/providers/aws/m2/environments/#permissions"><code>environments</code></a>


