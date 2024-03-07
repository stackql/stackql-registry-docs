---
title: containers
hide_title: false
hide_table_of_contents: false
keywords:
  - containers
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
Retrieves a list of <code>containers</code> in a region

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>containers</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>containers</td></tr>
<tr><td><b>Id</b></td><td><code>awscc.lightsail.containers</code></td></tr>
</tbody></table>

## Fields
<table><tbody>
<tr><th>Name</th><th>Datatype</th><th>Description</th></tr>
<tr><td><code>service_name</code></td><td><code>string</code></td><td>The name for the container service.</td></tr>
<tr><td><code>region</code></td><td><code>string</code></td><td>AWS region.</td></tr>

</tbody></table>

## Methods
Currently only <code>SELECT</code> is supported for this resource resource.

## Permissions

To operate on the <code>containers</code> resource, the following permissions are required:

### Create
<pre>
lightsail:CreateContainerService,
lightsail:CreateContainerServiceDeployment,
lightsail:GetContainerServices,
lightsail:TagResource,
lightsail:UntagResource,
lightsail:UpdateContainerService</pre>

### List
<pre>
lightsail:GetContainerServices</pre>


## Example
```sql
SELECT
region,
service_name
FROM awscc.lightsail.containers
WHERE region = 'us-east-1'
```
