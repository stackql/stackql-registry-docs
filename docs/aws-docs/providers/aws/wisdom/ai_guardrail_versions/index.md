---
title: ai_guardrail_versions
hide_title: false
hide_table_of_contents: false
keywords:
  - ai_guardrail_versions
  - wisdom
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

Creates, updates, deletes or gets an <code>ai_guardrail_version</code> resource or lists <code>ai_guardrail_versions</code> in a region

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>ai_guardrail_versions</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>Definition of AWS::Wisdom::AIGuardrailVersion Resource Type</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="aws.wisdom.ai_guardrail_versions" /></td></tr>
</tbody></table>

## Fields
<table><tbody><tr><th>Name</th><th>Datatype</th><th>Description</th></tr><tr><td><CopyableCode code="a_iguardrail_arn" /></td><td><code>string</code></td><td></td></tr>
<tr><td><CopyableCode code="assistant_arn" /></td><td><code>string</code></td><td></td></tr>
<tr><td><CopyableCode code="a_iguardrail_id" /></td><td><code>string</code></td><td></td></tr>
<tr><td><CopyableCode code="assistant_id" /></td><td><code>string</code></td><td></td></tr>
<tr><td><CopyableCode code="a_iguardrail_version_id" /></td><td><code>string</code></td><td></td></tr>
<tr><td><CopyableCode code="version_number" /></td><td><code>number</code></td><td></td></tr>
<tr><td><CopyableCode code="modified_time_seconds" /></td><td><code>number</code></td><td></td></tr>
<tr><td><CopyableCode code="region" /></td><td><code>string</code></td><td>AWS region.</td></tr>
</tbody></table>

For more information, see <a href="https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-wisdom-aiguardrailversion.html"><code>AWS::Wisdom::AIGuardrailVersion</code></a>.

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
    <td><CopyableCode code="AssistantId, AIGuardrailId, region" /></td>
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
Gets all <code>ai_guardrail_versions</code> in a region.
```sql
SELECT
region,
a_iguardrail_arn,
assistant_arn,
a_iguardrail_id,
assistant_id,
a_iguardrail_version_id,
version_number,
modified_time_seconds
FROM aws.wisdom.ai_guardrail_versions
WHERE region = 'us-east-1';
```
Gets all properties from an individual <code>ai_guardrail_version</code>.
```sql
SELECT
region,
a_iguardrail_arn,
assistant_arn,
a_iguardrail_id,
assistant_id,
a_iguardrail_version_id,
version_number,
modified_time_seconds
FROM aws.wisdom.ai_guardrail_versions
WHERE region = 'us-east-1' AND data__Identifier = '<AssistantId>|<AIGuardrailId>|<VersionNumber>';
```

## `INSERT` example

Use the following StackQL query and manifest file to create a new <code>ai_guardrail_version</code> resource, using [__`stack-deploy`__](https://pypi.org/project/stack-deploy/).

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
INSERT INTO aws.wisdom.ai_guardrail_versions (
 AIGuardrailId,
 AssistantId,
 region
)
SELECT 
'{{ AIGuardrailId }}',
 '{{ AssistantId }}',
'{{ region }}';
```
</TabItem>
<TabItem value="all">

```sql
/*+ create */
INSERT INTO aws.wisdom.ai_guardrail_versions (
 AIGuardrailId,
 AssistantId,
 ModifiedTimeSeconds,
 region
)
SELECT 
 '{{ AIGuardrailId }}',
 '{{ AssistantId }}',
 '{{ ModifiedTimeSeconds }}',
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
  - name: ai_guardrail_version
    props:
      - name: AIGuardrailId
        value: '{{ AIGuardrailId }}'
      - name: AssistantId
        value: '{{ AssistantId }}'
      - name: ModifiedTimeSeconds
        value: null

```
</TabItem>
</Tabs>

## `DELETE` example

```sql
/*+ delete */
DELETE FROM aws.wisdom.ai_guardrail_versions
WHERE data__Identifier = '<AssistantId|AIGuardrailId|VersionNumber>'
AND region = 'us-east-1';
```

## Permissions

To operate on the <code>ai_guardrail_versions</code> resource, the following permissions are required:

### Create
```json
wisdom:CreateAIGuardrailVersion
```

### Read
```json
wisdom:GetAIGuardrail,
wisdom:GetAIGuardrailVersion
```

### Update
```json
wisdom:GetAIGuardrail,
wisdom:GetAIGuardrailVersion
```

### Delete
```json
wisdom:DeleteAIGuardrailVersion
```

### List
```json
wisdom:ListAIGuardrailVersions
```
