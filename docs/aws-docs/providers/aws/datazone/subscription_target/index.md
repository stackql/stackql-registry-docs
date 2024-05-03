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

import CopyableCode from '@site/src/components/CopyableCode/CopyableCode';

Gets or operates on an individual <code>subscription_target</code> resource, use <code>subscription_targets</code> to retrieve a list of resources or to create a resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>subscription_target</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>Subscription targets enables one to access the data to which you have subscribed in your projects.</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="aws.datazone.subscription_target" /></td></tr>
</tbody></table>

## Fields
<table><tbody>
<tr><th>Name</th><th>Datatype</th><th>Description</th></tr>
<tr><td><CopyableCode code="applicable_asset_types" /></td><td><code>array</code></td><td>The asset types that can be included in the subscription target.</td></tr>
<tr><td><CopyableCode code="authorized_principals" /></td><td><code>array</code></td><td>The authorized principals of the subscription target.</td></tr>
<tr><td><CopyableCode code="created_at" /></td><td><code>string</code></td><td>The timestamp of when the subscription target was created.</td></tr>
<tr><td><CopyableCode code="created_by" /></td><td><code>string</code></td><td>The Amazon DataZone user who created the subscription target.</td></tr>
<tr><td><CopyableCode code="domain_id" /></td><td><code>string</code></td><td>The ID of the Amazon DataZone domain in which subscription target is created.</td></tr>
<tr><td><CopyableCode code="domain_identifier" /></td><td><code>string</code></td><td>The ID of the Amazon DataZone domain in which subscription target would be created.</td></tr>
<tr><td><CopyableCode code="environment_id" /></td><td><code>string</code></td><td>The ID of the environment in which subscription target is created.</td></tr>
<tr><td><CopyableCode code="environment_identifier" /></td><td><code>string</code></td><td>The ID of the environment in which subscription target would be created.</td></tr>
<tr><td><CopyableCode code="id" /></td><td><code>string</code></td><td>The ID of the subscription target.</td></tr>
<tr><td><CopyableCode code="manage_access_role" /></td><td><code>string</code></td><td>The manage access role that is used to create the subscription target.</td></tr>
<tr><td><CopyableCode code="name" /></td><td><code>string</code></td><td>The name of the subscription target.</td></tr>
<tr><td><CopyableCode code="project_id" /></td><td><code>string</code></td><td>The identifier of the project specified in the subscription target.</td></tr>
<tr><td><CopyableCode code="provider" /></td><td><code>string</code></td><td>The provider of the subscription target.</td></tr>
<tr><td><CopyableCode code="subscription_target_config" /></td><td><code>array</code></td><td>The configuration of the subscription target.</td></tr>
<tr><td><CopyableCode code="type" /></td><td><code>string</code></td><td>The type of the subscription target.</td></tr>
<tr><td><CopyableCode code="updated_at" /></td><td><code>string</code></td><td>The timestamp of when the subscription target was updated.</td></tr>
<tr><td><CopyableCode code="updated_by" /></td><td><code>string</code></td><td>The Amazon DataZone user who updated the subscription target.</td></tr>
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

