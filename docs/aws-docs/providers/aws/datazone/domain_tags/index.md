---
title: domain_tags
hide_title: false
hide_table_of_contents: false
keywords:
  - domain_tags
  - datazone
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

Expands all tag keys and values for <code>domains</code> in a region

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>domain_tags</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>A domain is an organizing entity for connecting together assets, users, and their projects</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="aws.datazone.domain_tags" /></td></tr>
</tbody></table>

## Fields
<table><tbody><tr><th>Name</th><th>Datatype</th><th>Description</th></tr><tr><td><CopyableCode code="arn" /></td><td><code>string</code></td><td>The ARN of the Amazon DataZone domain.</td></tr>
<tr><td><CopyableCode code="created_at" /></td><td><code>string</code></td><td>The timestamp of when the Amazon DataZone domain was last updated.</td></tr>
<tr><td><CopyableCode code="description" /></td><td><code>string</code></td><td>The description of the Amazon DataZone domain.</td></tr>
<tr><td><CopyableCode code="domain_execution_role" /></td><td><code>string</code></td><td>The domain execution role that is created when an Amazon DataZone domain is created. The domain execution role is created in the AWS account that houses the Amazon DataZone domain.</td></tr>
<tr><td><CopyableCode code="id" /></td><td><code>string</code></td><td>The id of the Amazon DataZone domain.</td></tr>
<tr><td><CopyableCode code="kms_key_identifier" /></td><td><code>string</code></td><td>The identifier of the AWS Key Management Service (KMS) key that is used to encrypt the Amazon DataZone domain, metadata, and reporting data.</td></tr>
<tr><td><CopyableCode code="last_updated_at" /></td><td><code>string</code></td><td>The timestamp of when the Amazon DataZone domain was last updated.</td></tr>
<tr><td><CopyableCode code="managed_account_id" /></td><td><code>string</code></td><td>The identifier of the AWS account that manages the domain.</td></tr>
<tr><td><CopyableCode code="name" /></td><td><code>string</code></td><td>The name of the Amazon DataZone domain.</td></tr>
<tr><td><CopyableCode code="portal_url" /></td><td><code>string</code></td><td>The URL of the data portal for this Amazon DataZone domain.</td></tr>
<tr><td><CopyableCode code="single_sign_on" /></td><td><code>object</code></td><td>The single-sign on configuration of the Amazon DataZone domain.</td></tr>
<tr><td><CopyableCode code="status" /></td><td><code>string</code></td><td>The status of the Amazon DataZone domain.</td></tr>
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
Expands tags for all <code>domains</code> in a region.
```sql
SELECT
region,
arn,
created_at,
description,
domain_execution_role,
id,
kms_key_identifier,
last_updated_at,
managed_account_id,
name,
portal_url,
single_sign_on,
status,
tag_key,
tag_value
FROM aws.datazone.domain_tags
WHERE region = 'us-east-1';
```


## Permissions

For permissions required to operate on the <code>domain_tags</code> resource, see <a href="/providers/aws/datazone/domains/#permissions"><code>domains</code></a>

