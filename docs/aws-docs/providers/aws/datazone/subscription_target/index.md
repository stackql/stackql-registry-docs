---
title: subscription_target
hide_title: false
hide_table_of_contents: false
keywords:
  - subscription_target
  - datazone
  - aws
  - stackql
  - infrastructure-as-code
  - configuration-as-data
  - cloud inventory
description: Query, deploy and manage AWS resources using SQL
custom_edit_url: null
image: /img/providers/aws/stackql-aws-provider-featured-image.png
---
Gets an individual <code>subscription_target</code> resource

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>subscription_target</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>Subscription targets enables one to access the data to which you have subscribed in your projects.</td></tr>
<tr><td><b>Id</b></td><td><code>aws.datazone.subscription_target</code></td></tr>
</tbody></table>

## Fields
<table><tbody>
<tr><th>Name</th><th>Datatype</th><th>Description</th></tr>
<tr><td><code>applicable_asset_types</code></td><td><code>array</code></td><td>The asset types that can be included in the subscription target.</td></tr>
<tr><td><code>authorized_principals</code></td><td><code>array</code></td><td>The authorized principals of the subscription target.</td></tr>
<tr><td><code>created_at</code></td><td><code>string</code></td><td>The timestamp of when the subscription target was created.</td></tr>
<tr><td><code>created_by</code></td><td><code>string</code></td><td>The Amazon DataZone user who created the subscription target.</td></tr>
<tr><td><code>domain_id</code></td><td><code>string</code></td><td>The ID of the Amazon DataZone domain in which subscription target is created.</td></tr>
<tr><td><code>domain_identifier</code></td><td><code>string</code></td><td>The ID of the Amazon DataZone domain in which subscription target would be created.</td></tr>
<tr><td><code>environment_id</code></td><td><code>string</code></td><td>The ID of the environment in which subscription target is created.</td></tr>
<tr><td><code>environment_identifier</code></td><td><code>string</code></td><td>The ID of the environment in which subscription target would be created.</td></tr>
<tr><td><code>id</code></td><td><code>string</code></td><td>The ID of the subscription target.</td></tr>
<tr><td><code>manage_access_role</code></td><td><code>string</code></td><td>The manage access role that is used to create the subscription target.</td></tr>
<tr><td><code>name</code></td><td><code>string</code></td><td>The name of the subscription target.</td></tr>
<tr><td><code>project_id</code></td><td><code>string</code></td><td>The identifier of the project specified in the subscription target.</td></tr>
<tr><td><code>provider</code></td><td><code>string</code></td><td>The provider of the subscription target.</td></tr>
<tr><td><code>subscription_target_config</code></td><td><code>array</code></td><td>The configuration of the subscription target.</td></tr>
<tr><td><code>type</code></td><td><code>string</code></td><td>The type of the subscription target.</td></tr>
<tr><td><code>updated_at</code></td><td><code>string</code></td><td>The timestamp of when the subscription target was updated.</td></tr>
<tr><td><code>updated_by</code></td><td><code>string</code></td><td>The Amazon DataZone user who updated the subscription target.</td></tr>
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
applicable_asset_types,
authorized_principals,
created_at,
created_by,
domain_id,
domain_identifier,
environment_id,
environment_identifier,
id,
manage_access_role,
name,
project_id,
provider,
subscription_target_config,
type,
updated_at,
updated_by
FROM aws.datazone.subscription_target
WHERE data__Identifier = '<DomainId>|<EnvironmentId>|<Id>';
```

## Permissions

To operate on the <code>subscription_target</code> resource, the following permissions are required:

### Read
```json
datazone:GetSubscriptionTarget
```

### Update
```json
datazone:UpdateSubscriptionTarget,
datazone:GetSubscriptionTarget,
iam:PassRole
```

### Delete
```json
datazone:DeleteSubscriptionTarget
```

