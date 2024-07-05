---
title: environment_tags
hide_title: false
hide_table_of_contents: false
keywords:
  - environment_tags
  - workspacesthinclient
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

Expands all tag keys and values for <code>environments</code> in a region

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>environment_tags</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>Resource type definition for AWS::WorkSpacesThinClient::Environment.</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="aws.workspacesthinclient.environment_tags" /></td></tr>
</tbody></table>

## Fields
<table><tbody><tr><th>Name</th><th>Datatype</th><th>Description</th></tr><tr><td><CopyableCode code="id" /></td><td><code>string</code></td><td>Unique identifier of the environment.</td></tr>
<tr><td><CopyableCode code="name" /></td><td><code>string</code></td><td>The name of the environment.</td></tr>
<tr><td><CopyableCode code="desktop_arn" /></td><td><code>string</code></td><td>The Amazon Resource Name (ARN) of the desktop to stream from Amazon WorkSpaces, WorkSpaces Web, or AppStream 2.0.</td></tr>
<tr><td><CopyableCode code="desktop_endpoint" /></td><td><code>string</code></td><td>The URL for the identity provider login (only for environments that use AppStream 2.0).</td></tr>
<tr><td><CopyableCode code="desktop_type" /></td><td><code>string</code></td><td>The type of VDI.</td></tr>
<tr><td><CopyableCode code="activation_code" /></td><td><code>string</code></td><td>Activation code for devices associated with environment.</td></tr>
<tr><td><CopyableCode code="registered_devices_count" /></td><td><code>integer</code></td><td>Number of devices registered to the environment.</td></tr>
<tr><td><CopyableCode code="software_set_update_schedule" /></td><td><code>string</code></td><td>An option to define if software updates should be applied within a maintenance window.</td></tr>
<tr><td><CopyableCode code="maintenance_window" /></td><td><code>object</code></td><td>A specification for a time window to apply software updates.</td></tr>
<tr><td><CopyableCode code="software_set_update_mode" /></td><td><code>string</code></td><td>An option to define which software updates to apply.</td></tr>
<tr><td><CopyableCode code="desired_software_set_id" /></td><td><code>string</code></td><td>The ID of the software set to apply.</td></tr>
<tr><td><CopyableCode code="pending_software_set_id" /></td><td><code>string</code></td><td>The ID of the software set that is pending to be installed.</td></tr>
<tr><td><CopyableCode code="pending_software_set_version" /></td><td><code>string</code></td><td>The version of the software set that is pending to be installed.</td></tr>
<tr><td><CopyableCode code="software_set_compliance_status" /></td><td><code>string</code></td><td>Describes if the software currently installed on all devices in the environment is a supported version.</td></tr>
<tr><td><CopyableCode code="created_at" /></td><td><code>string</code></td><td>The timestamp in unix epoch format when environment was created.</td></tr>
<tr><td><CopyableCode code="updated_at" /></td><td><code>string</code></td><td>The timestamp in unix epoch format when environment was last updated.</td></tr>
<tr><td><CopyableCode code="arn" /></td><td><code>string</code></td><td>The environment ARN.</td></tr>
<tr><td><CopyableCode code="kms_key_arn" /></td><td><code>string</code></td><td>The Amazon Resource Name (ARN) of the AWS Key Management Service key used to encrypt the environment.</td></tr>
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
Expands tags for all <code>environments</code> in a region.
```sql
SELECT
region,
id,
name,
desktop_arn,
desktop_endpoint,
desktop_type,
activation_code,
registered_devices_count,
software_set_update_schedule,
maintenance_window,
software_set_update_mode,
desired_software_set_id,
pending_software_set_id,
pending_software_set_version,
software_set_compliance_status,
created_at,
updated_at,
arn,
kms_key_arn,
tag_key,
tag_value
FROM aws.workspacesthinclient.environment_tags
WHERE region = 'us-east-1';
```


## Permissions

For permissions required to operate on the <code>environment_tags</code> resource, see <a href="/providers/aws/workspacesthinclient/environments/#permissions"><code>environments</code></a>


