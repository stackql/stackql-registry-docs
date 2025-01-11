---
title: environment_tags
hide_title: false
hide_table_of_contents: false
keywords:
  - environment_tags
  - appconfig
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

Expands all tag keys and values for <code>environments</code> in a region

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>environment_tags</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>Resource Type definition for AWS::AppConfig::Environment</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="aws.appconfig.environment_tags" /></td></tr>
</tbody></table>

## Fields
<table><tbody><tr><th>Name</th><th>Datatype</th><th>Description</th></tr><tr><td><CopyableCode code="environment_id" /></td><td><code>string</code></td><td>The environment ID.</td></tr>
<tr><td><CopyableCode code="description" /></td><td><code>string</code></td><td>A description of the environment.</td></tr>
<tr><td><CopyableCode code="monitors" /></td><td><code>array</code></td><td>Amazon CloudWatch alarms to monitor during the deployment process.</td></tr>
<tr><td><CopyableCode code="deletion_protection_check" /></td><td><code>string</code></td><td>On resource deletion this controls whether the Deletion Protection check should be applied, bypassed, or (the default) whether the behavior should be controlled by the account-level Deletion Protection setting. See https://docs.aws.amazon.com/appconfig/latest/userguide/deletion-protection.html</td></tr>
<tr><td><CopyableCode code="application_id" /></td><td><code>string</code></td><td>The application ID.</td></tr>
<tr><td><CopyableCode code="name" /></td><td><code>string</code></td><td>A name for the environment.</td></tr>
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
Expands tags for all <code>environments</code> in a region.
```sql
SELECT
region,
environment_id,
description,
monitors,
deletion_protection_check,
application_id,
name,
tag_key,
tag_value
FROM aws.appconfig.environment_tags
WHERE region = 'us-east-1';
```


## Permissions

For permissions required to operate on the <code>environment_tags</code> resource, see <a href="/providers/aws/appconfig/environments/#permissions"><code>environments</code></a>

