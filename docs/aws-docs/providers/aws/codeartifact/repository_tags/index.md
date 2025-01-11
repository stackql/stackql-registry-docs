---
title: repository_tags
hide_title: false
hide_table_of_contents: false
keywords:
  - repository_tags
  - codeartifact
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

Expands all tag keys and values for <code>repositories</code> in a region

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>repository_tags</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>The resource schema to create a CodeArtifact repository.</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="aws.codeartifact.repository_tags" /></td></tr>
</tbody></table>

## Fields
<table><tbody><tr><th>Name</th><th>Datatype</th><th>Description</th></tr><tr><td><CopyableCode code="repository_name" /></td><td><code>string</code></td><td>The name of the repository.</td></tr>
<tr><td><CopyableCode code="name" /></td><td><code>string</code></td><td>The name of the repository. This is used for GetAtt</td></tr>
<tr><td><CopyableCode code="domain_name" /></td><td><code>string</code></td><td>The name of the domain that contains the repository.</td></tr>
<tr><td><CopyableCode code="domain_owner" /></td><td><code>string</code></td><td>The 12-digit account ID of the AWS account that owns the domain.</td></tr>
<tr><td><CopyableCode code="description" /></td><td><code>string</code></td><td>A text description of the repository.</td></tr>
<tr><td><CopyableCode code="arn" /></td><td><code>string</code></td><td>The ARN of the repository.</td></tr>
<tr><td><CopyableCode code="external_connections" /></td><td><code>array</code></td><td>A list of external connections associated with the repository.</td></tr>
<tr><td><CopyableCode code="upstreams" /></td><td><code>array</code></td><td>A list of upstream repositories associated with the repository.</td></tr>
<tr><td><CopyableCode code="permissions_policy_document" /></td><td><code>object</code></td><td>The access control resource policy on the provided repository.</td></tr>
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
Expands tags for all <code>repositories</code> in a region.
```sql
SELECT
region,
repository_name,
name,
domain_name,
domain_owner,
description,
arn,
external_connections,
upstreams,
permissions_policy_document,
tag_key,
tag_value
FROM aws.codeartifact.repository_tags
WHERE region = 'us-east-1';
```


## Permissions

For permissions required to operate on the <code>repository_tags</code> resource, see <a href="/providers/aws/codeartifact/repositories/#permissions"><code>repositories</code></a>

