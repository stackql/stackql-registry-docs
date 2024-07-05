---
title: repositories_list_only
hide_title: false
hide_table_of_contents: false
keywords:
  - repositories_list_only
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

Lists <code>repositories</code> in a region or regions, for all properties use <a href="/providers/aws/serviceName/repositories/"><code>repositories</code></a>

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>repositories_list_only</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>The <code>AWS::ECR::Repository</code> resource specifies an Amazon Elastic Container Registry (Amazon ECR) repository, where users can push and pull Docker images, Open Container Initiative (OCI) images, and OCI compatible artifacts. For more information, see &#91;Amazon ECR private repositories&#93;(https://docs.aws.amazon.com/AmazonECR/latest/userguide/Repositories.html) in the *Amazon ECR User Guide*.</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="aws.ecr.repositories_list_only" /></td></tr>
</tbody></table>

## Fields
<table><tbody><tr><th>Name</th><th>Datatype</th><th>Description</th></tr><tr><td><CopyableCode code="empty_on_delete" /></td><td><code>boolean</code></td><td>If true, deleting the repository force deletes the contents of the repository. If false, the repository must be empty before attempting to delete it.</td></tr>
<tr><td><CopyableCode code="lifecycle_policy" /></td><td><code>object</code></td><td>Creates or updates a lifecycle policy. For information about lifecycle policy syntax, see &#91;Lifecycle policy template&#93;(https://docs.aws.amazon.com/AmazonECR/latest/userguide/LifecyclePolicies.html).</td></tr>
<tr><td><CopyableCode code="repository_name" /></td><td><code>string</code></td><td>The name to use for the repository. The repository name may be specified on its own (such as <code>nginx-web-app</code>) or it can be prepended with a namespace to group the repository into a category (such as <code>project-a/nginx-web-app</code>). If you don't specify a name, CFNlong generates a unique physical ID and uses that ID for the repository name. For more information, see &#91;Name type&#93;(https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-name.html).<br />The repository name must start with a letter and can only contain lowercase letters, numbers, hyphens, underscores, and forward slashes.<br />If you specify a name, you cannot perform updates that require replacement of this resource. You can perform updates that require no or some interruption. If you must replace the resource, specify a new name.</td></tr>
<tr><td><CopyableCode code="repository_policy_text" /></td><td><code>object</code></td><td>The JSON repository policy text to apply to the repository. For more information, see &#91;Amazon ECR repository policies&#93;(https://docs.aws.amazon.com/AmazonECR/latest/userguide/repository-policy-examples.html) in the *Amazon Elastic Container Registry User Guide*.</td></tr>
<tr><td><CopyableCode code="tags" /></td><td><code>array</code></td><td>An array of key-value pairs to apply to this resource.</td></tr>
<tr><td><CopyableCode code="arn" /></td><td><code>string</code></td><td></td></tr>
<tr><td><CopyableCode code="repository_uri" /></td><td><code>string</code></td><td></td></tr>
<tr><td><CopyableCode code="image_tag_mutability" /></td><td><code>string</code></td><td>The tag mutability setting for the repository. If this parameter is omitted, the default setting of <code>MUTABLE</code> will be used which will allow image tags to be overwritten. If <code>IMMUTABLE</code> is specified, all image tags within the repository will be immutable which will prevent them from being overwritten.</td></tr>
<tr><td><CopyableCode code="image_scanning_configuration" /></td><td><code>object</code></td><td>The image scanning configuration for the repository. This determines whether images are scanned for known vulnerabilities after being pushed to the repository.</td></tr>
<tr><td><CopyableCode code="encryption_configuration" /></td><td><code>object</code></td><td>The encryption configuration for the repository. This determines how the contents of your repository are encrypted at rest.</td></tr>
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
Lists all <code>repositories</code> in a region.
```sql
SELECT
region,
repository_name
FROM aws.ecr.repositories_list_only
WHERE region = 'us-east-1';
```


## Permissions

For permissions required to operate on the <code>repositories_list_only</code> resource, see <a href="/providers/aws/ecr/repositories/#permissions"><code>repositories</code></a>


