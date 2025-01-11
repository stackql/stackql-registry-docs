---
title: playback_restriction_policies
hide_title: false
hide_table_of_contents: false
keywords:
  - playback_restriction_policies
  - ivs
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

Creates, updates, deletes or gets a <code>playback_restriction_policy</code> resource or lists <code>playback_restriction_policies</code> in a region

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>playback_restriction_policies</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>Resource Type definition for AWS::IVS::PlaybackRestrictionPolicy.</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="aws.ivs.playback_restriction_policies" /></td></tr>
</tbody></table>

## Fields
<table><tbody><tr><th>Name</th><th>Datatype</th><th>Description</th></tr><tr><td><CopyableCode code="arn" /></td><td><code>string</code></td><td>Playback-restriction-policy identifier.</td></tr>
<tr><td><CopyableCode code="allowed_countries" /></td><td><code>array</code></td><td>A list of country codes that control geoblocking restriction. Allowed values are the officially assigned ISO 3166-1 alpha-2 codes. Default: All countries (an empty array).</td></tr>
<tr><td><CopyableCode code="allowed_origins" /></td><td><code>array</code></td><td>A list of origin sites that control CORS restriction. Allowed values are the same as valid values of the Origin header defined at https://developer.mozilla.org/en-US/docs/Web/HTTP/Headers/Origin</td></tr>
<tr><td><CopyableCode code="enable_strict_origin_enforcement" /></td><td><code>boolean</code></td><td>Whether channel playback is constrained by origin site.</td></tr>
<tr><td><CopyableCode code="name" /></td><td><code>string</code></td><td>Playback-restriction-policy name.</td></tr>
<tr><td><CopyableCode code="tags" /></td><td><code>array</code></td><td>An array of key-value pairs to apply to this resource.</td></tr>
<tr><td><CopyableCode code="region" /></td><td><code>string</code></td><td>AWS region.</td></tr>
</tbody></table>

For more information, see <a href="https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ivs-playbackrestrictionpolicy.html"><code>AWS::IVS::PlaybackRestrictionPolicy</code></a>.

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
    <td><CopyableCode code="AllowedCountries, AllowedOrigins, region" /></td>
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
Gets all <code>playback_restriction_policies</code> in a region.
```sql
SELECT
region,
arn,
allowed_countries,
allowed_origins,
enable_strict_origin_enforcement,
name,
tags
FROM aws.ivs.playback_restriction_policies
WHERE region = 'us-east-1';
```
Gets all properties from an individual <code>playback_restriction_policy</code>.
```sql
SELECT
region,
arn,
allowed_countries,
allowed_origins,
enable_strict_origin_enforcement,
name,
tags
FROM aws.ivs.playback_restriction_policies
WHERE region = 'us-east-1' AND data__Identifier = '<Arn>';
```

## `INSERT` example

Use the following StackQL query and manifest file to create a new <code>playback_restriction_policy</code> resource, using [__`stack-deploy`__](https://pypi.org/project/stack-deploy/).

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
INSERT INTO aws.ivs.playback_restriction_policies (
 AllowedCountries,
 AllowedOrigins,
 region
)
SELECT 
'{{ AllowedCountries }}',
 '{{ AllowedOrigins }}',
'{{ region }}';
```
</TabItem>
<TabItem value="all">

```sql
/*+ create */
INSERT INTO aws.ivs.playback_restriction_policies (
 AllowedCountries,
 AllowedOrigins,
 EnableStrictOriginEnforcement,
 Name,
 Tags,
 region
)
SELECT 
 '{{ AllowedCountries }}',
 '{{ AllowedOrigins }}',
 '{{ EnableStrictOriginEnforcement }}',
 '{{ Name }}',
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
  - name: playback_restriction_policy
    props:
      - name: AllowedCountries
        value:
          - '{{ AllowedCountries[0] }}'
      - name: AllowedOrigins
        value:
          - '{{ AllowedOrigins[0] }}'
      - name: EnableStrictOriginEnforcement
        value: '{{ EnableStrictOriginEnforcement }}'
      - name: Name
        value: '{{ Name }}'
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
DELETE FROM aws.ivs.playback_restriction_policies
WHERE data__Identifier = '<Arn>'
AND region = 'us-east-1';
```

## Permissions

To operate on the <code>playback_restriction_policies</code> resource, the following permissions are required:

### Create
```json
ivs:CreatePlaybackRestrictionPolicy,
ivs:TagResource
```

### Read
```json
ivs:GetPlaybackRestrictionPolicy,
ivs:ListTagsForResource
```

### Update
```json
ivs:GetPlaybackRestrictionPolicy,
ivs:UpdatePlaybackRestrictionPolicy,
ivs:ListTagsForResource,
ivs:UntagResource,
ivs:TagResource
```

### Delete
```json
ivs:DeletePlaybackRestrictionPolicy,
ivs:UntagResource
```

### List
```json
ivs:ListPlaybackRestrictionPolicies,
ivs:ListTagsForResource
```
