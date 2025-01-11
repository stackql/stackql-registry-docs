---
title: mail_manager_archive_tags
hide_title: false
hide_table_of_contents: false
keywords:
  - mail_manager_archive_tags
  - ses
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

Expands all tag keys and values for <code>mail_manager_archives</code> in a region

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>mail_manager_archive_tags</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>Definition of AWS::SES::MailManagerArchive Resource Type</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="aws.ses.mail_manager_archive_tags" /></td></tr>
</tbody></table>

## Fields
<table><tbody><tr><th>Name</th><th>Datatype</th><th>Description</th></tr><tr><td><CopyableCode code="archive_arn" /></td><td><code>string</code></td><td></td></tr>
<tr><td><CopyableCode code="archive_id" /></td><td><code>string</code></td><td></td></tr>
<tr><td><CopyableCode code="archive_name" /></td><td><code>string</code></td><td></td></tr>
<tr><td><CopyableCode code="archive_state" /></td><td><code>string</code></td><td></td></tr>
<tr><td><CopyableCode code="kms_key_arn" /></td><td><code>string</code></td><td></td></tr>
<tr><td><CopyableCode code="retention" /></td><td><code>undefined</code></td><td></td></tr>
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
Expands tags for all <code>mail_manager_archives</code> in a region.
```sql
SELECT
region,
archive_arn,
archive_id,
archive_name,
archive_state,
kms_key_arn,
retention,
tag_key,
tag_value
FROM aws.ses.mail_manager_archive_tags
WHERE region = 'us-east-1';
```


## Permissions

For permissions required to operate on the <code>mail_manager_archive_tags</code> resource, see <a href="/providers/aws/ses/mail_manager_archives/#permissions"><code>mail_manager_archives</code></a>

