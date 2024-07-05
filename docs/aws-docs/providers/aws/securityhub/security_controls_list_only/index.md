---
title: security_controls_list_only
hide_title: false
hide_table_of_contents: false
keywords:
  - security_controls_list_only
  - securityhub
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

Lists <code>security_controls</code> in a region or regions, for all properties use <a href="/providers/aws/serviceName/security_controls/"><code>security_controls</code></a>

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>security_controls_list_only</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>A security control in Security Hub describes a security best practice related to a specific resource.</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="aws.securityhub.security_controls_list_only" /></td></tr>
</tbody></table>

## Fields
<table><tbody><tr><th>Name</th><th>Datatype</th><th>Description</th></tr><tr><td><CopyableCode code="security_control_id" /></td><td><code>string</code></td><td>The unique identifier of a security control across standards. Values for this field typically consist of an AWS service name and a number, such as APIGateway.3.</td></tr>
<tr><td><CopyableCode code="security_control_arn" /></td><td><code>string</code></td><td>The Amazon Resource Name (ARN) for a security control across standards, such as `arn:aws:securityhub:eu-central-1:123456789012:security-control/S3.1`. This parameter doesn't mention a specific standard.</td></tr>
<tr><td><CopyableCode code="last_update_reason" /></td><td><code>string</code></td><td>The most recent reason for updating the customizable properties of a security control. This differs from the UpdateReason field of the BatchUpdateStandardsControlAssociations API, which tracks the reason for updating the enablement status of a control. This field accepts alphanumeric characters in addition to white spaces, dashes, and underscores.</td></tr>
<tr><td><CopyableCode code="parameters" /></td><td><code>object</code></td><td>An object that identifies the name of a control parameter, its current value, and whether it has been customized.</td></tr>
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
Lists all <code>security_controls</code> in a region.
```sql
SELECT
region,
security_control_id
FROM aws.securityhub.security_controls_list_only
WHERE region = 'us-east-1';
```


## Permissions

For permissions required to operate on the <code>security_controls_list_only</code> resource, see <a href="/providers/aws/securityhub/security_controls/#permissions"><code>security_controls</code></a>


