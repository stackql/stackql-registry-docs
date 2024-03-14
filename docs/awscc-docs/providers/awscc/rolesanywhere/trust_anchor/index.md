---
title: trust_anchor
hide_title: false
hide_table_of_contents: false
keywords:
  - trust_anchor
  - rolesanywhere
  - aws
  - stackql
  - infrastructure-as-code
  - configuration-as-data
  - cloud inventory
description: Query, deploy and manage AWS resources using SQL
custom_edit_url: null
image: /img/providers/aws/stackql-aws-provider-featured-image.png
---
Gets an individual <code>trust_anchor</code> resource

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>trust_anchor</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>trust_anchor</td></tr>
<tr><td><b>Id</b></td><td><code>awscc.rolesanywhere.trust_anchor</code></td></tr>
</tbody></table>

## Fields
<table><tbody>
<tr><th>Name</th><th>Datatype</th><th>Description</th></tr>
<tr><td><code>enabled</code></td><td><code>boolean</code></td><td></td></tr>
<tr><td><code>name</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>notification_settings</code></td><td><code>array</code></td><td></td></tr>
<tr><td><code>source</code></td><td><code>object</code></td><td></td></tr>
<tr><td><code>tags</code></td><td><code>array</code></td><td></td></tr>
<tr><td><code>trust_anchor_id</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>trust_anchor_arn</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>region</code></td><td><code>string</code></td><td>AWS region.</td></tr>

</tbody></table>

## Methods
Currently only <code>SELECT</code> is supported for this resource resource.

## Example
```sql
SELECT
region,
enabled,
name,
notification_settings,
source,
tags,
trust_anchor_id,
trust_anchor_arn
FROM awscc.rolesanywhere.trust_anchor
WHERE data__Identifier = '<TrustAnchorId>';
```

## Permissions

To operate on the <code>trust_anchor</code> resource, the following permissions are required:

### Read
```json
rolesanywhere:GetTrustAnchor,
rolesanywhere:ListTagsForResource
```

### Update
```json
acm-pca:GetCertificateAuthorityCertificate,
rolesanywhere:ListTagsForResource,
rolesanywhere:TagResource,
rolesanywhere:UntagResource,
rolesanywhere:EnableTrustAnchor,
rolesanywhere:DisableTrustAnchor,
rolesanywhere:UpdateTrustAnchor,
rolesanywhere:GetTrustAnchor,
rolesanywhere:PutNotificationSettings,
rolesanywhere:ResetNotificationSettings
```

### Delete
```json
rolesanywhere:DeleteTrustAnchor
```

