---
title: container_tags
hide_title: false
hide_table_of_contents: false
keywords:
  - container_tags
  - lightsail
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

Expands all tag keys and values for <code>containers</code> in a region

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>container_tags</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>Resource Type definition for AWS::Lightsail::Container</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="aws.lightsail.container_tags" /></td></tr>
</tbody></table>

## Fields
<table><tbody><tr><th>Name</th><th>Datatype</th><th>Description</th></tr><tr><td><CopyableCode code="service_name" /></td><td><code>string</code></td><td>The name for the container service.</td></tr>
<tr><td><CopyableCode code="power" /></td><td><code>string</code></td><td>The power specification for the container service.</td></tr>
<tr><td><CopyableCode code="container_arn" /></td><td><code>string</code></td><td></td></tr>
<tr><td><CopyableCode code="scale" /></td><td><code>integer</code></td><td>The scale specification for the container service.</td></tr>
<tr><td><CopyableCode code="public_domain_names" /></td><td><code>array</code></td><td>The public domain names to use with the container service, such as example.com and www.example.com.</td></tr>
<tr><td><CopyableCode code="container_service_deployment" /></td><td><code>object</code></td><td>Describes a container deployment configuration of an Amazon Lightsail container service.</td></tr>
<tr><td><CopyableCode code="is_disabled" /></td><td><code>boolean</code></td><td>A Boolean value to indicate whether the container service is disabled.</td></tr>
<tr><td><CopyableCode code="private_registry_access" /></td><td><code>object</code></td><td>A Boolean value to indicate whether the container service has access to private container image repositories, such as Amazon Elastic Container Registry (Amazon ECR) private repositories.</td></tr>
<tr><td><CopyableCode code="url" /></td><td><code>string</code></td><td>The publicly accessible URL of the container service.</td></tr>
<tr><td><CopyableCode code="principal_arn" /></td><td><code>string</code></td><td>The principal ARN of the container service.</td></tr>
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
Expands tags for all <code>containers</code> in a region.
```sql
SELECT
region,
service_name,
power,
container_arn,
scale,
public_domain_names,
container_service_deployment,
is_disabled,
private_registry_access,
url,
principal_arn,
tag_key,
tag_value
FROM aws.lightsail.container_tags
WHERE region = 'us-east-1';
```


## Permissions

For permissions required to operate on the <code>container_tags</code> resource, see <a href="/providers/aws/lightsail/containers/#permissions"><code>containers</code></a>


