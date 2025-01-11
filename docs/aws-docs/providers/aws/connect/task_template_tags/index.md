---
title: task_template_tags
hide_title: false
hide_table_of_contents: false
keywords:
  - task_template_tags
  - connect
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

Expands all tag keys and values for <code>task_templates</code> in a region

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>task_template_tags</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>Resource Type definition for AWS::Connect::TaskTemplate.</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="aws.connect.task_template_tags" /></td></tr>
</tbody></table>

## Fields
<table><tbody><tr><th>Name</th><th>Datatype</th><th>Description</th></tr><tr><td><CopyableCode code="arn" /></td><td><code>string</code></td><td>The identifier (arn) of the task template.</td></tr>
<tr><td><CopyableCode code="instance_arn" /></td><td><code>string</code></td><td>The identifier (arn) of the instance.</td></tr>
<tr><td><CopyableCode code="name" /></td><td><code>string</code></td><td>The name of the task template.</td></tr>
<tr><td><CopyableCode code="description" /></td><td><code>string</code></td><td>The description of the task template.</td></tr>
<tr><td><CopyableCode code="contact_flow_arn" /></td><td><code>string</code></td><td>The identifier of the contact flow.</td></tr>
<tr><td><CopyableCode code="self_assign_contact_flow_arn" /></td><td><code>string</code></td><td>The identifier of the contact flow.</td></tr>
<tr><td><CopyableCode code="constraints" /></td><td><code>object</code></td><td>The constraints for the task template</td></tr>
<tr><td><CopyableCode code="defaults" /></td><td><code>array</code></td><td></td></tr>
<tr><td><CopyableCode code="fields" /></td><td><code>array</code></td><td>The list of task template's fields</td></tr>
<tr><td><CopyableCode code="status" /></td><td><code>string</code></td><td>The status of the task template</td></tr>
<tr><td><CopyableCode code="client_token" /></td><td><code>string</code></td><td>the client token string in uuid format</td></tr>
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
Expands tags for all <code>task_templates</code> in a region.
```sql
SELECT
region,
arn,
instance_arn,
name,
description,
contact_flow_arn,
self_assign_contact_flow_arn,
constraints,
defaults,
fields,
status,
client_token,
tag_key,
tag_value
FROM aws.connect.task_template_tags
WHERE region = 'us-east-1';
```


## Permissions

For permissions required to operate on the <code>task_template_tags</code> resource, see <a href="/providers/aws/connect/task_templates/#permissions"><code>task_templates</code></a>

