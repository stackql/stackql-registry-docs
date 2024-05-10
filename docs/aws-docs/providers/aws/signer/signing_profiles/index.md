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


Used to retrieve a list of <code>signing_profiles</code> in a region or to create or delete a <code>signing_profiles</code> resource, use <code>signing_profile</code> to read or update an individual resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>signing_profiles</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>A signing profile is a signing template that can be used to carry out a pre-defined signing job.</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="aws.signer.signing_profiles" /></td></tr>
</tbody></table>

## Fields
<table><tbody>
<tr><th>Name</th><th>Datatype</th><th>Description</th></tr>
<tr><td><CopyableCode code="arn" /></td><td><code>undefined</code></td><td>The Amazon Resource Name (ARN) of the specified signing profile.</td></tr>
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
    <td><CopyableCode code="delete_resource" /></td>
    <td><code>DELETE</code></td>
    <td><CopyableCode code="data__Identifier, region" /></td>
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
arn
FROM aws.signer.signing_profiles
WHERE region = 'us-east-1';
```

## `INSERT` Example

Use the following StackQL query and manifest file to create a new <code>signing_profile</code> resource, using <a ref="https://pypi.org/project/stack-deploy/" target="_blank"><code><b>stack-deploy</b></code></a>.

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
-- signing_profile.iql (required properties only)
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
-- signing_profile.iql (all properties)
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

## `DELETE` Example

```sql
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

### Delete
```json
signer:CancelSigningProfile,
signer:GetSigningProfile
```

### List
```json
signer:ListSigningProfiles
```

