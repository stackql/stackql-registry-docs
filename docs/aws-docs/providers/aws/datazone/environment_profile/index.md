---
title: environment_profile
hide_title: false
hide_table_of_contents: false
keywords:
  - environment_profile
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
import Tabs from '@theme/Tabs';
import TabItem from '@theme/TabItem';


Gets or updates an individual <code>environment_profile</code> resource, use <code>environment_profiles</code> to retrieve a list of resources or to create or delete a resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>environment_profile</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>AWS Datazone Environment Profile is pre-configured set of resources and blueprints that provide reusable templates for creating environments.</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="aws.datazone.environment_profile" /></td></tr>
</tbody></table>

## Fields
<table><tbody>
<tr><th>Name</th><th>Datatype</th><th>Description</th></tr>
<tr><td><CopyableCode code="aws_account_id" /></td><td><code>string</code></td><td>The AWS account in which the Amazon DataZone environment is created.</td></tr>
<tr><td><CopyableCode code="aws_account_region" /></td><td><code>string</code></td><td>The AWS region in which this environment profile is created.</td></tr>
<tr><td><CopyableCode code="created_at" /></td><td><code>string</code></td><td>The timestamp of when this environment profile was created.</td></tr>
<tr><td><CopyableCode code="created_by" /></td><td><code>string</code></td><td>The Amazon DataZone user who created this environment profile.</td></tr>
<tr><td><CopyableCode code="description" /></td><td><code>string</code></td><td>The description of this Amazon DataZone environment profile.</td></tr>
<tr><td><CopyableCode code="domain_id" /></td><td><code>string</code></td><td>The ID of the Amazon DataZone domain in which this environment profile is created.</td></tr>
<tr><td><CopyableCode code="domain_identifier" /></td><td><code>string</code></td><td>The ID of the Amazon DataZone domain in which this environment profile is created.</td></tr>
<tr><td><CopyableCode code="environment_blueprint_id" /></td><td><code>string</code></td><td>The ID of the blueprint with which this environment profile is created.</td></tr>
<tr><td><CopyableCode code="environment_blueprint_identifier" /></td><td><code>string</code></td><td>The ID of the blueprint with which this environment profile is created.</td></tr>
<tr><td><CopyableCode code="id" /></td><td><code>string</code></td><td>The ID of this Amazon DataZone environment profile.</td></tr>
<tr><td><CopyableCode code="name" /></td><td><code>string</code></td><td>The name of this Amazon DataZone environment profile.</td></tr>
<tr><td><CopyableCode code="project_id" /></td><td><code>string</code></td><td>The identifier of the project in which to create the environment profile.</td></tr>
<tr><td><CopyableCode code="project_identifier" /></td><td><code>string</code></td><td>The identifier of the project in which to create the environment profile.</td></tr>
<tr><td><CopyableCode code="updated_at" /></td><td><code>string</code></td><td>The timestamp of when this environment profile was updated.</td></tr>
<tr><td><CopyableCode code="user_parameters" /></td><td><code>array</code></td><td>The user parameters of this Amazon DataZone environment profile.</td></tr>
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
    <td><CopyableCode code="get_resource" /></td>
    <td><code>SELECT</code></td>
    <td><CopyableCode code="data__Identifier, region" /></td>
  </tr>
</tbody></table>

## `SELECT` Example
```sql
SELECT
region,
aws_account_id,
aws_account_region,
created_at,
created_by,
description,
domain_id,
domain_identifier,
environment_blueprint_id,
environment_blueprint_identifier,
id,
name,
project_id,
project_identifier,
updated_at,
user_parameters
FROM aws.datazone.environment_profile
WHERE region = 'us-east-1' AND data__Identifier = '<DomainId>|<Id>';
```


## Permissions

To operate on the <code>environment_profile</code> resource, the following permissions are required:

### Read
```json
datazone:GetEnvironmentProfile
```

### Update
```json
datazone:UpdateEnvironmentProfile,
datazone:GetEnvironmentProfile
```

