---
title: message_template_tags
hide_title: false
hide_table_of_contents: false
keywords:
  - message_template_tags
  - wisdom
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

Expands all tag keys and values for <code>message_templates</code> in a region

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>message_template_tags</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>Definition of AWS::Wisdom::MessageTemplate Resource Type</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="aws.wisdom.message_template_tags" /></td></tr>
</tbody></table>

## Fields
<table><tbody><tr><th>Name</th><th>Datatype</th><th>Description</th></tr><tr><td><CopyableCode code="knowledge_base_arn" /></td><td><code>string</code></td><td>The Amazon Resource Name (ARN) of the knowledge base to which the message template belongs.</td></tr>
<tr><td><CopyableCode code="message_template_id" /></td><td><code>string</code></td><td>The unique identifier of the message template.</td></tr>
<tr><td><CopyableCode code="message_template_arn" /></td><td><code>string</code></td><td>The Amazon Resource Name (ARN) of the message template.</td></tr>
<tr><td><CopyableCode code="name" /></td><td><code>string</code></td><td>The name of the message template.</td></tr>
<tr><td><CopyableCode code="channel_subtype" /></td><td><code>string</code></td><td>The channel subtype this message template applies to.</td></tr>
<tr><td><CopyableCode code="content" /></td><td><code>object</code></td><td>The content of the message template.</td></tr>
<tr><td><CopyableCode code="description" /></td><td><code>string</code></td><td>The description of the message template.</td></tr>
<tr><td><CopyableCode code="language" /></td><td><code>string</code></td><td>The language code value for the language in which the message template is written. The supported language codes include de_DE, en_US, es_ES, fr_FR, id_ID, it_IT, ja_JP, ko_KR, pt_BR, zh_CN, zh_TW</td></tr>
<tr><td><CopyableCode code="grouping_configuration" /></td><td><code>object</code></td><td>The configuration information of the user groups that the message template is accessible to.</td></tr>
<tr><td><CopyableCode code="default_attributes" /></td><td><code>object</code></td><td>An object that specifies the default values to use for variables in the message template. This object contains different categories of key-value pairs. Each key defines a variable or placeholder in the message template. The corresponding value defines the default value for that variable.</td></tr>
<tr><td><CopyableCode code="message_template_content_sha256" /></td><td><code>string</code></td><td>The content SHA256 of the message template.</td></tr>
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
Expands tags for all <code>message_templates</code> in a region.
```sql
SELECT
region,
knowledge_base_arn,
message_template_id,
message_template_arn,
name,
channel_subtype,
content,
description,
language,
grouping_configuration,
default_attributes,
message_template_content_sha256,
tag_key,
tag_value
FROM aws.wisdom.message_template_tags
WHERE region = 'us-east-1';
```


## Permissions

For permissions required to operate on the <code>message_template_tags</code> resource, see <a href="/providers/aws/wisdom/message_templates/#permissions"><code>message_templates</code></a>

