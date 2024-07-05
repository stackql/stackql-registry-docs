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

Creates, updates, deletes or gets a <code>pull_through_cache_rule</code> resource or lists <code>pull_through_cache_rules</code> in a region

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>pull_through_cache_rules</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>The AWS::ECR::PullThroughCacheRule resource configures the upstream registry configuration details for an Amazon Elastic Container Registry (Amazon Private ECR) pull-through cache.</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="aws.ecr.pull_through_cache_rules" /></td></tr>
</tbody></table>

## Fields
<table><tbody><tr><th>Name</th><th>Datatype</th><th>Description</th></tr><tr><td><CopyableCode code="ecr_repository_prefix" /></td><td><code>string</code></td><td>The ECRRepositoryPrefix is a custom alias for upstream registry url.</td></tr>
<tr><td><CopyableCode code="upstream_registry_url" /></td><td><code>string</code></td><td>The upstreamRegistryUrl is the endpoint of upstream registry url of the public repository to be cached</td></tr>
<tr><td><CopyableCode code="credential_arn" /></td><td><code>string</code></td><td>The Amazon Resource Name (ARN) of the AWS Secrets Manager secret that identifies the credentials to authenticate to the upstream registry.</td></tr>
<tr><td><CopyableCode code="upstream_registry" /></td><td><code>string</code></td><td>The name of the upstream registry.</td></tr>
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
    <td><CopyableCode code="region" /></td>
  </tr>
  <tr>
    <td><CopyableCode code="delete_resource" /></td>
    <td><code>DELETE</code></td>
    <td><CopyableCode code="data__Identifier, region" /></td>
  </tr>
  <tr>
    <td><CopyableCode code="update_resource" /></td>
    <td><code>UPDATE</code></td>
    <td><CopyableCode code="data__Identifier, data__PatchDocument, region" /></td>
  </tr>
  <tr>
    <td><CopyableCode code="list_resources" /></td>
    <td><code>SELECT</code></td>
    <td><CopyableCode code="region" /></td>
  </tr>
  <tr>
    <td><CopyableCode code="get_resource" /></td>
    <td><code>SELECT</code></td>
    <td><CopyableCode code="data__Identifier, region" /></td>
  </tr>
</tbody></table>

## `SELECT` examples
Gets all <code>pull_through_cache_rules</code> in a region.
```sql
SELECT
region,
ecr_repository_prefix,
upstream_registry_url,
credential_arn,
upstream_registry
FROM aws.ecr.pull_through_cache_rules
WHERE region = 'us-east-1';
```
Gets all properties from an individual <code>pull_through_cache_rule</code>.
```sql
SELECT
region,
ecr_repository_prefix,
upstream_registry_url,
credential_arn,
upstream_registry
FROM aws.ecr.pull_through_cache_rules
WHERE region = 'us-east-1' AND data__Identifier = '<EcrRepositoryPrefix>';
```

## `INSERT` example

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
/*+ create */
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
/*+ create */
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

## `DELETE` example

```sql
/*+ delete */
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

### Read
```json
ecr:DescribePullThroughCacheRules
```

### Update
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

