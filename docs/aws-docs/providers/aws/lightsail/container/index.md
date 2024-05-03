---
title: container
hide_title: false
hide_table_of_contents: false
keywords:
  - container
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

Gets or operates on an individual <code>container</code> resource, use <code>containers</code> to retrieve a list of resources or to create a resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>container</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>Resource Type definition for AWS::Lightsail::Container</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="aws.lightsail.container" /></td></tr>
</tbody></table>

## Fields
<table><tbody>
<tr><th>Name</th><th>Datatype</th><th>Description</th></tr>
<tr><td><CopyableCode code="service_name" /></td><td><code>string</code></td><td>The name for the container service.</td></tr>
<tr><td><CopyableCode code="power" /></td><td><code>string</code></td><td>The power specification for the container service.</td></tr>
<tr><td><CopyableCode code="container_arn" /></td><td><code>string</code></td><td></td></tr>
<tr><td><CopyableCode code="scale" /></td><td><code>integer</code></td><td>The scale specification for the container service.</td></tr>
<tr><td><CopyableCode code="public_domain_names" /></td><td><code>array</code></td><td>The public domain names to use with the container service, such as example.com and www.example.com.</td></tr>
<tr><td><CopyableCode code="container_service_deployment" /></td><td><code>object</code></td><td>Describes a container deployment configuration of an Amazon Lightsail container service.</td></tr>
<tr><td><CopyableCode code="is_disabled" /></td><td><code>boolean</code></td><td>A Boolean value to indicate whether the container service is disabled.</td></tr>
<tr><td><CopyableCode code="private_registry_access" /></td><td><code>object</code></td><td>A Boolean value to indicate whether the container service has access to private container image repositories, such as Amazon Elastic Container Registry (Amazon ECR) private repositories.</td></tr>
<tr><td><CopyableCode code="url" /></td><td><code>string</code></td><td>The publicly accessible URL of the container service.</td></tr>
<tr><td><CopyableCode code="principal_arn" /></td><td><code>string</code></td><td>The principal ARN of the container service.</td></tr>
<tr><td><CopyableCode code="tags" /></td><td><code>array</code></td><td>An array of key-value pairs to apply to this resource.</td></tr>
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
    <td><CopyableCode code="update_resource" /></td>
    <td><code>UPDATE</code></td>
    <td><CopyableCode code="data__Identifier, data__PatchDocument, region" /></td>
  </tr>
  <tr>
    <td><CopyableCode code="delete_resource" /></td>
    <td><code>DELETE</code></td>
    <td><CopyableCode code="data__Identifier, region" /></td>
  </tr>
  <tr>
    <td><CopyableCode code="get_resource" /></td>
    <td><code>SELECT</code></td>
    <td><CopyableCode code="data__Identifier, region" /></td>
  </tr>
</tbody></table>

## `SELECT` Example
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
tags
FROM aws.lightsail.container
WHERE data__Identifier = '<ServiceName>';
```

## Permissions

To operate on the <code>container</code> resource, the following permissions are required:

### Read
```json
lightsail:GetContainerServices
```

### Delete
```json
lightsail:DeleteContainerService,
lightsail:GetContainerServices
```

### Update
```json
lightsail:CreateContainerServiceDeployment,
lightsail:GetContainerServices,
lightsail:TagResource,
lightsail:UntagResource,
lightsail:UpdateContainerService
```

