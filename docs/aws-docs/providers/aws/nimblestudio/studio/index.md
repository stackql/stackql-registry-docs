---
title: studio
hide_title: false
hide_table_of_contents: false
keywords:
  - studio
  - nimblestudio
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

Gets or operates on an individual <code>studio</code> resource, use <code>studios</code> to retrieve a list of resources or to create a resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>studio</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>Represents a studio that contains other Nimble Studio resources</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="aws.nimblestudio.studio" /></td></tr>
</tbody></table>

## Fields
<table><tbody>
<tr><th>Name</th><th>Datatype</th><th>Description</th></tr>
<tr><td><CopyableCode code="admin_role_arn" /></td><td><code>string</code></td><td>&lt;p&gt;The IAM role that Studio Admins will assume when logging in to the Nimble Studio portal.&lt;&#x2F;p&gt;</td></tr>
<tr><td><CopyableCode code="display_name" /></td><td><code>string</code></td><td>&lt;p&gt;A friendly name for the studio.&lt;&#x2F;p&gt;</td></tr>
<tr><td><CopyableCode code="home_region" /></td><td><code>string</code></td><td>&lt;p&gt;The Amazon Web Services Region where the studio resource is located.&lt;&#x2F;p&gt;</td></tr>
<tr><td><CopyableCode code="sso_client_id" /></td><td><code>string</code></td><td>&lt;p&gt;The Amazon Web Services SSO application client ID used to integrate with Amazon Web Services SSO to enable Amazon Web Services SSO users to log in to Nimble Studio portal.&lt;&#x2F;p&gt;</td></tr>
<tr><td><CopyableCode code="studio_encryption_configuration" /></td><td><code>object</code></td><td></td></tr>
<tr><td><CopyableCode code="studio_id" /></td><td><code>string</code></td><td></td></tr>
<tr><td><CopyableCode code="studio_name" /></td><td><code>string</code></td><td>&lt;p&gt;The studio name that is used in the URL of the Nimble Studio portal when accessed by Nimble Studio users.&lt;&#x2F;p&gt;</td></tr>
<tr><td><CopyableCode code="studio_url" /></td><td><code>string</code></td><td>&lt;p&gt;The address of the web page for the studio.&lt;&#x2F;p&gt;</td></tr>
<tr><td><CopyableCode code="tags" /></td><td><code>object</code></td><td></td></tr>
<tr><td><CopyableCode code="user_role_arn" /></td><td><code>string</code></td><td>&lt;p&gt;The IAM role that Studio Users will assume when logging in to the Nimble Studio portal.&lt;&#x2F;p&gt;</td></tr>
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
admin_role_arn,
display_name,
home_region,
sso_client_id,
studio_encryption_configuration,
studio_id,
studio_name,
studio_url,
tags,
user_role_arn
FROM aws.nimblestudio.studio
WHERE data__Identifier = '<StudioId>';
```

## Permissions

To operate on the <code>studio</code> resource, the following permissions are required:

### Read
```json
nimble:GetStudio,
kms:Encrypt,
kms:Decrypt,
kms:ListGrants,
kms:GenerateDataKey
```

### Update
```json
iam:PassRole,
nimble:UpdateStudio,
nimble:GetStudio,
kms:Encrypt,
kms:Decrypt,
kms:CreateGrant,
kms:ListGrants,
kms:GenerateDataKey
```

### Delete
```json
nimble:DeleteStudio,
nimble:GetStudio,
nimble:UntagResource,
kms:Encrypt,
kms:Decrypt,
kms:ListGrants,
kms:RetireGrant,
kms:GenerateDataKey,
sso:DeleteManagedApplicationInstance,
sso:GetManagedApplicationInstance
```

