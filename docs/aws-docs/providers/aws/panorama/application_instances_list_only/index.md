---
title: application_instances_list_only
hide_title: false
hide_table_of_contents: false
keywords:
  - application_instances_list_only
  - panorama
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

Lists <code>application_instances</code> in a region or regions, for all properties use <a href="/providers/aws/serviceName/application_instances/"><code>application_instances</code></a>

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>application_instances_list_only</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>Schema for ApplicationInstance CloudFormation Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="aws.panorama.application_instances_list_only" /></td></tr>
</tbody></table>

## Fields
<table><tbody><tr><th>Name</th><th>Datatype</th><th>Description</th></tr><tr><td><CopyableCode code="default_runtime_context_device_name" /></td><td><code>string</code></td><td></td></tr>
<tr><td><CopyableCode code="status" /></td><td><code>string</code></td><td></td></tr>
<tr><td><CopyableCode code="default_runtime_context_device" /></td><td><code>string</code></td><td></td></tr>
<tr><td><CopyableCode code="description" /></td><td><code>string</code></td><td></td></tr>
<tr><td><CopyableCode code="application_instance_id_to_replace" /></td><td><code>string</code></td><td></td></tr>
<tr><td><CopyableCode code="created_time" /></td><td><code>integer</code></td><td></td></tr>
<tr><td><CopyableCode code="health_status" /></td><td><code>string</code></td><td></td></tr>
<tr><td><CopyableCode code="manifest_overrides_payload" /></td><td><code>object</code></td><td></td></tr>
<tr><td><CopyableCode code="last_updated_time" /></td><td><code>integer</code></td><td></td></tr>
<tr><td><CopyableCode code="runtime_role_arn" /></td><td><code>string</code></td><td></td></tr>
<tr><td><CopyableCode code="name" /></td><td><code>string</code></td><td></td></tr>
<tr><td><CopyableCode code="application_instance_id" /></td><td><code>string</code></td><td></td></tr>
<tr><td><CopyableCode code="status_description" /></td><td><code>string</code></td><td></td></tr>
<tr><td><CopyableCode code="manifest_payload" /></td><td><code>object</code></td><td></td></tr>
<tr><td><CopyableCode code="arn" /></td><td><code>string</code></td><td></td></tr>
<tr><td><CopyableCode code="tags" /></td><td><code>array</code></td><td></td></tr>
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
Lists all <code>application_instances</code> in a region.
```sql
SELECT
region,
application_instance_id
FROM aws.panorama.application_instances_list_only
WHERE region = 'us-east-1';
```


## Permissions

For permissions required to operate on the <code>application_instances_list_only</code> resource, see <a href="/providers/aws/panorama/application_instances/#permissions"><code>application_instances</code></a>


