---
title: readiness_checks
hide_title: false
hide_table_of_contents: false
keywords:
  - readiness_checks
  - route53recoveryreadiness
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

Creates, updates, deletes or gets a <code>readiness_check</code> resource or lists <code>readiness_checks</code> in a region

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>readiness_checks</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>Aws Route53 Recovery Readiness Check Schema and API specification.</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="aws.route53recoveryreadiness.readiness_checks" /></td></tr>
</tbody></table>

## Fields
<table><tbody><tr><th>Name</th><th>Datatype</th><th>Description</th></tr><tr><td><CopyableCode code="resource_set_name" /></td><td><code>string</code></td><td>The name of the resource set to check.</td></tr>
<tr><td><CopyableCode code="readiness_check_name" /></td><td><code>string</code></td><td>Name of the ReadinessCheck to create.</td></tr>
<tr><td><CopyableCode code="readiness_check_arn" /></td><td><code>string</code></td><td>The Amazon Resource Name (ARN) of the readiness check.</td></tr>
<tr><td><CopyableCode code="tags" /></td><td><code>array</code></td><td>A collection of tags associated with a resource.</td></tr>
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
    <td><CopyableCode code="region" /></td>
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
Gets all <code>readiness_checks</code> in a region.
```sql
SELECT
region,
resource_set_name,
readiness_check_name,
readiness_check_arn,
tags
FROM aws.route53recoveryreadiness.readiness_checks
WHERE region = 'us-east-1';
```
Gets all properties from an individual <code>readiness_check</code>.
```sql
SELECT
region,
resource_set_name,
readiness_check_name,
readiness_check_arn,
tags
FROM aws.route53recoveryreadiness.readiness_checks
WHERE region = 'us-east-1' AND data__Identifier = '<ReadinessCheckName>';
```

## `INSERT` example

Use the following StackQL query and manifest file to create a new <code>readiness_check</code> resource, using [__`stack-deploy`__](https://pypi.org/project/stack-deploy/).

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
INSERT INTO aws.route53recoveryreadiness.readiness_checks (
 ResourceSetName,
 ReadinessCheckName,
 Tags,
 region
)
SELECT 
'{{ ResourceSetName }}',
 '{{ ReadinessCheckName }}',
 '{{ Tags }}',
'{{ region }}';
```
</TabItem>
<TabItem value="all">

```sql
/*+ create */
INSERT INTO aws.route53recoveryreadiness.readiness_checks (
 ResourceSetName,
 ReadinessCheckName,
 Tags,
 region
)
SELECT 
 '{{ ResourceSetName }}',
 '{{ ReadinessCheckName }}',
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
  - name: readiness_check
    props:
      - name: ResourceSetName
        value: '{{ ResourceSetName }}'
      - name: ReadinessCheckName
        value: '{{ ReadinessCheckName }}'
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
DELETE FROM aws.route53recoveryreadiness.readiness_checks
WHERE data__Identifier = '<ReadinessCheckName>'
AND region = 'us-east-1';
```

## Permissions

To operate on the <code>readiness_checks</code> resource, the following permissions are required:

### Create
```json
route53-recovery-readiness:CreateReadinessCheck,
route53-recovery-readiness:GetResourceSet,
route53-recovery-readiness:GetReadinessCheck,
route53-recovery-readiness:ListTagsForResources,
route53-recovery-readiness:TagResource
```

### Read
```json
route53-recovery-readiness:GetReadinessCheck,
route53-recovery-readiness:ListTagsForResources
```

### Update
```json
route53-recovery-readiness:UpdateReadinessCheck,
route53-recovery-readiness:GetResourceSet,
route53-recovery-readiness:GetReadinessCheck,
route53-recovery-readiness:ListTagsForResources,
route53-recovery-readiness:TagResource,
route53-recovery-readiness:UntagResource
```

### Delete
```json
route53-recovery-readiness:DeleteReadinessCheck,
route53-recovery-readiness:GetReadinessCheck
```

### List
```json
route53-recovery-readiness:ListReadinessChecks,
route53-recovery-readiness:GetReadinessChecks
```

