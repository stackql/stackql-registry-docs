---
title: web_experience_tags
hide_title: false
hide_table_of_contents: false
keywords:
  - web_experience_tags
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

Expands all tag keys and values for <code>web_experiences</code> in a region

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>web_experience_tags</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>Definition of AWS::QBusiness::WebExperience Resource Type</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="aws.qbusiness.web_experience_tags" /></td></tr>
</tbody></table>

## Fields
<table><tbody><tr><th>Name</th><th>Datatype</th><th>Description</th></tr><tr><td><CopyableCode code="application_id" /></td><td><code>string</code></td><td></td></tr>
<tr><td><CopyableCode code="created_at" /></td><td><code>string</code></td><td></td></tr>
<tr><td><CopyableCode code="default_endpoint" /></td><td><code>string</code></td><td></td></tr>
<tr><td><CopyableCode code="identity_provider_configuration" /></td><td><code>undefined</code></td><td></td></tr>
<tr><td><CopyableCode code="role_arn" /></td><td><code>string</code></td><td></td></tr>
<tr><td><CopyableCode code="sample_prompts_control_mode" /></td><td><code>string</code></td><td></td></tr>
<tr><td><CopyableCode code="status" /></td><td><code>string</code></td><td></td></tr>
<tr><td><CopyableCode code="subtitle" /></td><td><code>string</code></td><td></td></tr>
<tr><td><CopyableCode code="title" /></td><td><code>string</code></td><td></td></tr>
<tr><td><CopyableCode code="updated_at" /></td><td><code>string</code></td><td></td></tr>
<tr><td><CopyableCode code="web_experience_arn" /></td><td><code>string</code></td><td></td></tr>
<tr><td><CopyableCode code="web_experience_id" /></td><td><code>string</code></td><td></td></tr>
<tr><td><CopyableCode code="welcome_message" /></td><td><code>string</code></td><td></td></tr>
<tr><td><CopyableCode code="origins" /></td><td><code>array</code></td><td></td></tr>
<tr><td><CopyableCode code="customization_configuration" /></td><td><code>object</code></td><td></td></tr>
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
Expands tags for all <code>web_experiences</code> in a region.
```sql
SELECT
region,
application_id,
created_at,
default_endpoint,
identity_provider_configuration,
role_arn,
sample_prompts_control_mode,
status,
subtitle,
title,
updated_at,
web_experience_arn,
web_experience_id,
welcome_message,
origins,
customization_configuration,
tag_key,
tag_value
FROM aws.qbusiness.web_experience_tags
WHERE region = 'us-east-1';
```


## Permissions

For permissions required to operate on the <code>web_experience_tags</code> resource, see <a href="/providers/aws/qbusiness/web_experiences/#permissions"><code>web_experiences</code></a>

