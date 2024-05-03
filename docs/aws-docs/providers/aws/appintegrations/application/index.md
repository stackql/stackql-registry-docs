---
title: application
hide_title: false
hide_table_of_contents: false
keywords:
  - application
  - appintegrations
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

Gets or operates on an individual <code>application</code> resource, use <code>applications</code> to retrieve a list of resources or to create a resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>application</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>Resource Type definition for AWS:AppIntegrations::Application</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="aws.appintegrations.application" /></td></tr>
</tbody></table>

## Fields
<table><tbody>
<tr><th>Name</th><th>Datatype</th><th>Description</th></tr>
<tr><td><CopyableCode code="name" /></td><td><code>string</code></td><td>The name of the application.</td></tr>
<tr><td><CopyableCode code="id" /></td><td><code>string</code></td><td>The id of the application.</td></tr>
<tr><td><CopyableCode code="namespace" /></td><td><code>string</code></td><td>The namespace of the application.</td></tr>
<tr><td><CopyableCode code="description" /></td><td><code>string</code></td><td>The application description.</td></tr>
<tr><td><CopyableCode code="application_arn" /></td><td><code>string</code></td><td>The Amazon Resource Name (ARN) of the application.</td></tr>
<tr><td><CopyableCode code="application_source_config" /></td><td><code>object</code></td><td>Application source config</td></tr>
<tr><td><CopyableCode code="permissions" /></td><td><code>array</code></td><td>The configuration of events or requests that the application has access to.</td></tr>
<tr><td><CopyableCode code="tags" /></td><td><code>array</code></td><td>The tags (keys and values) associated with the application.</td></tr>
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
name,
id,
namespace,
description,
application_arn,
application_source_config,
permissions,
tags
FROM aws.appintegrations.application
WHERE data__Identifier = '<ApplicationArn>';
```

## Permissions

To operate on the <code>application</code> resource, the following permissions are required:

### Read
```json
app-integrations:GetApplication
```

### Update
```json
app-integrations:GetApplication,
app-integrations:UpdateApplication,
app-integrations:TagResource,
app-integrations:UntagResource
```

### Delete
```json
app-integrations:DeleteApplication
```

