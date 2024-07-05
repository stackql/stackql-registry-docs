---
title: virtualmfa_devices_list_only
hide_title: false
hide_table_of_contents: false
keywords:
  - virtualmfa_devices_list_only
  - iam
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

Lists <code>virtualmfa_devices</code> in a region or regions, for all properties use <a href="/providers/aws/serviceName/virtualmfa_devices/"><code>virtualmfa_devices</code></a>

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>virtualmfa_devices_list_only</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>Resource Type definition for AWS::IAM::VirtualMFADevice</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="aws.iam.virtualmfa_devices_list_only" /></td></tr>
</tbody></table>

## Fields
<table><tbody><tr><th>Name</th><th>Datatype</th><th>Description</th></tr><tr><td><CopyableCode code="virtual_mfa_device_name" /></td><td><code>string</code></td><td></td></tr>
<tr><td><CopyableCode code="path" /></td><td><code>string</code></td><td></td></tr>
<tr><td><CopyableCode code="serial_number" /></td><td><code>string</code></td><td></td></tr>
<tr><td><CopyableCode code="users" /></td><td><code>array</code></td><td></td></tr>
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
Lists all <code>virtualmfa_devices</code> in a region.
```sql
SELECT
region,
serial_number
FROM aws.iam.virtualmfa_devices_list_only
;
```


## Permissions

For permissions required to operate on the <code>virtualmfa_devices_list_only</code> resource, see <a href="/providers/aws/iam/virtualmfa_devices/#permissions"><code>virtualmfa_devices</code></a>


