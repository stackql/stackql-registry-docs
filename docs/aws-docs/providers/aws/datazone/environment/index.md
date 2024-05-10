---
title: environment
hide_title: false
hide_table_of_contents: false
keywords:
  - environment
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


Gets or updates an individual <code>environment</code> resource, use <code>environments</code> to retrieve a list of resources or to create or delete a resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>environment</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>Definition of AWS::DataZone::Environment Resource Type</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="aws.datazone.environment" /></td></tr>
</tbody></table>

## Fields
<table><tbody>
<tr><th>Name</th><th>Datatype</th><th>Description</th></tr>
<tr><td><CopyableCode code="aws_account_id" /></td><td><code>string</code></td><td>The AWS account in which the Amazon DataZone environment is created.</td></tr>
<tr><td><CopyableCode code="aws_account_region" /></td><td><code>string</code></td><td>The AWS region in which the Amazon DataZone environment is created.</td></tr>
<tr><td><CopyableCode code="created_at" /></td><td><code>string</code></td><td>The timestamp of when the environment was created.</td></tr>
<tr><td><CopyableCode code="created_by" /></td><td><code>string</code></td><td>The Amazon DataZone user who created the environment.</td></tr>
<tr><td><CopyableCode code="description" /></td><td><code>string</code></td><td>The description of the Amazon DataZone environment.</td></tr>
<tr><td><CopyableCode code="domain_id" /></td><td><code>string</code></td><td>The identifier of the Amazon DataZone domain in which the environment is created.</td></tr>
<tr><td><CopyableCode code="domain_identifier" /></td><td><code>string</code></td><td>The identifier of the Amazon DataZone domain in which the environment would be created.</td></tr>
<tr><td><CopyableCode code="environment_blueprint_id" /></td><td><code>string</code></td><td>The ID of the blueprint with which the Amazon DataZone environment was created.</td></tr>
<tr><td><CopyableCode code="environment_profile_id" /></td><td><code>string</code></td><td>The ID of the environment profile with which the Amazon DataZone environment was created.</td></tr>
<tr><td><CopyableCode code="environment_profile_identifier" /></td><td><code>string</code></td><td>The ID of the environment profile with which the Amazon DataZone environment would be created.</td></tr>
<tr><td><CopyableCode code="glossary_terms" /></td><td><code>array</code></td><td>The glossary terms that can be used in the Amazon DataZone environment.</td></tr>
<tr><td><CopyableCode code="id" /></td><td><code>string</code></td><td>The ID of the Amazon DataZone environment.</td></tr>
<tr><td><CopyableCode code="name" /></td><td><code>string</code></td><td>The name of the environment.</td></tr>
<tr><td><CopyableCode code="project_id" /></td><td><code>string</code></td><td>The ID of the Amazon DataZone project in which the environment is created.</td></tr>
<tr><td><CopyableCode code="project_identifier" /></td><td><code>string</code></td><td>The ID of the Amazon DataZone project in which the environment would be created.</td></tr>
<tr><td><CopyableCode code="provider" /></td><td><code>string</code></td><td>The provider of the Amazon DataZone environment.</td></tr>
<tr><td><CopyableCode code="status" /></td><td><code>string</code></td><td>The status of the Amazon DataZone environment.</td></tr>
<tr><td><CopyableCode code="updated_at" /></td><td><code>string</code></td><td>The timestamp of when the environment was updated.</td></tr>
<tr><td><CopyableCode code="user_parameters" /></td><td><code>array</code></td><td>The user parameters of the Amazon DataZone environment.</td></tr>
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
environment_profile_id,
environment_profile_identifier,
glossary_terms,
id,
name,
project_id,
project_identifier,
provider,
status,
updated_at,
user_parameters
FROM aws.datazone.environment
WHERE region = 'us-east-1' AND data__Identifier = '<DomainId>|<Id>';
```


## Permissions

To operate on the <code>environment</code> resource, the following permissions are required:

### Read
```json
datazone:GetEnvironment
```

### Update
```json
datazone:UpdateEnvironment,
datazone:GetEnvironment,
datazone:DeleteEnvironment
```

