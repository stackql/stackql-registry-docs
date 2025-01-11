---
title: portal_tags
hide_title: false
hide_table_of_contents: false
keywords:
  - portal_tags
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

Expands all tag keys and values for <code>portals</code> in a region

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>portal_tags</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>Definition of AWS::WorkSpacesWeb::Portal Resource Type</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="aws.workspacesweb.portal_tags" /></td></tr>
</tbody></table>

## Fields
<table><tbody><tr><th>Name</th><th>Datatype</th><th>Description</th></tr><tr><td><CopyableCode code="additional_encryption_context" /></td><td><code>object</code></td><td></td></tr>
<tr><td><CopyableCode code="authentication_type" /></td><td><code>string</code></td><td></td></tr>
<tr><td><CopyableCode code="browser_settings_arn" /></td><td><code>string</code></td><td></td></tr>
<tr><td><CopyableCode code="browser_type" /></td><td><code>string</code></td><td></td></tr>
<tr><td><CopyableCode code="creation_date" /></td><td><code>string</code></td><td></td></tr>
<tr><td><CopyableCode code="customer_managed_key" /></td><td><code>string</code></td><td></td></tr>
<tr><td><CopyableCode code="data_protection_settings_arn" /></td><td><code>string</code></td><td></td></tr>
<tr><td><CopyableCode code="display_name" /></td><td><code>string</code></td><td></td></tr>
<tr><td><CopyableCode code="instance_type" /></td><td><code>string</code></td><td></td></tr>
<tr><td><CopyableCode code="ip_access_settings_arn" /></td><td><code>string</code></td><td></td></tr>
<tr><td><CopyableCode code="max_concurrent_sessions" /></td><td><code>number</code></td><td></td></tr>
<tr><td><CopyableCode code="network_settings_arn" /></td><td><code>string</code></td><td></td></tr>
<tr><td><CopyableCode code="portal_arn" /></td><td><code>string</code></td><td></td></tr>
<tr><td><CopyableCode code="portal_endpoint" /></td><td><code>string</code></td><td></td></tr>
<tr><td><CopyableCode code="portal_status" /></td><td><code>string</code></td><td></td></tr>
<tr><td><CopyableCode code="renderer_type" /></td><td><code>string</code></td><td></td></tr>
<tr><td><CopyableCode code="service_provider_saml_metadata" /></td><td><code>string</code></td><td></td></tr>
<tr><td><CopyableCode code="status_reason" /></td><td><code>string</code></td><td></td></tr>
<tr><td><CopyableCode code="trust_store_arn" /></td><td><code>string</code></td><td></td></tr>
<tr><td><CopyableCode code="user_access_logging_settings_arn" /></td><td><code>string</code></td><td></td></tr>
<tr><td><CopyableCode code="user_settings_arn" /></td><td><code>string</code></td><td></td></tr>
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
Expands tags for all <code>portals</code> in a region.
```sql
SELECT
region,
additional_encryption_context,
authentication_type,
browser_settings_arn,
browser_type,
creation_date,
customer_managed_key,
data_protection_settings_arn,
display_name,
instance_type,
ip_access_settings_arn,
max_concurrent_sessions,
network_settings_arn,
portal_arn,
portal_endpoint,
portal_status,
renderer_type,
service_provider_saml_metadata,
status_reason,
trust_store_arn,
user_access_logging_settings_arn,
user_settings_arn,
tag_key,
tag_value
FROM aws.workspacesweb.portal_tags
WHERE region = 'us-east-1';
```


## Permissions

For permissions required to operate on the <code>portal_tags</code> resource, see <a href="/providers/aws/workspacesweb/portals/#permissions"><code>portals</code></a>

