---
title: virtualmfa_device_tags
hide_title: false
hide_table_of_contents: false
keywords:
  - virtualmfa_device_tags
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

Expands all tag keys and values for <code>virtualmfa_devices</code> in a region

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>virtualmfa_device_tags</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>Resource Type definition for AWS::IAM::VirtualMFADevice</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="aws.iam.virtualmfa_device_tags" /></td></tr>
</tbody></table>

## Fields
<table><tbody><tr><th>Name</th><th>Datatype</th><th>Description</th></tr><tr><td><CopyableCode code="virtual_mfa_device_name" /></td><td><code>string</code></td><td></td></tr>
<tr><td><CopyableCode code="path" /></td><td><code>string</code></td><td></td></tr>
<tr><td><CopyableCode code="serial_number" /></td><td><code>string</code></td><td></td></tr>
<tr><td><CopyableCode code="users" /></td><td><code>array</code></td><td></td></tr>
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
Expands tags for all <code>virtualmfa_devices</code> in a region.
```sql
SELECT
region,
virtual_mfa_device_name,
path,
serial_number,
users,
tag_key,
tag_value
FROM aws.iam.virtualmfa_device_tags
;
```


## Permissions

For permissions required to operate on the <code>virtualmfa_device_tags</code> resource, see <a href="/providers/aws/iam/virtualmfa_devices/#permissions"><code>virtualmfa_devices</code></a>

