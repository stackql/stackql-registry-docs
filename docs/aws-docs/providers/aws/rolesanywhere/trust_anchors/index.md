---
title: trust_anchors
hide_title: false
hide_table_of_contents: false
keywords:
  - trust_anchors
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

import CopyableCode from '@site/src/components/CopyableCode/CopyableCode';
import Tabs from '@theme/Tabs';
import TabItem from '@theme/TabItem';

Creates, updates, deletes or gets a <code>trust_anchor</code> resource or lists <code>trust_anchors</code> in a region

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>trust_anchors</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>Definition of AWS::RolesAnywhere::TrustAnchor Resource Type.</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="aws.rolesanywhere.trust_anchors" /></td></tr>
</tbody></table>

## Fields
<table><tbody><tr><th>Name</th><th>Datatype</th><th>Description</th></tr><tr><td><CopyableCode code="enabled" /></td><td><code>boolean</code></td><td></td></tr>
<tr><td><CopyableCode code="name" /></td><td><code>string</code></td><td></td></tr>
<tr><td><CopyableCode code="notification_settings" /></td><td><code>array</code></td><td></td></tr>
<tr><td><CopyableCode code="source" /></td><td><code>object</code></td><td></td></tr>
<tr><td><CopyableCode code="tags" /></td><td><code>array</code></td><td></td></tr>
<tr><td><CopyableCode code="trust_anchor_id" /></td><td><code>string</code></td><td></td></tr>
<tr><td><CopyableCode code="trust_anchor_arn" /></td><td><code>string</code></td><td></td></tr>
<tr><td><CopyableCode code="region" /></td><td><code>string</code></td><td>AWS region.</td></tr>
</tbody></table>

For more information, see <a href="https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-rolesanywhere-trustanchor.html"><code>AWS::RolesAnywhere::TrustAnchor</code></a>.

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
    <td><CopyableCode code="Name, Source, region" /></td>
  </tr>
  <tr>
    <td><CopyableCode code="delete_resource" /></td>
    <td><code>DELETE</code></td>
    <td><CopyableCode code="data__Identifier, region" /></td>
  </tr>
  <tr>
    <td><CopyableCode code="update_resource" /></td>
    <td><code>UPDATE</code></td>
    <td><CopyableCode code="data__Identifier, data__PatchDocument, region" /></td>
  </tr>
  <tr>
    <td><CopyableCode code="list_resources" /></td>
    <td><code>SELECT</code></td>
    <td><CopyableCode code="region" /></td>
  </tr>
  <tr>
    <td><CopyableCode code="get_resource" /></td>
    <td><code>SELECT</code></td>
    <td><CopyableCode code="data__Identifier, region" /></td>
  </tr>
</tbody></table>

## `SELECT` examples
Gets all <code>trust_anchors</code> in a region.
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
FROM aws.rolesanywhere.trust_anchors
WHERE region = 'us-east-1';
```
Gets all properties from an individual <code>trust_anchor</code>.
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
FROM aws.rolesanywhere.trust_anchors
WHERE region = 'us-east-1' AND data__Identifier = '<TrustAnchorId>';
```

## `INSERT` example

Use the following StackQL query and manifest file to create a new <code>trust_anchor</code> resource, using [__`stack-deploy`__](https://pypi.org/project/stack-deploy/).

<Tabs
    defaultValue="required"
    values={[
      { label: 'Required Properties', value: 'required', },
      { label: 'All Properties', value: 'all', },
      { label: 'Manifest', value: 'manifest', },
    ]
}>
<TabItem value="required">

```sql
/*+ create */
INSERT INTO aws.rolesanywhere.trust_anchors (
 Name,
 Source,
 region
)
SELECT 
'{{ Name }}',
 '{{ Source }}',
'{{ region }}';
```
</TabItem>
<TabItem value="all">

```sql
/*+ create */
INSERT INTO aws.rolesanywhere.trust_anchors (
 Enabled,
 Name,
 NotificationSettings,
 Source,
 Tags,
 region
)
SELECT 
 '{{ Enabled }}',
 '{{ Name }}',
 '{{ NotificationSettings }}',
 '{{ Source }}',
 '{{ Tags }}',
 '{{ region }}';
```
</TabItem>
<TabItem value="manifest">

```yaml
version: 1
name: stack name
description: stack description
providers:
  - aws
globals:
  - name: region
    value: '{{ vars.AWS_REGION }}'
resources:
  - name: trust_anchor
    props:
      - name: Enabled
        value: '{{ Enabled }}'
      - name: Name
        value: '{{ Name }}'
      - name: NotificationSettings
        value:
          - Enabled: '{{ Enabled }}'
            Event: '{{ Event }}'
            Threshold: null
            Channel: '{{ Channel }}'
      - name: Source
        value:
          SourceType: '{{ SourceType }}'
          SourceData: null
      - name: Tags
        value:
          - Key: '{{ Key }}'
            Value: '{{ Value }}'

```
</TabItem>
</Tabs>

## `DELETE` example

```sql
/*+ delete */
DELETE FROM aws.rolesanywhere.trust_anchors
WHERE data__Identifier = '<TrustAnchorId>'
AND region = 'us-east-1';
```

## Permissions

To operate on the <code>trust_anchors</code> resource, the following permissions are required:

### Create
```json
iam:CreateServiceLinkedRole,
rolesanywhere:CreateTrustAnchor,
rolesanywhere:TagResource,
rolesanywhere:ListTagsForResource
```

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

### List
```json
rolesanywhere:ListTrustAnchors,
rolesanywhere:ListTagsForResource
```
