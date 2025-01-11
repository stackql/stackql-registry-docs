---
title: user_settings_tags
hide_title: false
hide_table_of_contents: false
keywords:
  - user_settings_tags
  - workspacesweb
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

Expands all tag keys and values for <code>user_settings</code> in a region

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>user_settings_tags</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>Definition of AWS::WorkSpacesWeb::UserSettings Resource Type</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="aws.workspacesweb.user_settings_tags" /></td></tr>
</tbody></table>

## Fields
<table><tbody><tr><th>Name</th><th>Datatype</th><th>Description</th></tr><tr><td><CopyableCode code="additional_encryption_context" /></td><td><code>object</code></td><td></td></tr>
<tr><td><CopyableCode code="associated_portal_arns" /></td><td><code>array</code></td><td></td></tr>
<tr><td><CopyableCode code="cookie_synchronization_configuration" /></td><td><code>object</code></td><td></td></tr>
<tr><td><CopyableCode code="copy_allowed" /></td><td><code>string</code></td><td></td></tr>
<tr><td><CopyableCode code="customer_managed_key" /></td><td><code>string</code></td><td></td></tr>
<tr><td><CopyableCode code="disconnect_timeout_in_minutes" /></td><td><code>number</code></td><td></td></tr>
<tr><td><CopyableCode code="download_allowed" /></td><td><code>string</code></td><td></td></tr>
<tr><td><CopyableCode code="idle_disconnect_timeout_in_minutes" /></td><td><code>number</code></td><td></td></tr>
<tr><td><CopyableCode code="paste_allowed" /></td><td><code>string</code></td><td></td></tr>
<tr><td><CopyableCode code="print_allowed" /></td><td><code>string</code></td><td></td></tr>
<tr><td><CopyableCode code="upload_allowed" /></td><td><code>string</code></td><td></td></tr>
<tr><td><CopyableCode code="user_settings_arn" /></td><td><code>string</code></td><td></td></tr>
<tr><td><CopyableCode code="deep_link_allowed" /></td><td><code>string</code></td><td></td></tr>
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
Expands tags for all <code>user_settings</code> in a region.
```sql
SELECT
region,
additional_encryption_context,
associated_portal_arns,
cookie_synchronization_configuration,
copy_allowed,
customer_managed_key,
disconnect_timeout_in_minutes,
download_allowed,
idle_disconnect_timeout_in_minutes,
paste_allowed,
print_allowed,
upload_allowed,
user_settings_arn,
deep_link_allowed,
tag_key,
tag_value
FROM aws.workspacesweb.user_settings_tags
WHERE region = 'us-east-1';
```


## Permissions

For permissions required to operate on the <code>user_settings_tags</code> resource, see <a href="/providers/aws/workspacesweb/user_settings/#permissions"><code>user_settings</code></a>

