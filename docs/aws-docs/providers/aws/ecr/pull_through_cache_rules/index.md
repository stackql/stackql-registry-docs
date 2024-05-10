---
title: pull_through_cache_rules
hide_title: false
hide_table_of_contents: false
keywords:
  - pull_through_cache_rules
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


Used to retrieve a list of <code>pull_through_cache_rules</code> in a region or to create or delete a <code>pull_through_cache_rules</code> resource, use <code>pull_through_cache_rule</code> to read or update an individual resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>pull_through_cache_rules</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>The AWS::ECR::PullThroughCacheRule resource configures the upstream registry configuration details for an Amazon Elastic Container Registry (Amazon Private ECR) pull-through cache.</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="aws.ecr.pull_through_cache_rules" /></td></tr>
</tbody></table>

## Fields
<table><tbody>
<tr><th>Name</th><th>Datatype</th><th>Description</th></tr>
<tr><td><CopyableCode code="ecr_repository_prefix" /></td><td><code>string</code></td><td>The ECRRepositoryPrefix is a custom alias for upstream registry url.</td></tr>
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
    <td><CopyableCode code="create_resource" /></td>
    <td><code>INSERT</code></td>
    <td><CopyableCode code="data__DesiredState, region" /></td>
  </tr>
  <tr>
    <td><CopyableCode code="delete_resource" /></td>
    <td><code>DELETE</code></td>
    <td><CopyableCode code="data__Identifier, region" /></td>
  </tr>
  <tr>
    <td><CopyableCode code="list_resource" /></td>
    <td><code>SELECT</code></td>
    <td><CopyableCode code="region" /></td>
  </tr>
</tbody></table>

## `SELECT` Example
```sql
SELECT
region,
ecr_repository_prefix
FROM aws.ecr.pull_through_cache_rules
WHERE region = 'us-east-1';
```

## `INSERT` Example

Use the following StackQL query and manifest file to create a new <code>pull_through_cache_rule</code> resource, using [__`stack-deploy`__](https://pypi.org/project/stack-deploy/).

<Tabs
    defaultValue="required"
    values={[
      { label: 'Required Properties', value: 'required', },
      { label: 'All Properties', value: 'all', },
      { label: 'Manifest', value: 'manifest', },
    ]
}>
<TabItem value="required">

```sql
-- pull_through_cache_rule.iql (required properties only)
INSERT INTO aws.ecr.pull_through_cache_rules (
 EcrRepositoryPrefix,
 UpstreamRegistryUrl,
 CredentialArn,
 UpstreamRegistry,
 region
)
SELECT 
'{{ EcrRepositoryPrefix }}',
 '{{ UpstreamRegistryUrl }}',
 '{{ CredentialArn }}',
 '{{ UpstreamRegistry }}',
'{{ region }}';
```
</TabItem>
<TabItem value="all">

```sql
-- pull_through_cache_rule.iql (all properties)
INSERT INTO aws.ecr.pull_through_cache_rules (
 EcrRepositoryPrefix,
 UpstreamRegistryUrl,
 CredentialArn,
 UpstreamRegistry,
 region
)
SELECT 
 '{{ EcrRepositoryPrefix }}',
 '{{ UpstreamRegistryUrl }}',
 '{{ CredentialArn }}',
 '{{ UpstreamRegistry }}',
 '{{ region }}';
```
</TabItem>
<TabItem value="manifest">

```yaml
version: 1
name: stack name
description: stack description
providers:
  - aws
globals:
  - name: region
    value: '{{ vars.AWS_REGION }}'
resources:
  - name: pull_through_cache_rule
    props:
      - name: EcrRepositoryPrefix
        value: '{{ EcrRepositoryPrefix }}'
      - name: UpstreamRegistryUrl
        value: '{{ UpstreamRegistryUrl }}'
      - name: CredentialArn
        value: '{{ CredentialArn }}'
      - name: UpstreamRegistry
        value: '{{ UpstreamRegistry }}'

```
</TabItem>
</Tabs>

## `DELETE` Example

```sql
DELETE FROM aws.ecr.pull_through_cache_rules
WHERE data__Identifier = '<EcrRepositoryPrefix>'
AND region = 'us-east-1';
```

## Permissions

To operate on the <code>pull_through_cache_rules</code> resource, the following permissions are required:

### Create
```json
ecr:DescribePullThroughCacheRules,
ecr:CreatePullThroughCacheRule,
ecr:DeletePullThroughCacheRule,
iam:CreateServiceLinkedRole,
secretsmanager:GetSecretValue
```

### Delete
```json
ecr:DescribePullThroughCacheRules,
ecr:DeletePullThroughCacheRule
```

### List
```json
ecr:DescribePullThroughCacheRules
```

