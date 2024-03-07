---
title: pull_through_cache_rule
hide_title: false
hide_table_of_contents: false
keywords:
  - pull_through_cache_rule
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
Gets an individual <code>pull_through_cache_rule</code> resource

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>pull_through_cache_rule</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>pull_through_cache_rule</td></tr>
<tr><td><b>Id</b></td><td><code>awscc.ecr.pull_through_cache_rule</code></td></tr>
</tbody></table>

## Fields
<table><tbody>
<tr><th>Name</th><th>Datatype</th><th>Description</th></tr>
<tr><td><code>ecr_repository_prefix</code></td><td><code>string</code></td><td>The ECRRepositoryPrefix is a custom alias for upstream registry url.</td></tr>
<tr><td><code>upstream_registry_url</code></td><td><code>string</code></td><td>The upstreamRegistryUrl is the endpoint of upstream registry url of the public repository to be cached</td></tr>
<tr><td><code>credential_arn</code></td><td><code>string</code></td><td>The Amazon Resource Name (ARN) of the AWS Secrets Manager secret that identifies the credentials to authenticate to the upstream registry.</td></tr>
<tr><td><code>upstream_registry</code></td><td><code>string</code></td><td>The name of the upstream registry.</td></tr>
<tr><td><code>region</code></td><td><code>string</code></td><td>AWS region.</td></tr>

</tbody></table>

## Methods
Currently only <code>SELECT</code> is supported for this resource resource.

## Permissions

To operate on the <code>pull_through_cache_rule</code> resource, the following permissions are required:

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


## Example
```sql
SELECT
region,
ecr_repository_prefix,
upstream_registry_url,
credential_arn,
upstream_registry
FROM awscc.ecr.pull_through_cache_rule
WHERE region = 'us-east-1'
AND data__Identifier = '&lt;EcrRepositoryPrefix&gt;'
```
