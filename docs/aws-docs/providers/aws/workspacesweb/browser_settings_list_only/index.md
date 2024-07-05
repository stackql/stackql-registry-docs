---
title: browser_settings_list_only
hide_title: false
hide_table_of_contents: false
keywords:
  - browser_settings_list_only
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

Lists <code>browser_settings</code> in a region or regions, for all properties use <a href="/providers/aws/serviceName/browser_settings/"><code>browser_settings</code></a>

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>browser_settings_list_only</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>Definition of AWS::WorkSpacesWeb::BrowserSettings Resource Type</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="aws.workspacesweb.browser_settings_list_only" /></td></tr>
</tbody></table>

## Fields
<table><tbody><tr><th>Name</th><th>Datatype</th><th>Description</th></tr><tr><td><CopyableCode code="additional_encryption_context" /></td><td><code>object</code></td><td></td></tr>
<tr><td><CopyableCode code="associated_portal_arns" /></td><td><code>array</code></td><td></td></tr>
<tr><td><CopyableCode code="browser_policy" /></td><td><code>string</code></td><td></td></tr>
<tr><td><CopyableCode code="browser_settings_arn" /></td><td><code>string</code></td><td></td></tr>
<tr><td><CopyableCode code="customer_managed_key" /></td><td><code>string</code></td><td></td></tr>
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
Lists all <code>browser_settings</code> in a region.
```sql
SELECT
region,
browser_settings_arn
FROM aws.workspacesweb.browser_settings_list_only
WHERE region = 'us-east-1';
```


## Permissions

For permissions required to operate on the <code>browser_settings_list_only</code> resource, see <a href="/providers/aws/workspacesweb/browser_settings/#permissions"><code>browser_settings</code></a>


