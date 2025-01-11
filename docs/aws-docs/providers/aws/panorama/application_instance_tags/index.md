---
title: application_instance_tags
hide_title: false
hide_table_of_contents: false
keywords:
  - application_instance_tags
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

Expands all tag keys and values for <code>application_instances</code> in a region

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>application_instance_tags</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>Creates an application instance and deploys it to a device.</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="aws.panorama.application_instance_tags" /></td></tr>
</tbody></table>

## Fields
<table><tbody><tr><th>Name</th><th>Datatype</th><th>Description</th></tr><tr><td><CopyableCode code="default_runtime_context_device_name" /></td><td><code>string</code></td><td></td></tr>
<tr><td><CopyableCode code="status" /></td><td><code>string</code></td><td></td></tr>
<tr><td><CopyableCode code="default_runtime_context_device" /></td><td><code>string</code></td><td>The device's ID.</td></tr>
<tr><td><CopyableCode code="description" /></td><td><code>string</code></td><td>A description for the application instance.</td></tr>
<tr><td><CopyableCode code="application_instance_id_to_replace" /></td><td><code>string</code></td><td>The ID of an application instance to replace with the new instance.</td></tr>
<tr><td><CopyableCode code="created_time" /></td><td><code>integer</code></td><td></td></tr>
<tr><td><CopyableCode code="health_status" /></td><td><code>string</code></td><td></td></tr>
<tr><td><CopyableCode code="manifest_overrides_payload" /></td><td><code>object</code></td><td>Setting overrides for the application manifest.</td></tr>
<tr><td><CopyableCode code="last_updated_time" /></td><td><code>integer</code></td><td></td></tr>
<tr><td><CopyableCode code="runtime_role_arn" /></td><td><code>string</code></td><td>The ARN of a runtime role for the application instance.</td></tr>
<tr><td><CopyableCode code="name" /></td><td><code>string</code></td><td>A name for the application instance.</td></tr>
<tr><td><CopyableCode code="application_instance_id" /></td><td><code>string</code></td><td></td></tr>
<tr><td><CopyableCode code="status_description" /></td><td><code>string</code></td><td></td></tr>
<tr><td><CopyableCode code="manifest_payload" /></td><td><code>object</code></td><td>The application's manifest document.</td></tr>
<tr><td><CopyableCode code="arn" /></td><td><code>string</code></td><td></td></tr>
<tr><td><CopyableCode code="tag_key" /></td><td><code>string</code></td><td>Tag key.</td></tr>
<tr><td><CopyableCode code="tag_value" /></td><td><code>string</code></td><td>Tag value.</td></tr>
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
Expands tags for all <code>application_instances</code> in a region.
```sql
SELECT
region,
default_runtime_context_device_name,
status,
default_runtime_context_device,
description,
application_instance_id_to_replace,
created_time,
health_status,
manifest_overrides_payload,
last_updated_time,
runtime_role_arn,
name,
application_instance_id,
status_description,
manifest_payload,
arn,
tag_key,
tag_value
FROM aws.panorama.application_instance_tags
WHERE region = 'us-east-1';
```


## Permissions

For permissions required to operate on the <code>application_instance_tags</code> resource, see <a href="/providers/aws/panorama/application_instances/#permissions"><code>application_instances</code></a>

