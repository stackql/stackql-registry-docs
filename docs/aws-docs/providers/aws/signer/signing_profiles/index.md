---
title: signing_profiles
hide_title: false
hide_table_of_contents: false
keywords:
  - signing_profiles
  - signer
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

Creates, updates, deletes or gets a <code>signing_profile</code> resource or lists <code>signing_profiles</code> in a region

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>signing_profiles</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>A signing profile is a signing template that can be used to carry out a pre-defined signing job.</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="aws.signer.signing_profiles" /></td></tr>
</tbody></table>

## Fields
<table><tbody><tr><th>Name</th><th>Datatype</th><th>Description</th></tr><tr><td><CopyableCode code="profile_name" /></td><td><code>string</code></td><td>A name for the signing profile. AWS CloudFormation generates a unique physical ID and uses that ID for the signing profile name.</td></tr>
<tr><td><CopyableCode code="profile_version" /></td><td><code>string</code></td><td>A version for the signing profile. AWS Signer generates a unique version for each profile of the same profile name.</td></tr>
<tr><td><CopyableCode code="arn" /></td><td><code>string</code></td><td>The Amazon Resource Name (ARN) of the specified signing profile.</td></tr>
<tr><td><CopyableCode code="profile_version_arn" /></td><td><code>string</code></td><td>The Amazon Resource Name (ARN) of the specified signing profile version.</td></tr>
<tr><td><CopyableCode code="signature_validity_period" /></td><td><code>object</code></td><td>Signature validity period of the profile.</td></tr>
<tr><td><CopyableCode code="platform_id" /></td><td><code>string</code></td><td>The ID of the target signing platform.</td></tr>
<tr><td><CopyableCode code="tags" /></td><td><code>array</code></td><td>A list of tags associated with the signing profile.</td></tr>
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
    <td><CopyableCode code="PlatformId, region" /></td>
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
    <td><CopyableCode code="list_resource" /></td>
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
List all <code>signing_profiles</code> in a region.
```sql
SELECT
region,
arn
FROM aws.signer.signing_profiles
WHERE region = 'us-east-1';
```
Gets all properties from a <code>signing_profile</code>.
```sql
SELECT
region,
profile_name,
profile_version,
arn,
profile_version_arn,
signature_validity_period,
platform_id,
tags
FROM aws.signer.signing_profiles
WHERE region = 'us-east-1' AND data__Identifier = '<Arn>';
```


## `INSERT` example

Use the following StackQL query and manifest file to create a new <code>signing_profile</code> resource, using [__`stack-deploy`__](https://pypi.org/project/stack-deploy/).

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
INSERT INTO aws.signer.signing_profiles (
 PlatformId,
 region
)
SELECT 
'{{ PlatformId }}',
'{{ region }}';
```
</TabItem>
<TabItem value="all">

```sql
/*+ create */
INSERT INTO aws.signer.signing_profiles (
 SignatureValidityPeriod,
 PlatformId,
 Tags,
 region
)
SELECT 
 '{{ SignatureValidityPeriod }}',
 '{{ PlatformId }}',
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
  - name: signing_profile
    props:
      - name: SignatureValidityPeriod
        value:
          Value: '{{ Value }}'
          Type: '{{ Type }}'
      - name: PlatformId
        value: '{{ PlatformId }}'
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
DELETE FROM aws.signer.signing_profiles
WHERE data__Identifier = '<Arn>'
AND region = 'us-east-1';
```

## Permissions

To operate on the <code>signing_profiles</code> resource, the following permissions are required:

### Create
```json
signer:PutSigningProfile,
signer:TagResource
```

### Read
```json
signer:GetSigningProfile
```

### Delete
```json
signer:CancelSigningProfile,
signer:GetSigningProfile
```

### List
```json
signer:ListSigningProfiles
```

### Update
```json
signer:TagResource,
signer:UntagResource,
signer:GetSigningProfile
```

