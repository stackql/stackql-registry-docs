---
title: repository_link_tags
hide_title: false
hide_table_of_contents: false
keywords:
  - repository_link_tags
  - codestarconnections
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

Expands all tag keys and values for <code>repository_links</code> in a region

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>repository_link_tags</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>Schema for AWS::CodeStarConnections::RepositoryLink resource which is used to aggregate repository metadata relevant to synchronizing source provider content to AWS Resources.</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="aws.codestarconnections.repository_link_tags" /></td></tr>
</tbody></table>

## Fields
<table><tbody><tr><th>Name</th><th>Datatype</th><th>Description</th></tr><tr><td><CopyableCode code="connection_arn" /></td><td><code>string</code></td><td>The Amazon Resource Name (ARN) of the CodeStarConnection. The ARN is used as the connection reference when the connection is shared between AWS services.</td></tr>
<tr><td><CopyableCode code="provider_type" /></td><td><code>string</code></td><td>The name of the external provider where your third-party code repository is configured.</td></tr>
<tr><td><CopyableCode code="owner_id" /></td><td><code>string</code></td><td>the ID of the entity that owns the repository.</td></tr>
<tr><td><CopyableCode code="repository_name" /></td><td><code>string</code></td><td>The repository for which the link is being created.</td></tr>
<tr><td><CopyableCode code="encryption_key_arn" /></td><td><code>string</code></td><td>The ARN of the KMS key that the customer can optionally specify to use to encrypt RepositoryLink properties. If not specified, a default key will be used.</td></tr>
<tr><td><CopyableCode code="repository_link_id" /></td><td><code>string</code></td><td>A UUID that uniquely identifies the RepositoryLink.</td></tr>
<tr><td><CopyableCode code="repository_link_arn" /></td><td><code>string</code></td><td>A unique Amazon Resource Name (ARN) to designate the repository link.</td></tr>
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
Expands tags for all <code>repository_links</code> in a region.
```sql
SELECT
region,
connection_arn,
provider_type,
owner_id,
repository_name,
encryption_key_arn,
repository_link_id,
repository_link_arn,
tag_key,
tag_value
FROM aws.codestarconnections.repository_link_tags
WHERE region = 'us-east-1';
```


## Permissions

For permissions required to operate on the <code>repository_link_tags</code> resource, see <a href="/providers/aws/codestarconnections/repository_links/#permissions"><code>repository_links</code></a>


