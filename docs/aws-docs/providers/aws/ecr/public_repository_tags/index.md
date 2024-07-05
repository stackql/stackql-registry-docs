---
title: public_repository_tags
hide_title: false
hide_table_of_contents: false
keywords:
  - public_repository_tags
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

Expands all tag keys and values for <code>public_repositories</code> in a region

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>public_repository_tags</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>The AWS::ECR::PublicRepository resource specifies an Amazon Elastic Container Public Registry (Amazon Public ECR) repository, where users can push and pull Docker images. For more information, see https://docs.aws.amazon.com/AmazonECR</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="aws.ecr.public_repository_tags" /></td></tr>
</tbody></table>

## Fields
<table><tbody><tr><th>Name</th><th>Datatype</th><th>Description</th></tr><tr><td><CopyableCode code="repository_name" /></td><td><code>string</code></td><td>The name to use for the repository. The repository name may be specified on its own (such as nginx-web-app) or it can be prepended with a namespace to group the repository into a category (such as project-a/nginx-web-app). If you don't specify a name, AWS CloudFormation generates a unique physical ID and uses that ID for the repository name. For more information, see https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-name.html.</td></tr>
<tr><td><CopyableCode code="repository_policy_text" /></td><td><code>object</code></td><td>The JSON repository policy text to apply to the repository. For more information, see https://docs.aws.amazon.com/AmazonECR/latest/userguide/RepositoryPolicyExamples.html in the Amazon Elastic Container Registry User Guide.</td></tr>
<tr><td><CopyableCode code="arn" /></td><td><code>string</code></td><td></td></tr>
<tr><td><CopyableCode code="repository_catalog_data" /></td><td><code>object</code></td><td>The CatalogData property type specifies Catalog data for ECR Public Repository. For information about Catalog Data, see &lt;link&gt;</td></tr>
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
Expands tags for all <code>public_repositories</code> in a region.
```sql
SELECT
region,
repository_name,
repository_policy_text,
arn,
repository_catalog_data,
tag_key,
tag_value
FROM aws.ecr.public_repository_tags
WHERE region = 'us-east-1';
```


## Permissions

For permissions required to operate on the <code>public_repository_tags</code> resource, see <a href="/providers/aws/ecr/public_repositories/#permissions"><code>public_repositories</code></a>


