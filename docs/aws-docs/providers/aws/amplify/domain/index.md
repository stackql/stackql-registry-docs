---
title: domain
hide_title: false
hide_table_of_contents: false
keywords:
  - domain
  - amplify
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

Gets or operates on an individual <code>domain</code> resource, use <code>domains</code> to retrieve a list of resources or to create a resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>domain</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>The AWS::Amplify::Domain resource allows you to connect a custom domain to your app.</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="aws.amplify.domain" /></td></tr>
</tbody></table>

## Fields
<table><tbody>
<tr><th>Name</th><th>Datatype</th><th>Description</th></tr>
<tr><td><CopyableCode code="app_id" /></td><td><code>string</code></td><td></td></tr>
<tr><td><CopyableCode code="arn" /></td><td><code>string</code></td><td></td></tr>
<tr><td><CopyableCode code="auto_sub_domain_creation_patterns" /></td><td><code>array</code></td><td></td></tr>
<tr><td><CopyableCode code="auto_sub_domain_iam_role" /></td><td><code>string</code></td><td></td></tr>
<tr><td><CopyableCode code="certificate_record" /></td><td><code>string</code></td><td></td></tr>
<tr><td><CopyableCode code="certificate" /></td><td><code>object</code></td><td></td></tr>
<tr><td><CopyableCode code="certificate_settings" /></td><td><code>object</code></td><td></td></tr>
<tr><td><CopyableCode code="domain_name" /></td><td><code>string</code></td><td></td></tr>
<tr><td><CopyableCode code="domain_status" /></td><td><code>string</code></td><td></td></tr>
<tr><td><CopyableCode code="update_status" /></td><td><code>string</code></td><td></td></tr>
<tr><td><CopyableCode code="enable_auto_sub_domain" /></td><td><code>boolean</code></td><td></td></tr>
<tr><td><CopyableCode code="status_reason" /></td><td><code>string</code></td><td></td></tr>
<tr><td><CopyableCode code="sub_domain_settings" /></td><td><code>array</code></td><td></td></tr>
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
app_id,
arn,
auto_sub_domain_creation_patterns,
auto_sub_domain_iam_role,
certificate_record,
certificate,
certificate_settings,
domain_name,
domain_status,
update_status,
enable_auto_sub_domain,
status_reason,
sub_domain_settings
FROM aws.amplify.domain
WHERE data__Identifier = '<Arn>';
```

## Permissions

To operate on the <code>domain</code> resource, the following permissions are required:

### Delete
```json
amplify:DeleteDomainAssociation,
iam:PassRole,
amplify:DeleteDomainAssociation
```

### Read
```json
amplify:GetDomainAssociation,
route53:ListHostedZones,
iam:PassRole,
amplify:ListTagsForResource
```

### Update
```json
amplify:UpdateDomainAssociation,
route53:ListHostedZones,
route53:ChangeResourceRecordSets,
iam:PassRole,
amplify:ListTagsForResource,
amplify:TagResource,
amplify:UntagResource
```

