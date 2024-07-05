---
title: in_app_templates_list_only
hide_title: false
hide_table_of_contents: false
keywords:
  - in_app_templates_list_only
  - pinpoint
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

Lists <code>in_app_templates</code> in a region or regions, for all properties use <a href="/providers/aws/serviceName/in_app_templates/"><code>in_app_templates</code></a>

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>in_app_templates_list_only</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>Resource Type definition for AWS::Pinpoint::InAppTemplate</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="aws.pinpoint.in_app_templates_list_only" /></td></tr>
</tbody></table>

## Fields
<table><tbody><tr><th>Name</th><th>Datatype</th><th>Description</th></tr><tr><td><CopyableCode code="arn" /></td><td><code>string</code></td><td></td></tr>
<tr><td><CopyableCode code="content" /></td><td><code>array</code></td><td></td></tr>
<tr><td><CopyableCode code="custom_config" /></td><td><code>object</code></td><td></td></tr>
<tr><td><CopyableCode code="layout" /></td><td><code>string</code></td><td></td></tr>
<tr><td><CopyableCode code="tags" /></td><td><code>object</code></td><td></td></tr>
<tr><td><CopyableCode code="template_description" /></td><td><code>string</code></td><td></td></tr>
<tr><td><CopyableCode code="template_name" /></td><td><code>string</code></td><td></td></tr>
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
Lists all <code>in_app_templates</code> in a region.
```sql
SELECT
region,
template_name
FROM aws.pinpoint.in_app_templates_list_only
WHERE region = 'us-east-1';
```


## Permissions

For permissions required to operate on the <code>in_app_templates_list_only</code> resource, see <a href="/providers/aws/pinpoint/in_app_templates/#permissions"><code>in_app_templates</code></a>


