---
title: environment_profiles
hide_title: false
hide_table_of_contents: false
keywords:
  - environment_profiles
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

Used to retrieve a list of <code>environment_profiles</code> in a region or create a <code>environment_profiles</code> resource, use <code>environment_profile</code> to operate on an individual resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>environment_profiles</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>AWS Datazone Environment Profile is pre-configured set of resources and blueprints that provide reusable templates for creating environments.</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="aws.datazone.environment_profiles" /></td></tr>
</tbody></table>

## Fields
<table><tbody>
<tr><th>Name</th><th>Datatype</th><th>Description</th></tr>
<tr><td><CopyableCode code="domain_id" /></td><td><code>string</code></td><td>The ID of the Amazon DataZone domain in which this environment profile is created.</td></tr>
<tr><td><CopyableCode code="id" /></td><td><code>string</code></td><td>The ID of this Amazon DataZone environment profile.</td></tr>
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
    <td><CopyableCode code="create_resource" /></td>
    <td><code>INSERT</code></td>
    <td><CopyableCode code="data__DesiredState, region" /></td>
  </tr>
  <tr>
    <td><CopyableCode code="list_resource" /></td>
    <td><code>SELECT</code></td>
    <td><CopyableCode code="region" /></td>
  </tr>
</tbody></table>

## `SELECT` Example
```sql
SELECT
region,
domain_id,
id
FROM aws.datazone.environment_profiles
WHERE region = 'us-east-1'
```

## Permissions

To operate on the <code>environment_profiles</code> resource, the following permissions are required:

### Create
```json
datazone:CreateEnvironmentProfile,
datazone:GetEnvironmentProfile
```

### List
```json
datazone:ListEnvironmentProfiles
```
