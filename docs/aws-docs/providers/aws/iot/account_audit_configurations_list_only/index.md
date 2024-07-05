---
title: account_audit_configurations_list_only
hide_title: false
hide_table_of_contents: false
keywords:
  - account_audit_configurations_list_only
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
import Tabs from '@theme/Tabs';
import TabItem from '@theme/TabItem';

Lists <code>account_audit_configurations</code> in a region or regions, for all properties use <a href="/providers/aws/serviceName/account_audit_configurations/"><code>account_audit_configurations</code></a>

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>account_audit_configurations_list_only</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>Configures the Device Defender audit settings for this account. Settings include how audit notifications are sent and which audit checks are enabled or disabled.</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="aws.iot.account_audit_configurations_list_only" /></td></tr>
</tbody></table>

## Fields
<table><tbody><tr><th>Name</th><th>Datatype</th><th>Description</th></tr><tr><td><CopyableCode code="account_id" /></td><td><code>string</code></td><td>Your 12-digit account ID (used as the primary identifier for the CloudFormation resource).</td></tr>
<tr><td><CopyableCode code="audit_check_configurations" /></td><td><code>object</code></td><td>Specifies which audit checks are enabled and disabled for this account.</td></tr>
<tr><td><CopyableCode code="audit_notification_target_configurations" /></td><td><code>object</code></td><td>Information about the targets to which audit notifications are sent.</td></tr>
<tr><td><CopyableCode code="role_arn" /></td><td><code>string</code></td><td>The ARN of the role that grants permission to AWS IoT to access information about your devices, policies, certificates and other items as required when performing an audit.</td></tr>
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
Lists all <code>account_audit_configurations</code> in a region.
```sql
SELECT
region,
account_id
FROM aws.iot.account_audit_configurations_list_only
WHERE region = 'us-east-1';
```


## Permissions

For permissions required to operate on the <code>account_audit_configurations_list_only</code> resource, see <a href="/providers/aws/iot/account_audit_configurations/#permissions"><code>account_audit_configurations</code></a>


