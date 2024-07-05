---
title: domains_list_only
hide_title: false
hide_table_of_contents: false
keywords:
  - domains_list_only
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

Lists <code>domains</code> in a region or regions, for all properties use <a href="/providers/aws/serviceName/domains/"><code>domains</code></a>

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>domains_list_only</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>The resource schema to create a CodeArtifact domain.</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="aws.codeartifact.domains_list_only" /></td></tr>
</tbody></table>

## Fields
<table><tbody><tr><th>Name</th><th>Datatype</th><th>Description</th></tr><tr><td><CopyableCode code="domain_name" /></td><td><code>string</code></td><td>The name of the domain.</td></tr>
<tr><td><CopyableCode code="name" /></td><td><code>string</code></td><td>The name of the domain. This field is used for GetAtt</td></tr>
<tr><td><CopyableCode code="owner" /></td><td><code>string</code></td><td>The 12-digit account ID of the AWS account that owns the domain. This field is used for GetAtt</td></tr>
<tr><td><CopyableCode code="encryption_key" /></td><td><code>string</code></td><td>The ARN of an AWS Key Management Service (AWS KMS) key associated with a domain.</td></tr>
<tr><td><CopyableCode code="permissions_policy_document" /></td><td><code>object</code></td><td>The access control resource policy on the provided domain.</td></tr>
<tr><td><CopyableCode code="tags" /></td><td><code>array</code></td><td>An array of key-value pairs to apply to this resource.</td></tr>
<tr><td><CopyableCode code="arn" /></td><td><code>string</code></td><td>The ARN of the domain.</td></tr>
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
Lists all <code>domains</code> in a region.
```sql
SELECT
region,
arn
FROM aws.codeartifact.domains_list_only
WHERE region = 'us-east-1';
```


## Permissions

For permissions required to operate on the <code>domains_list_only</code> resource, see <a href="/providers/aws/codeartifact/domains/#permissions"><code>domains</code></a>


