---
title: object_type
hide_title: false
hide_table_of_contents: false
keywords:
  - object_type
  - customerprofiles
  - aws
  - stackql
  - infrastructure-as-code
  - configuration-as-data
  - cloud inventory
description: Query, deploy and manage AWS resources using SQL
custom_edit_url: null
image: /img/providers/aws/stackql-aws-provider-featured-image.png
---
Gets or operates on an individual <code>object_type</code> resource, use <code>object_types</code> to retrieve a list of resources or to create a resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>object_type</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>An ObjectType resource of Amazon Connect Customer Profiles</td></tr>
<tr><td><b>Id</b></td><td><code>aws.customerprofiles.object_type</code></td></tr>
</tbody></table>

## Fields
<table><tbody>
<tr><th>Name</th><th>Datatype</th><th>Description</th></tr>
<tr><td><code>domain_name</code></td><td><code>string</code></td><td>The unique name of the domain.</td></tr>
<tr><td><code>object_type_name</code></td><td><code>string</code></td><td>The name of the profile object type.</td></tr>
<tr><td><code>allow_profile_creation</code></td><td><code>boolean</code></td><td>Indicates whether a profile should be created when data is received.</td></tr>
<tr><td><code>description</code></td><td><code>string</code></td><td>Description of the profile object type.</td></tr>
<tr><td><code>encryption_key</code></td><td><code>string</code></td><td>The default encryption key</td></tr>
<tr><td><code>expiration_days</code></td><td><code>integer</code></td><td>The default number of days until the data within the domain expires.</td></tr>
<tr><td><code>fields</code></td><td><code>array</code></td><td>A list of the name and ObjectType field.</td></tr>
<tr><td><code>keys</code></td><td><code>array</code></td><td>A list of unique keys that can be used to map data to the profile.</td></tr>
<tr><td><code>created_at</code></td><td><code>string</code></td><td>The time of this integration got created.</td></tr>
<tr><td><code>last_updated_at</code></td><td><code>string</code></td><td>The time of this integration got last updated at.</td></tr>
<tr><td><code>source_last_updated_timestamp_format</code></td><td><code>string</code></td><td>The format of your sourceLastUpdatedTimestamp that was previously set up.</td></tr>
<tr><td><code>tags</code></td><td><code>array</code></td><td>The tags (keys and values) associated with the integration.</td></tr>
<tr><td><code>template_id</code></td><td><code>string</code></td><td>A unique identifier for the object template.</td></tr>
<tr><td><code>region</code></td><td><code>string</code></td><td>AWS region.</td></tr>

</tbody></table>

## Methods

<table><tbody>
  <tr>
    <th>Name</th>
    <th>Accessible by</th>
    <th>Required Params</th>
  </tr>
  <tr>
    <td><code>update_resource</code></td>
    <td><code>UPDATE</code></td>
    <td><code>data__Identifier, data__PatchDocument, region</code></td>
  </tr>
  <tr>
    <td><code>delete_resource</code></td>
    <td><code>DELETE</code></td>
    <td><code>data__Identifier, region</code></td>
  </tr>
  <tr>
    <td><code>get_resource</code></td>
    <td><code>SELECT</code></td>
    <td><code>data__Identifier, region</code></td>
  </tr>
</tbody></table>

## `SELECT` Example
```sql
SELECT
region,
domain_name,
object_type_name,
allow_profile_creation,
description,
encryption_key,
expiration_days,
fields,
keys,
created_at,
last_updated_at,
source_last_updated_timestamp_format,
tags,
template_id
FROM aws.customerprofiles.object_type
WHERE data__Identifier = '<DomainName>|<ObjectTypeName>';
```

## Permissions

To operate on the <code>object_type</code> resource, the following permissions are required:

### Read
```json
profile:GetProfileObjectType
```

### Update
```json
profile:GetProfileObjectType,
profile:PutProfileObjectType,
profile:UntagResource,
profile:TagResource
```

### Delete
```json
profile:DeleteProfileObjectType
```

