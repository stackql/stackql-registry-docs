---
title: repository_creation_templates_list_only
hide_title: false
hide_table_of_contents: false
keywords:
  - repository_creation_templates_list_only
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

Lists <code>repository_creation_templates</code> in a region or regions, for all properties use <a href="/providers/aws/serviceName/repository_creation_templates/"><code>repository_creation_templates</code></a>

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>repository_creation_templates_list_only</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>AWS::ECR::RepositoryCreationTemplate is used to create repository with configuration from a pre-defined template.</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="aws.ecr.repository_creation_templates_list_only" /></td></tr>
</tbody></table>

## Fields
<table><tbody><tr><th>Name</th><th>Datatype</th><th>Description</th></tr><tr><td><CopyableCode code="prefix" /></td><td><code>string</code></td><td>The prefix use to match the repository name and apply the template.</td></tr>
<tr><td><CopyableCode code="description" /></td><td><code>string</code></td><td>The description of the template.</td></tr>
<tr><td><CopyableCode code="image_tag_mutability" /></td><td><code>string</code></td><td>The image tag mutability setting for the repository.</td></tr>
<tr><td><CopyableCode code="repository_policy" /></td><td><code>string</code></td><td>The JSON repository policy text to apply to the repository. For more information, see https://docs.aws.amazon.com/AmazonECR/latest/userguide/RepositoryPolicyExamples.html</td></tr>
<tr><td><CopyableCode code="lifecycle_policy" /></td><td><code>string</code></td><td>The JSON lifecycle policy text to apply to the repository. For information about lifecycle policy syntax, see https://docs.aws.amazon.com/AmazonECR/latest/userguide/LifecyclePolicies.html</td></tr>
<tr><td><CopyableCode code="encryption_configuration" /></td><td><code>object</code></td><td>The encryption configuration for the repository. This determines how the contents of your repository are encrypted at rest. By default, when no encryption configuration is set or the AES256 encryption type is used, Amazon ECR uses server-side encryption with Amazon S3-managed encryption keys which encrypts your data at rest using an AES-256 encryption algorithm. This does not require any action on your part.<br />For more information, see https://docs.aws.amazon.com/AmazonECR/latest/userguide/encryption-at-rest.html</td></tr>
<tr><td><CopyableCode code="resource_tags" /></td><td><code>array</code></td><td>An array of key-value pairs to apply to this resource.</td></tr>
<tr><td><CopyableCode code="applied_for" /></td><td><code>array</code></td><td>A list of enumerable Strings representing the repository creation scenarios that the template will apply towards.</td></tr>
<tr><td><CopyableCode code="created_at" /></td><td><code>string</code></td><td>Create timestamp of the template.</td></tr>
<tr><td><CopyableCode code="updated_at" /></td><td><code>string</code></td><td>Update timestamp of the template.</td></tr>
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
Lists all <code>repository_creation_templates</code> in a region.
```sql
SELECT
region,
prefix
FROM aws.ecr.repository_creation_templates_list_only
WHERE region = 'us-east-1';
```


## Permissions

For permissions required to operate on the <code>repository_creation_templates_list_only</code> resource, see <a href="/providers/aws/ecr/repository_creation_templates/#permissions"><code>repository_creation_templates</code></a>


