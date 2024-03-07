---
title: service_profiles
hide_title: false
hide_table_of_contents: false
keywords:
  - service_profiles
  - iotwireless
  - aws
  - stackql
  - infrastructure-as-code
  - configuration-as-data
  - cloud inventory
description: Query, deploy and manage AWS resources using SQL
custom_edit_url: null
image: /img/providers/aws/stackql-aws-provider-featured-image.png
---
Retrieves a list of <code>service_profiles</code> in a region

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>service_profiles</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>service_profiles</td></tr>
<tr><td><b>Id</b></td><td><code>awscc.iotwireless.service_profiles</code></td></tr>
</tbody></table>

## Fields
<table><tbody>
<tr><th>Name</th><th>Datatype</th><th>Description</th></tr>
<tr><td><code>id</code></td><td><code>string</code></td><td>Service profile Id. Returned after successful create.</td></tr>
<tr><td><code>region</code></td><td><code>string</code></td><td>AWS region.</td></tr>

</tbody></table>

## Methods
Currently only <code>SELECT</code> is supported for this resource resource.

## Permissions

To operate on the <code>service_profiles</code> resource, the following permissions are required:

### Create
<pre>
iotwireless:CreateServiceProfile,
iotwireless:TagResource,
iotwireless:ListTagsForResource</pre>

### List
<pre>
iotwireless:ListServiceProfiles,
iotwireless:ListTagsForResource</pre>


## Example
```sql
SELECT
region,
id
FROM awscc.iotwireless.service_profiles
WHERE region = 'us-east-1'
```
