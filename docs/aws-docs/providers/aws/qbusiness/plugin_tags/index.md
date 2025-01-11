---
title: plugin_tags
hide_title: false
hide_table_of_contents: false
keywords:
  - plugin_tags
  - qbusiness
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

Expands all tag keys and values for <code>plugins</code> in a region

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>plugin_tags</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>Definition of AWS::QBusiness::Plugin Resource Type</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="aws.qbusiness.plugin_tags" /></td></tr>
</tbody></table>

## Fields
<table><tbody><tr><th>Name</th><th>Datatype</th><th>Description</th></tr><tr><td><CopyableCode code="application_id" /></td><td><code>string</code></td><td></td></tr>
<tr><td><CopyableCode code="auth_configuration" /></td><td><code>undefined</code></td><td></td></tr>
<tr><td><CopyableCode code="build_status" /></td><td><code>string</code></td><td></td></tr>
<tr><td><CopyableCode code="created_at" /></td><td><code>string</code></td><td></td></tr>
<tr><td><CopyableCode code="custom_plugin_configuration" /></td><td><code>object</code></td><td></td></tr>
<tr><td><CopyableCode code="display_name" /></td><td><code>string</code></td><td></td></tr>
<tr><td><CopyableCode code="plugin_arn" /></td><td><code>string</code></td><td></td></tr>
<tr><td><CopyableCode code="plugin_id" /></td><td><code>string</code></td><td></td></tr>
<tr><td><CopyableCode code="server_url" /></td><td><code>string</code></td><td></td></tr>
<tr><td><CopyableCode code="state" /></td><td><code>string</code></td><td></td></tr>
<tr><td><CopyableCode code="type" /></td><td><code>string</code></td><td></td></tr>
<tr><td><CopyableCode code="updated_at" /></td><td><code>string</code></td><td></td></tr>
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
Expands tags for all <code>plugins</code> in a region.
```sql
SELECT
region,
application_id,
auth_configuration,
build_status,
created_at,
custom_plugin_configuration,
display_name,
plugin_arn,
plugin_id,
server_url,
state,
type,
updated_at,
tag_key,
tag_value
FROM aws.qbusiness.plugin_tags
WHERE region = 'us-east-1';
```


## Permissions

For permissions required to operate on the <code>plugin_tags</code> resource, see <a href="/providers/aws/qbusiness/plugins/#permissions"><code>plugins</code></a>

