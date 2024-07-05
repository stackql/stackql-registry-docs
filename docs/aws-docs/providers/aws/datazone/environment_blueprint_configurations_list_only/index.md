---
title: environment_blueprint_configurations_list_only
hide_title: false
hide_table_of_contents: false
keywords:
  - environment_blueprint_configurations_list_only
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
import Tabs from '@theme/Tabs';
import TabItem from '@theme/TabItem';

Lists <code>environment_blueprint_configurations</code> in a region or regions, for all properties use <a href="/providers/aws/serviceName/environment_blueprint_configurations/"><code>environment_blueprint_configurations</code></a>

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>environment_blueprint_configurations_list_only</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>Definition of AWS::DataZone::EnvironmentBlueprintConfiguration Resource Type</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="aws.datazone.environment_blueprint_configurations_list_only" /></td></tr>
</tbody></table>

## Fields
<table><tbody><tr><th>Name</th><th>Datatype</th><th>Description</th></tr><tr><td><CopyableCode code="regional_parameters" /></td><td><code>array</code></td><td></td></tr>
<tr><td><CopyableCode code="provisioning_role_arn" /></td><td><code>string</code></td><td></td></tr>
<tr><td><CopyableCode code="domain_id" /></td><td><code>string</code></td><td></td></tr>
<tr><td><CopyableCode code="created_at" /></td><td><code>string</code></td><td></td></tr>
<tr><td><CopyableCode code="enabled_regions" /></td><td><code>array</code></td><td></td></tr>
<tr><td><CopyableCode code="environment_blueprint_identifier" /></td><td><code>string</code></td><td></td></tr>
<tr><td><CopyableCode code="environment_blueprint_id" /></td><td><code>string</code></td><td></td></tr>
<tr><td><CopyableCode code="updated_at" /></td><td><code>string</code></td><td></td></tr>
<tr><td><CopyableCode code="domain_identifier" /></td><td><code>string</code></td><td></td></tr>
<tr><td><CopyableCode code="manage_access_role_arn" /></td><td><code>string</code></td><td></td></tr>
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
Lists all <code>environment_blueprint_configurations</code> in a region.
```sql
SELECT
region,
domain_id,
environment_blueprint_id
FROM aws.datazone.environment_blueprint_configurations_list_only
WHERE region = 'us-east-1';
```


## Permissions

For permissions required to operate on the <code>environment_blueprint_configurations_list_only</code> resource, see <a href="/providers/aws/datazone/environment_blueprint_configurations/#permissions"><code>environment_blueprint_configurations</code></a>


