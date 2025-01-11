---
title: registry_policies_list_only
hide_title: false
hide_table_of_contents: false
keywords:
  - registry_policies_list_only
  - ecr
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

Lists <code>registry_policies</code> in a region or regions, for all properties use <a href="/providers/aws/serviceName/registry_policies/"><code>registry_policies</code></a>

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>registry_policies_list_only</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>The <code>AWS::ECR::RegistryPolicy</code> resource creates or updates the permissions policy for a private registry.<br />A private registry policy is used to specify permissions for another AWS-account and is used when configuring cross-account replication. For more information, see &#91;Registry permissions&#93;(https://docs.aws.amazon.com/AmazonECR/latest/userguide/registry-permissions.html) in the *Amazon Elastic Container Registry User Guide*.</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="aws.ecr.registry_policies_list_only" /></td></tr>
</tbody></table>

## Fields
<table><tbody><tr><th>Name</th><th>Datatype</th><th>Description</th></tr><tr><td><CopyableCode code="registry_id" /></td><td><code>string</code></td><td>The AWS account ID associated with the registry that contains the repository. If you do not specify a registry, the default registry is assumed.</td></tr>
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
Lists all <code>registry_policies</code> in a region.
```sql
SELECT
region,
registry_id
FROM aws.ecr.registry_policies_list_only
WHERE region = 'us-east-1';
```


## Permissions

For permissions required to operate on the <code>registry_policies_list_only</code> resource, see <a href="/providers/aws/ecr/registry_policies/#permissions"><code>registry_policies</code></a>

