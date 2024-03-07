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
Gets an individual <code>container</code> resource

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>container</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>container</td></tr>
<tr><td><b>Id</b></td><td><code>awscc.lightsail.container</code></td></tr>
</tbody></table>

## Fields
<table><tbody>
<tr><th>Name</th><th>Datatype</th><th>Description</th></tr>
<tr><td><code>service_name</code></td><td><code>string</code></td><td>The name for the container service.</td></tr>
<tr><td><code>power</code></td><td><code>string</code></td><td>The power specification for the container service.</td></tr>
<tr><td><code>container_arn</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>scale</code></td><td><code>integer</code></td><td>The scale specification for the container service.</td></tr>
<tr><td><code>public_domain_names</code></td><td><code>array</code></td><td>The public domain names to use with the container service, such as example.com and www.example.com.</td></tr>
<tr><td><code>container_service_deployment</code></td><td><code>object</code></td><td>Describes a container deployment configuration of an Amazon Lightsail container service.</td></tr>
<tr><td><code>is_disabled</code></td><td><code>boolean</code></td><td>A Boolean value to indicate whether the container service is disabled.</td></tr>
<tr><td><code>private_registry_access</code></td><td><code>object</code></td><td>A Boolean value to indicate whether the container service has access to private container image repositories, such as Amazon Elastic Container Registry (Amazon ECR) private repositories.</td></tr>
<tr><td><code>url</code></td><td><code>string</code></td><td>The publicly accessible URL of the container service.</td></tr>
<tr><td><code>principal_arn</code></td><td><code>string</code></td><td>The principal ARN of the container service.</td></tr>
<tr><td><code>tags</code></td><td><code>array</code></td><td>An array of key-value pairs to apply to this resource.</td></tr>
<tr><td><code>region</code></td><td><code>string</code></td><td>AWS region.</td></tr>

</tbody></table>

## Methods
Currently only <code>SELECT</code> is supported for this resource resource.

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


## Example
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
FROM awscc.lightsail.container
WHERE region = 'us-east-1'
AND data__Identifier = '&lt;ServiceName&gt;'
```
